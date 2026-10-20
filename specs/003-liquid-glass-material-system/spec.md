# Specification: Unit 003 — Liquid Glass Material System & Fallbacks

## 1. Objective & Purpose

Deliver a unified, reusable Liquid Glass material system that encapsulates Apple's iOS 26 optical aesthetic across all chrome surfaces. Rather than spreading ad-hoc `backdrop-filter` styles across components, this unit implements:
1. **The 6-Layer Optical Glass Recipe**:
   - Layer 1: Hardware-accelerated `backdrop-filter: blur(Npx) saturate(160%)` with `-webkit-backdrop-filter`.
   - Layer 2: Translucent tinted fill adapted to theme.
   - Layer 3: 1px translucent physical border (`--glass-border`).
   - Layer 4: Inset top/left specular highlight (`--glass-edge-highlight`) and inset bottom/right shadow (`--glass-edge-shade`).
   - Layer 5: Diagonal light-catching surface sheen (`--glass-sheen` via `::before`).
   - Layer 6: Layered tinted outer drop shadows (`--glass-shadow`, `--glass-shadow-floating`, `--glass-shadow-modal`).
2. **Material Variants**:
   - `thin` (8px blur, 32% fill): Badges, timer pill, segmented controls.
   - `regular` (18px blur, 48% fill): Inset topbar, floating sidebar, toolbars.
   - `thick` (28px blur, 68% fill): Modal sheets, mobile bottom navigation, popover menus.
3. **Glass Discipline Enforced (Rule 10)**:
   - Used exclusively for Chrome Layer.
   - Maximum 4 concurrent active layers.
   - Total glass area strictly $< 25\%$ of viewport area.
   - Zero nested `backdrop-filter` elements.
4. **Universal Fallbacks**:
   - Automatic degradation to 94% opaque tinted surfaces under `@supports not (backdrop-filter)`.
   - Instant non-translucent solid display under `prefers-reduced-transparency: reduce`.
   - High-contrast system borders under `forced-colors: active`.
   - Contrast proof guaranteeing $\ge 4.5:1$ text contrast against worst-case backdrops.

---

## 2. User-Visible Behavior & Scenarios

### Scenario 1: Interacting with Floating Glass Chrome
- **Given** a floating glass topbar, sidebar, or timer pill,
- **When** content cards scroll beneath the surface,
- **Then** the text and colors underneath blur softly with an optical saturation boost,
- **And** the specular top edge catches the light with a crisp white highlight,
- **And** all text rendered on the glass remains crisp, legible, and passes $\ge 4.5:1$ contrast.

### Scenario 2: Reduced Transparency Activation
- **Given** a user has enabled "Reduce Transparency" in their system accessibility preferences,
- **When** viewing any glass surface,
- **Then** all `backdrop-filter` blur effects are removed,
- **And** surfaces display with 94% solid opaque fill and high-contrast border,
- **And** zero visual distortion or legibility issues occur.

### Scenario 3: Non-Supporting Browser Fallback
- **Given** an environment without `backdrop-filter` support,
- **When** rendering glass surfaces,
- **Then** the `@supports not ((backdrop-filter: blur(1px)) or (-webkit-backdrop-filter: blur(1px)))` rules activate,
- **And** surfaces render as clean, semi-opaque cards with soft box-shadows.

---

## 3. Traceable Requirements

| Requirement ID | Description | Acceptance Criteria |
| :--- | :--- | :--- |
| **FR-001** | Tokenized styling | Optical properties driven by `--glass-*` tokens. |
| **NFR-003** | 60 fps scrolling | Hardware composited; no scroll jank over solid content. |
| **NFR-004** | Glass budget (<25% area, max 4 layers)| Surface area strictly bounded; no nested blurs. |
| **NFR-005** | Mobile blur limit ($\le 12px$) | Blur capped to 12px on viewports $< 768px$. |
| **NFR-006** | Text contrast on glass ($\ge 4.5:1$) | Passes 4-point worst-case backdrop contrast matrix. |
| **NFR-009** | Reduced transparency fallback | Degrades to 94% opaque fill when active. |
| **NFR-011** | Forced colors fallback | Degrades to system borders and solid canvas. |
| **NFR-013** | `@supports` browser fallback | Pure CSS fallback for browsers without backdrop-filter. |
| **NFR-017** | Zero CSS duplication | Implemented via single reusable `GlassSurface` component/utility. |

---

## 4. Edge Cases & Boundary Conditions

1. **Safari WebKit Clipping**: In WebKit, combining `backdrop-filter` on an element with `overflow: hidden` and `border-radius` can clip incorrectly during transforms. Solved by specifying `-webkit-backdrop-filter` and `isolation: isolate` on the glass container.
2. **Text Over Sharp Contrast Boundaries**: Where a glass surface crosses from a light card onto an ambient gradient orb, the 0.48 fill opacity + 18px blur ensures the background is averaged out smoothly, maintaining $\ge 4.5:1$ text contrast across the entire surface.
3. **No Nested Blurs**: When a modal sheet is displayed, the background scrim does NOT apply a second `backdrop-filter` over the topbar/sidebar; instead, a lightweight dimming scrim (`rgba(0,0,0,0.50)`) is used.
