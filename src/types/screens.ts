// src/types/screens.ts
import { AttemptResult, QuizSessionState } from './quiz';

export interface LandingScreenProps {
  onStartQuiz: (labType: 'lab1' | 'lab2' | 'mixed', timerDurationSeconds: number | null) => void;
  onResumeQuiz: () => void;
  hasActiveSession: boolean;
  onOpenHistory: () => void;
  selectedLab?: 'lab1' | 'lab2' | 'mixed';
  onSelectLab?: (lab: 'lab1' | 'lab2' | 'mixed') => void;
}

export interface QuizScreenProps {
  session: QuizSessionState;
  onAnswerChange: (questionId: string, answer: string | string[]) => void;
  onToggleFlag: (questionId: string) => void;
  onNavigateTo: (index: number) => void;
  onFinishQuiz: () => void;
  onQuitQuiz: () => void;
  onTimerTick: (remainingSeconds: number) => void;
}

export interface ResultsScreenProps {
  result: AttemptResult;
  onRetryWrong: () => void;
  onNewQuiz: () => void;
  onHome: () => void;
  onOpenHistory: () => void;
}
