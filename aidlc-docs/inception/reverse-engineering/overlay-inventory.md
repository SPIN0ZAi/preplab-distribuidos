# Reverse Engineering: Overlay & Chrome Inventory (Glass Discipline Analysis)

## 1. Classification Methodology (Rule 10 Enforced)

In strict accordance with **Rule 10 (Glass Discipline)**:
- **Chrome Layer (Glass Candidates)**: Elements that float above, overlay, anchor navigation, or act as transient contextual controls.
- **Content Layer (Solid Venus Cards)**: Elements conveying primary pedagogical data, questions, forms, explanations, statistics, and charts.

---

## 2. Element Inventory & Surface Classification

| ID | Element Name | Screen / Context | Role | Classification | Glass Material Variant | Fallback Behavior |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **E-01** | App Header / Topbar | All screens | Sticky/floating global header | **Chrome Layer** | `regular` (blur ~18px, fill ~0.45, border 1px) | Solid `#FFFFFF` or `#111827` border-b |
| **E-02** | Desktop Floating Sidebar | All screens (Desktop) | Primary navigation & mode switcher | **Chrome Layer** | `regular` (blur ~20px, fill ~0.40, shadow-md) | Solid `#FFFFFF` with soft shadow |
| **E-03** | Mobile Floating Bottom Bar | All screens (Mobile) | Primary navigation pill / drawer | **Chrome Layer** | `thick` (blur ~24px, fill ~0.55, pill shape) | Opaque tinted pill (`#FFFFFF` 0.95 alpha) |
| **E-04** | `HistoryModal` Overlay & Card | Global Dialog | Full-screen dim with floating sheet | **Chrome Layer** | Scrim: `thin` blur (8px); Modal Sheet: `thick` glass | Dimmed solid scrim (`rgba(0,0,0,0.6)`), solid white card |
| **E-05** | Submit Confirmation Dialog | Quiz Screen | Confirmation modal before scoring | **Chrome Layer** | `thick` glass sheet with specular edge | Opaque card with high contrast border |
| **E-06** | Quit Confirmation Dialog | Quiz Screen | Confirmation modal before abandoning | **Chrome Layer** | `thick` glass sheet with warning accent | Opaque card with danger border |
| **E-07** | Floating Timer Pill | Quiz Screen | Time countdown & pulse warning | **Chrome Layer** | `thin` floating pill with status glow | Solid tinted pill (`#F1F5F9`) |
| **E-08** | Question Navigator Bar | Quiz Screen | 20-pill question status track | **Chrome Layer** | `thin` glass container surface | Solid card container with inset border |
| **E-09** | Results Review Filter Bar | Results Screen | Segmented pills ("Todas", "Falladas", etc.) | **Chrome Layer** | `thin` segmented glass track | Solid grey pill track (`#E2E8F0`) |
| **E-10** | Practice Mode Selectors | Landing Screen | Selection of P1, P2, Mixto | **Content Layer** | **SOLID** (Venus white card, border-radius 24px) | Solid soft-UI card with hover lift |
| **E-11** | Question & Options Card | Quiz Screen | Question statement & multiple choice tiles | **Content Layer** | **SOLID** (Venus white card, zero transparency) | Solid soft-UI card, full opacity |
| **E-12** | Explanation & Distractor Box | Results Screen | Detailed reasons for correct and wrong options | **Content Layer** | **SOLID** (Venus tinted content card, high contrast) | Solid soft-UI card with crisp text |
| **E-13** | Score Summary & Stat Boxes | Results Screen | Score circle, duration, correct/wrong counts | **Content Layer** | **SOLID** (Venus stat widgets with bold indigo accent) | Solid soft-UI card, zero blur |
| **E-14** | Topic Weakness Table & Bars | History Modal | Table of topics with success rate bars | **Content Layer** | **SOLID** (Crisp table rows, solid SVG progress bars) | Solid high-contrast data rows |

---

## 3. Glass Surface Area Budget Calculation

### 3.1 Viewport Analysis Across Screen States

#### Desktop (1440 × 900 px = 1,296,000 px² Total Viewport Area)
1. **Landing View**:
   - Floating Inset Topbar: $1380 \times 64 = 88,320\text{ px}^2$ (~6.8%)
   - Floating Inset Sidebar: $260 \times 820 = 213,200\text{ px}^2$ (~16.4%)
   - Content area: Solid Venus white cards on ambient background (~76.8%)
   - **Total Glass Area**: $\approx 23.2\%$ (**< 25% budget PASSED**)
   - **Concurrent backdrop-filter layers**: 2 (Topbar, Sidebar) (**≤ 4 budget PASSED**)

2. **Quiz View**:
   - Floating Inset Topbar (with Timer pill): $88,320\text{ px}^2$ (~6.8%)
   - Floating 20-Question Pill Bar: $720 \times 54 = 38,880\text{ px}^2$ (~3.0%)
   - Question & Options: 100% Solid white card
   - **Total Glass Area**: $\approx 9.8\%$ (**< 25% budget PASSED**)
   - **Concurrent backdrop-filter layers**: 2 (**≤ 4 budget PASSED**)

3. **Results View**:
   - Floating Inset Topbar: $88,320\text{ px}^2$ (~6.8%)
   - Filter Segment Bar: $360 \times 44 = 15,840\text{ px}^2$ (~1.2%)
   - Results & Explanations: 100% Solid Venus cards
   - **Total Glass Area**: $\approx 8.0\%$ (**< 25% budget PASSED**)
   - **Concurrent backdrop-filter layers**: 2 (**≤ 4 budget PASSED**)

4. **Modal Active State (e.g., History or Submit Confirmation)**:
   - Fullscreen background Scrim: uses lightweight CSS opacity or single backdrop-filter (blur 6px) over ambient viewport.
   - Modal Sheet: $640 \times 560 = 358,400\text{ px}^2$ (~27.6% of viewport, but scrim dims background).
   - Under Rule 10, modal sheets replace active page interaction. To strictly respect the 25% guideline without nesting bugs, the modal scrim does NOT nest a blurred layer inside another active blurred container.

#### Mobile (375 × 812 px = 304,500 px² Total Viewport Area)
1. **Landing View**:
   - Floating Topbar: $343 \times 56 = 19,208\text{ px}^2$ (~6.3%)
   - Bottom Floating Pill Bar: $310 \times 60 = 18,600\text{ px}^2$ (~6.1%)
   - **Total Glass Area**: $\approx 12.4\%$ (**< 25% budget PASSED**)
   - **Concurrent backdrop-filter layers**: 2 (**≤ 4 budget PASSED**)

2. **Quiz View**:
   - Floating Top Header with Timer: $343 \times 56 = 19,208\text{ px}^2$ (~6.3%)
   - Floating Bottom Action Bar: $343 \times 60 = 20,580\text{ px}^2$ (~6.7%)
   - Question & Options: 100% Solid
   - **Total Glass Area**: $\approx 13.0\%$ (**< 25% budget PASSED**)
   - **Concurrent backdrop-filter layers**: 2 (**≤ 4 budget PASSED**)

---

## 4. Anti-Pattern Guardrails
1. **No Frosted-Card-Everywhere**: Questions, choices, and explanations must NEVER use glass. They remain solid high-contrast cards.
2. **No Nested Backdrop Filters**: A glass modal dialog shall never sit directly on top of another active glass surface without an intervening solid or dimmed scrim barrier.
3. **Hardware Acceleration Guard**: Blur radii are capped at **24px on desktop** and **12px on mobile** to eliminate GPU scrolling jank and maintain 60 fps.
