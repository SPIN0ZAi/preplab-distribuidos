export type Difficulty = 'easy' | 'medium' | 'hard';
export type QuestionType = 'single' | 'multi' | 'truefalse';

export interface Option {
  id: string;
  text: string;
}

export interface QuestionExplanation {
  correct: string;
  wrong: Record<string, string>;
}

export interface Question {
  id: string;
  lab: 1 | 2;
  topic: string;
  difficulty: Difficulty;
  type: QuestionType;
  question: string;
  options: Option[];
  correct: string[];
  explanation: QuestionExplanation;
  source: string;
}

export interface QuizSessionState {
  questions: Question[];
  currentIndex: number;
  userAnswers: Record<string, string[]>; // questionId -> array of selected optionIds
  flaggedQuestionIds: string[];
  timeRemainingSeconds: number | null; // null if timer is turned off
  initialDurationSeconds: number | null;
  timerStartedAtTimestamp: number | null;
  isCompleted: boolean;
  labType: 'lab1' | 'lab2' | 'mixed';
}

export interface AttemptResult {
  id: string;
  date: string;
  username: string;
  labType: 'lab1' | 'lab2' | 'mixed';
  score: number;
  totalQuestions: number;
  percentage: number;
  timeTakenSeconds: number;
  questionResults: {
    question: Question;
    selectedAnswers: string[];
    isCorrect: boolean;
  }[];
  topicStats: Record<string, { total: number; correct: number }>;
}

export type TimerPreset = 0 | 600 | 1200 | 1800 | 2700 | 3600; // 0 = off, 10, 20, 30, 45, 60 min
