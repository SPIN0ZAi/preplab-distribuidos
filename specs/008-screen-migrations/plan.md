# Construction Plan: Unit 008 — Screen Migrations

## 1. Architectural Strategy
Migrate each screen sequentially, linking them into `AppShell` in `src/App.tsx`:
```
src/
├── components/
│   ├── LandingScreen.tsx (Venus dashboard grid & activity charts)
│   ├── QuizScreen.tsx (High-contrast solid cards + glass sticky actions)
│   ├── ResultsScreen.tsx (Circular score gauge & review deck)
│   └── App.tsx (Root orchestrator wrapped in AppShell)
└── styles/
    └── screens/
        ├── landing-screen.css
        ├── quiz-screen.css
        └── results-screen.css
```

## 2. Execution Phases
1. **Screen Contracts (`T031`)**: Verify and define any screen interface updates in `src/types/screens.ts`.
2. **LandingScreen Modernization (`T032`)**: Author `landing-screen.css` and rebuild `LandingScreen.tsx` with stat cards, `RoundedBarChart`, and lab launchers.
3. **QuizScreen Modernization (`T033`)**: Author `quiz-screen.css` and rebuild `QuizScreen.tsx` with solid question cards, radio choices, glass toolbars, and question drawer.
4. **ResultsScreen Modernization (`T034`)**: Author `results-screen.css` and rebuild `ResultsScreen.tsx` with `CircularGauge` and answer review.
5. **Root App.tsx Integration & Production Build (`T035`)**: Mount `AppShell` around the active screen, wire sidebar/topbar state handlers, run `npm run build`, and confirm bundle size budget $< 200\text{ KB}$ gzipped.
