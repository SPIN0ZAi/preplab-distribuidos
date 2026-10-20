# Clarifications: Unit 008 — Screen Migrations

## Clarification Log

### C001: Will quiz timer or question randomization algorithms be altered?
- **Decision**: No. The underlying quiz engine functions (`selectQuestions`, `calculateAttemptResult`, `storage`) remain 100% untouched. All question banks (520 questions across Lab 1 and Lab 2) are verified and preserved with zero changes.

### C002: How does the application preserve existing quiz sessions during a reload?
- **Decision**: The existing `storage.getActiveSession()` mechanism in `App.tsx` is preserved completely. The user can resume an active session from either the Landing Screen banner or the Sidebar "Active Exam" item.

### C003: Where are the screen-specific CSS stylesheets located?
- **Decision**: To avoid massive monolithic CSS files, screen styles will be authored in `src/styles/screens/landing-screen.css`, `src/styles/screens/quiz-screen.css`, and `src/styles/screens/results-screen.css` and imported cleanly into `src/styles/theme.css`.
