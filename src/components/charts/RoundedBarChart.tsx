// src/components/charts/RoundedBarChart.tsx
import React, { useState } from 'react';
import '../../styles/charts/charts.css';
import { RoundedBarChartProps } from '../../types/charts';

export const RoundedBarChart: React.FC<RoundedBarChartProps> = ({
  data,
  height = 180,
  highlightColor = 'var(--venus-primary-indigo)',
  barColor = 'var(--venus-chart-bar-inactive, #E2E8F0)',
  className = '',
  'aria-label': ariaLabel = 'Gráfico de barras de actividad',
  ...restProps
}) => {
  const [hoveredIndex, setHoveredIndex] = useState<number | null>(null);

  const svgWidth = 500;
  const svgHeight = 160;
  const baselineY = 125;
  const maxBarHeight = 85;
  const barWidth = 28;

  const count = data.length || 1;
  const step = (svgWidth - 40) / count;

  return (
    <div
      className={`venus-chart-container ${className}`}
      style={{ height }}
      role="img"
      aria-label={ariaLabel}
      {...restProps}
    >
      <svg
        viewBox={`0 0 ${svgWidth} ${svgHeight}`}
        className="venus-chart-svg"
        preserveAspectRatio="xMidYMid meet"
      >
        {/* Baseline */}
        <line
          x1={20}
          y1={baselineY}
          x2={svgWidth - 20}
          y2={baselineY}
          stroke="var(--venus-card-border)"
          strokeWidth={1}
          strokeDasharray="4 4"
        />

        {data.map((item, index) => {
          const x = 20 + index * step + (step - barWidth) / 2;
          const rawHeight = (Math.max(0, Math.min(100, item.value)) / 100) * maxBarHeight;
          const barHeight = Math.max(10, rawHeight);
          const y = baselineY - barHeight;

          const isHighlighted = item.highlighted || hoveredIndex === index;
          const fill = isHighlighted ? highlightColor : barColor;

          return (
            <g key={item.label || index}>
              {/* Rounded Bar */}
              <rect
                x={x}
                y={y}
                width={barWidth}
                height={barHeight}
                rx={10}
                ry={10}
                fill={fill}
                className={`chart-bar ${isHighlighted ? 'chart-bar--highlighted' : ''}`}
                onMouseEnter={() => setHoveredIndex(index)}
                onMouseLeave={() => setHoveredIndex(null)}
              >
                <title>{`${item.label}: ${item.value}%`}</title>
              </rect>

              {/* X Axis Label */}
              <text
                x={x + barWidth / 2}
                y={baselineY + 18}
                className={`chart-axis-label ${isHighlighted ? 'chart-axis-label--active' : ''}`}
              >
                {item.label}
              </text>
            </g>
          );
        })}
      </svg>
    </div>
  );
};
