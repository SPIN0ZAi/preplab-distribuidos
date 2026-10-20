# Inception: Intent & Vision

## 1. Executive Summary & Business Intent

The objective of this initiative is to execute a comprehensive visual and architectural redesign of the **Distributed Systems Exam-Practice Platform (PrepLab)**. The application serves computer engineering students preparing for rigorous university laboratory examinations on Docker containerization, .NET 10 microservices, and gRPC distributed concurrency.

While the existing platform is functionally complete—featuring a verified 520-question bank with complete distractor rationales, zero-error validation, and resilient session persistence—its current interface is generic and lacks visual polish. This redesign implements a **Two-Layer Visual System**:
1. **Content Layer**: Follows the Figma "Venus Dashboard Builder" aesthetic: luminous soft-UI solid cards, bold indigo accent (`#4318FF`), clean card geometry, rounded-top bar charts with single-accent emphasis, smooth area curves, and clear typographic hierarchy.
2. **Chrome Layer**: Apple's Liquid Glass (iOS 26 aesthetic): translucent, light-catching floating surfaces for navigation, toolbars, overlays, dropdowns, dialogs, and selected interactive controls, engineered with authentic multi-layer optics (backdrop blur, saturation boost, specular edge highlights, inner sheen, and soft outer shadows).

The goal is to deliver an interface with authentic translucent layering, refined depth, and responsive tactile interaction, while enforcing strict **Glass Discipline** (<25% viewport area, max 4 concurrent backdrop filters, solid high-contrast content cards).

---

## 2. Problem Statement

1. **Visual Monotony**: The current dark theme (`#0B0F19`) is flat, monochromatic, and visually uninspiring, offering low motivation for multi-hour exam preparation sessions.
2. **Lack of Visual Analytics**: Complex mastery data (e.g., topic weakness percentages across 18 distinct topics) is presented as basic HTML tables and divs, lacking the engaging, glanceable charts featured in modern dashboards.
3. **Absence of Layered Depth**: Modern desktop and tablet users expect responsive, floating chrome that preserves context while scrolling through long-form content.
4. **Fragile Custom Styling**: Existing styles reside in a single monolithic 1001-line CSS file with ad-hoc classes, making design consistency difficult to maintain.

---

## 3. Target Users & Usage Context

- **Primary Persona**: Computer Engineering Students studying for 3rd-year Distributed Systems exams.
- **Context of Use**: Intensive 20–60 minute practice sprints on desktop/laptops (1440px/1080p), tablet study sessions (768px–1024px), and on-the-go quick drills on mobile phones (375px–414px).
- **User Needs**:
  - High reading comfort and contrast for long study sessions.
  - Clear, immediate feedback on why answers are right or wrong.
  - Glanceable visual analytics revealing exactly which topics need remediation.
  - Zero cognitive friction from slow page loads or distracting UI jank.

---

## 4. Measurable Success Metrics

| Metric Category | Target Key Performance Indicator (KPI) | Measurement Method |
| :--- | :--- | :--- |
| **Visual Fidelity** | Reference-fidelity score $\ge 4.5 / 5.0$ on Venus content aesthetic and Liquid Glass chrome authenticity. | Independent design heuristic audit against reference images. |
| **Glass Discipline** | Glass area strictly $< 25\%$ of viewport area across all responsive breakpoints; maximum 4 concurrent `backdrop-filter` layers. | Automated CSS/DOM viewport area analysis. |
| **Performance Budget** | Initial client JavaScript bundle **$< 200\text{ KB}$ gzipped** (baseline: ~56 KB). Zero bundle regression. | Vite production build audit (`npm run build`). |
| **Core Web Vitals** | **LCP $< 2.5\text{s}$**, **CLS $< 0.1$**, **INP $< 200\text{ms}$**; 60 fps scrolling on 60 Hz/120 Hz displays with glass chrome active. | Lighthouse CI & Chrome DevTools Performance profile. |
| **Accessibility** | **100% WCAG 2.2 AA Compliance**. Text on glass $\ge 4.5:1$, UI controls $\ge 3:1$ against worst-case backdrops; 0 Axe serious/critical issues. | Automated Axe-core test suite & manual keyboard checklist. |
| **Functional Integrity** | **0 functional regressions**. All 520 questions, timestamp timer accuracy, scoring, and session recovery preserved 100%. | Automated characterization test suite (`npm test`). |

---

## 5. Scope In / Scope Out

### In-Scope
- Re-architecting CSS into a centralized, tokenized design system (`tokens/`, `materials/`, `primitives/`, `composites/`).
- Implementing Venus design tokens (colors, radii, shadows, typography, grid) with primary Light Mode and toggleable Dark Mode.
- Building the Liquid Glass material system (`GlassSurface`) with specular rim highlights, inner sheen, soft outer shadows, and full fallback support.
- Implementing an inset floating glass app shell: desktop sidebar, topbar, and mobile floating bottom navigation.
- Creating bespoke, zero-dependency SVG chart primitives (rounded-top bar chart with 1 highlighted indigo bar, smooth area sparkline, circular score gauge).
- Polishing interactive states (spring-like micro-interactions, focus rings, hover lift, active scale-down).
- Authoring characterization and accessibility test suites under Vitest.

### Out-of-Scope
- Backend server or cloud database integration (application remains 100% client-side with `localStorage`).
- Copying Venus branding, fake names, or dollar amounts (all content remains authentic course material).
- Using third-party heavy charting libraries (e.g., Chart.js, Recharts, D3).
- Altering the 520 question records or quiz engine scoring logic.
- Using Apple proprietary trademarks, SF Pro font files, or copyrighted assets.

---

## 6. Assumptions & Constraints

### Assumptions
- Modern browsers (Chrome, Edge, Safari, Firefox) support CSS `backdrop-filter` with `-webkit-backdrop-filter`.
- Users with older hardware or `prefers-reduced-transparency` will receive a clean, high-contrast, semi-opaque fallback without loss of functionality.
- Custom SVG charting is sufficient to replicate the bar, area, and gauge visuals shown in the Venus reference images.

### Constraints
- Zero new runtime production dependencies (React 18 and React-DOM remain the only production dependencies).
- Bundle budget must remain strictly under 200 KB gzipped.
- Specs are the source of truth; no component code may be authored until specifications and task plans are finalized and approved.
