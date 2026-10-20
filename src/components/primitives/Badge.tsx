// src/components/primitives/Badge.tsx
import React from 'react';
import '../../styles/primitives/badge.css';
import { BadgeProps } from '../../types/primitives';

export const Badge: React.FC<BadgeProps> = ({
  tone = 'neutral',
  size = 'md',
  dot = false,
  className = '',
  children,
  ...restProps
}) => {
  const classes = [
    'badge',
    `badge--${tone}`,
    `badge--${size}`,
    className,
  ]
    .filter(Boolean)
    .join(' ');

  return (
    <span className={classes} {...restProps}>
      {dot && <span className="badge__dot" aria-hidden="true" />}
      <span>{children}</span>
    </span>
  );
};
