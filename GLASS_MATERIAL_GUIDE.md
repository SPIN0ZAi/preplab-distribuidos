# Apple Liquid Glass Material Guide (iOS 26 / macOS Sequoia)

> **Architectural Specification & Optical Recipe**  
> Formulated for the Chrome Layer of the Distributed Systems Exam Prep Platform.

---

## 1. The 6-Layer Optical Recipe

To achieve authentic, light-catching physical realism comparable to Apple's design language, every glass surface implements a multi-layer optical formula:

```
┌──────────────────────────────────────────────────────────────┐
│  Layer 6: Tinted Ambient Drop Shadow                         │
│  Layer 5: Diagonal Directional Sheen (::before pseudo)       │
│  Layer 4: Inset Specular Edge Shade (inset 0 -1px 1px ...)   │
│  Layer 3: Inset Specular Edge Highlight (inset 0 1px 1px ...)│
│  Layer 2: High-Translucency Tinted Acrylic Base Fill         │
│  Layer 1: Dual-Pass Backdrop Filter (blur + saturate)        │
└──────────────────────────────────────────────────────────────┘
```

### Detailed Layer Breakdown

1. **Dual-Pass Backdrop Filter**:
   ```css
   backdrop-filter: blur(var(--glass-blur-regular, 24px)) saturate(var(--glass-saturate, 180%));
   -webkit-backdrop-filter: blur(var(--glass-blur-regular, 24px)) saturate(var(--glass-saturate, 180%));
   ```
   *Optical purpose*: Softens high-frequency background noise while boosting color saturation to prevent murky graying.

2. **Tinted Acrylic Base Fill**:
   ```css
   background-color: var(--glass-fill-regular);
   /* Light mode: rgba(255, 255, 255, 0.72) */
   /* Dark mode:  rgba(17, 24, 39, 0.54) */
   ```
   *Optical purpose*: Imparts material thickness and establishes the color temperature of the substrate.

3. **1px Specular Rim Border**:
   ```css
   border: var(--glass-border);
   /* Light mode: 1px solid rgba(255, 255, 255, 0.40) */
   /* Dark mode:  1px solid rgba(255, 255, 255, 0.12) */
   ```
   *Optical purpose*: Delineates the edge where light refracts off the cut glass perimeter.

4. **Inset Edge Highlight & Shade**:
   ```css
   box-shadow: var(--glass-edge-highlight), var(--glass-edge-shade), var(--glass-shadow-regular);
   /* Edge highlight: inset 0 1px 1px 0 rgba(255, 255, 255, 0.65) */
   /* Edge shade:     inset 0 -1px 1px 0 rgba(0, 0, 0, 0.05) */
   ```
   *Optical purpose*: Simulates a directional light source from above, giving the surface tangible depth.

5. **Diagonal Directional Sheen (`::before`)**:
   ```css
   .glass-surface::before {
     content: '';
     position: absolute;
     inset: 0;
     border-radius: inherit;
     background: var(--glass-sheen);
     /* 135deg linear-gradient: rgba(255, 255, 255, 0.14) -> rgba(255, 255, 255, 0) */
     pointer-events: none;
   }
   ```
   *Optical purpose*: Adds an anisotropic reflection characteristic of polished curved mineral glass.

6. **Tinted Ambient Drop Shadow**:
   ```css
   box-shadow: 0 18px 40px rgba(112, 144, 176, 0.12), 0 4px 12px rgba(0, 0, 0, 0.04);
   ```
   *Optical purpose*: Floats the glass panel gently above the canvas without creating muddy black occlusion.

---

## 2. Rule 10: Glass Discipline & Budgeting

Glass creates visual magic only when used with restraint. Unchecked glass leads to legibility degradation and GPU thermal issues.

| Constraint | Specification | Rationale |
| :--- | :--- | :--- |
| **Max Viewport Area** | $< 25\%$ | Retains clarity and keeps focus on exam content |
| **Max Concurrent Blurs** | 4 on desktop, 1 on mobile | Caps GPU fragment shader convolution passes |
| **Nested Glass** | **0 (Strictly Forbidden)** | Compounding backdrop filters causes extreme frame drops |
| **Content on Glass** | **Forbidden** | Questions, options, and code blocks MUST use solid Venus cards |
| **Mobile Blur Radius** | Max 12px on $\le 768\text{px}$ | Avoids mobile GPU thermal throttling |

---

## 3. Degradation & Accessibility Fallbacks

The material system features progressive degradation across all platforms:

### 1. Browser Without `backdrop-filter`
```css
@supports not (backdrop-filter: blur(10px)) {
  .glass-surface {
    background-color: var(--glass-fallback-fill); /* 94% solid white / dark */
    border: 1px solid var(--glass-fallback-border);
  }
}
```

### 2. User Prefers Reduced Transparency
```css
@media (prefers-reduced-transparency: reduce) {
  :root {
    --glass-blur-regular: 0px;
    --glass-fill-regular: var(--glass-fallback-fill);
  }
}
```

### 3. User Prefers Reduced Motion
```css
@media (prefers-reduced-motion: reduce) {
  * {
    animation-duration: 0.001ms !important;
    transition-duration: 0.001ms !important;
  }
}
```

### 4. Windows High Contrast Mode
```css
@media (forced-colors: active) {
  .glass-surface {
    backdrop-filter: none !important;
    background-color: Canvas !important;
    border: 1.5px solid CanvasText !important;
  }
}
```
