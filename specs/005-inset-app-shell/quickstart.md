# Quickstart: Unit 005 — Inset App Shell

## Usage Example

```tsx
import { AppShell } from './components/shell/AppShell';

export function App() {
  const [currentScreen, setCurrentScreen] = useState<ScreenId>('home');
  const [examInProgress, setExamInProgress] = useState(false);

  return (
    <AppShell
      currentScreen={currentScreen}
      onNavigate={setCurrentScreen}
      examInProgress={examInProgress}
      onQuitExam={() => handleQuitExam()}
      title="Distributed Systems Exam Prep"
    >
      <main className="content-area">
        {currentScreen === 'home' && <HomeScreen />}
        {currentScreen === 'quiz' && <QuizScreen />}
        {currentScreen === 'results' && <ResultsScreen />}
      </main>
    </AppShell>
  );
}
```
