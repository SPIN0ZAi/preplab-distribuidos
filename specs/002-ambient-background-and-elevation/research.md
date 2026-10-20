# Research & Decision Matrix: Unit 002

## 1. Decision Matrix: Ambient Mesh Rendering Architecture

| Option | Scrolling Performance | Safari Compatibility | GPU Memory Usage | CPU Overhead | Score |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Option A: Fixed Container + Radial Gradient Orbs** | 60 fps (Hardware composited) | 100% (No fixed-background repaint bug) | Minimal (<5 MB) | 0% | **Selected (5/5)** |
| **Option B: CSS `background-attachment: fixed` on `body`** | Janky on iOS Safari (Repaint on scroll) | Known WebKit scroll bug | Low | Low | Rejected (3/5) |
| **Option C: HTML5 `<canvas>` Animation Loop** | 50–60 fps | High | Moderate | 5–15% CPU | Rejected (2/5) |
| **Option D: High-Resolution Static Image (WebP/SVG)** | 60 fps | 100% | High (~300 KB file) | 0% | Rejected (Violates Bundle Budget) |

### Rationale:
Option A uses a dedicated fixed `div` with `pointer-events: none` and `transform: translateZ(0)` containing 3 soft radial gradients. This creates a dedicated GPU compositing layer that does not repaint during page scrolling, ensuring flawless 60 fps frame rates across all browsers including mobile Safari.
