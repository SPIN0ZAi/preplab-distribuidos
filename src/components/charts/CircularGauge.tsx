// src/components/charts/CircularGauge.tsx
import React from 'react';
import '../../styles/charts/charts.css';
import { CircularGaugeProps } from '../../types/charts';

export const CircularGauge: React.FC<CircularGaugeProps> = ({
  percentage,
  size = 120,
  strokeWidth = 10,
  tone = 'dynamic',
  showLabel = true,
  className = '',
  'aria-label': ariaLabel,
  ...restProps
}) => {
  const radius = 45;
  const circumference = 2 * Math.PI * radius; // ~282.74
  const clampedPercentage = Math.max(0, Math.min(100, percentage));
  const offset = circumference - (clampedPercentage / 100) * circumference;

  let strokeColor = 'var(--venus-primary-indigo)';
  if (tone === 'emerald') {
    strokeColor = 'var(--venus-accent-emerald)';
  } else if (tone === 'coral') {
    strokeColor = 'var(--venus-accent-coral)';
  } else if (tone === 'dynamic') {
    strokeColor = clampedPercentage >= 50 ? 'var(--venus-accent-emerald)' : 'var(--venus-accent-coral)';
  }

  const accessibleLabel = ariaLabel || `Puntuación: ${Math.round(clampedPercentage)}%`;

  return (
    <div
      className={`circular-gauge-container ${className}`}
      style={{ width: size, height: size }}
      role="meter"
      aria-valuenow={Math.round(clampedPercentage)}
      aria-valuemin={0}
      aria-valuemax={100}
      aria-label={accessibleLabel}
      {...restProps}
    >
      <svg
        viewBox="0 0 110 110"
        style={{ width: size, height: size, transform: 'rotate(-90deg)' }}
      >
        {/* Background Track */}
        <circle
          cx="55"
          cy="55"
          r={radius}
          strokeWidth={strokeWidth}
          className="circular-gauge__bg"
        />

        {/* Foreground Animated Progress */}
        <circle
          cx="55"
          cy="55"
          r={radius}
          strokeWidth={strokeWidth}
          strokeDasharray={circumference}
          strokeDashoffset={offset}
          stroke={strokeColor}
          className="circular-gauge__fg"
        />
      </svg>

      {/* Centered Typography */}
      {showLabel && (
        <div className="circular-gauge__label">
          <span className="circular-gauge__value" style={{ fontSize: size * 0.24 }}>
            {Math.round(clampedPercentage)}%
          </span>
          <span className="circular-gauge__subtext">Acierto</span>
        </div>
      )}
    </div>
  );
};
