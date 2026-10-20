// src/components/charts/AreaSparkline.tsx
import React, { useId } from 'react';
import '../../styles/charts/charts.css';
import { AreaSparklineProps } from '../../types/charts';

export const AreaSparkline: React.FC<AreaSparklineProps> = ({
  data,
  height = 100,
  strokeColor = 'var(--venus-primary-indigo)',
  fillColor,
  gradientId: customGradientId,
  className = '',
  'aria-label': ariaLabel = 'Gráfico de evolución y tendencia',
  ...restProps
}) => {
  const generatedId = useId().replace(/:/g, '');
  const gradientId = customGradientId || `sparkline-grad-${generatedId}`;

  const svgWidth = 320;
  const svgHeight = 100;
  const paddingX = 14;
  const paddingY = 14;

  const innerWidth = svgWidth - paddingX * 2;
  const innerHeight = svgHeight - paddingY * 2;

  if (!data || data.length === 0) {
    return null;
  }

  // Calculate points coordinates
  const points = data.map((item, index) => {
    const x = paddingX + (index / Math.max(1, data.length - 1)) * innerWidth;
    const clampedValue = Math.max(0, Math.min(100, item.value));
    const y = svgHeight - paddingY - (clampedValue / 100) * innerHeight;
    return { x, y, label: item.label, value: item.value };
  });

  // Build cubic Bézier path
  let pathD = `M ${points[0].x} ${points[0].y}`;
  for (let i = 1; i < points.length; i++) {
    const prev = points[i - 1];
    const curr = points[i];
    const dx = curr.x - prev.x;
    const cp1x = prev.x + dx * 0.45;
    const cp1y = prev.y;
    const cp2x = curr.x - dx * 0.45;
    const cp2y = curr.y;
    pathD += ` C ${cp1x} ${cp1y}, ${cp2x} ${cp2y}, ${curr.x} ${curr.y}`;
  }

  // Build closed area path
  const lastPoint = points[points.length - 1];
  const firstPoint = points[0];
  const areaD = `${pathD} L ${lastPoint.x} ${svgHeight - paddingY} L ${firstPoint.x} ${svgHeight - paddingY} Z`;

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
        preserveAspectRatio="none"
      >
        <defs>
          <linearGradient id={gradientId} x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stopColor={fillColor || strokeColor} stopOpacity="0.28" />
            <stop offset="100%" stopColor={fillColor || strokeColor} stopOpacity="0.00" />
          </linearGradient>
        </defs>

        {/* Shaded Area Fill */}
        <path d={areaD} fill={`url(#${gradientId})`} className="sparkline-area" />

        {/* Outline Spline */}
        <path d={pathD} stroke={strokeColor} className="sparkline-line" />

        {/* Data Points */}
        {points.map((p, idx) => (
          <circle
            key={idx}
            cx={p.x}
            cy={p.y}
            r={3.5}
            className="sparkline-point"
            stroke={strokeColor}
          >
            <title>{`${p.label}: ${p.value}%`}</title>
          </circle>
        ))}
      </svg>
    </div>
  );
};
