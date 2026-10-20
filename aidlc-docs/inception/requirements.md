# Inception: Requirements Specification (EARS Format)

## 1. Specification Standard

All requirements are specified using the **EARS syntax** (Easy Approach to Requirements Syntax):
- **Ubiquitous**: *The system shall <action>.*
- **Event-driven**: *When <event/trigger>, the system shall <action>.*
- **State-driven**: *While in <state>, the system shall <action>.*
- **Unwanted behavior**: *If <error/edge case>, the system shall <action>.*
- **Optional feature**: *Where <feature is present>, the system shall <action>.*

---

## 2. Functional Requirements (FR)

### Theme & Design System
- **FR-001**: While rendering any view, the system shall source all visual attributes (colors, spacing, shadows, radii, blur levels) exclusively from centralized CSS custom properties (`--venus-*`, `--glass-*`).
- **FR-002**: When the user activates the theme toggle control, the system shall transition between Venus Light Mode (`data-theme="light"`) and Dark Mode (`data-theme="dark"`) within 200ms without page reloads.
- **FR-003**: When initializing the application, the system shall detect the user's OS preference (`prefers-color-scheme`) and default to Venus Light Mode if no explicit preference has been saved in `localStorage`.

### App Shell & Navigation
- **FR-004**: While in a desktop viewport ($\ge 1024\text{px}$), the system shall render an inset floating glass sidebar on the left and an inset floating glass topbar across the top.
- **FR-005**: While in a mobile viewport ($< 768\text{px}$), the system shall collapse the desktop sidebar into a floating glass bottom navigation pill with safe-area padding.
- **FR-006**: When the user clicks a navigation item (Simulacros, Historial, Analítica, Ajustes), the system shall update the active view or trigger the corresponding overlay while preserving active quiz state.

### Exam Selection & Configuration (Landing Screen)
- **FR-007**: When the user selects a practice mode card (Práctica 1, Práctica 2, or Mixto), the system shall apply an active indigo highlight border and update the selected mode in state.
- **FR-008**: When the user selects a timer preset (Desactivado, 10m, 20m, 30m, 45m, 60m, or Personalizado), the system shall store the duration preference in `localStorage`.
- **FR-009**: When an incomplete session exists in `storage`, the system shall display a floating resume card showing the question count, elapsed time, and a "Continuar intento" action.

### Active Quiz Execution (Quiz Screen)
- **FR-010**: When a quiz is initiated, the system shall display a 20-pill navigation track in the chrome layer, reflecting question numbers 1 through 20.
- **FR-011**: When the user answers or alters an option for question $N$, the system shall immediately update the visual status of pill $N$ (answered with solid accent indicator) and persist the answer to `localStorage`.
- **FR-012**: When the user toggles the flag button for question $N$, the system shall toggle a flag indicator on pill $N$ and update `flaggedQuestionIds`.
- **FR-013**: While the timer is active and remaining time is $< 60\text{ seconds}$, the system shall animate the timer pill with a rhythmic warning pulse.
- **FR-014**: If the countdown timer reaches $0\text{ seconds}$, the system shall automatically freeze user input, calculate scores, and transition to the Results Screen.
- **FR-015**: When the user clicks "Finalizar Intento", the system shall display a thick-glass confirmation modal displaying the count of unanswered questions before grading.

### Results & Remediation (Results Screen)
- **FR-016**: When grading is completed, the system shall render a solid Venus summary card with a circular SVG score meter, percentage, and pass/fail indicator ($\ge 50\%$).
- **FR-017**: When the user selects a review filter (*Todas*, *Solo Falladas*, *Acertadas*), the system shall update the review list within 50ms without layout shifts.
- **FR-018**: While rendering each review item card, the system shall display the user's selection, the correct target, the pedagogical justification (`explanation.correct`), and individual distractor explanations (`explanation.wrong[optId]`).
- **FR-019**: When the user clicks "Reintentar preguntas falladas", the system shall construct a new exam session containing exclusively the failed questions and transition to the Quiz Screen.

### Analytics & History Modal
- **FR-020**: When the user opens the History Modal, the system shall display a thick-glass sheet over a dimmed scrim, containing the attempt history log and the topic weakness table.
- **FR-021**: While rendering the topic weakness view, the system shall sort topics by lowest success rate first and display a custom SVG progress bar color-coded by mastery tier (<60% coral, 60–79% amber, ≥80% green).
- **FR-022**: When the user clicks "Borrar historial", the system shall require explicit double-confirmation before purging `ds_quiz_attempt_history`.

---

## 3. Non-Functional Requirements (NFR)

### Performance Budgets
- **NFR-001 (Bundle Budget)**: The initial client JavaScript bundle size shall not exceed **$200\text{ KB}$ gzipped**; `lab1.json` and `lab2.json` shall remain lazy-loaded on demand.
- **NFR-002 (Core Web Vitals)**:
  - **Largest Contentful Paint (LCP)**: $< 2.5\text{ seconds}$ on standard 4G mobile emulation.
  - **Cumulative Layout Shift (CLS)**: $< 0.1$ across all viewport dimensions.
  - **Interaction to Next Paint (INP)**: $< 200\text{ milliseconds}$.
- **NFR-003 (Frame Rate & Scrolling)**: The system shall maintain **60 fps** scrolling performance while solid content cards pass visibly under floating glass chrome.
- **NFR-004 (Glass Layer Budget)**: At any single point in time, the system shall render **no more than 4 concurrent `backdrop-filter` layers**, and the total visible glass surface shall not exceed **25% of the total viewport area**.
- **NFR-005 (Mobile Blur Limit)**: On mobile viewports ($< 768\text{px}$), the system shall cap all `backdrop-filter` blur radii to a maximum of **$12\text{px}$** to eliminate GPU thermal throttling.

### Accessibility (WCAG 2.2 AA)
- **NFR-006 (Contrast on Glass)**: All text rendered on glass surfaces shall maintain a minimum contrast ratio of **$4.5:1$** (and **$3.0:1$** for UI component boundaries/icons) measured against worst-case backdrops (pure white `#FFFFFF`, dark navy `#1B2559`, electric indigo `#4318FF`, and gradient orbs).
- **NFR-007 (Contrast on Content Cards)**: All primary text rendered on solid Venus white cards shall maintain a contrast ratio $\ge 7:1$ (exceeding AAA), and secondary text shall maintain $\ge 4.5:1$ (AA).
- **NFR-008 (Focus Rings)**: All interactive elements shall display an unambiguous `:focus-visible` offset ring (2px solid with 2px offset) that remains clearly visible on both glass and solid surfaces.
- **NFR-009 (Reduced Transparency)**: When `prefers-reduced-transparency: reduce` is detected, the system shall disable all `backdrop-filter` blurs and render glass surfaces as $92\%$ opaque tinted solid surfaces.
- **NFR-010 (Reduced Motion)**: When `prefers-reduced-motion: reduce` is detected, the system shall disable all spring animations, transitions, and pulsing alerts, replacing them with instant state changes.
- **NFR-011 (High Contrast & Forced Colors)**: When `forced-colors: active` or `prefers-contrast: more` is detected, the system shall render high-contrast solid borders and system colors, removing all translucent filters.
- **NFR-012 (Keyboard Operability)**: The entire application—including navigation, quiz option selection, question pill jumping, and modal dialogs—shall be 100% operable via keyboard alone with trap focus inside active modals.

### Graceful Fallbacks & Browser Compatibility
- **NFR-013 (Backdrop-Filter Fallback)**: Where `backdrop-filter` is unsupported by the browser, the system shall automatically fall back via CSS `@supports not ((backdrop-filter: blur(1px)) or (-webkit-backdrop-filter: blur(1px)))` to solid semi-opaque surfaces without visual defects.
- **NFR-014 (Cross-Browser Matrix)**: The application shall render identically and without script/layout errors on Apple Safari (macOS & iOS), Google Chrome, Microsoft Edge, and Mozilla Firefox.
- **NFR-015 (Responsive Matrix)**: The application shall provide responsive, horizontal-overflow-free layouts at viewports $375\text{px}$, $768\text{px}$, $1024\text{px}$, $1440\text{px}$, and $1920\text{px}$.

### Maintainability & Architecture
- **NFR-016 (Zero New Production Dependencies)**: The redesign shall not introduce any new runtime production packages into `package.json`.
- **NFR-017 (Zero Component CSS Duplication)**: The Liquid Glass styling recipe shall be encapsulated in a single reusable component/utility (`GlassSurface` and `--glass-*` tokens) rather than duplicated across component files.
