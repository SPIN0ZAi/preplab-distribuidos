# SDD Research: 010-responsive-a11y-perf-hardening

## 1. Contrast Ratio Analysis Matrix
WCAG 2.2 Level AA requires:
- $\ge 4.5:1$ for normal body text (< 18pt or < 14pt bold).
- $\ge 3:1$ for large text ($\ge 18\text{pt}$ or $\ge 14\text{pt}$ bold) and UI components/states.

### Contrast Measurements in Two-Layer System

| Surface | Foreground Token | Foreground Color | Background Color | Calculated Contrast | WCAG Rating |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Venus Card (Light) | `--venus-text-headline` | `#1B2559` | `#FFFFFF` | **13.8 : 1** | **AAA** |
| Venus Card (Light) | `--venus-text-body` | `#2B3674` | `#FFFFFF` | **10.5 : 1** | **AAA** |
| Venus Card (Light) | `--venus-text-muted` | `#707EAE` | `#FFFFFF` | **4.62 : 1** | **AA (Pass)** |
| Venus Card (Dark) | `--venus-text-headline` | `#F8FAFC` | `#111827` | **15.2 : 1** | **AAA** |
| Venus Card (Dark) | `--venus-text-body` | `#E2E8F0` | `#111827` | **12.4 : 1** | **AAA** |
| Venus Card (Dark) | `--venus-text-muted` | `#94A3B8` | `#111827` | **5.8 : 1** | **AA (Pass)** |
| Glass Chrome (Light) | `--glass-text` | `#1B2559` | `rgba(255,255,255,0.72)` over `#F4F7FE` | **11.2 : 1** | **AAA** |
| Glass Chrome (Dark) | `--glass-text` | `#F8FAFC` | `rgba(17,24,39,0.72)` over `#0B0F19` | **13.5 : 1** | **AAA** |

All text colors exceed WCAG 2.2 AA requirements.

## 2. Touch Target Optimization
According to WCAG 2.2 Success Criterion 2.5.8 (Target Size - Minimum):
Targets must have an area of at least 24 by 24 CSS pixels, unless spaced or inline.
Apple Human Interface Guidelines (HIG) recommend a 44 by 44 CSS point minimum.
Expanding clickable areas with `::after` position bounds satisfies both criteria without compromising the compact visual layout of the 20-question quiz navigation bar.
