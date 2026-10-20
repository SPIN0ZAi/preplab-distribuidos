# ADR-0002: Token Architecture, Color Formulation, and Font Delivery Strategy

## Status
Approved

## Context
Unit U1 requires establishing the design tokens for the Venus Content Layer (soft-UI light default) and Liquid Glass Chrome Layer (translucent iOS 26 optics). We must decide:
1. The CSS color formulation strategy (Hex/RGBA vs HSL vs OKLCH).
2. The delivery mechanism for the `Poppins` display font.
3. The storage and synchronization mechanism for the user's theme preference.

## Decision
1. **Color Formulation**: We standardize on standard `#RRGGBB` and `rgba(r, g, b, alpha)` custom properties. This guarantees 100% universal browser rendering across Safari, Chrome, Edge, and Firefox without requiring any build-time PostCSS transpilation.
2. **Font Delivery**: We load `Poppins` (weights 500, 600, 700, 800) alongside existing `Plus Jakarta Sans` and `JetBrains Mono` via Google Fonts preconnected CDN links in `index.html`. This adds 0 KB to the JavaScript/CSS bundle.
3. **Theme Synchronization**: Theme state is managed via `data-theme="light"` (default) or `data-theme="dark"` on `document.documentElement`, persisted in `localStorage` (`ds_quiz_theme_preference`), and initialized via a synchronous 4-line script in `<head>` to prevent Flash of Unstyled Content (FOUC).

## Consequences
### Positive
- Zero runtime bundle overhead.
- Universal cross-browser compatibility.
- Instant theme toggle transitions (200ms) with zero layout thrashing.
- Fully accessible contrast in both themes.

### Negative
- Requires internet connectivity for first-time font download (gracefully falls back to `Plus Jakarta Sans` and system `sans-serif` if offline).

## Compliance
- Constitution Principle 5 (Design-Token-Only): Passed.
- Constitution Principle 6 (ADR Required): Passed.
- Constitution Principle 9 (Performance Budget): Passed (< 200 KB initial JS).
