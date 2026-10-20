# SDD Plan: 009-interaction-polish-and-motion

## Phase 1: Foundation & Token Declaration
1. Define standardized motion tokens in `src/styles/tokens/venus-tokens.css` and `glass-tokens.css`:
   - Easing functions: `--motion-ease-spring`, `--motion-ease-bounce`, `--motion-ease-smooth`.
   - Durations: `--motion-duration-fast`, `--motion-duration-normal`, `--motion-duration-deliberate`.
2. Ensure consistent token availability across light and dark modes.

## Phase 2: Core Motion System (`src/styles/motion.css`)
1. Create dedicated `src/styles/motion.css` stylesheet:
   - Micro-lift interaction classes (`.hover-lift`, `.press-tactile`).
   - Celebratory keyframes (`@keyframes victory-shimmer`, `@keyframes victory-pulse`).
   - SVG gauge sweep animation.
   - Guarded touch hover states (`@media (hover: hover)`).
   - Global `prefers-reduced-motion: reduce` overrides.
2. Import `motion.css` into `src/styles/theme.css`.

## Phase 3: Component Integration
1. Apply `.hover-lift` to mode selection cards, stat cards, and attempt cards.
2. Apply tactile press feedback to all buttons and segmented controls.
3. Apply celebratory pass animation to `ResultsScreen.tsx` score hero when score $\ge 70\%$.
4. Ensure smooth transition when switching themes between light and dark.

## Phase 4: Verification & Performance Hardening
1. Verify 0 layout shifts (CLS = 0) with Chrome DevTools Performance panel.
2. Verify reduced-motion mode completely stops animations instantly.
3. Run `npm run build` to confirm 0 TypeScript errors and bundle size within budget.
