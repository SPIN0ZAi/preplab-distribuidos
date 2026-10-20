# Quickstart & Verification Guide: Unit 002 — Ambient Background Layer

## 1. Automated Verification
```bash
npm run build
```
- Must compile cleanly with 0 errors.

## 2. Manual Verification Checklist
1. **Visual Appearance (Light Mode)**:
   - Open browser at `http://localhost:5173/`.
   - Inspect the background canvas. Confirm soft ambient indigo, purple, and coral gradient orbs are visible behind the content.
   - Confirm solid cards (`.card`) sit cleanly on top with high contrast and zero visual interference.
2. **Visual Appearance (Dark Mode)**:
   - Click the Theme Toggle.
   - Confirm the canvas transitions smoothly to deep navy `#0B0F19` with subtle deep indigo, purple, and cyan orbs.
3. **Scroll Performance**:
   - Scroll up and down rapidly. Confirm 60 fps smooth scrolling with zero jitter or repainting artifacts.
4. **Accessibility Check**:
   - Verify `aria-hidden="true"` is present on `.ambient-background`.
   - Confirm screen readers ignore the element.
