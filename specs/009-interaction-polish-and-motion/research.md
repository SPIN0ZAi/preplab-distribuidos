# SDD Research: 009-interaction-polish-and-motion

## 1. Physics of Apple Liquid Glass Springs
Apple's iOS motion language relies heavily on damped harmonic oscillators. In standard CSS approximations, standard Bézier curves can mimic these dynamics without requiring JavaScript `requestAnimationFrame` loops.
The standard spring curve:
```css
cubic-bezier(0.16, 1, 0.3, 1)
```
produces a rapid acceleration from rest followed by a critically damped, smooth deceleration curve that mimics a spring under moderate tension with zero overshoot.
For tactile micro-rebounds (such as pressing and releasing a pill button), an underdamped curve:
```css
cubic-bezier(0.34, 1.56, 0.64, 1)
```
produces a brief $6\%$ overshoot, providing responsive tactile feedback.

## 2. GPU Compositor Optimization
To prevent repaints and layout thrashing (which cause dropped frames on 120Hz ProMotion displays), all animations must be limited strictly to:
- `transform: translate3d(...)` / `translateY(...)` / `scale(...)`
- `opacity`
- `filter: drop-shadow(...)`

Properties that trigger CPU reflows (`width`, `height`, `margin`, `padding`, `top`, `left`, `border-width`) are strictly prohibited in transition declarations. Elements undergoing continuous hover transitions receive:
```css
will-change: transform;
backface-visibility: hidden;
```
to ensure promotion to dedicated GPU composition layers.

## 3. WCAG 2.2 Criterion 2.3.3 (Animation from Interactions)
Under WCAG 2.2 Level AAA (and recommended for AA), motion animation triggered by interaction can be disabled unless the animation is essential.
The stylesheet guarantees that under `@media (prefers-reduced-motion: reduce)`, all transitions resolve in $\le 0.01\text{ms}$, preventing vestibular discomfort while maintaining instantaneous state changes.
