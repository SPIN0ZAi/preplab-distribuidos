# SDD Data Model: 010-responsive-a11y-perf-hardening

## Breakpoint Model
```typescript
export interface BreakpointConfig {
  mobileSm: 375;
  mobile: 414;
  tablet: 768;
  desktopSm: 1024;
  desktop: 1280;
  wide: 1440;
  ultrawide: 1920;
}
```

## Accessibility Token Model
```typescript
export interface AccessibilityTokens {
  focusRingColor: string;
  focusRingWidth: string;
  focusRingOffset: string;
  minTouchTarget: string; // 44px
  mobileBlurCap: string; // 12px
}
```

## CSS Variable Mappings
- `--focus-ring-color`: `var(--venus-primary-indigo, #4318FF)`
- `--focus-ring-width`: `2px`
- `--focus-ring-offset`: `2px`
- `--touch-target-min`: `44px`
- `--glass-blur-mobile`: `12px`
