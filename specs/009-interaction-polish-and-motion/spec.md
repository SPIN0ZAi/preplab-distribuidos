# SDD Specification: 009-interaction-polish-and-motion

## 1. Executive Summary & Objective
Unit U9 standardizes all micro-interactions, transition timings, spring physics, and celebratory animations across the Two-Layer Visual System (Venus Soft-UI cards + Apple Liquid Glass chrome). It establishes Apple's fluid spring deceleration curves (`cubic-bezier(0.16, 1, 0.3, 1)`), tactile click response, smooth card elevation lifts, and high-performance SVG animation reveals, accompanied by comprehensive `prefers-reduced-motion` compliance.

## 2. Requirements & Scope
- **REQ-009-01 (Fluid Spring Deceleration)**: Standardize all UI element transitions to use Apple iOS 26 fluid spring curve `cubic-bezier(0.16, 1, 0.3, 1)` for surface movement and `cubic-bezier(0.34, 1.56, 0.64, 1)` for subtle tactile rebounds.
- **REQ-009-02 (Card Elevation & Micro-Lifts)**: Venus cards lift subtly (`translateY(-2px)`) with expanded elevation shadow on hover, returning cleanly on blur/rest without layout shifts (subpixel antialiasing with `backface-visibility: hidden`).
- **REQ-009-03 (Tactile Press Feedback)**: Buttons, segmented control tabs, and quiz option choices provide active press scale compression (`scale(0.98)`) and specular highlight reflection adjustments.
- **REQ-009-04 (Celebratory Exam Animation)**: The Results screen hero gauge and score card incorporate an energetic victory pulse and shimmer when a passing grade ($\ge 70\%$) is achieved.
- **REQ-009-05 (Zero Layout Thrashing)**: All animations must operate exclusively on compositor-friendly CSS properties (`transform`, `opacity`, `filter`). No width/height/margin/padding animations.
- **REQ-009-06 (Strict Reduced Motion Mode)**: When `@media (prefers-reduced-motion: reduce)` is enabled, all transition and animation durations collapse to `0.001ms`, disabling all spatial transforms while maintaining functional state changes.

## 3. Interaction Mechanics & Specifications
### 3.1 Spring Curves & Duration Scale
| Token | Timing Function | Value | Typical Usage |
| :--- | :--- | :--- | :--- |
| `--motion-ease-spring` | `cubic-bezier(0.16, 1, 0.3, 1)` | iOS 26 Fluid Spring | Modals, drawers, card lifts, tabs |
| `--motion-ease-bounce` | `cubic-bezier(0.34, 1.56, 0.64, 1)` | Subtle Rebound | Badge pop, pill selection, checkmarks |
| `--motion-ease-smooth` | `cubic-bezier(0.4, 0, 0.2, 1)` | Standard EaseInOut | Color, opacity, background crossfades |
| `--motion-duration-fast` | 140ms | Snappy feedback | Active clicks, tooltip reveals, icon hover |
| `--motion-duration-normal`| 240ms | Natural movement | Card hover lifts, tab slides, drawer open |
| `--motion-duration-deliberate` | 420ms | Dramatic reveal | Modal entry, results score gauge sweep |

### 3.2 Celebratory Reveal Physics
When exam score $\ge 70\%$:
- Circular gauge sweeps smoothly via SVG `stroke-dashoffset` animation over 1.2s using `--motion-ease-spring`.
- Hero score badge receives a continuous subtle ambient glow pulse (opacity 0.6 to 1.0, 3s cycle).
- Passing badge exhibits a one-time celebratory pop scale animation (`0.8` -> `1.08` -> `1.0`).

### 3.3 Strict Reduced Motion Matrix
```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}
```

## 4. Verification & Acceptance Criteria
1. Production bundle impact $< 2\text{ KB}$ gzipped.
2. 60 FPS scrolling and interaction verified across desktop and mobile viewports.
3. Zero layout shifts (CLS = 0) during hover and active state transitions.
4. Immediate, instantaneous UI updates when OS reduced motion is active.
