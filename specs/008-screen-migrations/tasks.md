# Atomic Tasks: Unit 008 — Screen Migrations

## Dependency Graph
```
T031 [Screen Contracts] ──> T032 [LandingScreen] ──> T033 [QuizScreen] ──> T034 [ResultsScreen] ──> T035 [App.tsx Integration & Build]
```

---

## Detailed Tasks Matrix

### T031: Verify Screen Interface Contracts
- **File**: `src/types/screens.ts`
- **Requirement Link**: `FR-006`, `NFR-011`
- **Estimated Effort**: 15 mins
- **Description**: Ensure all screen prop types and callback signatures are typed and exported cleanly.
- **Definition of Done**: Clean TypeScript compilation with zero type errors.

### T032: Modernize `LandingScreen.tsx` & Build `landing-screen.css`
- **Files**: `src/styles/screens/landing-screen.css`, `src/components/LandingScreen.tsx`
- **Requirement Link**: `FR-001`, `FR-002`, `FR-003`, `FR-005`
- **Estimated Effort**: 90 mins
- **Description**: Rebuild `LandingScreen` with Venus dashboard builder grid: 4 stat metric cards with icons, weekly activity `RoundedBarChart`, topic mastery `AreaSparkline`, and three interactive exam launcher cards with `Button`.
- **Definition of Done**: Landing screen renders with Venus soft-UI cards and charts; quiz launch handlers work.

### T033: Modernize `QuizScreen.tsx` & Build `quiz-screen.css`
- **Files**: `src/styles/screens/quiz-screen.css`, `src/components/QuizScreen.tsx`
- **Requirement Link**: `FR-001`, `FR-002`, `FR-006`, `NFR-001`, `NFR-006`
- **Estimated Effort**: 90 mins
- **Description**: Rebuild `QuizScreen` following Rule 10 (Glass Discipline): Solid `#FFFFFF` question card, selectable option cards with active indigo tint and check indicators, code snippet styling, sticky bottom glass toolbar with timer and navigation, and question drawer pill navigation.
- **Definition of Done**: Exam timer ticks accurately; answers update state; flag toggle works; finish confirmation works.

### T034: Modernize `ResultsScreen.tsx` & Build `results-screen.css`
- **Files**: `src/styles/screens/results-screen.css`, `src/components/ResultsScreen.tsx`
- **Requirement Link**: `FR-001`, `FR-002`, `FR-005`, `NFR-006`
- **Estimated Effort**: 90 mins
- **Description**: Rebuild `ResultsScreen` with `CircularGauge` score hero card, breakdown metric chips, retry incorrect questions trigger, and filterable question review deck.
- **Definition of Done**: Results calculate accurately; retry wrong questions filters correctly; question review displays explanations.

### T035: Integrate Root `App.tsx` & Production Build Verification
- **Files**: `src/App.tsx`, `src/styles/theme.css`
- **Requirement Link**: `FR-001`, `FR-006`, `NFR-009`
- **Estimated Effort**: 45 mins
- **Description**: Wrap root view in `<AppShell>`, link sidebar and mobile nav state to screen transitions, import all screen CSS files in `theme.css`, run `npm run build`, and confirm bundle size budget $< 200\text{ KB}$ gzipped.
- **Definition of Done**: Entire application compiles cleanly; 520 questions verified; all transitions functional.
