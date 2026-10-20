# Clarifications & Ambiguity Scan: Unit 003

## 1. Ambiguity Scan Matrix

| Area | Question / Ambiguity | Resolution / Decision | Source |
| :--- | :--- | :--- | :--- |
| **Component vs. CSS Class** | Should the glass system be a React component (`<GlassSurface>`) or pure CSS classes (`.glass-surface`, `.glass-thin`, etc.)? | **Both**: Provide a set of atomic CSS classes (`.glass-surface`, `.glass-thin`, `.glass-regular`, `.glass-thick`, `.glass-pill`) AND a flexible polymorphic React component `<GlassSurface as="div" variant="regular" shape="rounded">` that wraps children with standard props and accessibility defaults. | Architecture Decision |
| **Specular Sheen Implementation** | How should the surface sheen be drawn without extra DOM elements? | Use CSS pseudo-element `::before` with `content: ""; position: absolute; inset: 0; pointer-events: none; border-radius: inherit; background: var(--glass-sheen);`. | Best Practice |
| **Edge Highlight Technique** | How should the physical specular rim be drawn? | Use `box-shadow` with inset values: `var(--glass-edge-highlight)` (top/left inner white highlight) + `var(--glass-edge-shade)` (bottom/right subtle shade). This avoids extra border elements and scales with all border radii. | Optical Physics Model |
| **Nested Blur Guard** | How do we programmatically prevent nested backdrop filters? | Architecturally, the modal scrim is a plain dimming layer (`rgba(0,0,0,0.50)`). The modal sheet itself is the single active glass layer at that z-index. | Rule 10 Enforcement |

---

## 2. Unresolved Items
*Zero unresolved `[NEEDS CLARIFICATION]` items remain for Unit 003.*
