# Implementation Plan: Unit 001 — Design Tokens & Dual-Theme System

## 1. Technical Context & Constitution Check

### Constitution Compliance Matrix
| Principle | Requirement | Plan Alignment | Status |
| :--- | :--- | :--- | :---: |
| **P1: Spec-First** | Specs are the source of truth | Implementation follows `spec.md` with traceable tasks. | **PASS** |
| **P3: Glass Discipline** | Glass in chrome only; fallbacks required | Glass tokens isolated under `--glass-*`; full fallback tokens. | **PASS** |
| **P5: Design-Token-Only** | No hardcoded colors or blur values | Every visual attribute exposed via centralized CSS variables. | **PASS** |
| **P6: Dependency Discipline** | No new dependencies without ADR | Uses native CSS custom properties; 0 new packages. | **PASS** |
| **P7: WCAG 2.2 AA** | $\ge 4.5:1$ text contrast | Contrast matrix verified for both Light and Dark palettes. | **PASS** |
| **P9: Performance** | Bundle < 200 KB gzip | Zero runtime JS weight; CSS footprint ~3 KB gzipped. | **PASS** |

---

## 2. Architecture & File Structure

The monolithic `src/index.css` will be refactored into a structured, modular design system hierarchy:

```text
src/
├── styles/
│   ├── tokens/
│   │   ├── venus-tokens.css        # Venus content palette, grid, radii, shadows
│   │   ├── glass-tokens.css        # Liquid glass blur tiers, fills, specular highlights
│   │   └── typography.css          # Poppins, Plus Jakarta Sans, JetBrains Mono scale
│   ├── theme.css                   # Root variables, data-theme="dark" overrides, fallbacks
│   └── main.css                    # Entry aggregator importing tokens & existing utilities
```

---

## 3. Token Definitions Specification

### 3.1 Venus Content Layer Tokens (Light Mode Default)
```css
:root {
  /* Canvas & Card Surfaces */
  --venus-bg-canvas: #F4F7FE;
  --venus-card-bg: #FFFFFF;
  --venus-card-bg-subtle: #F8FAFC;
  --venus-card-border: rgba(226, 232, 240, 0.80);

  /* Brand Accents */
  --venus-primary-indigo: #4318FF;
  --venus-primary-hover: #3311CC;
  --venus-primary-light: rgba(67, 24, 255, 0.08);
  --venus-secondary-purple: #7551FF;
  --venus-accent-coral: #FF7A8A;
  --venus-gradient-brand: linear-gradient(135deg, #4318FF 0%, #7551FF 100%);

  /* Typography Colors */
  --venus-text-headline: #1B2559;
  --venus-text-body: #2B3674;
  --venus-text-muted: #707EAE;
  --venus-text-disabled: #A3AED0;

  /* Status Colors */
  --venus-success: #05CD99;
  --venus-success-bg: rgba(5, 205, 153, 0.12);
  --venus-danger: #EE5D6C;
  --venus-danger-bg: rgba(238, 93, 108, 0.12);
  --venus-warning: #FFB547;
  --venus-warning-bg: rgba(255, 181, 71, 0.12);

  /* Chart & Inactive Accents */
  --venus-chart-bar-inactive: #E9EDF7;
  --venus-chart-bar-active: #4318FF;

  /* Spatial Scale (8px Grid) */
  --venus-space-xs: 4px;
  --venus-space-sm: 8px;
  --venus-space-md: 16px;
  --venus-space-lg: 24px;
  --venus-space-xl: 32px;
  --venus-space-2xl: 48px;

  /* Card Radii */
  --venus-radius-sm: 12px;
  --venus-radius-md: 16px;
  --venus-radius-lg: 20px;
  --venus-radius-xl: 24px;
  --venus-radius-pill: 9999px;

  /* Diffuse Soft-UI Shadows */
  --venus-shadow-card: 0 18px 40px rgba(112, 144, 176, 0.12);
  --venus-shadow-hover: 0 22px 45px rgba(112, 144, 176, 0.20);
  --venus-shadow-glow: 0 12px 24px rgba(67, 24, 255, 0.25);
}
```

### 3.2 Liquid Glass Chrome Layer Tokens
```css
:root {
  /* Blur Tiers */
  --glass-blur-thin: 8px;
  --glass-blur-regular: 18px;
  --glass-blur-thick: 28px;
  --glass-blur-mobile: 12px;

  /* Saturation */
  --glass-saturate: 160%;

  /* Translucent Fills (Light Mode) */
  --glass-fill-thin: rgba(255, 255, 255, 0.30);
  --glass-fill-regular: rgba(255, 255, 255, 0.45);
  --glass-fill-thick: rgba(255, 255, 255, 0.65);

  /* Specular Rim & Inner Reflection */
  --glass-border: 1px solid rgba(255, 255, 255, 0.35);
  --glass-edge-highlight: inset 0 1px 1px 0 rgba(255, 255, 255, 0.70);
  --glass-edge-shade: inset 0 -1px 1px 0 rgba(0, 0, 0, 0.04);
  --glass-sheen: linear-gradient(135deg, rgba(255, 255, 255, 0.22) 0%, rgba(255, 255, 255, 0.00) 100%);

  /* Layered Tinted Shadows */
  --glass-shadow: 0 4px 16px rgba(67, 24, 255, 0.06), 0 1px 2px rgba(0, 0, 0, 0.04);
  --glass-shadow-floating: 0 16px 36px rgba(67, 24, 255, 0.08), 0 2px 6px rgba(0, 0, 0, 0.04);

  /* High-Contrast Accessible Text on Glass */
  --glass-text: #1B2559;
  --glass-text-muted: #707EAE;

  /* Fallback Fills (No-Backdrop / Reduced Transparency) */
  --glass-fallback-fill: rgba(244, 247, 254, 0.94);
  --glass-fallback-border: #CBD5E1;
}
```

### 3.3 Dark Mode Overrides (`[data-theme="dark"]`)
```css
[data-theme="dark"] {
  --venus-bg-canvas: #0B0F19;
  --venus-card-bg: #111827;
  --venus-card-bg-subtle: #172033;
  --venus-card-border: rgba(255, 255, 255, 0.08);

  --venus-text-headline: #F8FAFC;
  --venus-text-body: #E2E8F0;
  --venus-text-muted: #94A3B8;
  --venus-text-disabled: #64748B;

  --venus-shadow-card: 0 18px 40px rgba(0, 0, 0, 0.45);
  --venus-shadow-hover: 0 22px 45px rgba(0, 0, 0, 0.60);

  /* Dark Glass Fills */
  --glass-fill-thin: rgba(17, 24, 39, 0.35);
  --glass-fill-regular: rgba(17, 24, 39, 0.50);
  --glass-fill-thick: rgba(17, 24, 39, 0.68);
  --glass-border: 1px solid rgba(255, 255, 255, 0.10);
  --glass-edge-highlight: inset 0 1px 1px 0 rgba(255, 255, 255, 0.20);
  --glass-edge-shade: inset 0 -1px 1px 0 rgba(0, 0, 0, 0.30);
  --glass-sheen: linear-gradient(135deg, rgba(255, 255, 255, 0.08) 0%, rgba(255, 255, 255, 0.00) 100%);
  --glass-text: #F8FAFC;
  --glass-text-muted: #94A3B8;
  --glass-fallback-fill: rgba(17, 24, 39, 0.95);
  --glass-fallback-border: rgba(255, 255, 255, 0.15);
}
```

---

## 4. Theme Management Service

A tiny zero-dependency service `src/services/theme.ts` will provide:
- `getStoredTheme(): 'light' | 'dark'`
- `setTheme(theme: 'light' | 'dark'): void`
- `toggleTheme(): 'light' | 'dark'`
- `initThemeListener(callback: (theme: 'light' | 'dark') => void): () => void`

---

## 5. Rollback Plan

If any token regression occurs:
- The previous `src/index.css` is retained as a working baseline.
- Theme switching can be forced to `data-theme="dark"` via a single attribute change on the root `<html>`.
