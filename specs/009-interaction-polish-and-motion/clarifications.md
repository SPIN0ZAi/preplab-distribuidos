# SDD Clarifications: 009-interaction-polish-and-motion

## Resolved Design Decisions

### Q1: Should motion be orchestrated using JavaScript animation libraries (e.g. Framer Motion, GSAP)?
- **Decision**: No. In accordance with Constitutional Rule 8 (Zero New Runtime Dependencies) and the $< 200\text{ KB}$ bundle budget, all spring curves and transitions are implemented in pure CSS using hardware-accelerated transforms and standard keyframes.
- **Rationale**: JavaScript animation runtimes add 30–75 KB gzipped. Pure CSS `@keyframes` and `transition` with GPU-promoted properties deliver sustained 60 FPS performance with zero bundle overhead.

### Q2: What spring easing best approximates Apple Liquid Glass in CSS?
- **Decision**: `cubic-bezier(0.16, 1, 0.3, 1)` for surface translation and deceleration, paired with `cubic-bezier(0.34, 1.56, 0.64, 1)` for micro-spring rebounds (e.g., active toggles, badge pop).
- **Rationale**: iOS system animations feature high initial velocity followed by a prolonged, smooth asymptotic arrival without harsh clamping.

### Q3: How should hover transforms behave on touch devices?
- **Decision**: All `:hover` transforms (`translateY(-2px)`) are guarded by `@media (hover: hover) and (pointer: fine)` to avoid sticky hover states on mobile Safari and Android Chrome.
- **Rationale**: On mobile touch screens, tapped elements can retain pseudo-hover states indefinitely, causing visual artifacts. Guarding hover states ensures clean touch response.

### Q4: How is celebratory feedback triggered on exam completion?
- **Decision**: Conditional CSS class `.celebrating` or `.passed` on the Results hero card and gauge when score $\ge 70\%$, activating subtle sheen sweep and ring pulse.
- **Rationale**: Keeps logic lightweight and declarative without external particle or confetti libraries.
