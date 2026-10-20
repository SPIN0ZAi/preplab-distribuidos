# Inception: User Stories & Acceptance Criteria

## 1. Persona Definitions

- **Persona P1: Alex (The Focused Engineering Student)**: 3rd-year CS student doing 45-minute timed exam simulations on a MacBook/laptop. Alex wants high visual clarity, zero distractions, glanceable weakness analytics, and deep pedagogical feedback on distractors.
- **Persona P2: Elena (The Mobile Commuter)**: Studying during transit on an iPhone/Android device. Elena wants responsive touch targets, smooth 60fps scrolling, instant question navigation, and minimal battery drain.
- **Persona P3: Marcos (The Accessibility-Conscious Learner)**: Uses keyboard navigation, high-contrast settings, and has `prefers-reduced-transparency` enabled on his OS to reduce eye fatigue.

---

## 2. User Stories Catalog

### Epic 1: Two-Layer Design System & Visual Atmosphere

#### US-001: Luminous Venus Light Mode with Liquid Glass Chrome
- **Story**: As Alex, I want the application to present a clean, airy Venus soft-UI theme with floating glass navigation, so that my study sessions feel modern, premium, and visually engaging.
- **Priority**: Must Have (M) | **Size**: M | **Traceability**: `FR-001`, `FR-004`, `NFR-006`
- **Acceptance Criteria**:
  - **Given** the user visits the application on a desktop browser,
  - **When** the page loads,
  - **Then** the background displays an ultra-light canvas (`#F4F7FE`) with subtle ambient gradient orbs,
  - **And** the sidebar and topbar float as translucent Liquid Glass surfaces with specular edge highlights,
  - **And** main content displays on solid white cards (`#FFFFFF`) with 20px–24px rounded corners and soft diffuse shadows.

#### US-002: Dual-Theme Toggle (Venus Light / Modern Dark)
- **Story**: As Alex, I want to switch effortlessly between Venus Light Mode and Dark Mode, so that I can study comfortably at night without glare.
- **Priority**: Should Have (S) | **Size**: S | **Traceability**: `FR-002`, `FR-003`
- **Acceptance Criteria**:
  - **Given** the application is running in Light Mode,
  - **When** the user clicks the theme toggle button in the floating topbar or sidebar,
  - **Then** the page transitions smoothly to Dark Mode within 200ms,
  - **And** all glass surfaces adapt their tint from translucent white to translucent deep navy (`rgba(17, 24, 39, 0.50)`),
  - **And** all text maintains WCAG 2.2 AA contrast compliance.

---

### Epic 2: Exam Initiation & Mode Selection (Landing Screen)

#### US-003: Venus-Styled Practice Mode Selection
- **Story**: As Alex, I want to clearly distinguish between Lab 1 (Docker), Lab 2 (gRPC), and Mixed mode cards, so that I can immediately launch the exact practice session I need.
- **Priority**: Must Have (M) | **Size**: M | **Traceability**: `FR-007`, `FR-008`
- **Acceptance Criteria**:
  - **Given** the user is on the Landing Screen,
  - **When** they view the practice mode cards,
  - **Then** each card displays an icon tile with colored glow, title, question count, and brief syllabus summary,
  - **When** the user clicks a card,
  - **Then** the selected card elevates with an active indigo border (`#4318FF`) and spring transition.

#### US-004: Incomplete Session Resumption
- **Story**: As Elena, I want to be alerted if I left an exam unfinished, so that I can resume immediately without losing my answers or remaining time.
- **Priority**: Must Have (M) | **Size**: S | **Traceability**: `FR-009`
- **Acceptance Criteria**:
  - **Given** an active session is saved in `localStorage`,
  - **When** Elena opens the application,
  - **Then** a prominent resume banner appears with the current question index, elapsed time, and a "Continuar intento" button,
  - **When** she clicks the button,
  - **Then** the Quiz Screen opens at the exact question where she left off with all prior answers preserved.

---

### Epic 3: Active Exam Execution & Interaction (Quiz Screen)

#### US-005: 20-Question Fluid Pill Navigator
- **Story**: As Elena, I want a glanceable question navigation bar, so that I can see at a glance which questions are answered, which are flagged, and quickly jump between them.
- **Priority**: Must Have (M) | **Size**: M | **Traceability**: `FR-010`, `FR-011`, `FR-012`
- **Acceptance Criteria**:
  - **Given** an active quiz session with 20 questions,
  - **When** Elena views the question navigator in the chrome layer,
  - **Then** unanswered questions show a subtle border,
  - **And** answered questions display an active indigo fill/indicator,
  - **And** flagged questions display an amber/coral flag icon,
  - **And** the currently viewed question has an illuminated halo,
  - **When** she taps pill 14,
  - **Then** the viewport immediately displays Question 14.

#### US-006: High-Contrast Solid Question & Option Cards
- **Story**: As Marcos, I want questions and option choices to be rendered on solid, high-contrast cards, so that I never have to strain to read complex code snippets or technical phrasing.
- **Priority**: Must Have (M) | **Size**: M | **Traceability**: `NFR-007`, `FR-001`
- **Acceptance Criteria**:
  - **Given** the user is on the Quiz Screen,
  - **When** examining question prompts and option choices,
  - **Then** the question and choices are rendered on 100% solid, opaque cards (`#FFFFFF` in light mode, `#111827` in dark mode),
  - **And** zero backdrop-filter blur is applied behind long-form text,
  - **And** text contrast is $\ge 7:1$ for prompt text.

#### US-007: Timestamp-Accurate Glass Timer & Alert Pulse
- **Story**: As Alex, I want a floating countdown timer that accurately tracks time and alerts me when 1 minute remains, so that I manage my pacing effectively.
- **Priority**: Must Have (M) | **Size**: S | **Traceability**: `FR-013`, `FR-014`, `NFR-004`
- **Acceptance Criteria**:
  - **Given** a timed quiz session,
  - **When** remaining time drops below 60 seconds,
  - **Then** the floating timer pill displays a warning border and rhythmic amber/red pulse,
  - **When** time reaches 0,
  - **Then** the exam is automatically submitted and scored without data loss.

---

### Epic 4: Results Review & Targeted Remediation (Results Screen)

#### US-008: Venus Score Summary & SVG Progress Gauge
- **Story**: As Alex, I want to see my score visualized as an engaging circular SVG meter and quick stat cards, so that I immediately understand my level of exam readiness.
- **Priority**: Must Have (M) | **Size**: M | **Traceability**: `FR-016`, `NFR-001`
- **Acceptance Criteria**:
  - **Given** a finished exam attempt,
  - **When** the Results Screen renders,
  - **Then** a circular SVG gauge displays the score out of 20 and percentage,
  - **And** a clear pass ($\ge 50\%$) or fail status badge is displayed,
  - **And** 4 Venus stat cards display Mode, Time Employed, Correct Count, and Fallos Count.

#### US-009: In-Depth Distractor Analysis & Review Filters
- **Story**: As Alex, I want to filter questions by "Solo Falladas" and read why each wrong option is invalid, so that I understand my mistakes and do not repeat them on the official exam.
- **Priority**: Must Have (M) | **Size**: L | **Traceability**: `FR-017`, `FR-018`
- **Acceptance Criteria**:
  - **Given** the Results Screen,
  - **When** Alex clicks "Solo Falladas" on the segmented filter pill,
  - **Then** only incorrect questions are displayed,
  - **And** each question item displays:
    1. The student's choice marked in red (`✗ Tu elección`),
    2. The correct choice marked in green (`✓ Respuesta correcta`),
    3. An explanation box explaining why the correct choice is valid (`explanation.correct`),
    4. Explicit itemized rationale explaining why each other distractor is invalid (`explanation.wrong[optId]`).

#### US-010: "Reintentar Falladas" Instant Drill
- **Story**: As Alex, I want a single-click action to immediately retry only the questions I got wrong, so that I can reinforce weak concepts while they are fresh.
- **Priority**: Must Have (M) | **Size**: S | **Traceability**: `FR-019`
- **Acceptance Criteria**:
  - **Given** an attempt with 4 incorrect questions,
  - **When** Alex clicks "🔄 Reintentar 4 falladas",
  - **Then** a new 4-question session is generated containing those exact questions with freshly shuffled option orders,
  - **And** the Quiz Screen opens immediately.

---

### Epic 5: Analytics & Weakness Breakdown (History Modal)

#### US-011: Topic Weakness Analytics with Rounded-Top Bar Progress
- **Story**: As Alex, I want to see an aggregated breakdown of my performance across all syllabus topics, so that I know exactly which Docker or gRPC topics to study next.
- **Priority**: Should Have (S) | **Size**: M | **Traceability**: `FR-020`, `FR-021`
- **Acceptance Criteria**:
  - **Given** the user opens the History & Weaknesses modal,
  - **When** they select the "Debilidades por Tema" tab,
  - **Then** topics are listed sorted from lowest percentage to highest,
  - **And** each topic row displays total attempts, correct count, and a custom SVG progress bar with rounded ends,
  - **And** topics with $<60\%$ success are colored coral/red, 60–79% amber, and $\ge 80\%$ green.

---

### Epic 6: Accessibility & Fallback Experience

#### US-012: Graceful Degradation for Reduced Transparency
- **Story**: As Marcos, I want the UI to respect my `prefers-reduced-transparency: reduce` operating system setting, so that I experience zero translucent glare or motion strain.
- **Priority**: Must Have (M) | **Size**: S | **Traceability**: `NFR-009`, `NFR-011`
- **Acceptance Criteria**:
  - **Given** the user's OS has "Reduce transparency" enabled,
  - **When** navigating the website,
  - **Then** all `backdrop-filter` rules are deactivated,
  - **And** all chrome surfaces render as 92% opaque tinted cards with solid high-contrast borders,
  - **And** all text maintains $\ge 4.5:1$ contrast against the opaque surface.

#### US-013: Fallback for Browsers Without `backdrop-filter`
- **Story**: As a student using an older or locked-down browser without CSS `backdrop-filter` support, I want the site to remain fully legible and visually pleasing without broken transparent text.
- **Priority**: Must Have (M) | **Size**: S | **Traceability**: `NFR-013`
- **Acceptance Criteria**:
  - **Given** a browser environment where `CSS.supports('backdrop-filter', 'blur(1px)')` returns false,
  - **When** loading the application,
  - **Then** CSS `@supports not ((backdrop-filter: blur(1px)) or (-webkit-backdrop-filter: blur(1px)))` activates,
  - **And** all floating surfaces render with clean opaque fills and soft shadows,
  - **And** zero layout breakage or illegible overlapping occurs.
