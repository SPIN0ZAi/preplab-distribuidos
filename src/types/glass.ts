// src/types/glass.ts
import React from 'react';

export type GlassVariant = 'thin' | 'regular' | 'thick';
export type GlassTone = 'default' | 'accent' | 'clear';
export type GlassShape = 'rounded' | 'pill' | 'circle' | 'flat';

export interface GlassSurfaceProps extends React.HTMLAttributes<HTMLElement> {
  variant?: GlassVariant;
  tone?: GlassTone;
  shape?: GlassShape;
  interactive?: boolean;
  as?: React.ElementType;
  className?: string;
  children?: React.ReactNode;
}
