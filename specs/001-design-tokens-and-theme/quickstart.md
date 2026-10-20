# Quickstart & Verification Guide: Unit 001 — Design Tokens & Theme

## 1. Prerequisites
- Workspace active in terminal.
- Node.js environment ready.

---

## 2. Verification Checklist

### Automated Verification
1. **Compilation & Build Check**:
   ```bash
   npm run build
   ```
   - Must pass with 0 TypeScript errors and 0 build warnings.
2. **Question Bank Integrity Check**:
   ```bash
   npm run validate
   ```
   - Must confirm 520 valid questions.

### Manual Verification
1. **Initial Theme Inspection**:
   - Open [http://localhost:5173/](http://localhost:5173/).
   - Inspect the root `<html>` element in DevTools Elements tab.
   - Confirm `data-theme="light"` is active by default.
   - Inspect CSS variables under `:root` and verify `--venus-bg-canvas` resolves to `#F4F7FE`.
2. **Typography Verification**:
   - Verify Network tab confirms parallel loading of `Poppins` from Google Fonts.
   - Verify headings render with geometric Poppins font styling.
3. **Theme Toggling**:
   - Trigger theme change (via toggle UI or `document.documentElement.setAttribute('data-theme', 'dark')`).
   - Confirm canvas smoothly shifts to deep navy `#0B0F19` within 200ms without flicker.
4. **Reload Persistence**:
   - Set theme to dark.
   - Reload page (`Ctrl+R` / `Cmd+R`).
   - Confirm page immediately reloads in Dark Mode with zero white flash (FOUC).
5. **Reduced Transparency Check**:
   - In DevTools Rendering drawer, enable `Emulate CSS media feature prefers-reduced-transparency: reduce`.
   - Confirm glass variables resolve to 0px blur and opaque fills.
