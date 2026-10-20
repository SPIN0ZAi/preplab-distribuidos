# Atomic Tasks: Unit 005 — Inset App Shell

## Dependency Graph
```
T018 [Contracts & Types] ──> T019 [InsetSidebar] ──> T020 [InsetTopbar] ──> T021 [MobileNavPill] ──> T022 [AppShell Assembly & Build]
```

---

## Detailed Tasks Matrix

### T018: Author Shell Types & Navigation Config
- **File**: `src/types/shell.ts`
- **Requirement Link**: `FR-001`, `FR-006`, `NFR-011`
- **Estimated Effort**: 30 mins
- **Description**: Define TypeScript interfaces for `AppShellProps`, `InsetSidebarProps`, `InsetTopbarProps`, `MobileNavPillProps`, and navigation item configurations.
- **Definition of Done**: Clean TypeScript compilation with zero type errors.

### T019: Build Desktop Inset Glass Sidebar
- **Files**: `src/styles/shell/inset-sidebar.css`, `src/components/shell/InsetSidebar.tsx`
- **Requirement Link**: `FR-001`, `FR-004`, `NFR-003`, `NFR-006`
- **Estimated Effort**: 60 mins
- **Description**: Implement 260px wide floating inset sidebar with `<GlassSurface variant="regular">`. Feature brand header with indigo gradient badge, navigation links with active indicators, and status pill footer.
- **Definition of Done**: Sidebar renders floating with 20px margins on viewports $\ge 768\text{px}$, hides cleanly on $< 768\text{px}$.

### T020: Build Floating Inset Topbar
- **Files**: `src/styles/shell/inset-topbar.css`, `src/components/shell/InsetTopbar.tsx`
- **Requirement Link**: `FR-001`, `FR-002`, `NFR-006`
- **Estimated Effort**: 45 mins
- **Description**: Implement floating topbar with breadcrumb display, active exam timer / question count badge, theme toggle `<IconButton>`, and quick navigation shortcuts.
- **Definition of Done**: Topbar floats with regular glass optics; theme toggle switches themes instantly.

### T021: Build Mobile Floating Bottom Navigation Pill
- **Files**: `src/styles/shell/mobile-nav-pill.css`, `src/components/shell/MobileNavPill.tsx`
- **Requirement Link**: `FR-001`, `FR-004`, `NFR-006`, `NFR-008`
- **Estimated Effort**: 45 mins
- **Description**: Implement mobile floating glass pill bar positioned fixed at `bottom: 16px`, visible only on $< 768\text{px}$. Touch targets $\ge 48\times 48\text{px}$.
- **Definition of Done**: Renders fixed on mobile; switches active tabs; disappears on desktop.

### T022: Assemble AppShell & Verify Responsive Viewports
- **Files**: `src/styles/shell/app-shell.css`, `src/components/shell/AppShell.tsx`, `src/components/shell/index.ts`
- **Requirement Link**: `FR-001`, `FR-004`, `FR-006`, `NFR-009`
- **Estimated Effort**: 45 mins
- **Description**: Assemble the responsive shell orchestrator. Ensure desktop two-column grid (`sidebar + main`) transitions to single column with bottom padding on mobile. Run `npm run build` to verify 0 errors and bundle budget $< 200\text{ KB}$ gzipped.
- **Definition of Done**: Production build succeeds; responsive layout handles 375px to 1440px.
