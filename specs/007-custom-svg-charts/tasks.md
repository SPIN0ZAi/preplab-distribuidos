# Atomic Tasks: Unit 007 — Custom SVG Charts

## Dependency Graph
```
T027 [Types & Contracts] ──> T028 [RoundedBarChart & CSS] ──> T029 [AreaSparkline & CircularGauge] ──> T030 [Build & Verification]
```

---

## Detailed Tasks Matrix

### T027: Author Chart Types & Contracts
- **File**: `src/types/charts.ts`
- **Requirement Link**: `FR-001`, `FR-005`, `NFR-011`
- **Estimated Effort**: 20 mins
- **Description**: Define TypeScript interfaces for `BarDataPoint`, `RoundedBarChartProps`, `AreaDataPoint`, `AreaSparklineProps`, and `CircularGaugeProps`.
- **Definition of Done**: Clean TypeScript compilation with zero type errors.

### T028: Build `RoundedBarChart.tsx` Component & `charts.css`
- **Files**: `src/styles/charts/charts.css`, `src/components/charts/RoundedBarChart.tsx`
- **Requirement Link**: `FR-001`, `FR-005`, `NFR-008`, `NFR-009`
- **Estimated Effort**: 60 mins
- **Description**: Implement zero-dependency SVG rounded-top bar chart matching the Venus dashboard kit with fully rounded pill tops, inactive neutral gray bars, and active Electric Indigo highlighted bar with hover effects.
- **Definition of Done**: Bar chart scales responsively via SVG `viewBox`; active bar stands out distinctly in Electric Indigo.

### T029: Build `AreaSparkline.tsx` and `CircularGauge.tsx`
- **Files**: `src/components/charts/AreaSparkline.tsx`, `src/components/charts/CircularGauge.tsx`
- **Requirement Link**: `FR-001`, `FR-005`, `NFR-006`, `NFR-009`
- **Estimated Effort**: 60 mins
- **Description**: Implement smooth cubic Bézier curve area spline with indigo-to-transparent vertical gradient fill, and circular score progress ring with animated stroke dashoffset.
- **Definition of Done**: Curves connect smoothly; gauge displays circular progress cleanly.

### T030: Index Export & Bundle Budget Verification
- **Files**: `src/components/charts/index.ts`, `src/styles/theme.css`
- **Requirement Link**: `NFR-001`, `NFR-009`
- **Estimated Effort**: 20 mins
- **Description**: Export all chart primitives via barrel file, import CSS into `theme.css`, run `npm run build`, and confirm bundle size impact < 5 KB.
- **Definition of Done**: Build passes with 0 errors; bundle size remains < 200 KB gzipped.
