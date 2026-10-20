# Specification: Unit 007 — Custom SVG Charts (Zero-Dependency)

## 1. Executive Summary
Unit U7 implements lightweight, zero-dependency SVG data visualization components precisely reflecting the **Venus Dashboard Builder** reference aesthetics (`media_1792515753271.png`, `media_1792515760287.png`, and `media_1792515764444.png`):
1. **Rounded-Top Bar Chart (`RoundedBarChart`)**:
   - Distinctive Venus aesthetic: vertical bars with fully rounded tops (`rx="8"`), inactive bars in soft neutral (`#E2E8F0` / dark `#1E293B`), and one prominently highlighted active bar in Electric Indigo (`#4318FF`) with a subtle glow or hover tooltip.
2. **Smooth Area Sparkline (`AreaSparkline`)**:
   - Smooth cubic Bézier spline (`M... C...`) with Electric Indigo stroke and translucent vertical gradient fill (`stop-color="#4318FF"` at 20% opacity tapering to 0%).
3. **Circular Score Gauge (`CircularGauge`)**:
   - SVG dual-circle progress ring with rounded stroke caps (`stroke-linecap="round"`), smooth CSS `stroke-dashoffset` transition, and centered percentage label in bold Poppins typography.

---

## 2. Traceability & Requirements Mapping
| Chart Component | Requirements | User Stories | Non-Functional Requirements |
| :--- | :--- | :--- | :--- |
| `RoundedBarChart` | FR-001, FR-005 | US-001, US-004, US-010 | NFR-008, NFR-009 (< 5 KB overhead) |
| `AreaSparkline` | FR-001, FR-005 | US-001, US-004, US-007 | NFR-009, NFR-011 |
| `CircularGauge` | FR-001, FR-005 | US-001, US-007, US-008 | NFR-006, NFR-009 |

---

## 3. Optical Physics & Geometry

### 3.1 `RoundedBarChart`
- SVG `viewBox="0 0 320 180"`.
- Bars are dynamically spaced with fixed column widths (`width="22"`), `rx="10"`, `ry="10"`.
- Base line in subtle `var(--venus-card-border)`.
- Interactive tooltip overlay on hover with data values.

### 3.2 `AreaSparkline`
- SVG `viewBox="0 0 320 100"`.
- Calculates smooth control points for cubic Bézier curves:
  $$\mathbf{C}_1 = (x_{i-1} + \Delta x / 2, y_{i-1}), \quad \mathbf{C}_2 = (x_i - \Delta x / 2, y_i)$$
- LinearGradient `<defs>` with ID based on component instance.

### 3.3 `CircularGauge`
- SVG `viewBox="0 0 120 120"`.
- Radius $r = 50$, circumference $C = 2\pi r \approx 314.159$.
- Stroke width: 10px.
- Background ring: `stroke="var(--venus-bg-canvas)"`.
- Foreground ring: `stroke="var(--venus-primary-indigo)"` (or emerald/coral based on pass/fail).
- Offset calculation: `dashoffset = C * (1 - percentage / 100)`.
