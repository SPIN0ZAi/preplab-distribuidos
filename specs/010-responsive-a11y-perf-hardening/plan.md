# SDD Plan: 010-responsive-a11y-perf-hardening

## Phase 1: High Contrast & Accessibility Hardening
1. Add high contrast mode and forced colors styles in a new dedicated stylesheet `src/styles/hardening.css`.
2. Standardize `:focus-visible` styling across all interactive elements (`button`, `a`, `input`, `.segmented-tab`, `.pill-btn`, `.option-card`).
3. Add touch target expansion pseudo-elements (`::after`) for navigator pills and icon buttons.

## Phase 2: Mobile Thermal & Viewport Optimization
1. Implement mobile blur capping: `@media (max-width: 768px)` throttles blur to 12px.
2. Verify all layouts prevent horizontal scroll (`overflow-x: hidden` on viewport roots, `max-width: 100%` on code blocks and cards).
3. Ensure padding on mobile leaves safe areas for the floating mobile navigation pill (`padding-bottom: 96px`).

## Phase 3: Performance & Bundle Verification
1. Run `npm run build` to verify total bundle footprint remains $< 200\text{ KB}$ gzipped.
2. Audit contrast ratios across light and dark modes.
3. Import `hardening.css` into `src/styles/theme.css`.
