// src/types/charts.ts
import React from 'react';

export interface BarDataPoint {
  label: string;
  value: number; // 0 to 100
  secondaryValue?: number;
  highlighted?: boolean;
}

export interface RoundedBarChartProps extends React.HTMLAttributes<HTMLDivElement> {
  data: BarDataPoint[];
  height?: number;
  highlightColor?: string;
  barColor?: string;
  className?: string;
  'aria-label'?: string;
}

export interface AreaDataPoint {
  label: string;
  value: number; // 0 to 100
}

export interface AreaSparklineProps extends React.HTMLAttributes<HTMLDivElement> {
  data: AreaDataPoint[];
  height?: number;
  strokeColor?: string;
  fillColor?: string;
  gradientId?: string;
  className?: string;
  'aria-label'?: string;
}

export interface CircularGaugeProps extends React.HTMLAttributes<HTMLDivElement> {
  percentage: number; // 0 to 100
  size?: number;
  strokeWidth?: number;
  tone?: 'indigo' | 'emerald' | 'coral' | 'dynamic';
  showLabel?: boolean;
  className?: string;
  'aria-label'?: string;
}
