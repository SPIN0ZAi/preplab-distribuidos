# Data Model: Unit 003 — Liquid Glass Material System

## 1. Component Interface Contract

```typescript
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
```

See complete TypeScript interface definitions in [`contracts/glass.ts`](file:///c:/Users/ssola/Desktop/documentos%20de%20estudios/3%20year/distribuidos/LAB/lab%201%20and%202%20test%20preparation/specs/003-liquid-glass-material-system/contracts/glass.ts).
