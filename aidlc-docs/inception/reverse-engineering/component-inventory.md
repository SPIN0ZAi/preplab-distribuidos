# Reverse Engineering: Component Inventory

## Inventory Matrix

| Component | File Path | Type | Props Interface | Key Internal State | Dependencies |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **App** | `src/App.tsx` | Container / State Machine | None (Root) | `screen`, `session`, `lastResult`, `isHistoryOpen`, `isLoading`, `hasActiveSavedSession` | `LandingScreen`, `QuizScreen`, `ResultsScreen`, `HistoryModal`, `storage`, `quizEngine` |
| **LandingScreen** | `src/components/LandingScreen.tsx` | View | `onStartQuiz`, `onResumeQuiz`, `hasActiveSession`, `onOpenHistory` | `username`, `selectedLab`, `timerPreset`, `isCustomTimer`, `customMinutes` | `storage`, `types/quiz` |
| **QuizScreen** | `src/components/QuizScreen.tsx` | View | `session`, `onAnswerChange`, `onToggleFlag`, `onNavigateTo`, `onFinishQuiz`, `onQuitQuiz`, `onTimerTick` | `showConfirmModal`, `showQuitModal` | `Timer`, `types/quiz` |
| **Timer** | `src/components/Timer.tsx` | Widget | `initialDurationSeconds`, `remainingSeconds`, `startedAtTimestamp`, `onTick`, `onExpire` | `secondsLeft` | `types/quiz` |
| **ResultsScreen** | `src/components/ResultsScreen.tsx` | View | `result`, `onRetryWrong`, `onNewQuiz`, `onHome`, `onOpenHistory` | `filter` ('all' \| 'wrong' \| 'correct') | `types/quiz` |
| **HistoryModal** | `src/components/HistoryModal.tsx` | Overlay | `isOpen`, `onClose` | `activeTab` ('history' \| 'weaknesses'), `showClearConfirm` | `storage`, `types/quiz` |

---

## Detailed Component Specifications

### 1. `App.tsx`
- **Role**: Coordinates screen transitions between `'landing'`, `'quiz'`, and `'results'`.
- **Invariants**:
  - Automatically loads incomplete sessions from `storage.getActiveSession()` on mount.
  - Ensures question banks are loaded dynamically without blocking initial render.
  - Manages the opening/closing of the global `HistoryModal`.

### 2. `LandingScreen.tsx`
- **Role**: Entry screen where the student inputs their name, chooses an exam mode (Lab 1, Lab 2, Mixto), selects a timer duration, and launches or resumes attempts.
- **Controls**:
  - Mode selector cards (3 cards: P1 Docker, P2 gRPC, Mixto).
  - Timer preset pills (Off, 10 min, 20 min, 30 min, 45 min, 60 min, Custom input).
  - Active session resume banner (shown conditionally if `hasActiveSession === true`).
  - History launcher button.

### 3. `QuizScreen.tsx`
- **Role**: Interactive test runner for the 20 selected questions.
- **Sub-elements**:
  - Sticky/top progress row with question number, topic tag, difficulty pill, flag button, and timer countdown.
  - 20-question navigation bar with pill buttons reflecting answer status (unanswered, answered, flagged, current active).
  - Question card with question statement and option choices.
  - Bottom action bar: Previous, Next, Entregar Examen, Abandonar.
  - Two modal sheets: Submission confirmation (warns about unanswered questions) and Abandon confirmation.

### 4. `Timer.tsx`
- **Role**: Displays remaining time, pulses amber/red when time < 60 seconds, and invokes `onExpire()` at 0 seconds to auto-submit.
- **Invariants**:
  - Uses `Date.now() - startedAtTimestamp` to ensure exactness regardless of browser throttling.

### 5. `ResultsScreen.tsx`
- **Role**: Post-exam score breakdown and deep pedagogical review.
- **Sub-elements**:
  - Score badge circle (displays score/20, percentage, and pass/fail indicator based on 50% threshold).
  - Quick summary stat boxes (Mode, Time, Correct, Incorrect).
  - Action buttons: "Reintentar preguntas falladas", "Nuevo intento", "Historial y Debilidades", "Volver al inicio".
  - Filter bar: "Todas", "Falladas", "Acertadas".
  - Detailed review cards displaying:
    - User selection vs. correct answer.
    - Pedagogical explanation (`explanation.correct`).
    - Distractor analysis (`explanation.wrong[optId]`) detailing why each incorrect alternative is wrong.

### 6. `HistoryModal.tsx`
- **Role**: Slide-in / popover dialog presenting attempt history and topic weakness analytics.
- **Sub-elements**:
  - Tab 1 (Historial): List of past exam runs with timestamp, duration, score badge, and pass/fail tag.
  - Tab 2 (Debilidades por Tema): Table of topics sorted by lowest percentage first, featuring color-coded progress bars (red < 60%, yellow 60–79%, green ≥ 80%).
  - Action to clear history with double-confirmation prompt.
