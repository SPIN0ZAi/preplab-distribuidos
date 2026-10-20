// src/services/quizEngine.ts
import { AttemptResult, Question, QuestionType } from '../types/quiz';
import { storage } from './storage';

// In-memory cache for dynamically imported question banks
let lab1Cache: Question[] | null = null;
let lab2Cache: Question[] | null = null;

export async function loadLab1Questions(): Promise<Question[]> {
  if (lab1Cache) return lab1Cache;
  const module = await import('../data/lab1.json');
  lab1Cache = ((module.default || module) as unknown) as Question[];
  return lab1Cache;
}

export async function loadLab2Questions(): Promise<Question[]> {
  if (lab2Cache) return lab2Cache;
  const module = await import('../data/lab2.json');
  lab2Cache = ((module.default || module) as unknown) as Question[];
  return lab2Cache;
}

// Fisher-Yates shuffle helper
function shuffleArray<T>(array: T[]): T[] {
  const arr = [...array];
  for (let i = arr.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [arr[i], arr[j]] = [arr[j], arr[i]];
  }
  return arr;
}

// Weighted random selection without replacement
function weightedSampleWithoutReplacement<T extends { id: string }>(
  pool: T[],
  weights: Map<string, number>,
  k: number
): T[] {
  if (pool.length <= k) return shuffleArray(pool);

  const selected: T[] = [];
  const remaining = [...pool];

  for (let step = 0; step < k; step++) {
    if (remaining.length === 0) break;

    // Calculate sum of weights for remaining items
    let totalWeight = 0;
    for (const item of remaining) {
      totalWeight += weights.get(item.id) || 1.0;
    }

    let r = Math.random() * totalWeight;
    let chosenIndex = remaining.length - 1;

    for (let i = 0; i < remaining.length; i++) {
      const w = weights.get(remaining[i].id) || 1.0;
      if (r <= w) {
        chosenIndex = i;
        break;
      }
      r -= w;
    }

    selected.push(remaining[chosenIndex]);
    remaining.splice(chosenIndex, 1);
  }

  return selected;
}

export async function selectQuestions(
  labType: 'lab1' | 'lab2' | 'mixed',
  count = 20,
  overrideQuestions?: Question[]
): Promise<Question[]> {
  if (overrideQuestions && overrideQuestions.length > 0) {
    // Shuffle options for override questions
    return overrideQuestions.map(q => ({
      ...q,
      options: shuffleArray(q.options),
    }));
  }

  const seenIds = storage.getSeenQuestionIds();
  const pastWrongIds = storage.getPastIncorrectQuestionIds();

  const getWeight = (qId: string): number => {
    if (!seenIds.has(qId)) return 3.0; // Unseen questions get highest priority
    if (pastWrongIds.has(qId)) return 2.5; // Previously incorrect questions get high priority
    return 1.0; // Previously correct questions get normal priority
  };

  let selected: Question[] = [];

  if (labType === 'lab1') {
    const bank = await loadLab1Questions();
    const weights = new Map<string, number>();
    bank.forEach(q => weights.set(q.id, getWeight(q.id)));
    selected = weightedSampleWithoutReplacement(bank, weights, count);
  } else if (labType === 'lab2') {
    const bank = await loadLab2Questions();
    const weights = new Map<string, number>();
    bank.forEach(q => weights.set(q.id, getWeight(q.id)));
    selected = weightedSampleWithoutReplacement(bank, weights, count);
  } else {
    // Mixed: select half from Lab 1, half from Lab 2
    const halfCount = Math.floor(count / 2);
    const bank1 = await loadLab1Questions();
    const bank2 = await loadLab2Questions();

    const weights1 = new Map<string, number>();
    bank1.forEach(q => weights1.set(q.id, getWeight(q.id)));
    const selected1 = weightedSampleWithoutReplacement(bank1, weights1, halfCount);

    const weights2 = new Map<string, number>();
    bank2.forEach(q => weights2.set(q.id, getWeight(q.id)));
    const selected2 = weightedSampleWithoutReplacement(bank2, weights2, count - halfCount);

    // Merge and shuffle the mixed set
    selected = shuffleArray([...selected1, ...selected2]);
  }

  // Shuffle options for each question so answers aren't predictable by position
  return selected.map(q => ({
    ...q,
    options: shuffleArray(q.options),
  }));
}

export function isAnswerCorrect(
  type: QuestionType,
  correctOptionIds: string[],
  userSelectedOptionIds: string[] | undefined
): boolean {
  if (!userSelectedOptionIds || userSelectedOptionIds.length === 0) {
    return false;
  }

  if (type === 'single' || type === 'truefalse') {
    return (
      userSelectedOptionIds.length === 1 &&
      correctOptionIds.includes(userSelectedOptionIds[0])
    );
  }

  if (type === 'multi') {
    if (userSelectedOptionIds.length !== correctOptionIds.length) return false;
    const userSet = new Set(userSelectedOptionIds);
    return correctOptionIds.every(id => userSet.has(id));
  }

  return false;
}

export function calculateAttemptResult(
  username: string,
  labType: 'lab1' | 'lab2' | 'mixed',
  questions: Question[],
  userAnswers: Record<string, string[]>,
  timeTakenSeconds: number
): AttemptResult {
  let score = 0;
  const questionResults = questions.map(q => {
    const selected = userAnswers[q.id] || [];
    const correct = isAnswerCorrect(q.type, q.correct, selected);
    if (correct) score++;
    return {
      question: q,
      selectedAnswers: selected,
      isCorrect: correct,
    };
  });

  const totalQuestions = questions.length;
  const percentage = totalQuestions > 0 ? Math.round((score / totalQuestions) * 100) : 0;

  // Topic breakdown
  const topicStats: Record<string, { total: number; correct: number }> = {};
  for (const qr of questionResults) {
    const t = qr.question.topic || 'General';
    if (!topicStats[t]) {
      topicStats[t] = { total: 0, correct: 0 };
    }
    topicStats[t].total++;
    if (qr.isCorrect) {
      topicStats[t].correct++;
    }
  }

  const result: AttemptResult = {
    id: `attempt_${Date.now()}_${Math.random().toString(36).substring(2, 7)}`,
    date: new Date().toISOString(),
    username: username || 'Estudiante',
    labType,
    score,
    totalQuestions,
    percentage,
    timeTakenSeconds,
    questionResults,
    topicStats,
  };

  return result;
}
