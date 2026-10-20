# Clarifications & Ambiguity Scan: Unit 001

## 1. Ambiguity Scan Matrix

| Area | Question / Ambiguity | Resolution / Decision | Source |
| :--- | :--- | :--- | :--- |
| **Token Naming** | Should tokens be prefixed with `--venus-*` and `--glass-*`, or generic `--color-*`? | **Prefixing standard**: Use `--venus-*` for content layer tokens (palette, spacing, shadows) and `--glass-*` for chrome layer tokens (blur, fills, specular borders) to explicitly enforce Rule 10 (Glass Discipline) at the code level. | Architecture Decision |
| **Color Space** | Should colors be stored as Hex, HSL, or OKLCH? | Use **Hex + RGBA** for root tokens to ensure 100% universal browser compatibility without relying on PostCSS color transform plugins. | `research.md` |
| **Theme Default** | Should the app boot into Light or Dark mode if user has no saved preference? | Default to **Venus Light Mode** to immediately showcase reference fidelity with the 5 Venus design images, unless the user's OS has explicitly requested dark mode. | Approved in Batch 1 |
| **Font Delivery** | How should Poppins be imported? | Add Google Fonts `<link rel="preconnect">` and `<link href="...family=Poppins:wght@500;600;700;800...">` to `index.html` to avoid blocking `@import` statements inside CSS files. | Performance Budget |
| **FOUC Prevention** | How do we avoid flash of light theme on reload if user previously selected Dark Mode? | Place a tiny (~150-byte) synchronous inline `<script>` in `index.html` right inside `<head>`: `const t = localStorage.getItem('ds_quiz_theme_preference') || (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light'); document.documentElement.setAttribute('data-theme', t);`. | UX Best Practice |
| **Transition Scope** | Which properties should animate when toggling themes? | Animate `background-color`, `border-color`, `box-shadow`, and `color` over `200ms ease`. Do NOT animate layout dimensions (`width`, `height`, `margin`, `padding`) to prevent reflow lag. | 60 fps Budget |

---

## 2. Unresolved Items
*Zero unresolved `[NEEDS CLARIFICATION]` items remain for Unit 001.*
