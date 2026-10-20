# SDD Data Model: 009-interaction-polish-and-motion

## Motion Token Schema

```typescript
export interface MotionTokens {
  /** Easing functions */
  easings: {
    spring: 'cubic-bezier(0.16, 1, 0.3, 1)';
    bounce: 'cubic-bezier(0.34, 1.56, 0.64, 1)';
    smooth: 'cubic-bezier(0.4, 0, 0.2, 1)';
    linear: 'linear';
  };

  /** Standard duration intervals in milliseconds */
  durations: {
    instant: '0ms';
    fast: '140ms';
    normal: '240ms';
    deliberate: '420ms';
    sweep: '1200ms';
  };

  /** Interaction transforms */
  transforms: {
    liftHover: 'translateY(-2px)';
    pressActive: 'scale(0.98)';
    badgePop: 'scale(1.08)';
  };
}
```

## CSS Custom Property Mapping
- `--motion-ease-spring`: `cubic-bezier(0.16, 1, 0.3, 1)`
- `--motion-ease-bounce`: `cubic-bezier(0.34, 1.56, 0.64, 1)`
- `--motion-ease-smooth`: `cubic-bezier(0.4, 0, 0.2, 1)`
- `--motion-duration-fast`: `140ms`
- `--motion-duration-normal`: `240ms`
- `--motion-duration-deliberate`: `420ms`
- `--motion-lift-y`: `-2px`
- `--motion-press-scale`: `0.98`
