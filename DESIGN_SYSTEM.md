# Venus & Liquid Glass Design System

> **A Two-Layer Visual System for High-Stakes Technical Assessment**  
> Combines the clean, airy, high-contrast Soft-UI cards of the **Venus Dashboard Builder** kit with Apple's **Liquid Glass** chrome aesthetic (iOS 26 / macOS Sequoia).

---

## 1. Architectural Philosophy: The Two-Layer System

To solve the central tension between high-aesthetic translucency and readability during exams, the platform separates all UI into two distinct functional layers:

```
┌────────────────────────────────────────────────────────┐
│  CHROME LAYER (Apple Liquid Glass)                    │
│  Translucent, floating, light-catching navigation,     │
│  modals, segmented tabs, toolbars & floating pills     │
└───────────────────────────┬────────────────────────────┘
                            │
┌───────────────────────────▼────────────────────────────┐
│  CONTENT LAYER (Venus Soft-UI Cards)                  │
│  Solid, opaque (#FFFFFF / #111827) cards with          │
│  diffuse shadows, bold indigo accents, and > 7:1       │
│  contrast for all questions, code blocks & metrics     │
└────────────────────────────────────────────────────────┘
```

### Rule 10: Glass Discipline
- **Glass is strictly for chrome**: Viewport glass coverage must remain $< 25\%$.
- **Zero content on glass**: Questions, options, explanations, and long code blocks must never be rendered on translucent glass. They reside on solid Venus cards.
- **Max 4 concurrent blurs**: At most 4 blur surfaces active simultaneously (capped to 1 on mobile $\le 768\text{px}$).
- **No nested backdrops**: Never render a glass surface inside another glass surface.

---

## 2. Color System & Tokens

### Primary Brand Accents
- **Electric Indigo**: `#4318FF` (`--venus-primary-indigo`) — Primary calls-to-action, selected question borders, active tab highlights.
- **Electric Indigo Hover**: `#3311CC` (`--venus-primary-indigo-hover`)
- **Neon Purple**: `#7551FF` (`--venus-primary-purple`) — Gradient pairings and category badges.
- **Dark Navy**: `#1B2559` (`--venus-text-headline`) — High-contrast headlines and stat values.
- **Steel Indigo**: `#2B3674` (`--venus-text-body`) — Readable paragraph body text.
- **Soft Muted**: `#707EAE` (`--venus-text-muted`) — Secondary labels, timestamps, metadata.

### Semantic Status Accents
- **Emerald (Success)**: `#05CD99` (`--venus-accent-emerald`) — Correct answers, passing scores $\ge 70\%$.
- **Coral (Error)**: `#EE5D50` (`--venus-accent-coral`) — Incorrect answers, missed questions.
- **Amber (Warning)**: `#FFB547` (`--venus-accent-amber`) — Retry actions, active countdown timers.
- **Cyan (Info)**: `#01B8FF` (`--venus-accent-cyan`) — Informational notes, mode tags.

### Surfaces: Dual-Theme Contrast Matrix

| Token | Light Theme | Dark Theme | Purpose |
| :--- | :--- | :--- | :--- |
| `--venus-bg-canvas` | `#F4F7FE` | `#0B0F19` | Ambient canvas background |
| `--venus-card-bg` | `#FFFFFF` (Solid) | `#111827` (Solid) | High-contrast content cards |
| `--venus-card-border` | `#E0E5F2` | `rgba(255, 255, 255, 0.08)` | Subtly bounded card edges |
| `--venus-text-headline`| `#1B2559` | `#F8FAFC` | Primary titles and metrics |
| `--venus-text-body` | `#2B3674` | `#E2E8F0` | Body text, explanation paragraphs |
| `--venus-text-muted` | `#707EAE` | `#94A3B8` | Subtle metadata and labels |

---

## 3. Typography & Spacing Scales

### Font Families
- **Display & Numerical Metrics**: `'Poppins', -apple-system, sans-serif` (`--font-display`).
- **Body & Code Block Narratives**: `'Plus Jakarta Sans', 'Inter', -apple-system, sans-serif` (`--font-sans`).
- **Technical Snippets & CLI Output**: `'JetBrains Mono', 'Fira Code', monospace` (`--font-mono`).

### Spacing Scale
- `2xs`: `2px` | `xs`: `4px` | `sm`: `8px` | `md`: `16px` | `lg`: `24px` | `xl`: `32px` | `2xl`: `48px` | `3xl`: `64px`

### Border Radii
- Pill Buttons / Badges: `9999px` (`--venus-radius-pill`)
- Small Inputs / Tags: `12px` (`--venus-radius-sm`)
- Standard Cards: `16px` (`--venus-radius-md`)
- Large Dashboard Cards: `20px` (`--venus-radius-lg`)
- Hero & Quiz Containers: `24px` (`--venus-radius-xl`)

---

## 4. Component Catalog

### UI Primitives
1. **`<Button>`** (`src/components/primitives/Button.tsx`):
   - Variants: `primary` (Electric Indigo), `secondary` (Soft Venus outline), `ghost` (clean text button), `danger` (Coral).
   - Shapes: `pill` (rounded 9999px) or `rounded` (14px).
   - Micro-interaction: tactile scale press `scale(0.98)`.
2. **`<IconButton>`** (`src/components/primitives/IconButton.tsx`):
   - Square/circular touch-expanded icon button with accessible `aria-label`.
3. **`<Badge>`** (`src/components/primitives/Badge.tsx`):
   - Tones: `indigo`, `purple`, `emerald`, `amber`, `coral`, `neutral`.
   - Subtle tinted backgrounds with bold text.
4. **`<SegmentedControl>`** (`src/components/primitives/SegmentedControl.tsx`):
   - Apple-style floating sliding indicator with spring easing.
5. **`<TextInput>`** (`src/components/primitives/TextInput.tsx`):
   - Soft-UI input field with icon adornments and clear button.

### Chrome & Shell
1. **`<AppShell>`** (`src/components/shell/AppShell.tsx`):
   - Floating desktop inset sidebar (w: 260px) + floating topbar + mobile bottom navigation pill.
2. **`<GlassSurface>`** (`src/components/GlassSurface.tsx`):
   - Foundational Apple Liquid Glass surface implementing the 6-layer optical formula.
3. **`<ModalSheet>`** (`src/components/primitives/ModalSheet.tsx`):
   - Translucent glass modal with focus trap, backdrop blur scrim, and Escape key dismissal.

### Zero-Dependency SVG Charts
1. **`<RoundedBarChart>`** (`src/components/charts/RoundedBarChart.tsx`):
   - Custom SVG vertical bars with top corner rounding (`rx="10"`) and 1 highlighted Electric Indigo bar.
2. **`<AreaSparkline>`** (`src/components/charts/AreaSparkline.tsx`):
   - Smooth cubic Bézier spline curve ($C_1, C_2$) with semi-transparent gradient fill.
3. **`<CircularGauge>`** (`src/components/charts/CircularGauge.tsx`):
   - Circular percentage gauge with smooth `stroke-dashoffset` animation.

---

## 5. Accessibility & Motion Rules

- **WCAG 2.2 AA Certified**: Minimum $4.5:1$ text on glass; $> 7:1$ text on cards.
- **Reduced Motion**: Automatically zeroes all transition durations when `prefers-reduced-motion: reduce` is detected.
- **Reduced Transparency**: Fills convert to $94\%$ solid fallback colors when `prefers-reduced-transparency: reduce` is enabled.
- **Windows High Contrast**: Full `@media (forced-colors: active)` support using system `Canvas`, `CanvasText`, and `Highlight`.
