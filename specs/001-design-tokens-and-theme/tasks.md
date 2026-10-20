# Atomic Tasks: Unit 001 — Design Tokens & Dual-Theme System

## Task Dependency Ordering

```
T001 [Setup & Typography in HTML] ──> T002 [Venus Content Tokens] ──> T004 [Dark Theme Overrides]
                                  ──> T003 [Liquid Glass Tokens]  ──> T005 [Theme Service & FOUC Script]
                                                                  ──> T006 [Build & Contrast Verification]
```

---

## Detailed Tasks Matrix

### T001: Configure Typography & Preconnect in `index.html`
- **File**: `index.html`
- **Requirement Link**: `FR-001`, `US-001`
- **Parallelizable**: No
- **Estimated Effort**: 30 mins
- **Description**: Add Google Fonts preconnect and link for `Poppins` (weights 500, 600, 700, 800) alongside existing `Plus Jakarta Sans` and `JetBrains Mono`. Update `<title>` and meta tags.
- **Definition of Done**: Network tab shows Poppins loads cleanly without render-blocking delays.

### T002 [P]: Author Venus Content Tokens CSS
- **File**: `src/styles/tokens/venus-tokens.css`
- **Requirement Link**: `FR-001`, `US-001`, `NFR-007`
- **Parallelizable**: Yes (with T003)
- **Estimated Effort**: 45 mins
- **Description**: Formulate all Venus soft-UI CSS custom properties: light canvas `#F4F7FE`, solid card `#FFFFFF`, primary electric indigo `#4318FF`, brand gradient, typography colors, 8px spatial grid, radii (12/16/20/24px), and diffuse shadows.
- **Definition of Done**: Tokens load under `:root`; CSS variables are inspectable and resolve properly in browser.

### T003 [P]: Author Liquid Glass Chrome Tokens CSS
- **File**: `src/styles/tokens/glass-tokens.css`
- **Requirement Link**: `FR-001`, `US-001`, `NFR-006`, `NFR-009`
- **Parallelizable**: Yes (with T002)
- **Estimated Effort**: 45 mins
- **Description**: Formulate Liquid Glass CSS custom properties: blur tiers (`thin: 8px`, `regular: 18px`, `thick: 28px`), saturation boosts, specular 1px border, inset highlights, diagonal sheen gradient, and fallback tokens for `@supports not (backdrop-filter)` and `prefers-reduced-transparency`.
- **Definition of Done**: Glass tokens load under `:root`; media queries for reduced transparency resolve fallback fills.

### T004: Author Dark Mode Token Overrides
- **File**: `src/styles/theme.css`
- **Requirement Link**: `FR-002`, `FR-003`, `US-002`
- **Parallelizable**: No (depends on T002, T003)
- **Estimated Effort**: 45 mins
- **Description**: Create `[data-theme="dark"]` token mapping overriding Venus canvas to deep navy `#0B0F19`, cards to `#111827`, and glass fills to translucent navy (`rgba(17, 24, 39, 0.50)`). Add transition smoothness rules (`200ms ease`).
- **Definition of Done**: Setting `data-theme="dark"` on `<html>` instantaneously updates all visual tokens cleanly.

### T005: Implement Theme Service & Anti-FOUC Script
- **Files**: `src/services/theme.ts`, `index.html`
- **Requirement Link**: `FR-002`, `FR-003`, `US-002`
- **Parallelizable**: No (depends on T004)
- **Estimated Effort**: 30 mins
- **Description**: Build `src/services/theme.ts` exporting `getTheme()`, `setTheme()`, and `toggleTheme()`. Insert inline `<head>` script in `index.html` reading `localStorage` before paint to eliminate FOUC.
- **Definition of Done**: Page reloads in dark mode with zero white flash; `theme.ts` manages persistence reliably.

### T006: Build, TypeScript & Contrast Verification
- **Files**: Workspace-wide
- **Requirement Link**: `NFR-001`, `NFR-006`, `NFR-007`
- **Parallelizable**: No (final gate task)
- **Estimated Effort**: 30 mins
- **Description**: Execute `npm run build` to verify clean TypeScript compilation and asset bundling. Run manual contrast checks verifying $\ge 4.5:1$ text contrast in both Light and Dark modes.
- **Definition of Done**: `npm run build` exits 0 with zero warnings; bundle budget remains $< 200\text{ KB}$ gzipped.
