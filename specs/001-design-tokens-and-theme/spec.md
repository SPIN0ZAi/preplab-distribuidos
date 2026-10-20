# Specification: Unit 001 — Design Tokens & Dual-Theme System

## 1. Objective & Purpose

Establish a robust, centralized design token architecture that serves as the single source of truth for all visual attributes across the application. This unit delivers:
1. **Venus Content Layer Tokens**: Luminous soft-UI light theme (`#F4F7FE` page canvas, `#FFFFFF` solid cards, `#4318FF` electric indigo accent, `#7551FF` purple secondary, `#1B2559` bold navy text, `#707EAE` secondary text), 8px spatial grid, card radii (12px, 16px, 20px, 24px), and diffuse colored shadows (`0 18px 40px rgba(112, 144, 176, 0.12)`).
2. **Liquid Glass Chrome Layer Tokens**: Three blur tiers (`thin: 8px`, `regular: 18px`, `thick: 28px`), saturation boosts (`140%`–`180%`), specular 1px borders, inner highlights, diagonal surface sheen gradients, and layered tinted shadows.
3. **Dual-Theme Engine**: Seamless switching between Venus Light Mode (`data-theme="light"`, default) and Modern Dark Mode (`data-theme="dark"`, `#0B0F19` deep navy canvas, `#111827` cards) with instant token re-mapping and local storage persistence.
4. **Typography Scale**: Integration of `Poppins` for geometric display titles and metric numbers, retaining `Plus Jakarta Sans` for body copy and `JetBrains Mono` for code snippets.

---

## 2. User-Visible Behavior & Scenarios

### Scenario 1: Initial Application Load
- **Given** a user opens the application for the first time with no prior stored preferences,
- **When** the page renders,
- **Then** the system detects the user's OS color scheme via `window.matchMedia('(prefers-color-scheme: dark)')`,
- **And** defaults to **Venus Light Mode** (`data-theme="light"`), rendering a clean `#F4F7FE` canvas with soft ambient meshes and solid white cards.

### Scenario 2: Manual Theme Toggle
- **Given** the application is rendering in Light Mode,
- **When** the user clicks the Theme Switcher control,
- **Then** `data-theme` on the `<html>` root attribute switches to `"dark"`,
- **And** all CSS variables transition smoothly over 200ms without visual flash or layout shift,
- **And** the chosen preference is saved to `localStorage` under key `ds_quiz_theme_preference`.

### Scenario 3: Page Reload Theme Persistence
- **Given** the user previously toggled the theme to Dark Mode,
- **When** they reload or revisit the application,
- **Then** an inline script in the document `<head>` reads `localStorage` before DOM paint,
- **And** applies `data-theme="dark"` immediately to prevent any white-to-dark flash of unstyled content (FOUC).

### Scenario 4: Accessibility Fallbacks (Reduced Transparency & High Contrast)
- **Given** a user with `prefers-reduced-transparency: reduce` enabled on their OS,
- **When** the design tokens are applied,
- **Then** `--glass-blur-*` variables resolve to `0px`,
- **And** `--glass-fill-*` variables resolve to high-contrast opaque tinted fills (`0.92` to `0.96` alpha),
- **And** all text maintains $\ge 4.5:1$ contrast against the opaque fallback surface.

---

## 3. Traceable Requirements

| Requirement ID | Description | Acceptance Criteria |
| :--- | :--- | :--- |
| **FR-001** | Tokenized styling | 100% of colors, spaces, radii, and blurs sourced from CSS variables. |
| **FR-002** | Theme toggle transition | Mode transition completes within 200ms without reload. |
| **FR-003** | Default theme & OS detection | Defaults to Venus Light, respects OS dark preference if unset. |
| **NFR-006** | Text contrast on glass | Text on glass achieves $\ge 4.5:1$ contrast across all backdrops. |
| **NFR-007** | Text contrast on content | Text on solid cards achieves $\ge 7:1$ (primary) and $\ge 4.5:1$ (secondary). |
| **NFR-009** | Reduced transparency | Instant degradation to opaque surfaces when active. |
| **NFR-010** | Reduced motion | Transitions evaluate to 0s when active. |
| **NFR-011** | Forced colors | Borders and text map to system colors (`CanvasText`, `ButtonText`). |

---

## 4. Edge Cases & Boundary Conditions

1. **Rapid Theme Toggling**: If the user rapidly clicks the toggle, CSS transitions must not desynchronize or trigger layout recalculation bottlenecks. Handled via pure CSS variable re-binding.
2. **Unsupported Browsers (No Custom Properties)**: Modern browsers targeted (Vite build output target `esnext` / `es2020`); CSS variables are universally supported (100% baseline).
3. **Contrast with Ambient Gradient Orbs**: In Light Mode, ambient orbs (`rgba(67, 24, 255, 0.07)`) must remain sufficiently low in opacity so that text on top of glass retains $\ge 4.5:1$ contrast even when passing directly over the orb centers.

---

## 5. Scope Boundaries

- **In-Scope**: CSS custom properties, dual-theme definitions, font loading for Poppins in `index.html`, theme toggle service and event listener.
- **Out-of-Scope**: Component refactoring (handled in subsequent units U2–U8).
