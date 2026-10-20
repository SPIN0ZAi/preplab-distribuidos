# SDD Specification: 010-responsive-a11y-perf-hardening

## 1. Executive Summary & Objective
Unit U10 executes systemic hardening across all responsive breakpoints (375px to 1920px+), accessibility standards (WCAG 2.2 AA and forced-colors modes), mobile thermal blur optimization, and bundle/runtime performance limits. It guarantees that the Two-Layer Visual System performs flawlessly on low-power mobile devices and high-end workstations alike with 0 accessibility violations and 0 layout shifts.

## 2. Requirements & Scope
- **REQ-010-01 (Responsive Breakpoints Matrix)**: Flawless layout across:
  - Mobile Small: 375px (iPhone SE)
  - Mobile Standard: 390px–414px (iPhone 14 / Pro Max)
  - Tablet Portrait: 768px (iPad Mini)
  - Tablet Landscape / Laptop: 1024px–1280px (MacBook Air)
  - Desktop Standard: 1440px
  - Ultra-Wide / Workstation: 1920px+
- **REQ-010-02 (Mobile Thermal Blur Throttling)**: On viewports $\le 768\text{px}$, backdrop filter blur radius is capped to $12\text{px}$ maximum, background mesh pulse frequency is slowed, and concurrent glass layers are limited to 1 (either topbar or bottom pill, never stacked) to preserve GPU battery and eliminate thermal throttling on mobile devices.
- **REQ-010-03 (WCAG 2.2 AA Contrast Verification)**:
  - Text on Glass: $\ge 4.5:1$ contrast against the worst-case dynamic background.
  - Text on Venus Cards: $\ge 7:1$ contrast (AAA level) against `#FFFFFF` (light) and `#111827` (dark).
  - Active interactive elements: $\ge 3:1$ boundary contrast.
- **REQ-010-04 (Accessible Focus Visibility)**: All keyboard focusable elements (`button`, `input`, `a`, `[tabindex="0"]`) display a prominent `:focus-visible` ring: `2px solid var(--venus-primary-indigo)` with `2px offset`, adapting to `CanvasText` in forced-colors mode.
- **REQ-010-05 (Touch Target Sizing)**: All mobile touch targets measure $\ge 44 \times 44\text{px}$ in computed layout or use invisible touch target expansions via `::after` pseudo-elements.
- **REQ-010-06 (Windows High Contrast / Forced Colors)**: When `@media (forced-colors: active)` is detected, glass semi-transparency and blur fall back to system `Canvas`, borders use `ButtonBorder` or `CanvasText`, and icons use `LinkText`/`CanvasText`.
- **REQ-010-07 (Production Bundle Budget Enforcement)**: Initial JS bundle strictly $< 200\text{ KB}$ gzipped (current baseline ~61 KB gzipped).

## 3. Verification Criteria
1. Production build passes with 0 TypeScript errors and bundle size $< 200\text{ KB}$ gzipped.
2. 520 questions verified with 100% integrity.
3. Contrast ratios meet or exceed WCAG 2.2 AA requirements.
4. Clean rendering without horizontal overflow (0 sideways scroll) from 375px to 1920px.
