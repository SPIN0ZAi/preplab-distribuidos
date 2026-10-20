# ADR-0003: Ambient Mesh Background Architecture and GPU Compositing

## Status
Approved

## Context
Liquid Glass surfaces require a background with soft chromatic variation to exhibit authentic refraction and optical depth. However, rendering gradient meshes must not induce GPU lag, drain battery on mobile devices, or trigger iOS Safari background repaint bugs during scrolling.

## Decision
We implement the ambient background as an isolated, fixed DOM container (`<div className="ambient-background" aria-hidden="true">`) with `z-index: 0`, `pointer-events: none`, and `transform: translateZ(0)` compositing. It hosts three radial gradient orbs (indigo, purple, coral in Light Mode; indigo, purple, cyan in Dark Mode) styled with pure CSS.

## Consequences
### Positive
- Zero CPU usage at idle.
- Zero layout repaints during window scrolling (60 fps guaranteed).
- Eliminates the well-known iOS Safari `background-attachment: fixed` jitter bug.
- Pure CSS implementation with 0 bytes of external assets.
- Hidden from accessibility tree (`aria-hidden="true"`).

### Negative
- Requires a wrapper container in the React tree (`App.tsx`).

## Compliance
- Constitution Principle 3 (Glass Discipline): Passed.
- Constitution Principle 6 (ADR Required): Passed.
- Constitution Principle 9 (Performance Budgets): Passed.
