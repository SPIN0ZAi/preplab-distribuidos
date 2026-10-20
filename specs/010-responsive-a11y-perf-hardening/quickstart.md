# SDD Quickstart: 010-responsive-a11y-perf-hardening

## 1. Using Hardening Classes & Rules

### Applying Standard Focus Ring
```html
<button class="venus-button focus-ring">
  Acción
</button>
```

### Expanding Mobile Touch Targets
```css
.compact-pill {
  position: relative;
}

@media (pointer: coarse) {
  .compact-pill::after {
    content: '';
    position: absolute;
    top: -6px;
    bottom: -6px;
    left: -6px;
    right: -6px;
  }
}
```

### High Contrast / Forced Colors Verification
To preview forced-colors mode locally in Chromium:
1. Open DevTools -> More Tools -> Rendering.
2. Emulate CSS media feature `forced-colors: active`.
3. Verify all translucent glass borders convert to system `ButtonBorder` or `CanvasText`.
