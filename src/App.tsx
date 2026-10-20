import React, { useEffect, useState } from 'react';
import { AmbientBackground } from './components/AmbientBackground';
import { AppShell } from './components/shell/AppShell';
import { HistoryModal } from './components/HistoryModal';
import { LandingScreen } from './components/LandingScreen';
import { QuizScreen } from './components/QuizScreen';
import { ResultsScreen } from './components/ResultsScreen';
import { calculateAttemptResult, selectQuestions } from './services/quizEngine';
import { storage } from './services/storage';
import { AttemptResult, Question, QuizSessionState } from './types/quiz';
import { ScreenId } from './types/shell';

export const App: React.FC = () => {
  const [screen, setScreen] = useState<'landing' | 'quiz' | 'results'>('landing');
  const [session, setSession] = useState<QuizSessionState | null>(null);
  const [lastResult, setLastResult] = useState<AttemptResult | null>(null);
  const [isHistoryOpen, setIsHistoryOpen] = useState<boolean>(false);
  const [isLoading, setIsLoading] = useState<boolean>(false);
  const [hasActiveSavedSession, setHasActiveSavedSession] = useState<boolean>(false);
  const [selectedLab, setSelectedLab] = useState<'lab1' | 'lab2' | 'mixed'>('lab1');

  // Check for existing active session on mount
  useEffect(() => {
    const active = storage.getActiveSession();
    if (active && !active.isCompleted && active.questions && active.questions.length > 0) {
      setHasActiveSavedSession(true);
    }
  }, []);

  // Start new randomized quiz with user-selected question count (5, 10, or 20)
  const handleStartQuiz = async (
    labType: 'lab1' | 'lab2' | 'mixed',
    timerDurationSeconds: number | null,
    questionCount: number = 10
  ) => {
    setIsLoading(true);
    try {
      const questions = await selectQuestions(labType, questionCount);

      const newSession: QuizSessionState = {
        questions,
        currentIndex: 0,
        userAnswers: {},
        flaggedQuestionIds: [],
        timeRemainingSeconds: timerDurationSeconds,
        initialDurationSeconds: timerDurationSeconds,
        timerStartedAtTimestamp: timerDurationSeconds ? Date.now() : null,
        isCompleted: false,
        labType,
      };

      storage.saveActiveSession(newSession);
      setSession(newSession);
      setScreen('quiz');
      setHasActiveSavedSession(true);
    } catch (err) {
      console.error('Error starting quiz:', err);
      alert('Error al cargar el banco de preguntas. Por favor recarga la página.');
    } finally {
      setIsLoading(false);
    }
  };

  // Resume unfinished session
  const handleResumeQuiz = () => {
    const saved = storage.getActiveSession();
    if (saved && !saved.isCompleted) {
      setSession(saved);
      setScreen('quiz');
    }
  };

  // Answer selection handler
  const handleAnswerChange = (questionId: string, selectedOptionIds: string[]) => {
    if (!session) return;
    const updatedSession: QuizSessionState = {
      ...session,
      userAnswers: {
        ...session.userAnswers,
        [questionId]: selectedOptionIds,
      },
    };
    setSession(updatedSession);
    storage.saveActiveSession(updatedSession);
  };

  // Toggle flag for later review
  const handleToggleFlag = (questionId: string) => {
    if (!session) return;
    const isCurrentlyFlagged = session.flaggedQuestionIds.includes(questionId);
    const updatedFlags = isCurrentlyFlagged
      ? session.flaggedQuestionIds.filter(id => id !== questionId)
      : [...session.flaggedQuestionIds, questionId];

    const updatedSession: QuizSessionState = {
      ...session,
      flaggedQuestionIds: updatedFlags,
    };
    setSession(updatedSession);
    storage.saveActiveSession(updatedSession);
  };

  // Navigate between questions
  const handleNavigateTo = (index: number) => {
    if (!session) return;
    const updatedSession: QuizSessionState = {
      ...session,
      currentIndex: index,
    };
    setSession(updatedSession);
    storage.saveActiveSession(updatedSession);
  };

  // Timer tick update
  const handleTimerTick = (remaining: number) => {
    if (!session) return;
    // Update local state without excessively spamming localStorage
    setSession(prev => (prev ? { ...prev, timeRemainingSeconds: remaining } : null));
  };

  // Finish and grade quiz
  const handleFinishQuiz = () => {
    if (!session) return;

    let timeTakenSeconds = 0;
    if (session.timerStartedAtTimestamp) {
      timeTakenSeconds = Math.max(1, Math.floor((Date.now() - session.timerStartedAtTimestamp) / 1000));
      if (session.initialDurationSeconds) {
        timeTakenSeconds = Math.min(session.initialDurationSeconds, timeTakenSeconds);
      }
    } else {
      timeTakenSeconds = 60; // fallback if no timer
    }

    const username = storage.getUsername() || 'Estudiante';
    const result = calculateAttemptResult(
      username,
      session.labType,
      session.questions,
      session.userAnswers,
      timeTakenSeconds
    );

    storage.saveAttempt(result);
    setLastResult(result);
    setSession(null);
    setHasActiveSavedSession(false);
    setScreen('results');
  };

  // Abandon attempt
  const handleQuitQuiz = () => {
    storage.clearActiveSession();
    setSession(null);
    setHasActiveSavedSession(false);
    setScreen('landing');
  };

  // Retry only wrong questions from previous attempt
  const handleRetryWrong = async (wrongQuestions: Question[]) => {
    setIsLoading(true);
    try {
      const shuffledOptionsQuestions = await selectQuestions(
        lastResult?.labType || 'mixed',
        wrongQuestions.length,
        wrongQuestions
      );

      // Give 1 minute per question for the retry attempt
      const timerDuration = wrongQuestions.length * 60;

      const newSession: QuizSessionState = {
        questions: shuffledOptionsQuestions,
        currentIndex: 0,
        userAnswers: {},
        flaggedQuestionIds: [],
        timeRemainingSeconds: timerDuration,
        initialDurationSeconds: timerDuration,
        timerStartedAtTimestamp: Date.now(),
        isCompleted: false,
        labType: lastResult?.labType || 'mixed',
      };

      storage.saveActiveSession(newSession);
      setSession(newSession);
      setScreen('quiz');
      setHasActiveSavedSession(true);
    } catch (err) {
      console.error('Error retrying wrong questions:', err);
    } finally {
      setIsLoading(false);
    }
  };

  const handleSelectLab = (lab: 'all' | 'lab1' | 'lab2') => {
    const mapped = lab === 'all' ? 'mixed' : lab;
    setSelectedLab(mapped);
    if (screen !== 'landing') {
      setScreen('landing');
    }
  };

  // Retry failed questions from a past attempt selected in HistoryModal
  const handleRetryAttemptFailed = async (
    failedQuestions: Question[],
    labType: 'lab1' | 'lab2' | 'mixed'
  ) => {
    setIsLoading(true);
    try {
      const shuffledOptionsQuestions = await selectQuestions(
        labType,
        failedQuestions.length,
        failedQuestions
      );

      const timerDuration = failedQuestions.length * 60;

      const newSession: QuizSessionState = {
        questions: shuffledOptionsQuestions,
        currentIndex: 0,
        userAnswers: {},
        flaggedQuestionIds: [],
        timeRemainingSeconds: timerDuration,
        initialDurationSeconds: timerDuration,
        timerStartedAtTimestamp: Date.now(),
        isCompleted: false,
        labType,
      };

      storage.saveActiveSession(newSession);
      setSession(newSession);
      setScreen('quiz');
      setHasActiveSavedSession(true);
    } catch (err) {
      console.error('Error retrying attempt failed questions:', err);
    } finally {
      setIsLoading(false);
    }
  };

  const handleViewAttemptInResults = (attempt: AttemptResult) => {
    setLastResult(attempt);
    setScreen('results');
  };

  const currentShellScreen = screen === 'landing' ? 'home' : screen;
  const handleShellNavigate = (target: ScreenId) => {
    if (target === 'history') {
      setIsHistoryOpen(true);
    } else if (target === 'home') {
      setScreen('landing');
    } else if (target === 'quiz' || target === 'results') {
      setScreen(target);
    }
  };

  return (
    <>
      <AmbientBackground />
      <AppShell
        currentScreen={currentShellScreen}
        onNavigate={handleShellNavigate}
        examInProgress={screen === 'quiz' && !!session}
        onQuitExam={handleQuitQuiz}
        onOpenHistory={() => setIsHistoryOpen(true)}
        activeLab={selectedLab === 'mixed' ? 'all' : selectedLab}
        onSelectLab={handleSelectLab}
        title="PrepLab SSDD"
        subtitle="Banco Oficial de 520 Preguntas"
      >
        {isLoading && (
          <div style={{ textAlign: 'center', padding: '60px 20px', color: 'var(--venus-text-muted)' }}>
            <div style={{ fontSize: '2.5rem', marginBottom: '16px', animation: 'spin 1s infinite linear' }}>⚡</div>
            <p style={{ fontWeight: 600 }}>Cargando y preparando el simulacro de examen...</p>
          </div>
        )}

        {!isLoading && screen === 'landing' && (
          <LandingScreen
            onStartQuiz={handleStartQuiz}
            onResumeQuiz={handleResumeQuiz}
            hasActiveSession={hasActiveSavedSession}
            onOpenHistory={() => setIsHistoryOpen(true)}
            selectedLab={selectedLab}
            onSelectLab={setSelectedLab}
          />
        )}

        {!isLoading && screen === 'quiz' && session && (
          <QuizScreen
            session={session}
            onAnswerChange={handleAnswerChange}
            onToggleFlag={handleToggleFlag}
            onNavigateTo={handleNavigateTo}
            onFinishQuiz={handleFinishQuiz}
            onQuitQuiz={handleQuitQuiz}
            onTimerTick={handleTimerTick}
          />
        )}

        {!isLoading && screen === 'results' && lastResult && (
          <ResultsScreen
            result={lastResult}
            onRetryWrong={handleRetryWrong}
            onNewQuiz={() => setScreen('landing')}
            onHome={() => setScreen('landing')}
            onOpenHistory={() => setIsHistoryOpen(true)}
          />
        )}

        {/* History & Weaknesses Modal */}
        <HistoryModal
          isOpen={isHistoryOpen}
          onClose={() => setIsHistoryOpen(false)}
          onRetryAttemptFailed={handleRetryAttemptFailed}
          onViewInResultsScreen={handleViewAttemptInResults}
        />
      </AppShell>
    </>
  );
};
