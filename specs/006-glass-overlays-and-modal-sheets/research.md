# Research & Optical Analysis: Unit 006 — Glass Overlays & Modal Sheets

## 1. Reference Figma Analysis ("Venus Dashboard Builder")
The reference modal dialogs in the Figma design system (`media_1792515762854.png` and `media_1792515757180.png`):
- Soft luminous surfaces with deep, diffuse elevation (`box-shadow: 0 24px 48px rgba(0, 0, 0, 0.16)`).
- Crisp close button in top right (`IconButton` circle).
- Divided sections: header, scrollable body with generous padding, action button bar at bottom.
- Tables for tabular statistics (e.g., topic weaknesses, attempt dates) use alternating subtle rows (`#F4F7FE`) with rounded corners and high-contrast typography.

## 2. Apple iOS 26 Glass Sheet Physics
- Backdrop scrim uses a gentle dark blur (`8px` blur) that softly defuses the ambient mesh background and underlying cards.
- The modal sheet features specular rim lighting (`1px solid rgba(255, 255, 255, 0.35)` in light mode, `rgba(255, 255, 255, 0.12)` in dark mode).
- Spring micro-motion on entry: `scale(0.96) translateY(8px)` -> `scale(1) translateY(0)` with `cubic-bezier(0.16, 1, 0.3, 1)`.
