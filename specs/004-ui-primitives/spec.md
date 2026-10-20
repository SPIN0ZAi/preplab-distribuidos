# Specification: Unit 004 — UI Component Primitives

## 1. Executive Summary
Unit U4 constructs the core design-token-backed, accessible UI primitives for the Distributed Systems Exam Prep platform: `Button`, `IconButton`, `Badge` (Pill), `SegmentedControl`, and `TextInput`. These primitives form the tactile foundation for all subsequent screens (App Shell, Exam Views, Results, Modals), embodying the Venus soft-UI aesthetic with subtle Apple-inspired micro-interactions (tactile scaling, spring lift, specular rim highlights, and WCAG 2.2 AA compliant focus states).

---

## 2. Traceability & Requirements Mapping
| Primitive | Requirements | User Stories | Non-Functional Requirements |
| :--- | :--- | :--- | :--- |
| `Button` | FR-001, FR-002, FR-006 | US-001, US-003, US-005, US-008 | NFR-006, NFR-008, NFR-009, NFR-011 |
| `IconButton` | FR-001, FR-002 | US-001, US-002, US-005 | NFR-008, NFR-009, NFR-011 |
| `Badge` (Pill) | FR-001, FR-002 | US-001, US-004, US-007 | NFR-006, NFR-008 |
| `SegmentedControl` | FR-001, FR-002, FR-004 | US-003, US-004, US-005 | NFR-006, NFR-008, NFR-009 |
| `TextInput` | FR-001, FR-002 | US-003, US-007 | NFR-006, NFR-008, NFR-009 |

---

## 3. Component Specifications

### 3.1 Button
- **Variants**:
  - `primary`: Background `#4318FF` (Electric Indigo), text `#FFFFFF`, diffuse shadow `0 14px 24px rgba(67, 24, 255, 0.28)`.
  - `secondary`: Background `var(--venus-bg-canvas)` (`#F4F7FE`), text `var(--venus-text-headline)` (`#1B2559`), border `1px solid var(--venus-card-border)`.
  - `glass`: Integrates `.glass-surface--thin`, translucent fill with specular highlight.
  - `danger`: Background `#EE5D50` (Coral Red), text `#FFFFFF`, shadow `0 14px 24px rgba(238, 93, 80, 0.25)`.
  - `ghost`: Transparent background, hover tint `rgba(67, 24, 255, 0.06)`, text `var(--venus-primary-indigo)`.
- **Sizes**:
  - `sm`: Height 36px, font 13px, padding `6px 14px`, border-radius 10px.
  - `md`: Height 44px, font 14px, padding `10px 20px`, border-radius 12px.
  - `lg`: Height 52px, font 15px, padding `14px 28px`, border-radius 16px.
  - `pill`: Modifier `shape="pill"` setting border-radius to `9999px`.
- **States**:
  - Hover: `transform: translateY(-1px) translateZ(0);`
  - Active: `transform: scale(0.97) translateZ(0);`
  - Focus: `outline: 2px solid var(--venus-primary-indigo); outline-offset: 2px;`
  - Disabled: `opacity: 0.5; pointer-events: none; filter: grayscale(40%);`
  - Loading: Replaces content with accessible SVG spinner, retains width.

### 3.2 IconButton
- Polymorphic button optimized for icons (e.g. theme toggle, modal close, navigation drawer toggle).
- Enforces required `aria-label` for screen readers.
- Shapes: `circle` (border-radius 50%) and `rounded` (border-radius 12px).
- Variants: `default`, `glass`, `primary`.
- Touch target minimum: $\ge 44 \times 44\text{px}$ adhering to WCAG 2.5.5.

### 3.3 Badge / Pill
- Visual tag indicator for question status (Answered, Unanswered, Marked), difficulty (Easy, Medium, Hard), or Lab badge (Lab 1, Lab 2).
- Tones:
  - `neutral`: Soft gray background `#F4F7FE`, text `#707EAE`.
  - `indigo`: Indigo tint `rgba(67, 24, 255, 0.08)`, text `#4318FF`.
  - `success`: Emerald tint `rgba(5, 205, 153, 0.12)`, text `#05CD99`.
  - `warning`: Amber tint `rgba(255, 181, 71, 0.15)`, text `#FFB547`.
  - `danger`: Coral tint `rgba(238, 93, 80, 0.12)`, text `#EE5D50`.
  - `glass`: Ultra-thin glass pill badge.

### 3.4 SegmentedControl
- Replaces generic `<select>` or raw button bars for switching:
  - Active Lab: "Lab 1 (Distributed Basics)" vs "Lab 2 (Consistency & Consensus)".
  - Mode: "Practice Mode" vs "Timed Exam" vs "Weak Spots".
  - Question Filters: "All (520)" vs "Flagged" vs "Incorrect".
- **Optical Architecture**:
  - Container: Soft recessed track (`#F4F7FE` / dark `#0F172A`), border-radius `14px`, padding `4px`.
  - Active Segment: Elevated floating card (`#FFFFFF` with soft shadow `0 2px 8px rgba(0,0,0,0.08)` in Light mode; `#1E293B` in Dark mode).
  - ARIA: `role="radiogroup"`, segments have `role="radio"`, `aria-checked="true|false"`. Keyboard navigation via Arrow Left / Arrow Right.

### 3.5 TextInput
- Search and filter input for question browsing and keyword lookup across 520 questions.
- Background `var(--venus-bg-canvas)` (`#F4F7FE`), font-size 14px, border-radius 12px.
- Subtle 1px border `var(--venus-card-border)`, glowing focus ring on active.
- Integrated left slot (search icon) and right slot (clear button / keyboard shortcut pill).

---

## 4. Accessibility & Degradation Guarantees
1. **WCAG 2.2 AA Contrast**:
   - Primary Indigo text on `#FFFFFF`: $8.6:1$ (exceeds $4.5:1$).
   - White text on Electric Indigo `#4318FF`: $5.2:1$ (exceeds $4.5:1$).
   - Text in `TextInput` on `#F4F7FE`: $12.1:1$.
2. **Motion Preference**:
   - When `prefers-reduced-motion: reduce` is enabled, all hover lifts, scale transforms, and indicator transitions are reduced to `0ms`.
3. **High Contrast / Forced Colors**:
   - Buttons, controls, and inputs use `1px solid CanvasText` and semantic `Highlight` colors under `forced-colors: active`.
