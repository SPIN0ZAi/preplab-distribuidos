# Research & Layout Analysis: Unit 005 — Inset App Shell

## 1. Reference Figma Analysis ("Venus Dashboard Builder")
In the reference Figma dashboard (`media_1792515753271.png` and `media_1792515764444.png`), the left navigation sidebar features:
- Inset floating card geometry surrounded by airy margins.
- Clean vertical navigation links with dedicated icons, subtle gray text for inactive items, and bold electric indigo accents for the active route.
- A vertical brand pill or indicator on the active route item.
- Generous padding and clean grouping of routes into primary, lab-specific, and secondary utility sections.

## 2. Apple iOS 26 Glass Elevation & Compositing
- Both the sidebar and topbar float above the ambient mesh background (`z-index: 10`), using regular glass (`16px` blur desktop, `12px` mobile).
- The main content area sits beside the sidebar with a fixed gutter of `20px–28px`.
- Hardware acceleration (`transform: translateZ(0)`) is maintained on all fixed/floating chrome layers to prevent compositing redraws while the main content area scrolls.
