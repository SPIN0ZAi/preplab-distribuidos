# Quickstart & Verification Guide: Unit 003 — Liquid Glass Material System

## 1. Automated Verification
```bash
npm run build
```
- Must complete with 0 TypeScript compilation errors and 0 CSS syntax warnings.

## 2. Manual Verification Checklist
1. **Optical Inspection (Chrome Layer)**:
   - Render a `<GlassSurface variant="regular">Test</GlassSurface>`.
   - Inspect the top edge: confirm 1px bright specular highlight (`inset 0 1px 1px`).
   - Inspect the diagonal sheen: confirm 135-degree faint gradient overlay via `::before`.
   - Scroll content behind: verify text and cards blur cleanly with saturation boost.
2. **Variants Check**:
   - `thin`: 8px blur, subtle fill (badges).
   - `regular`: 18px blur, medium fill (topbar).
   - `thick`: 28px blur, heavier fill (modals).
3. **Fallback Simulation**:
   - In DevTools Rendering drawer, enable `prefers-reduced-transparency: reduce`.
   - Confirm surfaces degrade instantly to opaque 94% tinted cards with solid borders.
4. **Contrast Verification**:
   - Measure text contrast against pure white, dark navy, brand indigo, and ambient gradient orbs.
   - Confirm contrast is $\ge 4.5:1$ across all test regions.
