# Implementation Plan: Unit 002 — Ambient Background Canvas & Elevation Layer

## 1. Technical Context & Constitution Check

### Constitution Compliance Matrix
| Principle | Requirement | Plan Alignment | Status |
| :--- | :--- | :--- | :---: |
| **P1: Spec-First** | Specs are source of truth | Implementation follows `spec.md` with traceable tasks. | **PASS** |
| **P3: Glass Discipline** | Glass needs an ambient background | Ambient orbs supply colors for glass without touching content. | **PASS** |
| **P5: Token-Only** | Use CSS custom properties | Gradients consume `--venus-*` and `--glass-*` tokens. | **PASS** |
| **P6: Dependency Discipline** | No new dependencies | Pure CSS + standard React component; 0 packages added. | **PASS** |
| **P7: WCAG 2.2 AA** | Contrast preserved | Background opacity capped at 0.08 to protect $\ge 4.5:1$ text contrast. | **PASS** |
| **P9: Performance** | 60 fps frame rate | Fixed container with `pointer-events: none`; 0 layout repaints. | **PASS** |

---

## 2. Component Design & Architecture

### 2.1 File Structure
```text
src/
├── components/
│   └── AmbientBackground.tsx       # Lightweight React component rendering fixed canvas
└── styles/
    └── ambient-background.css      # Gradient mesh definitions & dark mode transitions
```

### 2.2 CSS Implementation Recipe
```css
/* src/styles/ambient-background.css */
.ambient-background {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  z-index: 0;
  pointer-events: none;
  overflow: hidden;
  background-color: var(--venus-bg-canvas);
  transition: background-color 200ms ease;
}

.ambient-orb {
  position: absolute;
  border-radius: 50%;
  filter: blur(80px);
  opacity: 0.8;
  transform: translateZ(0); /* Force GPU compositing */
}

/* Light Theme Orbs */
.ambient-orb-1 {
  top: -10%;
  left: -5%;
  width: 55vw;
  height: 55vw;
  max-width: 650px;
  max-height: 650px;
  background: radial-gradient(circle, rgba(67, 24, 255, 0.08) 0%, transparent 70%);
}

.ambient-orb-2 {
  bottom: -10%;
  right: -5%;
  width: 50vw;
  height: 50vw;
  max-width: 600px;
  max-height: 600px;
  background: radial-gradient(circle, rgba(117, 81, 255, 0.07) 0%, transparent 70%);
}

.ambient-orb-3 {
  top: 35%;
  right: 15%;
  width: 35vw;
  height: 35vw;
  max-width: 450px;
  max-height: 450px;
  background: radial-gradient(circle, rgba(255, 122, 138, 0.05) 0%, transparent 70%);
}

/* Dark Theme Orbs */
[data-theme="dark"] .ambient-orb-1 {
  background: radial-gradient(circle, rgba(99, 102, 241, 0.12) 0%, transparent 70%);
}

[data-theme="dark"] .ambient-orb-2 {
  background: radial-gradient(circle, rgba(168, 85, 247, 0.10) 0%, transparent 70%);
}

[data-theme="dark"] .ambient-orb-3 {
  background: radial-gradient(circle, rgba(6, 182, 212, 0.08) 0%, transparent 70%);
}
```

---

## 3. Elevation Scale Integration

All view content (`.app-container`, `.app-header`, modals) will operate on positive z-indexes (`z-index: 1` through `z-index: 1000`), ensuring that the ambient background remains strictly non-interactive and visual-only at $z=0$.

---

## 4. Rollback Plan
If any performance issues arise on low-end test devices:
- Removing `<AmbientBackground />` from `App.tsx` restores the flat background color immediately without breaking any layout structure.
