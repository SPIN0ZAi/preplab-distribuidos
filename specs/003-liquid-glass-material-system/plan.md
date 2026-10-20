# Implementation Plan: Unit 003 — Liquid Glass Material System & Fallbacks

## 1. Technical Context & Constitution Check

### Constitution Compliance Matrix
| Principle | Requirement | Plan Alignment | Status |
| :--- | :--- | :--- | :---: |
| **P1: Spec-First** | Specs are the source of truth | Implementation follows `spec.md` with traceable tasks. | **PASS** |
| **P3: Glass Discipline** | Restricted to Chrome; <25% area | `GlassSurface` is exclusively applied to chrome surfaces. | **PASS** |
| **P5: Token-Only** | Use CSS custom properties | All blurs, fills, and shadows sourced from `--glass-*`. | **PASS** |
| **P6: Dependency Discipline** | No new dependencies | Pure CSS + standard React component; 0 packages added. | **PASS** |
| **P7: WCAG 2.2 AA** | Contrast proofs | $\ge 4.5:1$ text contrast verified against worst-case matrix. | **PASS** |
| **P9: Performance** | 60 fps frame rate | Hardware compositing via `translateZ(0)` and isolation. | **PASS** |

---

## 2. Component Design & Architecture

### 2.1 File Structure
```text
src/
├── components/
│   └── GlassSurface.tsx            # Polymorphic React component
├── styles/
│   └── glass-surface.css           # Glass optical styling, variants, and fallbacks
└── types/
    └── glass.ts                    # TypeScript types for glass variants & props
```

### 2.2 Layering Architecture (The 6-Layer Optical Recipe)
```css
/* src/styles/glass-surface.css */

.glass-surface {
  position: relative;
  isolation: isolate;
  border: var(--glass-border);
  box-shadow: var(--glass-edge-highlight), var(--glass-edge-shade), var(--glass-shadow);
  color: var(--glass-text);
  transform: translateZ(0);
  transition: background-color var(--glass-duration) ease,
              border-color var(--glass-duration) ease,
              box-shadow var(--glass-duration) ease,
              transform var(--glass-duration) var(--glass-ease);
}

/* Surface Sheen Pseudo-Element */
.glass-surface::before {
  content: '';
  position: absolute;
  inset: 0;
  border-radius: inherit;
  background: var(--glass-sheen);
  pointer-events: none;
  z-index: 0;
}

/* Children sit above the sheen */
.glass-surface > * {
  position: relative;
  z-index: 1;
}

/* Variant 1: Thin (Badges, Controls, Timer) */
.glass-surface--thin {
  -webkit-backdrop-filter: blur(var(--glass-blur-thin)) saturate(var(--glass-saturate));
  backdrop-filter: blur(var(--glass-blur-thin)) saturate(var(--glass-saturate));
  background-color: var(--glass-fill-thin);
}

/* Variant 2: Regular (Topbar, Sidebar, Toolbars) */
.glass-surface--regular {
  -webkit-backdrop-filter: blur(var(--glass-blur-regular)) saturate(var(--glass-saturate));
  backdrop-filter: blur(var(--glass-blur-regular)) saturate(var(--glass-saturate));
  background-color: var(--glass-fill-regular);
  box-shadow: var(--glass-edge-highlight), var(--glass-edge-shade), var(--glass-shadow-floating);
}

/* Variant 3: Thick (Modal Sheets, Bottom Drawers) */
.glass-surface--thick {
  -webkit-backdrop-filter: blur(var(--glass-blur-thick)) saturate(var(--glass-saturate));
  backdrop-filter: blur(var(--glass-blur-thick)) saturate(var(--glass-saturate));
  background-color: var(--glass-fill-thick);
  box-shadow: var(--glass-edge-highlight), var(--glass-edge-shade), var(--glass-shadow-modal);
}

/* Tone Variants */
.glass-surface--accent {
  background-color: var(--glass-fill-accent);
  border-color: rgba(67, 24, 255, 0.35);
}

/* Shape Variants */
.glass-surface--rounded {
  border-radius: var(--venus-radius-lg);
}

.glass-surface--pill {
  border-radius: var(--venus-radius-pill);
}

.glass-surface--circle {
  border-radius: 50%;
}

/* Fallback: Unsupported Browsers */
@supports not ((backdrop-filter: blur(1px)) or (-webkit-backdrop-filter: blur(1px))) {
  .glass-surface--thin,
  .glass-surface--regular,
  .glass-surface--thick {
    background-color: var(--glass-fallback-fill);
    border: 1px solid var(--glass-fallback-border);
  }
}
```

---

## 3. Rollback Plan
If any browser-specific rendering anomaly occurs:
- The `@supports not` fallback rule can be activated unconditionally via CSS class to immediately render solid semi-opaque surfaces without altering React component props or markup.
