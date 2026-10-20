# Clarifications: Unit 005 — Inset App Shell

## Clarification Log

### C001: Should the App Shell use React Router or state-based view switching?
- **Decision**: The existing application uses state-based routing (`currentScreen: 'home' | 'quiz' | 'results' | 'history'`). The App Shell will bind to these states and provide navigation handlers without introducing an external routing library, maintaining 100% zero-regression backward compatibility and avoiding bundle inflation.
- **Rationale**: Preserves all 520 questions, active quiz session timers, and localStorage persistence without rewriting the application controller.

### C002: How does the sidebar behave during an active quiz session?
- **Decision**: During an active quiz session, the sidebar shows an "Exam in Progress" lock state with a prominent "Quit / Pause Exam" confirmation trigger, preventing accidental navigation and data loss while still displaying current progress.
- **Rationale**: Direct adherence to Principle 4 (Zero-Regression Functional Integrity).

### C003: How is content padding handled to prevent bottom nav pill overlap on mobile?
- **Decision**: The main scrollable container on mobile will have `padding-bottom: 96px;` ensuring that all questions, choices, action buttons, and explanations scroll completely above the floating bottom pill.
