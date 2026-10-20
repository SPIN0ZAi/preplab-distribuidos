# Constitution of the Redesign Project

## Core Principles

### 1. Spec-First & Traceability (SDD & AI-DLC)
- Specifications are the single source of truth. Code is a generated output of specs, never the other way around.
- Everything built must be traceable: **Intent → Requirement (EARS) → User Story (Given/When/Then) → Spec → Plan → Task → Commit → Test**.
- Unspecced work shall not be implemented. Any deviation or scope adjustment requires updating the specification first.

### 2. Human-In-The-Loop Governance
- Every phase and unit gate requires an explicit human review and approval ("approved" / "continue") before advancing.
- Decisions, questions, answers, and approvals must be logged with timestamps in `/aidlc-docs/audit.md`.
- Unresolved ambiguities must be flagged with `[NEEDS CLARIFICATION]` and surfaced in structured batches (max 8) with recommended defaults.

### 3. Glass Discipline (Rule 10)
- **Glass is strictly for the Chrome Layer**: floating navigation (sidebar, topbar, mobile bottom bar), modals, dropdowns, popovers, tooltips, toasts, floating action buttons, and segmented control track pills.
- **Content stays Solid**: ordinary content, including question text, options, explanations, tables, forms, stat cards, and chart bodies, MUST live on solid, high-contrast surfaces (Venus soft-UI white cards).
- **Surface Budgets**:
  - Maximum **25%** of any viewport area may be composed of glass/translucent surfaces.
  - Maximum **4** concurrent active `backdrop-filter` rendering layers in any view.
  - No nested `backdrop-filter` elements inside other blurred containers.
- **Graceful Fallback Guarantee**: Every glass surface must provide an immediate, attractive, high-contrast opaque or semi-opaque fallback when `backdrop-filter` is unsupported, when `prefers-reduced-transparency: reduce` is active, or when `forced-colors: active` is enabled.
- **Contrast Proof**: Every text element on glass must achieve a contrast ratio of at least **4.5:1** (and **3.0:1** for UI boundaries/icons) against worst-case backdrops (pure white, pure black, vibrant brand indigo, and busy gradient areas).

### 4. Preservation of Functionality & Zero Regression
- Existing application logic, question datasets (520 verified questions), local storage persistence, weighted question sampling, timestamp-accurate timer countdowns, scoring, and auto-submit behavior must be preserved 100%.
- This is an architectural visual redesign, not a functional rewrite. No business logic changes unless explicitly mandated by an approved spec.

### 5. Design Tokens as the Sole Styling Source
- Components shall NEVER contain hardcoded colors, spacing numbers, radii, shadows, or blur values.
- All styles must consume design tokens defined in the centralized CSS variable system (`--venus-*`, `--glass-*`).
- Dual-theme tokenization: Venus Light Mode is the primary reference showcase, with Dark Mode fully supported through parallel token mappings.

### 6. Dependency Discipline & Architecture Decision Records (ADR)
- Use installed dependencies and existing project conventions.
- No new runtime or development dependency may be added without an approved Architecture Decision Record (ADR) in `/docs/adr/NNNN-title.md` detailing context, options, decision, consequences, and bundle impact.

### 7. Accessibility Baseline (WCAG 2.2 AA)
- Full compliance with WCAG 2.2 AA across all pages and interactive components.
- Visible, high-contrast focus rings (`:focus-visible`) tailored for glass and solid cards.
- Complete keyboard operability, screen-reader semantic landmarks, and ARIA attributes for modals, progress meters, and dynamic alerts.
- Full respect for user system preferences: `prefers-reduced-motion`, `prefers-reduced-transparency`, `prefers-contrast: more`, and `forced-colors`.

### 8. Mobile-First & Responsive Geometry
- Responsive layout behavior across 375px, 768px, 1024px, 1440px, and 1920px viewports with zero horizontal overflow.
- Respect device safe-area insets (`env(safe-area-inset-*)`), virtual keyboard appearance, and touch target minimums (44x44px).
- Mobile blur radii reduced appropriately to prevent GPU throttling and battery drain.

### 9. Performance & Quality Budgets
- Production initial JavaScript bundle budget: **< 200 KB gzipped** (currently ~56 KB).
- Core Web Vitals: LCP < 2.5s, CLS < 0.1, INP < 200ms.
- 60 fps smooth scrolling with glass chrome positioned over scrolling content.

### 10. Engineering Rigor
- Characterization testing before refactoring to prevent regressions.
- Conventional commits referencing specific Task and Requirement IDs.
- Zero dead code; documentation is a mandatory deliverable of "Done".
