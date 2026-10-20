# SDD Clarifications: 010-responsive-a11y-perf-hardening

## Resolved Design Decisions

### Q1: How do we handle Windows High Contrast Mode with Apple Liquid Glass?
- **Decision**: In `@media (forced-colors: active)`, all CSS `backdrop-filter` and transparent RGBA fills are overridden. Surfaces adopt system keyword colors (`Canvas`, `CanvasText`, `Highlight`, `ButtonText`, `ButtonBorder`). Specular rim box-shadows are converted to solid 1.5px borders.
- **Rationale**: Windows High Contrast Mode users require sharp, opaque borders and high foreground separation. Liquid Glass transparency would impair legibility.

### Q2: What is the maximum acceptable blur radius on mobile?
- **Decision**: 12px blur radius on screens $\le 768\text{px}$ (via `--glass-blur-mobile: 12px`).
- **Rationale**: Large radius 24px–32px blurs require multiple convolution passes per frame on mobile GPUs (Mali, Adreno, Apple A-series), causing thermal degradation and battery drain. Capping at 12px preserves the frosted aesthetic with 60% lower convolution cost.

### Q3: What is the minimum touch target for quiz question navigator pills?
- **Decision**: The visual pill is 32px diameter, but the clickable tap target is expanded to 44px using an invisible `::after` pseudo-element with `position: absolute; inset: -6px;`.
- **Rationale**: WCAG 2.2 Success Criterion 2.5.8 (Target Size - Minimum) requires a minimum 24px target, while Apple HIG and Google Material recommend 44–48px. Expanding via pseudo-element keeps visual spacing dense while satisfying the 44px tap target.
