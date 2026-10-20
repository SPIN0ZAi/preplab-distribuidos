# Quickstart: Unit 008 — Screen Migrations

## Overview

The three primary screens integrate into `AppShell`:
```tsx
<AppShell
  currentScreen={screen}
  onNavigate={(s) => setScreen(s)}
  examInProgress={screen === 'quiz' && !!session}
  onQuitExam={handleQuitQuiz}
  onOpenHistory={() => setIsHistoryOpen(true)}
>
  {screen === 'landing' && <LandingScreen ... />}
  {screen === 'quiz' && <QuizScreen ... />}
  {screen === 'results' && <ResultsScreen ... />}
</AppShell>
```
