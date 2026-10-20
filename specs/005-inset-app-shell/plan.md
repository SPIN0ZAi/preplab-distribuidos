# Construction Plan: Unit 005 — Inset App Shell

## 1. Architectural Strategy
Implement a responsive layout shell with the following component tree:
```
src/
├── components/
│   └── shell/
│       ├── AppShell.tsx (Main Layout orchestrator)
│       ├── InsetSidebar.tsx (Desktop glass sidebar)
│       ├── InsetTopbar.tsx (Desktop & tablet floating topbar)
│       └── MobileNavPill.tsx (Mobile bottom floating navigation)
├── styles/
│   └── shell/
│       ├── app-shell.css
│       ├── inset-sidebar.css
│       ├── inset-topbar.css
│       └── mobile-nav-pill.css
└── types/
    └── shell.ts
```

## 2. Execution Phases
1. **Types & Shell Contracts (`T018`)**: Formulate navigation item definitions, layout props, and breadcrumb structures in `src/types/shell.ts`.
2. **Inset Sidebar Styles & Component (`T019`)**: Build `inset-sidebar.css` and `InsetSidebar.tsx` utilizing `<GlassSurface variant="regular">`.
3. **Inset Topbar Styles & Component (`T020`)**: Build `inset-topbar.css` and `InsetTopbar.tsx` with breadcrumbs, theme toggle, and search trigger.
4. **Mobile Navigation Pill (`T021`)**: Build `mobile-nav-pill.css` and `MobileNavPill.tsx`.
5. **App Shell Assembly & Responsive Verification (`T022`)**: Build `AppShell.tsx` wrapping main view content, verify responsive layout (375px to 1440px), and run `npm run build`.
