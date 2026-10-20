# Inception: Comprehensive Test Strategy

## 1. Testing Philosophy & Test Pyramid

Our test strategy is structured around Spec-Driven Development (SDD) to ensure zero functional regressions, rigorous accessibility compliance (WCAG 2.2 AA), and high visual fidelity:

```
              ┌────────────────────────┐
              │      Manual Review     │  Reference fidelity (1-5 score),
              │     & Human Gate       │  optical polish, tactile spring feel
              ├────────────────────────┤
              │ Visual & A11y Audits   │  Axe-core scans, contrast matrix,
              │ (Worst-Case Backdrops) │  Lighthouse CI, 375px-1920px viewports
              ├────────────────────────┤
              │ Integration & E2E Flow │  Full quiz run, timer auto-submit,
              │ (Critical User Paths)  │  session recovery, retry wrong flow
              ├────────────────────────┤
              │ Component & Fallback   │  GlassSurface variants, `@supports` fallbacks,
              │ Tests (Vitest + RTL)   │  prefers-reduced-transparency, primitives
              ├────────────────────────┤
              │ Unit & Characterization│  quizEngine scoring, storage sync,
              │ (Contract Baseline)    │  520-question integrity, timer math
              └────────────────────────┘
```

---

## 2. Test Suites Detailed Specifications

### 2.1 Characterization & Unit Tests (Vitest)
- **Target Components**: `storage.ts`, `quizEngine.ts`, `Timer.tsx`.
- **Objectives**:
  - Lock in existing behavioral contracts *before* modifying UI code.
  - Test weighted random selection (`selectQuestions`) ensuring unseen questions (3.0x) and wrong questions (2.5x) receive proper statistical sampling.
  - Verify timestamp-accurate timer calculations during tab suspension or page reloads.
  - Verify scoring accuracy for single-choice and multiple-choice questions.
  - Verify 520-question schema validation (260 P1 + 260 P2, zero duplicates, 100% distractor rationales present).
- **Target Coverage**: $\ge 90\%$ line coverage on core services.

### 2.2 Component & Material Tests (Vitest + Testing Library)
- **Target Components**: `GlassSurface`, `Button`, `IconButton`, `Pill`, `SegmentedControl`, `SvgBarChart`, `SvgGauge`.
- **Objectives**:
  - Verify all variants (`thin`, `regular`, `thick`) render correct optical classes and CSS properties.
  - Verify ARIA roles, states (`aria-pressed`, `aria-selected`, `aria-expanded`), and accessible labels.
  - Verify high-contrast `:focus-visible` ring presence on keyboard tab navigation.
  - Verify SVG charts render proportional coordinate paths without NaN errors.

### 2.3 Fallback Test Suite
- **Fallback 1: No `backdrop-filter` Support**:
  - Simulate `@supports not (backdrop-filter: blur(1px))`.
  - Assert that all glass surfaces degrade to $92\%$ opaque tinted surfaces with clear 1px solid borders.
  - Assert zero text overlapping or illegible elements.
- **Fallback 2: `prefers-reduced-transparency: reduce`**:
  - Simulate reduced transparency media query.
  - Assert that `backdrop-filter` is disabled and opaque surfaces are applied.
- **Fallback 3: `prefers-reduced-motion: reduce`**:
  - Simulate reduced motion.
  - Assert that all CSS transition durations and animation iterations are set to 0s / none.
- **Fallback 4: `forced-colors: active` (High Contrast Mode)**:
  - Assert that all box-shadows and glass sheens degrade to system high-contrast borders (`CanvasText` on `Canvas`).

### 2.4 Automated Accessibility & Contrast Matrix
- **Axe-core Integration**: Run `axe.run()` against every rendered screen (Landing, Quiz, Results, History Modal) in both Light and Dark themes.
- **Worst-Case Backdrop Contrast Matrix**:
  Test text on glass surfaces against 4 worst-case backdrops:
  1. **Pure White (`#FFFFFF`)**: Test glass text readability.
  2. **Dark Navy (`#1B2559`)**: Test glass text readability.
  3. **Vibrant Indigo (`#4318FF`)**: Test glass text readability.
  4. **Multi-color Ambient Gradient Orb**: Test glass text readability.
  - **Pass Threshold**: Contrast ratio $\ge 4.5:1$ for normal text, $\ge 3.0:1$ for UI boundaries and icons.

### 2.5 Performance & Frame Rate Profiling
- **Initial Bundle Budget**: Run `vite build` and verify initial JavaScript bundle is strictly $< 200\text{ KB}$ gzipped.
- **Scroll Frame Rate**: Profile scrolling performance with DevTools Performance trace; verify solid cards scrolling under floating glass topbar/sidebar maintain 60 fps without dropped frames.
- **Mobile Throttling Check**: Emulate 4x CPU throttling on a 375px mobile viewport to confirm blur radius of 12px prevents GPU lag.

### 2.6 Cross-Browser Matrix
- **Desktop**: Google Chrome (Blink), Apple Safari (WebKit), Mozilla Firefox (Gecko), Microsoft Edge (Blink).
- **Mobile Emulation**: iOS Safari (WebKit rendering engine), Android Chrome (Blink).

---

## 3. Quality Gate Thresholds

| Quality Gate | Minimum Pass Requirement |
| :--- | :--- |
| **Unit & Characterization Tests** | 100% pass (0 failures). |
| **Axe Accessibility Audit** | 0 Critical, 0 Serious violations. |
| **Worst-Case Glass Contrast** | 100% pass ($\ge 4.5:1$ text). |
| **Bundle Size Check** | Initial JS $< 200\text{ KB}$ gzipped. |
| **TypeScript Typecheck** | 0 errors (`tsc --noEmit`). |
| **Production Build** | Clean build with 0 warnings. |
| **Visual Fidelity Review** | Score $\ge 4.5 / 5.0$ across all 12 heuristic criteria. |
