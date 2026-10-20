# Research & Design Analysis: Unit 004 — UI Component Primitives

## 1. Reference Figma Analysis ("Venus Dashboard Builder")
Analyzing the provided reference images (`media_1792515753271.png` through `media_1792515764444.png`) reveals distinctive styling across buttons, badges, and controls:
- **Primary Buttons**: Saturated Electric Indigo `#4318FF` with pure white text, medium weight (600), high diffuse drop shadow (`box-shadow: 0 14px 24px rgba(67, 24, 255, 0.28)`), generous horizontal padding (`20px–24px`), and curved corners (`12px–16px` or full pill `9999px`).
- **Badges/Pills**: Soft luminous tinted backgrounds with matching saturated foreground text (e.g., `#05CD99` with `rgba(5, 205, 153, 0.12)`, `#EE5D50` with `rgba(238, 93, 80, 0.12)`). Typography is bold uppercase or capitalized 11–12px.
- **Segmented Controls**: Embedded in soft background tracks with elevated white pills for the active selection, providing instant spatial cues.
- **Inputs**: Seamlessly integrated with light `#F4F7FE` backgrounds, soft gray placeholder text `#A3AED0`, and electric indigo accents.

## 2. Apple iOS 26 Liquid Glass Integration
- **Glass Buttons & Badges**: Secondary actions and toolbar controls can adopt the `.glass-surface--thin` class, providing tactile glass floating over the canvas with specular rim highlights.
- **Tactile Physics**: Micro-interactions utilize spring curve `cubic-bezier(0.16, 1, 0.3, 1)`, providing an immediate active scale-down (`scale(0.97)`) and subtle elevation lift on hover (`translateY(-1px)`).
