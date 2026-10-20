# Clarifications: Unit 006 — Glass Overlays & Modal Sheets

## Clarification Log

### C001: Should modal backdrop scrolling be disabled when open?
- **Decision**: Yes. When a modal opens, `document.body.style.overflow = 'hidden'` is applied, and restored to `''` when closed, preventing background jitter or dual-scroll confusion on mobile.

### C002: How are nested backdrop filters handled (Rule 10)?
- **Decision**: The backdrop overlay uses `blur(6px)`. To avoid exceeding our Rule 10 limit of 4 concurrent blurs and avoid nested blur artifacts on WebKit, the modal sheet content itself uses high-opacity thick glass fill (`rgba(255, 255, 255, 0.92)` in Light Mode, `rgba(17, 24, 39, 0.94)` in Dark Mode) with specular borders and shadows. This guarantees crisp text contrast and eliminates mobile rendering lag.
