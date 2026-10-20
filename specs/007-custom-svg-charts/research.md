# Research & SVG Geometry: Unit 007 — Custom SVG Charts

## 1. Reference Figma Analysis ("Venus Dashboard Builder")
The reference image `media_1792515753271.png` displays two key charts:
1. **Weekly Activity Bar Chart**:
   - 6 or 7 vertical columns with rounded pill tops (`border-radius: 10px 10px 0 0` or SVG `rx="10"`).
   - Inactive columns are neutral gray `#E2E8F0` / dark `#1E293B`.
   - The selected / active column is saturated Electric Indigo `#4318FF`.
   - Below each bar is a soft label (e.g. `L`, `M`, `X`, `J`, `V`, `S`, `D` or `Test 1`, `Test 2`).
2. **Performance Area Chart**:
   - Continuous curve spline with Electric Indigo outline and transparent purple/indigo fill gradient.
   - Smoothly connects discrete exam attempt scores.

## 2. Bézier Mathematics for Smooth Spline
Given discrete points $(x_0, y_0), (x_1, y_1), \dots, (x_n, y_n)$:
For each segment $i$ from $(x_{i-1}, y_{i-1})$ to $(x_i, y_i)$, the cubic control points are calculated with horizontal bias:
$$C_{1x} = x_{i-1} + (x_i - x_{i-1}) \cdot 0.5, \quad C_{1y} = y_{i-1}$$
$$C_{2x} = x_i - (x_i - x_{i-1}) \cdot 0.5, \quad C_{2y} = y_i$$
This creates an S-curve transition identical to Apple Health and Figma charts without complex poly-spline solving libraries.
