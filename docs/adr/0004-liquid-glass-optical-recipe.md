# ADR-0004: Liquid Glass Optical Layering Formulation and Fallback Architecture

## Status
Approved

## Context
The chrome redesign requires an authentic Apple Liquid Glass aesthetic (translucent floating navigation, modals, and badges) while strictly adhering to:
1. Cross-browser stability (preventing WebKit/Safari rectangular clipping bugs and black box glitches).
2. 60 fps smooth scrolling over content cards.
3. WCAG 2.2 AA accessibility and graceful degradation under non-supporting browsers and `prefers-reduced-transparency`.

## Decision
We implement the Liquid Glass material system using a standardized 6-layer CSS optical formula:
1. `-webkit-backdrop-filter` and `backdrop-filter: blur(...) saturate(160%)`.
2. Translucent tinted background fill (`--glass-fill-thin`, `--glass-fill-regular`, `--glass-fill-thick`).
3. 1px translucent physical border (`--glass-border`).
4. Inset specular rim highlight (`inset 0 1px 1px 0 rgba(255,255,255,0.70)`) and bottom shade (`inset 0 -1px 1px 0 rgba(0,0,0,0.04)`).
5. Diagonal sheen reflection (`linear-gradient(135deg, rgba(255,255,255,0.22) 0%, transparent 100%)`) on `::before`.
6. Layered tinted outer drop shadows.

We reject SVG displacement refraction for the baseline due to rendering crashes and lack of support in Apple WebKit, maintaining 100% universal compatibility.

## Consequences
### Positive
- Authentic specular reflection and depth without JavaScript animation loops.
- Rock-solid stability in Safari on macOS and iOS.
- Clean declarative fallback to 94% solid opaque fill via `@supports not (backdrop-filter)` and `@media (prefers-reduced-transparency: reduce)`.
- Reusable across all chrome elements (topbar, sidebar, modals, badges).

### Negative
- Requires maintaining `-webkit-backdrop-filter` alongside `backdrop-filter`.

## Compliance
- Constitution Principle 3 (Glass Discipline): Passed.
- Constitution Principle 6 (ADR Required): Passed.
- Constitution Principle 7 (WCAG 2.2 AA): Passed.
- Constitution Principle 9 (Performance Budgets): Passed.
