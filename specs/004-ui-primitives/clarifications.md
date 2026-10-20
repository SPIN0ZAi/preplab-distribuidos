# Clarifications: Unit 004 — UI Component Primitives

## Clarification Log

### C001: Should Button primitives use external icon libraries or inline SVGs?
- **Decision**: Zero external dependencies. All icons (search icon, close icon, chevron, spinner, checkmark) will be authored as accessible, lightweight zero-dependency inline SVGs or shared SVG icon components to respect our bundle budget (< 200 KB gzipped).
- **Rationale**: Adding Lucide or FontAwesome would inflate bundle size by 15–30 KB for only 5–6 icons.

### C002: How does SegmentedControl handle responsive viewports (< 480px)?
- **Decision**: On narrow viewports, the control allows horizontal scrolling (`overflow-x: auto`) with hidden scrollbars or flex-wraps smoothly depending on container width, with full touch swipe support and minimum 44px touch targets.
- **Rationale**: Ensures lab selection and question count tabs are comfortable to tap on mobile devices without accidental misclicks.

### C003: Can Button support polymorphic rendering (e.g. as `<a>` link or `<button>`)?
- **Decision**: Yes. The `Button` and `IconButton` components accept an `as` prop (defaulting to `'button'`), supporting `<a>` or React Router links while preserving full button styling, keyboard handlers, and accessibility attributes.
