# Atomic Tasks: Unit 004 — UI Component Primitives

## Dependency Graph
```
T013 [Types & Contracts] ──> T014 [Inline SVG Icons] ──> T015 [Button, IconButton, Badge] ──> T016 [SegmentedControl, TextInput] ──> T017 [Build Verification]
```

---

## Detailed Tasks Matrix

### T013: Author TypeScript Contracts for UI Primitives
- **File**: `src/types/primitives.ts`
- **Requirement Link**: `FR-001`, `NFR-008`, `NFR-011`
- **Estimated Effort**: 30 mins
- **Description**: Formulate all type definitions, variant enumerations, sizes, and HTML attribute extensions for `Button`, `IconButton`, `Badge`, `SegmentedControl`, and `TextInput`.
- **Definition of Done**: Clean TypeScript compilation with zero type errors.

### T014: Author Zero-Overhead Inline SVG Icons
- **File**: `src/components/primitives/Icons.tsx`
- **Requirement Link**: `FR-001`, `NFR-009` (Bundle size < 200 KB)
- **Estimated Effort**: 30 mins
- **Description**: Implement lightweight, zero-dependency inline SVG icon components (`SearchIcon`, `CloseIcon`, `ChevronDownIcon`, `CheckIcon`, `SpinnerIcon`, `SparklesIcon`, `FlameIcon`, `ClockIcon`).
- **Definition of Done**: SVGs render crisply at 16px/20px/24px with `currentColor` inheritance.

### T015: Build `Button`, `IconButton`, and `Badge` Components & Styles
- **Files**: `src/styles/primitives/button.css`, `src/styles/primitives/badge.css`, `src/components/primitives/Button.tsx`, `src/components/primitives/IconButton.tsx`, `src/components/primitives/Badge.tsx`
- **Requirement Link**: `FR-001`, `FR-002`, `NFR-006`, `NFR-008`
- **Estimated Effort**: 60 mins
- **Description**: Implement Venus soft-UI button styles (`primary`, `secondary`, `glass`, `danger`, `ghost`), tactile spring physics (`hover: translateY(-1px)`, `active: scale(0.97)`), WCAG 2.2 focus visible rings, and luminous pill badges.
- **Definition of Done**: Components render with complete variant support, keyboard accessibility, and loading state.

### T016: Build `SegmentedControl` & `TextInput` Components & Styles
- **Files**: `src/styles/primitives/segmented-control.css`, `src/styles/primitives/text-input.css`, `src/components/primitives/SegmentedControl.tsx`, `src/components/primitives/TextInput.tsx`
- **Requirement Link**: `FR-001`, `FR-004`, `NFR-006`, `NFR-008`
- **Estimated Effort**: 60 mins
- **Description**: Implement soft-track segmented control with animated active pill indicator, arrow-key navigation, ARIA radiogroup roles, and soft search text input with clear button.
- **Definition of Done**: Keyboard navigation works cleanly; active tab transitions smoothly; input handles typing and clearing.

### T017: Index Export & Production Build Verification
- **Files**: `src/components/primitives/index.ts`, `src/styles/theme.css`
- **Requirement Link**: `NFR-001`, `NFR-009`
- **Estimated Effort**: 30 mins
- **Description**: Export all primitives via barrel file, import primitive styles into `theme.css`, run `npm run build`, and verify bundle size remains under 200 KB gzipped.
- **Definition of Done**: `npm run build` succeeds with 0 errors; 520 questions verified.
