# Specification: Unit 005 — Inset App Shell (Sidebar, Topbar & Mobile Nav)

## 1. Executive Summary
Unit U5 implements the chrome navigation shell for the Distributed Systems Exam Prep platform, embodying the **Apple Liquid Glass (iOS 26)** aesthetic. It provides a dual responsive architecture:
1. **Desktop / Tablet ($\ge 768\text{px}$)**:
   - A floating **Inset Glass Sidebar** (`width: 260px`, `margin: 20px 0 20px 20px`, `border-radius: 24px`, regular glass material with specular border and sheen).
   - A floating **Glass Topbar** (`height: 70px`, `margin: 20px 20px 20px 0`, regular glass material) featuring active route breadcrumb, exam status pill, search input trigger, theme toggle, and characterization metrics indicator.
2. **Mobile ($< 768\text{px}$)**:
   - A floating **Bottom Navigation Pill** (`height: 64px`, `margin: 0 16px 16px 16px`, regular glass with mobile blur capping) with 4 quick navigation destinations: Practice, Exam, Weak Spots, and Stats.
   - A compact floating header with brand title, active mode badge, and theme toggle.

---

## 2. Traceability & Requirements Mapping
| Requirement ID | Description | Component Mapping |
| :--- | :--- | :--- |
| **FR-001** | Content Layer & Chrome Layer separation | Floating chrome shells (`GlassSurface`) over ambient mesh |
| **FR-002** | Dual-theme token binding | Uses `--glass-*` and `--venus-*` tokens |
| **FR-004** | Responsive viewports (375px–1440px) | Media query transitions between sidebar and mobile bottom pill |
| **FR-006** | Zero functional regression | Preserves all exam states, modes, and actions |
| **NFR-003** | Glass surface limits (< 25% viewport area) | Desktop sidebar + topbar $\approx 18\%$ viewport area |
| **NFR-006** | WCAG 2.2 AA accessibility | All navigation links have text labels, ARIA landmarks, and focus rings |
| **NFR-008** | Keyboard accessibility | Tab order traverses Topbar -> Main Content -> Navigation cleanly |
| **NFR-009** | Performance | Hardware compositing (`translateZ(0)`), 0% idle CPU |

---

## 3. Optical & Layout Architecture

### 3.1 Inset Sidebar (Desktop $\ge 768\text{px}$)
- **Dimensions**: Fixed width `260px`, inset `20px` from top, bottom, and left viewport edges. `height: calc(100vh - 40px)`.
- **Material**: `<GlassSurface variant="regular" shape="rounded">` with specular edge highlight and diffuse shadow.
- **Sections**:
  1. **Brand Header**: Luminous logo icon with Electric Indigo gradient, title "DISTRIBUIDOS", subtitle "Lab 1 & Lab 2 Exam Prep".
  2. **Navigation Menu**:
     - Practice Hub (All 520 Questions)
     - Lab 1 Focus (260 Questions)
     - Lab 2 Focus (260 Questions)
     - Timed Exam Simulation (Real test conditions)
     - Weak Spot Review (Mistakes & flagged)
     - Performance Analytics
  3. **Sidebar Footer**: Lab coverage stats badge (520 Verified Qs), theme toggle shortcut, and version tag.

### 3.2 Inset Topbar (Desktop $\ge 768\text{px}$)
- **Dimensions**: Inset floating bar, `height: 64px`, flex layout with space-between alignment.
- **Left**: Current view breadcrumb (e.g. `Home / Lab 1 Simulation`) with bold title.
- **Right**: Search bar, current streak / question counter badge, theme toggle `<IconButton>`, and Github / info link.

### 3.3 Mobile Bottom Navigation Pill ($< 768\text{px}$)
- **Dimensions**: Fixed floating bottom bar `position: fixed; bottom: 16px; left: 16px; right: 16px; max-width: 500px; margin: 0 auto; z-index: 50;`.
- **Material**: `<GlassSurface variant="regular" shape="pill">` with mobile blur capping at `12px`.
- **Items**: 4 equally spaced navigation buttons with touch targets $\ge 48\times 48\text{px}$.
