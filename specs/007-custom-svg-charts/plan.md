# Construction Plan: Unit 007 — Custom SVG Charts

## 1. Architectural Strategy
Implement atomic, zero-overhead SVG chart components in `src/components/charts/`:
```
src/
├── components/
│   └── charts/
│       ├── RoundedBarChart.tsx
│       ├── AreaSparkline.tsx
│       ├── CircularGauge.tsx
│       └── index.ts
├── styles/
│   └── charts/
│       └── charts.css
└── types/
    └── charts.ts
```

## 2. Execution Phases
1. **Types & Contracts (`T027`)**: Define data structures (`ChartDataPoint`, `BarChartProps`, `AreaChartProps`, `GaugeProps`) in `src/types/charts.ts`.
2. **RoundedBarChart Component & Styles (`T028`)**: Implement SVG rounded bar chart with 1 highlighted bar in `src/components/charts/RoundedBarChart.tsx` and `src/styles/charts/charts.css`.
3. **AreaSparkline & CircularGauge (`T029`)**: Implement smooth Bézier curve area chart and circular score gauge.
4. **Build & Bundle Verification (`T030`)**: Export barrel file, import CSS, run `npm run build`, and confirm bundle size impact < 5 KB.
