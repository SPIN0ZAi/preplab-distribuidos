// specs/007-custom-svg-charts/contracts/charts.ts
import React from 'react';

export interface BarDataPoint {
  label: string;
  value: number;
  highlighted?: boolean;
}

export interface RoundedBarChartProps extends React.HTMLAttributes<HTMLDivElement> {
  data: BarDataPoint[];
  height?: number;
  highlightColor?: string;
  barColor?: string;
  'aria-label'?: string;
}

export interface AreaDataPoint {
  label: string;
  value: number;
}

export interface AreaSparklineProps extends React.HTMLAttributes<HTMLDivElement> {
  data: AreaDataPoint[];
  height?: number;
  strokeColor?: string;
  fillColor?: string;
  'aria-label'?: string;
}

export interface CircularGaugeProps extends React.HTMLAttributes<HTMLDivElement> {
  percentage: number;
  size?: number;
  strokeWidth?: number;
  tone?: 'indigo' | 'emerald' | 'coral' | 'dynamic';
  showLabel?: boolean;
  'aria-label'?: string;
}
