# Reverse Engineering: Route & Screen Inventory

## Screen Architecture

The application is structured as a single-page state machine without heavy client-side router dependencies, maintaining zero routing latency and fast reloads.

| Virtual Route / State | Component Root | Trigger / Entry | Available Transitions | Overlays Present |
| :--- | :--- | :--- | :--- | :--- |
| **`/` (`landing`)** | `LandingScreen.tsx` | App Initial Mount or "Volver al inicio" | → `quiz` (Start New or Resume) | `HistoryModal` (on demand) |
| **`/quiz` (`quiz`)** | `QuizScreen.tsx` | User clicks "Comenzar simulacro", "Continuar intento", or "Reintentar falladas" | → `results` (Submit / Time Expire)<br>→ `landing` (Abandon) | `HistoryModal`, Submit Confirm Dialog, Quit Confirm Dialog |
| **`/results` (`results`)** | `ResultsScreen.tsx` | Quiz completion or submission | → `landing` (New Quiz / Home)<br>→ `quiz` (Retry Wrong Questions) | `HistoryModal` (on demand) |

---

## State Transition Matrix

```text
+--------------+      Start New / Resume      +-----------+
|              | ---------------------------> |           |
| Landing View |                              | Quiz View |
|              | <--------------------------- |           |
+--------------+        Abandon Confirm       +-----------+
      ^                                             |
      |                                             | Submit / Timeout
      |               New Quiz / Home               v
      +-------------------------------------- +--------------+
                                              |              |
                                              | Results View |
      <-------------------------------------- |              |
            Retry Wrong Questions             +--------------+
```

---

## Screen Characteristics & Responsive Behavior

1. **Landing View**:
   - Desktop (1440px): 3-column practice mode selector, centered user name, horizontal timer preset row.
   - Tablet (768px): 2-column or stacked mode cards, wrapping timer preset pills.
   - Mobile (375px): 1-column vertical stack, full-width start button, touch-friendly 44px minimum target sizes.

2. **Quiz View**:
   - Desktop (1440px): Header row with timer & question count, horizontal 20-pill navigator bar, central question card with option tiles.
   - Tablet (768px): Responsive grid wrapping for the 20 navigator pills, stacked previous/next navigation buttons.
   - Mobile (375px): 2-row navigator pill bar or compact scrollable pill strip, sticky bottom action bar.

3. **Results View**:
   - Desktop (1440px): Hero card with circular score meter, 4-column quick statistics grid, review filter toggle bar, full-width review cards.
   - Tablet (768px): 2-column quick statistics grid, wrapped filter pills.
   - Mobile (375px): Single-column stacked stat boxes, full-width review options, sticky scroll-to-top button.
