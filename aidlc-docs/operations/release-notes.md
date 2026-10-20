# PrepLab v2.0.0 Release Notes

**Release Date**: 2026-10-20  
**Methodology**: AI-DLC (AI Development Life Cycle) + SDD (Spec-Driven Development)  
**Lead Architecture**: Antigravity Autonomous Engineering Suite  

---

## 🌟 Highlights & Major Changes

### 1. Two-Layer Visual System
- **Content Layer (Venus Dashboard Builder)**: Clean, airy soft-UI cards with diffuse shadows, bold indigo accents (`#4318FF`), and high-contrast typography (> 7:1 contrast) ensuring optimal reading ergonomics for all 520 exam questions.
- **Chrome Layer (Apple Liquid Glass - iOS 26)**: Ultra-translucent floating surfaces implementing a 6-layer optical formula (dual-pass blur + saturation, 1px specular rim, inset top edge highlight, inset bottom shade, diagonal directional sheen, and ambient tinted shadows).
- **Rule 10 (Glass Discipline)**: Glass strictly confined to navigation, toolbars, and modals (< 25% viewport area). Content remains on solid, high-contrast cards.

### 2. Dual-Theme Engine (Venus Light & Dark)
- Light theme is now the primary default matching the Venus Figma Kit reference.
- Full dark mode support (`data-theme="dark"`) with customized dark acrylic glass fills and high-contrast slate text.
- System preference auto-detection with smooth 200ms background crossfades.

### 3. Zero-Dependency SVG Data Visualizations
- Custom-engineered inline SVG charts matching the Venus Dashboard Builder reference:
  - `RoundedBarChart`: Vertical bars with `rx="10"` and highlighted Electric Indigo bar.
  - `AreaSparkline`: Organic cubic Bézier spline curve with gradient fill.
  - `CircularGauge`: Circular score hero gauge with animated stroke dashoffset.
- Eliminates 100+ KB of heavy charting libraries from the client bundle.

### 4. Interactive Polish & Spring Physics
- Apple iOS 26 fluid spring curve `cubic-bezier(0.16, 1, 0.3, 1)` applied to modals, tab indicator sliding, and card elevation lifts.
- Active click tactile compression (`scale(0.98)`).
- Celebratory victory sheen and ambient pulse for passing scores ($\ge 70\%$).
- Comprehensive `@media (prefers-reduced-motion: reduce)` zero-duration killswitch.

### 5. Performance & Accessibility Hardening
- Production initial JavaScript bundle size: **61.00 KB gzipped** (strict budget: < 200 KB).
- Production CSS bundle: **11.50 KB gzipped**.
- Mobile thermal blur throttling (capped to 12px blur on $\le 768\text{px}$).
- Minimum 44px touch targets on mobile viewports.
- Full Windows High Contrast (`@media (forced-colors: active)`) support.
- 520 questions verified with 100% integrity (260 Lab 1, 260 Lab 2).

---

## 📦 Deliverables & Artifacts
- [DESIGN_SYSTEM.md](file:///c:/Users/ssola/Desktop/documentos%20de%20estudios/3%20year/distribuidos/LAB/lab%201%20and%202%20test%20preparation/DESIGN_SYSTEM.md)
- [GLASS_MATERIAL_GUIDE.md](file:///c:/Users/ssola/Desktop/documentos%20de%20estudios/3%20year/distribuidos/LAB/lab%201%20and%202%20test%20preparation/GLASS_MATERIAL_GUIDE.md)
- [ARCHITECTURE.md](file:///c:/Users/ssola/Desktop/documentos%20de%20estudios/3%20year/distribuidos/LAB/lab%201%20and%202%20test%20preparation/ARCHITECTURE.md)
- [README.md](file:///c:/Users/ssola/Desktop/documentos%20de%20estudios/3%20year/distribuidos/LAB/lab%201%20and%202%20test%20preparation/README.md)
