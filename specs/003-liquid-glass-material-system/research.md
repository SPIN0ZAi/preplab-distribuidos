# Research & Decision Matrix: Unit 003

## 1. Decision Matrix: Liquid Glass Optical Layering Implementation

| Technique | Optical Authenticity | Safari/WebKit Stability | Performance (60 fps) | Fallback Simplicity | Score |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Option A: Multi-Layer CSS (Backdrop + Box-Shadow Inset + Pseudo Sheen)** | High (Authentic specular rim + sheen) | High (Standard properties) | High (Zero JS overhead) | Very High (Pure CSS media queries) | **Selected (5/5)** |
| **Option B: SVG Displacement Filter Refraction** | Very High (True edge refraction) | Low (Blink only; broken in WebKit) | Low–Moderate (GPU pipeline stall) | Low (Requires feature detection) | Rejected for Baseline (2/5) |
| **Option C: Nested Blurs (Dual Filter)** | Poor (Produces black artifacts in WebKit) | Very Low (Known Safari bug) | Low | Low | Rejected (1/5) |
| **Option D: Simple Opacity with No Rim** | Very Low (Looks like generic tinted box) | High | High | High | Rejected (Fails Quality Bar) |

### Rationale:
Option A combines standard CSS `backdrop-filter: blur() saturate()`, an inset white top/left highlight via `box-shadow`, an inset bottom shade, and a subtle diagonal linear gradient sheen on `::before`. This achieves authentic Apple-grade optical physics across Chrome, Edge, Safari, and Firefox with zero JavaScript overhead.
