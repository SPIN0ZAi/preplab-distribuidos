# Atomic Tasks: Unit 002 — Ambient Background Canvas & Elevation Layer

## Task Dependency Ordering

```
T007 [Ambient Background CSS] ──> T008 [AmbientBackground React Component] ──> T009 [App Shell Integration & Build Check]
```

---

## Detailed Tasks Matrix

### T007: Author Ambient Background CSS Stylesheet
- **File**: `src/styles/ambient-background.css`
- **Requirement Link**: `FR-001`, `FR-004`, `NFR-003`, `NFR-007`
- **Estimated Effort**: 30 mins
- **Description**: Formulate the fixed container and radial gradient orbs (indigo, purple, coral for light mode; indigo, purple, cyan for dark mode) with hardware-composited `transform: translateZ(0)`.
- **Definition of Done**: Orbs render with soft 80px blur; dark mode selector shifts gradient stops smoothly.

### T008: Build `AmbientBackground.tsx` Component
- **File**: `src/components/AmbientBackground.tsx`
- **Requirement Link**: `FR-004`, `NFR-002`, `NFR-010`
- **Estimated Effort**: 20 mins
- **Description**: Create stateless React component returning `<div className="ambient-background" aria-hidden="true">` with the 3 orb elements.
- **Definition of Done**: Component renders semantic, accessible container with `aria-hidden="true"`.

### T009: Mount `AmbientBackground` in `App.tsx` & Verify Build
- **Files**: `src/App.tsx`, `src/index.css`
- **Requirement Link**: `NFR-001`, `NFR-003`
- **Estimated Effort**: 25 mins
- **Description**: Import and mount `<AmbientBackground />` at the root of `App.tsx` behind main content. Ensure `app-container` sits on `z-index: 1`. Run `npm run build`.
- **Definition of Done**: Clean compilation with 0 errors; ambient glow visible behind layout; initial JS bundle remains $< 200\text{ KB}$ gzipped.
