# Reverse Engineering: Current UI/UX Audit & Visual Baseline

## 1. Visual Design Baseline Evaluation

| Dimension | Current State | Target State (Venus + Liquid Glass) | Gap Analysis |
| :--- | :--- | :--- | :--- |
| **Color System** | Single-theme dark palette (`#0B0F19`, `#111827`, `#1E293B`, `#6366F1`). | Dual-theme system: Venus Light Mode (`#F4F7FE` page bg, `#FFFFFF` cards, `#4318FF` primary indigo, `#7551FF` gradient, `#1B2559` navy text) + Dark Mode. | Current palette lacks the luminous, clean soft-UI feel of Venus. Needs complete tokenization. |
| **Surface Depth & Materials** | Flat dark cards with simple 1px borders (`rgba(255,255,255,0.08)`) and basic box-shadows. | Two-layer system: Solid soft-UI white cards with layered diffuse shadows (`0 18px 40px rgba(112,144,176,0.12)`) + Liquid Glass chrome with specular edge highlights and inner reflections. | Flat cards lack depth; no authentic translucent glass layering or ambient refraction. |
| **Navigation & App Shell** | Static top header (`.app-header`) bounded within a max-width 1080px container. | Inset floating glass topbar + desktop floating inset glass sidebar + mobile bottom glass drawer. | Missing modern dashboard navigation structure and floating glass aesthetic. |
| **Typography** | `Plus Jakarta Sans` for UI, `JetBrains Mono` for code. | Add `Poppins` for bold metric numbers and primary headings; retain `Plus Jakarta Sans` for body text. | Metrics and titles need the geometric presence and bold weight of Venus headers. |
| **Card Radii & Corners** | 12px (`--radius-md`) to 16px (`--radius-lg`). | 20px–24px for cards, 12px–16px for controls, concentric nested pill radii for glass chrome. | Current corners are slightly tight compared to modern soft-UI standards. |
| **Interactive Controls** | Basic hover states with slight opacity changes. | Fluid spring-like transitions (150–250ms), active scale-down (`0.97`), specular lighting shifts on hover. | Needs high-fidelity micro-interactions and tactile response. |
| **Data Visualization** | Raw numbers, simple styled percentage texts, basic div-based progress bars. | Custom SVG rounded-top bar charts with 1 highlighted indigo bar, smooth area curve charts, circular gauge meters. | Major opportunity to elevate engagement and pedagogical clarity. |

---

## 2. Accessibility Baseline (WCAG 2.2 AA)

1. **Color Contrast**:
   - Current dark mode text colors (`#F8FAFC` on `#111827`) pass AAA (> 11:1).
   - Under the new Venus Light Mode, secondary text must maintain ≥ 4.5:1 against `#FFFFFF` cards (using `#707EAE` or `#A3AED0` tuned to compliant values).
   - Text on Liquid Glass surfaces must maintain ≥ 4.5:1 against both light ambient mesh and dark regions.
2. **Focus Visibility**:
   - Currently uses default browser outlines or soft box-shadows.
   - Target: Standardize high-contrast 2px `:focus-visible` offset rings that remain visible across all glass and solid card states.
3. **Screen Reader Landmarks**:
   - Currently uses basic `<header>` and `<main>` tags.
   - Target: Add semantic `<nav>` for sidebar/topbar, `<section>` for review blocks, and proper ARIA live regions for the countdown timer and modal announcements.
4. **Motion & Transparency Preferences**:
   - Currently lacks `@media (prefers-reduced-transparency: reduce)` and `@media (prefers-reduced-motion: reduce)`.
   - Target: Full compliance with immediate static/opaque degradation.
