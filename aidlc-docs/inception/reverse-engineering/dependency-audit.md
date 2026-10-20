# Reverse Engineering: Dependency Audit

## 1. Production Dependencies

| Package | Version | Purpose | Bundle Size (Gzip) | Tree-shakeable | Vulnerabilities | Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `react` | `^18.3.1` | Core UI library | ~2.5 KB | Yes | 0 (Clean) | Retain |
| `react-dom` | `^18.3.1` | DOM Renderer | ~42 KB | Yes | 0 (Clean) | Retain |

**Total Runtime Production Dependencies**: 2 packages.
Runtime dependency footprint is clean, minimal, and carries zero third-party UI framework bloat.

---

## 2. Development Dependencies

| Package | Version | Purpose | Dev Only | Vulnerabilities | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `@types/react` | `^18.3.12` | TypeScript definitions | Yes | 0 | Retain |
| `@types/react-dom`| `^18.3.1` | TypeScript definitions | Yes | 0 | Retain |
| `@vitejs/plugin-react` | `^4.3.4` | Vite React fast-refresh plugin | Yes | 0 | Retain |
| `typescript` | `^5.6.3` | Typechecker & compiler | Yes | 0 | Retain |
| `vite` | `^5.4.11` | Build tool & dev server | Yes | 0 | Retain |

---

## 3. Planned Developer Dependencies (ADR-0001 Approved)

In accordance with **ADR-0001**:
- `vitest` (`^2.1.0`): Fast Vite-native test runner.
- `@testing-library/react` (`^16.0.0`): DOM assertion utilities.
- `@testing-library/jest-dom` (`^6.6.0`): Jest matchers for DOM.
- `jsdom` (`^25.0.0`): Headless DOM environment.
- `axe-core` & `vitest-axe` (`^4.10.0`): Automated accessibility and contrast validation.

Impact on Production Bundle: **0 bytes** (dev-only).

---

## 4. Production Build Baseline Metrics

Measured from clean `npm run build` run:
- `dist/index.html`: **1.13 kB** (gzip: 0.65 kB)
- `dist/assets/index-FBmR8OYE.css`: **15.22 kB** (gzip: 3.74 kB)
- `dist/assets/index-BXtLxJnK.js`: **179.27 kB** (gzip: 56.27 kB)
- `dist/assets/lab1-CuNYKHuq.js`: **246.61 kB** (gzip: 59.05 kB) — Lazy Loaded
- `dist/assets/lab2-D--cnYuZ.js`: **254.58 kB** (gzip: 65.83 kB) — Lazy Loaded

**Current Initial JavaScript Load (Gzip)**: **56.27 KB** (Well under the **200 KB** budget limit).
