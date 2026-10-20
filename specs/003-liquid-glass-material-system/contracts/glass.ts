// specs/003-liquid-glass-material-system/contracts/glass.ts
import React from 'react';

export type GlassVariant = 'thin' | 'regular' | 'thick';
export type GlassTone = 'default' | 'accent' | 'clear';
export type GlassShape = 'rounded' | 'pill' | 'circle' | 'flat';

export interface GlassSurfaceProps extends React.HTMLAttributes<HTMLDivElement> {
  variant?: GlassVariant;
  tone?: GlassTone;
  shape?: GlassShape;
  as?: React.ElementType;
  className?: string;
  children?: React.ReactNode;
}
