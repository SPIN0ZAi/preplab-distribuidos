// src/components/GlassSurface.tsx
import React from 'react';
import '../styles/glass-surface.css';
import { GlassSurfaceProps } from '../types/glass';

export const GlassSurface: React.FC<GlassSurfaceProps> = ({
  variant = 'regular',
  tone = 'default',
  shape = 'rounded',
  interactive = false,
  as: Component = 'div',
  className = '',
  children,
  ...restProps
}) => {
  const classes = [
    'glass-surface',
    `glass-surface--${variant}`,
    tone !== 'default' ? `glass-surface--${tone}` : '',
    `glass-surface--${shape}`,
    interactive ? 'glass-surface--interactive' : '',
    className,
  ]
    .filter(Boolean)
    .join(' ');

  return (
    <Component className={classes} {...restProps}>
      {children}
    </Component>
  );
};
