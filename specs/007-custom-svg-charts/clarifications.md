# Clarifications: Unit 007 — Custom SVG Charts

## Clarification Log

### C001: Why build custom SVG charts instead of installing Recharts or Chart.js?
- **Decision**: Recharts or Chart.js would add 80–150 KB gzipped to the production bundle, violating our hard constraint ($< 200\text{ KB}$ gzipped total JS bundle) and introducing hydration overhead. Building pure React SVG charts gives us complete visual control over the Venus rounded bar tops and gradient fills with less than 3 KB total bundle impact.

### C002: How do the charts adapt to responsive container resizing?
- **Decision**: All charts use native SVG `viewBox` coordinates with `width="100%"` and `preserveAspectRatio="xMidYMid meet"`, scaling naturally to any container width without JavaScript resize listeners.

### C003: Are the SVG charts accessible to screen readers?
- **Decision**: Yes. Each SVG includes `role="img"` with an `aria-label` or `<title>` summarizing the visualized data (e.g., "Gráfico de barras de acierto en los últimos 7 días: promedio 82%").
