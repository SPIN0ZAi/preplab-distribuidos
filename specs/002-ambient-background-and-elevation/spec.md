# Specification: Unit 002 — Ambient Background Canvas & Elevation Layer

## 1. Objective & Purpose

Establish an optimized ambient background canvas layer ($z=0$) that supplies luminous, low-contrast color information for the floating Liquid Glass chrome to refract.

In order for a translucent `backdrop-filter: blur() saturate()` surface to look like real treated glass, the surface behind it cannot be flat white or monochromatic grey; it requires gentle chromatic variation (soft indigo, purple, and coral gradient orbs). At the same time, **Glass Discipline (Rule 10)** dictates that:
1. The ambient background must remain subtle and low in contrast so that text contrast on solid white content cards remains unaffected ($\ge 7:1$).
2. The implementation must be **GPU-cheap**: pure CSS radial gradients fixed to the viewport background, avoiding heavy canvas render loops, expensive CSS blur filters on full-screen containers, or large bitmap image assets.
3. The background must adapt cleanly to both Light Mode (`#F4F7FE` base canvas) and Dark Mode (`#0B0F19` deep navy base).
4. The background must respect user motion preferences (`prefers-reduced-motion: reduce`) by remaining completely static.

---

## 2. User-Visible Behavior & Scenarios

### Scenario 1: Default Viewport Rendering (Light Mode)
- **Given** the user is viewing any screen in Light Mode,
- **When** the viewport renders,
- **Then** the base canvas displays a luminous light tone (`#F4F7FE`),
- **And** three soft, fixed radial gradient meshes are visible:
  1. Top-left: Indigo orb `rgba(67, 24, 255, 0.07)`
  2. Bottom-right: Purple orb `rgba(117, 81, 255, 0.06)`
  3. Center-right: Soft coral sheen `rgba(255, 122, 138, 0.04)`
- **And** as the user scrolls, the floating topbar and sidebar refract these soft tones with optical saturation boost.

### Scenario 2: Dark Mode Ambient Mesh
- **Given** the application transitions to Dark Mode (`[data-theme="dark"]`),
- **When** the background re-renders,
- **Then** the canvas shifts to deep navy (`#0B0F19`),
- **And** the ambient orbs shift to deep indigo (`rgba(99, 102, 241, 0.12)`) and electric cyan/purple (`rgba(6, 182, 212, 0.08)`),
- **And** the transition executes smoothly over 200ms.

### Scenario 3: Respecting `prefers-reduced-motion`
- **Given** a user with OS setting `prefers-reduced-motion: reduce`,
- **When** the page renders or scrolls,
- **Then** zero parallax shifts, pulse animations, or position transitions are executed on the background mesh.

---

## 3. Traceable Requirements

| Requirement ID | Description | Acceptance Criteria |
| :--- | :--- | :--- |
| **FR-001** | Tokenized styling | Ambient mesh colors derive from `--venus-*` and `--glass-*` variables. |
| **FR-004** | Floating chrome refraction | Provides colored backdrop for floating sidebar and topbar. |
| **NFR-002** | Core Web Vitals (CLS & LCP) | Zero layout shift ($CLS < 0.1$); $LCP < 2.5s$. |
| **NFR-003** | 60 fps frame rate | Zero GPU thermal throttling during scroll. |
| **NFR-007** | Contrast on content | Primary text on solid cards maintains $\ge 7:1$ contrast over ambient base. |
| **NFR-010** | Reduced motion | Static rendering when reduced motion is preferred. |

---

## 4. Edge Cases & Boundary Conditions

1. **Window Resizing**: Radial gradients must use percentage-based coordinates (`circle at 10% 10%`, etc.) so they scale smoothly without distortion on ultra-wide (1920px+) or narrow mobile (375px) displays.
2. **Body Scrolling & Overscroll Bounce**: Fixed background attachment (`background-attachment: fixed` or fixed container with `pointer-events: none; z-index: 0`) ensures that overscroll bounce on iOS Safari does not reveal unstyled white borders.
3. **Contrast Preservation**: Gradient opacity must never exceed `0.10` in Light Mode to ensure that text on glass retains $\ge 4.5:1$ contrast even at the exact center of the gradient orbs.
