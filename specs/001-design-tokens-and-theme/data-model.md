# Data Model: Unit 001 — Design Tokens & Theme State

## 1. Domain Entities & Storage Contract

### 1.1 LocalStorage Entity: `ThemePreference`
- **Key**: `'ds_quiz_theme_preference'`
- **Values**: `'light' | 'dark'`
- **Default**: `'light'` (or system match via `prefers-color-scheme`)

```typescript
export type ThemeMode = 'light' | 'dark';

export interface ThemeState {
  currentTheme: ThemeMode;
  systemPreference: ThemeMode;
  isReducedTransparency: boolean;
  isReducedMotion: boolean;
}
```

---

## 2. Token Data Dictionary (TypeScript Representation)

See full TypeScript definitions in [`contracts/theme-tokens.ts`](file:///c:/Users/ssola/Desktop/documentos%20de%20estudios/3%20year/distribuidos/LAB/lab%201%20and%202%20test%20preparation/specs/001-design-tokens-and-theme/contracts/theme-tokens.ts).
