# Construction Plan: Unit 004 — UI Component Primitives

## 1. Architectural Strategy
Build atomic, modular UI primitives that strictly map to the Venus token system and the Liquid Glass material system. These primitives will reside in `src/components/primitives/` with accompanying CSS stylesheets in `src/styles/primitives/`.

```
src/
├── components/
│   └── primitives/
│       ├── Button.tsx
│       ├── IconButton.tsx
│       ├── Badge.tsx
│       ├── SegmentedControl.tsx
│       ├── TextInput.tsx
│       └── Icons.tsx (zero-dependency SVGs)
├── styles/
│   └── primitives/
│       ├── button.css
│       ├── badge.css
│       ├── segmented-control.css
│       └── text-input.css
└── types/
    └── primitives.ts
```

## 2. Execution Phases
1. **Types & Contracts (`T013`)**: Define rigorous TypeScript interfaces for all primitives in `src/types/primitives.ts`.
2. **Shared Lightweight SVG Icons (`T014`)**: Create zero-overhead SVG helper components in `src/components/primitives/Icons.tsx` (Search, Close, Chevron, Check, Spinner, Flame, Sparkles).
3. **Core Buttons & Badges (`T015`)**: Author `button.css`, `badge.css`, `Button.tsx`, `IconButton.tsx`, and `Badge.tsx`.
4. **Interactive Controls (`T016`)**: Author `segmented-control.css`, `text-input.css`, `SegmentedControl.tsx`, and `TextInput.tsx`.
5. **Integration & Build Verification (`T017`)**: Export all primitives from `src/components/primitives/index.ts`, run `npm run build`, and verify bundle size, keyboard accessibility, and contrast.
