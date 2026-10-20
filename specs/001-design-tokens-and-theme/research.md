# Research & Decision Matrices: Unit 001

## 1. Decision Matrix 1: CSS Color Notation Strategy

| Option | Browser Compatibility | Transparency Ease | Preprocessing Need | Contrast Tuning | Decision Score |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Option A: Hex + RGBA** | 100% (Universal) | High (Native `rgba()`) | None | High | **Selected (5/5)** |
| **Option B: HSL** | 99% (Modern) | Moderate | None | High | Alternate (4/5) |
| **Option C: OKLCH** | ~92% (Newer browsers) | High | Requires PostCSS fallback | Very High | Rejected (3/5) |

### Rationale:
Option A (`#RRGGBB` + `rgba(...)`) is chosen because it requires **zero PostCSS plugins**, operates identically in WebKit (Safari), Blink (Chrome/Edge), and Gecko (Firefox), and avoids color-gamut clipping bugs on older devices while meeting all WCAG 2.2 contrast requirements.

---

## 2. Decision Matrix 2: Font Loading Strategy for `Poppins`

| Option | Bundle Overhead | First Contentful Paint | Setup Complexity | Licensing | Decision Score |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Option A: Google Fonts with Preconnect** | 0 KB in bundle | Fast (<150ms) | Low (`index.html`) | SIL Open Font License | **Selected (5/5)** |
| **Option B: Self-Hosted WOFF2 in `public/`** | ~80 KB in dist | Instant after cache | Medium | SIL Open Font License | Alternate (4/5) |
| **Option C: Fallback to System Sans** | 0 KB | Instant | None | N/A | Rejected (Fails Venus Aesthetic) |

### Rationale:
Option A is chosen using `<link rel="preconnect" href="https://fonts.googleapis.com">` and `<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>` directly in `index.html`. This ensures immediate parallel DNS resolution and asset streaming without increasing the static bundle size beyond the 200 KB gzipped budget.

---

## 3. ADR-0002 Reference
The formal Architecture Decision Record for token architecture and font delivery is documented in `/docs/adr/0002-token-architecture-and-font-delivery.md`.
