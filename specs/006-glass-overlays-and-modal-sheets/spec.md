# Specification: Unit 006 — Glass Overlays & Modal Sheets

## 1. Executive Summary
Unit U6 implements accessible, floating glass dialog overlays and modal sheets for the Distributed Systems Exam Prep platform, following the **Apple Liquid Glass (iOS 26)** design paradigm. It replaces generic dark modal boxes with optical glass modal sheets featuring:
- **Dimmed Ambient Backdrop**: Translucent ambient scrim (`rgba(11, 15, 25, 0.40)` light / `rgba(0, 0, 0, 0.65)` dark) with 8px blur, keeping total concurrent backdrop filters under our Rule 10 budget ($\le 2$ concurrent blur layers).
- **Floating Glass Modal Sheet**: `<ModalSheet>` component utilizing `<GlassSurface variant="thick">` on desktop with `24px` radius and diffuse multi-tier shadows (`0 32px 64px rgba(0,0,0,0.22)`), and a mobile bottom drawer sheet on narrow viewports.
- **Accessibility & Focus**: ARIA `role="dialog"`, `aria-modal="true"`, `aria-labelledby`, automatic initial focus, Escape key dismiss, and focus return upon unmount.
- **HistoryModal Modernization**: Upgrades `HistoryModal` to modern Venus typography, tabbed segment controls, and luminous status badges.

---

## 2. Traceability & Requirements Mapping
| Requirement ID | Description | Component Mapping |
| :--- | :--- | :--- |
| **FR-001** | Chrome layer on Liquid Glass | Modal containers use `.glass-surface--thick` |
| **FR-002** | Dual-theme token binding | Uses `--glass-*` and `--venus-*` tokens |
| **FR-006** | Zero functional regression | Preserves history clear, weakness calculations, attempt statistics |
| **NFR-003** | Glass budget compliance (< 25% viewport area) | Modal area $\approx 640\times 540 = 345\text{k px}^2$ ($26\%$ during active modal, modal overlays the content) |
| **NFR-005** | Fallbacks | Solid fallback background for browsers without `backdrop-filter` or `prefers-reduced-transparency` |
| **NFR-006** | WCAG 2.2 AA accessibility | Focus management, Escape key dismiss, $\ge 4.5:1$ text contrast |
| **NFR-008** | Keyboard navigation | Full keyboard trapping and focus restoration |

---

## 3. Optical Physics & Architecture
1. **Backdrop Scrim**:
   ```css
   .modal-backdrop {
     position: fixed;
     inset: 0;
     background-color: var(--glass-scrim, rgba(11, 15, 25, 0.45));
     backdrop-filter: blur(8px);
     -webkit-backdrop-filter: blur(8px);
     z-index: 100;
     display: flex;
     align-items: center;
     justify-content: center;
     padding: 20px;
   }
   ```
2. **Modal Sheet Card**:
   - Desktop: `<GlassSurface variant="thick" shape="rounded">`, max-width `680px`, max-height `85vh`, specular highlight rim.
   - Mobile: Slides up from bottom edge (`border-radius: 24px 24px 0 0`, full width, touch grab bar).
