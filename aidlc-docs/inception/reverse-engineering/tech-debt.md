# Reverse Engineering: Technical Debt & Risk Assessment

## 1. Identified Technical Debt

| Item ID | Component / Area | Description | Severity | Remediation Strategy |
| :--- | :--- | :--- | :---: | :--- |
| **TD-01** | `src/index.css` | Monolithic 1001-line CSS file mixing reset, utilities, component styles, and theme variables without modular separation. | High | Refactor into modular architecture: `tokens/` (Venus + Glass), `materials/` (GlassSurface), `primitives/`, `composites/`, and `views/`. |
| **TD-02** | Theme Hardcoding | Styles assume dark mode exclusively (`#0B0F19`, `#1E293B`) with no light mode tokens or dynamic theme switching. | High | Implement dual-theme design tokens where Venus Light Mode is default and Dark Mode is a clean variable swap (`data-theme="dark"`). |
| **TD-03** | Automated Testing Gap | Zero unit tests for `storage.ts`, `quizEngine.ts`, `Timer.tsx`, or UI components. | High | Install Vitest + React Testing Library (ADR-0001) and write characterization tests before any UI refactor. |
| **TD-04** | Responsive Layout Debt | Center-column layout max-width 1080px with fixed paddings; lacks modern inset floating app shell (sidebar + topbar) featured in Venus kit. | Medium | Build responsive app shell with desktop floating glass sidebar and mobile glass pill. |
| **TD-05** | Charting & Data Visuals | Weaknesses and scores are presented in standard HTML tables and simple divs; lacks the rich visual engagement of Venus rounded-top bar charts and area curves. | Medium | Introduce custom SVG chart primitives (< 5 KB total footprint, zero external deps). |
| **TD-06** | Focus & Keyboard Ring Inconsistencies | Focus rings rely partly on browser default outlines which have poor contrast on dark or translucent surfaces. | Medium | Standardize custom high-contrast focus rings (`:focus-visible`) tailored for both solid and glass surfaces. |

---

## 2. Technical Risk Matrix

| Risk ID | Risk Description | Likelihood | Impact | Mitigation Plan |
| :--- | :--- | :---: | :---: | :--- |
| **R-01** | **Backdrop-filter GPU jank on mobile / low-end devices** | Medium | High | Limit glass blur to 12px on mobile, restrict glass to <25% viewport area, avoid animating blur radii, use `will-change: backdrop-filter` conservatively. |
| **R-02** | **Legibility failure over dynamic / moving backdrops** | Medium | High | Enforce minimum 4.5:1 text contrast using tuned glass fills (white 0.45+ alpha) and specular edge highlights. Test with automated contrast matrix. |
| **R-03** | **Nested backdrop-filter rendering bugs in Safari / WebKit** | Low | High | Enforce rule: zero nested backdrop filters. Modals use solid or lightly dimmed scrims rather than multi-layered blurs. |
| **R-04** | **Browser fallback failure where backdrop-filter is unsupported** | Low | High | Provide complete `@supports not (backdrop-filter: blur(1px))` fallbacks to 92% opaque tinted surfaces. Respect `prefers-reduced-transparency`. |
| **R-05** | **Regression of existing 520-question quiz engine or session saving** | Low | Critical | Lock in characterization tests for `storage.ts` and `quizEngine.ts` before modifying any component logic. |
