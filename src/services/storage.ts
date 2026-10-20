// src/services/storage.ts
import { AttemptResult, QuizSessionState, TimerPreset } from '../types/quiz';

const STORAGE_KEYS = {
  USERNAME: 'ds_quiz_username',
  ACTIVE_SESSION: 'ds_quiz_active_session',
  ATTEMPT_HISTORY: 'ds_quiz_attempt_history',
  TIMER_PRESET: 'ds_quiz_timer_preset',
  CUSTOM_TIMER_MINUTES: 'ds_quiz_custom_timer_minutes',
};

export const storage = {
  // --- Username ---
  getUsername(): string {
    return localStorage.getItem(STORAGE_KEYS.USERNAME) || '';
  },

  setUsername(name: string): void {
    localStorage.setItem(STORAGE_KEYS.USERNAME, name.trim());
  },

  // --- Active Quiz Session ---
  getActiveSession(): QuizSessionState | null {
    try {
      const raw = localStorage.getItem(STORAGE_KEYS.ACTIVE_SESSION);
      if (!raw) return null;
      const parsed: QuizSessionState = JSON.parse(raw);

      // Re-calculate remaining time based on timestamp if active
      if (
        parsed.timerStartedAtTimestamp &&
        parsed.initialDurationSeconds &&
        !parsed.isCompleted
      ) {
        const elapsedSeconds = Math.floor(
          (Date.now() - parsed.timerStartedAtTimestamp) / 1000
        );
        const remaining = parsed.initialDurationSeconds - elapsedSeconds;
        parsed.timeRemainingSeconds = remaining > 0 ? remaining : 0;
      }

      return parsed;
    } catch {
      return null;
    }
  },

  saveActiveSession(session: QuizSessionState): void {
    try {
      localStorage.setItem(STORAGE_KEYS.ACTIVE_SESSION, JSON.stringify(session));
    } catch (e) {
      console.error('Failed to save active session to localStorage', e);
    }
  },

  clearActiveSession(): void {
    localStorage.removeItem(STORAGE_KEYS.ACTIVE_SESSION);
  },

  // --- History & Attempts ---
  getAttempts(): AttemptResult[] {
    try {
      const raw = localStorage.getItem(STORAGE_KEYS.ATTEMPT_HISTORY);
      return raw ? JSON.parse(raw) : [];
    } catch {
      return [];
    }
  },

  saveAttempt(attempt: AttemptResult): void {
    try {
      const history = storage.getAttempts();
      history.unshift(attempt); // latest attempt first
      // Keep up to 100 recent attempts
      const trimmed = history.slice(0, 100);
      localStorage.setItem(STORAGE_KEYS.ATTEMPT_HISTORY, JSON.stringify(trimmed));
      storage.clearActiveSession();
    } catch (e) {
      console.error('Failed to save attempt to history', e);
    }
  },

  clearHistory(): void {
    localStorage.removeItem(STORAGE_KEYS.ATTEMPT_HISTORY);
  },

  // --- Topic Weakness Analytics ---
  getTopicWeaknesses(): Record<string, { total: number; correct: number; percentage: number }> {
    const attempts = storage.getAttempts();
    const stats: Record<string, { total: number; correct: number }> = {};

    for (const attempt of attempts) {
      for (const [topic, data] of Object.entries(attempt.topicStats || {})) {
        if (!stats[topic]) {
          stats[topic] = { total: 0, correct: 0 };
        }
        stats[topic].total += data.total;
        stats[topic].correct += data.correct;
      }
    }

    const result: Record<string, { total: number; correct: number; percentage: number }> = {};
    for (const [topic, data] of Object.entries(stats)) {
      result[topic] = {
        total: data.total,
        correct: data.correct,
        percentage: data.total > 0 ? Math.round((data.correct / data.total) * 100) : 0,
      };
    }

    return result;
  },

  // Get list of question IDs answered incorrectly in past attempts
  getPastIncorrectQuestionIds(): Set<string> {
    const attempts = storage.getAttempts();
    const incorrectIds = new Set<string>();

    for (const attempt of attempts) {
      for (const qr of attempt.questionResults) {
        if (!qr.isCorrect) {
          incorrectIds.add(qr.question.id);
        }
      }
    }

    return incorrectIds;
  },

  // Get set of all question IDs seen so far
  getSeenQuestionIds(): Set<string> {
    const attempts = storage.getAttempts();
    const seenIds = new Set<string>();

    for (const attempt of attempts) {
      for (const qr of attempt.questionResults) {
        seenIds.add(qr.question.id);
      }
    }

    return seenIds;
  },

  // --- Timer Preferences ---
  getTimerPreset(): TimerPreset {
    const raw = localStorage.getItem(STORAGE_KEYS.TIMER_PRESET);
    if (raw === null) return 1200; // default 20 minutes
    const val = parseInt(raw, 10);
    return isNaN(val) ? 1200 : (val as TimerPreset);
  },

  setTimerPreset(preset: TimerPreset): void {
    localStorage.setItem(STORAGE_KEYS.TIMER_PRESET, preset.toString());
  },

  getCustomTimerMinutes(): number {
    const raw = localStorage.getItem(STORAGE_KEYS.CUSTOM_TIMER_MINUTES);
    if (!raw) return 25;
    const val = parseInt(raw, 10);
    return isNaN(val) || val <= 0 ? 25 : val;
  },

  setCustomTimerMinutes(mins: number): void {
    localStorage.setItem(STORAGE_KEYS.CUSTOM_TIMER_MINUTES, mins.toString());
  },
};
