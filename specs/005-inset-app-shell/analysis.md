# Traceability & Verification Analysis: Unit 005 — Inset App Shell

## 1. Compliance Matrix
| Requirement ID | Description | Verification Method | Pass Criteria |
| :--- | :--- | :--- | :--- |
| **FR-001** | Two-layer system (Chrome on Glass, Content on Solid Cards) | Layout inspection | Sidebar & topbar render in Glass; content injected in solid cards |
| **FR-002** | Dual-theme token binding | CSS variables check | All shell surfaces adapt via `--glass-*` and `--venus-*` tokens |
| **FR-004** | Responsive viewports (375px–1440px) | Viewport resize check | Desktop shows inset sidebar; mobile hides sidebar and mounts bottom pill |
| **FR-006** | Zero functional regression | Characterization check | Active exam state preserved; modal triggers work as expected |
| **NFR-003** | Glass budget compliance (< 25% viewport area) | Geometry calculation | Desktop: Sidebar ($260\times 900 = 234\text{k}$) + Topbar ($1100\times 64 = 70.4\text{k}$) $\approx 304.4\text{k px}^2$ / $1440\times 900 = 1.296\text{M px}^2$ ($23.4\% \le 25\%$). Mobile: $375\times 64 \approx 24\text{k px}^2$ / $375\times 812 = 304.5\text{k px}^2$ ($7.8\% \le 25\%$) |
| **NFR-006** | WCAG 2.2 AA accessibility | Contrast & ARIA | All navigation elements have accessible names and semantic landmarks (`<aside>`, `<header>`, `<nav>`) |
| **NFR-009** | Performance & bundle budget | `npm run build` | Bundle remains $< 200\text{ KB}$ gzipped |
