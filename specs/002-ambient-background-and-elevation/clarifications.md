# Clarifications & Ambiguity Scan: Unit 002

## 1. Ambiguity Scan Matrix

| Area | Question / Ambiguity | Resolution / Decision | Source |
| :--- | :--- | :--- | :--- |
| **DOM Architecture** | Should the ambient mesh be rendered via `body` CSS gradients or a dedicated fixed `<div>`? | Use a dedicated fixed `<div className="ambient-background" aria-hidden="true">` with `pointer-events: none` and `z-index: 0`. This avoids mobile Safari `background-attachment: fixed` repaint performance bugs during momentum scrolling. | Performance Audit (`research.md`) |
| **Animation vs. Static** | Should the gradient orbs animate (slowly drift) or stay static? | By default, keep the orbs **completely static** with CSS gradients. This uses 0% CPU/GPU idle overhead. An optional slow, hardware-accelerated ambient drift can be evaluated later, but static is the safest 60fps baseline. | 60 fps Budget |
| **Dark Mode Palette** | What exact gradient stops should be used for Dark Mode? | Indigo `rgba(99, 102, 241, 0.12)`, purple `rgba(168, 85, 247, 0.08)`, and cyan `rgba(6, 182, 212, 0.06)` on `#0B0F19`. | Visual Consistency |
| **Accessibility Tree** | How do we ensure screen readers ignore the ambient background layer? | Set `aria-hidden="true"` and `tabIndex={-1}` on the background container so assistive technologies completely skip it. | WCAG 2.2 AA |

---

## 2. Unresolved Items
*Zero unresolved `[NEEDS CLARIFICATION]` items remain for Unit 002.*
