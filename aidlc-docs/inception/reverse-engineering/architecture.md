# Reverse Engineering: Architecture & Data Flow

## 1. System Topology Overview

The application is a single-page web application (SPA) built on **React 18.3**, **TypeScript 5.6**, and **Vite 5.4**. It operates as a 100% client-side, zero-backend, statically deployable architecture hosted on Vercel.

```mermaid
graph TD
    subgraph UI_Layer [User Interface Layer]
        App[App.tsx - Finite State Machine]
        Landing[LandingScreen.tsx]
        Quiz[QuizScreen.tsx]
        Results[ResultsScreen.tsx]
        Timer[Timer.tsx]
        History[HistoryModal.tsx]
        App --> Landing
        App --> Quiz
        App --> Results
        App --> History
        Quiz --> Timer
    end

    subgraph Service_Layer [Domain Services Layer]
        Engine[quizEngine.ts]
        Storage[storage.ts]
    end

    subgraph Data_Layer [Data & Persistence Layer]
        Lab1Data[src/data/lab1.json - 260 Questions]
        Lab2Data[src/data/lab2.json - 260 Questions]
        LocalStorage[(Browser localStorage)]
    end

    Landing -->|Start / Resume| App
    Quiz -->|Answer, Flag, Finish| App
    Results -->|Retry Wrong, New Quiz| App
    History -->|View History / Weaknesses| App

    App -->|Generate Question Set| Engine
    App -->|Evaluate Scores| Engine
    App -->|Read / Write Sessions & Attempts| Storage

    Engine -.->|Dynamic import on demand| Lab1Data
    Engine -.->|Dynamic import on demand| Lab2Data
    Storage <-->|Synchronous JSON Storage| LocalStorage
```

---

## 2. Finite State Machine (Screen Lifecycle)

The root state machine resides in `src/App.tsx`:

```mermaid
stateDiagram-v2
    [*] --> Landing: App Mount
    Landing --> Quiz: onStartQuiz(labType, duration)
    Landing --> Quiz: onResumeQuiz() [If saved session exists]
    
    state Quiz {
        [*] --> AnsweringQuestion
        AnsweringQuestion --> NavigateQuestion: onNavigateTo(index)
        AnsweringQuestion --> ToggleFlag: onToggleFlag(qId)
        AnsweringQuestion --> UpdateAnswer: onAnswerChange(qId, selectedIds)
        AnsweringQuestion --> TimerTick: onTimerTick(remaining)
        AnsweringQuestion --> SubmitModalPrompt: onFinishQuiz()
        SubmitModalPrompt --> QuitModalPrompt: onQuitQuiz()
    }

    Quiz --> Results: Confirm Submit / Timer Auto-Submit
    Quiz --> Landing: Confirm Abandon / Quit
    
    state Results {
        [*] --> ReviewScores
        ReviewScores --> FilterReview: Filter (All / Wrong / Correct)
    }

    Results --> Landing: onHome() / onNewQuiz()
    Results --> Quiz: onRetryWrong(wrongQuestions)

    state HistoryModalOverlay {
        [*] --> AttemptList
        AttemptList --> WeaknessTable: Switch Tab
        WeaknessTable --> ClearDataPrompt: Clear History
    }

    Landing --> HistoryModalOverlay: Open History
    Quiz --> HistoryModalOverlay: Open History (from topbar)
    Results --> HistoryModalOverlay: Open History
```

---

## 3. Data Flow & State Contracts

### 3.1 Question Bank Streaming (Lazy Chunks)
To satisfy the <200 KB initial bundle budget, `lab1.json` (260 questions) and `lab2.json` (260 questions) are dynamically loaded via `import('../data/lab1.json')` and `import('../data/lab2.json')` only when the user starts a quiz. They are cached in-memory in `quizEngine.ts`.

### 3.2 Sampling Algorithm
`selectQuestions(labType, count)` applies a weighted sampling algorithm without replacement:
- **Unseen questions** (never attempted): weight **3.0**
- **Previously incorrect questions**: weight **2.5**
- **Previously correct questions**: weight **1.0**
- Fisher-Yates shuffle is executed on both the selected question set and each question's `options` array.

### 3.3 Timer Synchronization & Resilience
Rather than relying on naive `setInterval` countdowns that freeze when the browser tab is backgrounded, `Timer.tsx` and `storage.ts` store `timerStartedAtTimestamp` (epoch ms) and `initialDurationSeconds`. Upon re-render or page reload, elapsed time is computed as:
$$\text{elapsed} = \lfloor(\text{Date.now()} - \text{timerStartedAtTimestamp}) / 1000\rfloor$$
$$\text{remaining} = \max(0, \text{initialDurationSeconds} - \text{elapsed})$$

### 3.4 Local Storage Schema
| Key | Type | Purpose |
| :--- | :--- | :--- |
| `ds_quiz_username` | `string` | Display name for student attempts. |
| `ds_quiz_active_session` | `QuizSessionState` | JSON serialization of active exam, answers, flags, and timestamp. |
| `ds_quiz_attempt_history` | `AttemptResult[]` | Array of completed attempts (max 100 entries). |
| `ds_quiz_timer_preset` | `number` | Preset in seconds (0, 600, 1200, 1800, 2700, 3600). |
| `ds_quiz_custom_timer_minutes`| `number` | Custom countdown minutes when preset is overridden. |
