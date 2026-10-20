# Data Model: Unit 007 — Custom SVG Charts

## Chart Data Entities
```typescript
export interface BarDataPoint {
  label: string;
  value: number; // 0 to 100
  secondaryValue?: number;
  highlighted?: boolean;
}

export interface RoundedBarChartProps {
  data: BarDataPoint[];
  height?: number;
  barColor?: string;
  highlightColor?: string;
  className?: string;
  'aria-label'?: string;
}

export interface AreaDataPoint {
  label: string;
  value: number; // e.g. score percentage 0 to 100
}

export interface AreaSparklineProps {
  data: AreaDataPoint[];
  height?: number;
  strokeColor?: string;
  gradientId?: string;
  className?: string;
  'aria-label'?: string;
}

export interface CircularGaugeProps {
  percentage: number; // 0 to 100
  size?: number;
  strokeWidth?: number;
  tone?: 'indigo' | 'emerald' | 'coral' | 'dynamic';
  showLabel?: boolean;
  className?: string;
  'aria-label'?: string;
}
```
