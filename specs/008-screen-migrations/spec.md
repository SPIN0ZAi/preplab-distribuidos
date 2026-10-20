# Specification: Unit 008 — Screen Migrations (Landing, Quiz & Results)

## 1. Executive Summary
Unit U8 migrates the three primary screen components (`LandingScreen.tsx`, `QuizScreen.tsx`, `ResultsScreen.tsx`) and the root orchestrator (`App.tsx`) to the completed **Two-Layer Visual System**:
1. **Content Layer**: Follows the Figma "Venus Dashboard Builder" kit (`media_1792515753271.png`–`media_1792515764444.png`) — clean solid white cards (`#FFFFFF` in light mode, `#111827` in dark mode), diffuse indigo shadows, `Poppins` metric headlines, `RoundedBarChart` activity charts, and high-contrast typography.
2. **Chrome Layer**: Floating `AppShell` with Inset Glass Sidebar, Floating Topbar, and Mobile Navigation Pill utilizing the Liquid Glass material system.
3. **Rule 10 (Glass Discipline)**: All 520 questions, answer choices, code snippets, and explanations are strictly rendered on solid, opaque cards to guarantee $> 7:1$ contrast and zero visual fatigue.

---

## 2. Traceability & Requirements Mapping
| Screen Component | Requirements | User Stories | Non-Functional Requirements |
| :--- | :--- | :--- | :--- |
| `LandingScreen.tsx` | FR-001, FR-002, FR-003 | US-001, US-003, US-004 | NFR-006, NFR-008, NFR-009 |
| `QuizScreen.tsx` | FR-001, FR-002, FR-006 | US-005, US-006, US-008 | NFR-001, NFR-006, NFR-008 |
| `ResultsScreen.tsx` | FR-001, FR-002, FR-005 | US-007, US-009, US-010 | NFR-006, NFR-008, NFR-009 |
| `App.tsx` | FR-001, FR-006 | US-001 through US-010 | NFR-001, NFR-009 (< 200 KB gzipped) |

---

## 3. Screen Architectural Blueprints

### 3.1 LandingScreen (Venus Dashboard Grid)
- **Top Row - Metric Cards**:
  - Total Questions Card (520 Qs, 100% verified badge, Sparkles icon).
  - Lab 1 Docker & RPC Card (260 Qs, progress bar, Book icon).
  - Lab 2 gRPC & Raft Card (260 Qs, progress bar, Book icon).
  - Exam Streak & Average Score Card (Dynamic based on attempt history).
- **Middle Row - Charts & Analytics**:
  - Weekly Activity / Attempt Frequency with `RoundedBarChart` (with Electric Indigo highlighted active bar).
  - Topic Mastery curve with `AreaSparkline`.
- **Bottom Row - Exam Launch Deck**:
  - Three interactive mode cards with hover lift:
    1. **Lab 1 Simulation** (20 questions, 30 min, Docker/RPC).
    2. **Lab 2 Simulation** (20 questions, 30 min, gRPC/Consensus).
    3. **Full Comprehensive Exam** (20 questions randomized, 30 min).
  - Resume saved session banner if `hasActiveSession` is true.

### 3.2 QuizScreen (High-Contrast Solid Cards + Glass Toolbars)
- **Top Question Progress Bar**: Multi-step indicator bar with answered/flagged status.
- **Question Card**:
  - Solid card (`var(--venus-card-bg)`), 20px padding, 20px radius.
  - Header: Question index badge (e.g. `Pregunta 4 de 20`), Lab pill (`P1: Docker`), Difficulty pill (`Media`), Flag question toggle `<IconButton>`.
  - Question text: `var(--venus-text-headline)` in 17px font weight 600.
  - Options list: Each option is a full-width selectable card (`padding: 16px 20px`, radio circle icon, hover lift, keyboard selectable).
  - Explanation block (in review/practice mode): Luminous soft alert with checkmark and detailed concept breakdown.
- **Sticky Glass Bottom Toolbar**:
  - Next/Previous navigation buttons, Flag toggle, Question Drawer trigger pill, and Submit Exam button.

### 3.3 ResultsScreen (Celebration & Score Gauge)
- **Hero Card**:
  - `CircularGauge` showing score percentage.
  - Pass/Fail banner ("¡ENHORABUENA! HAS APROBADO" or "NECESITAS REPASAR").
  - Breakdown grid: Correct count, Incorrect count, Unanswered, Time spent.
- **Action Bar**:
  - Retry Incorrect Questions button (`Button variant="primary"`).
  - Start New Simulation button (`Button variant="secondary"`).
  - View Attempts History button (`Button variant="glass"`).
- **Detailed Question Review Deck**:
  - Filterable by: "All", "Only Incorrect", "Flagged".
  - Shows each question, user's answer, correct answer, and explanation.
