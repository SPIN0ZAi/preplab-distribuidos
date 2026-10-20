# ADR-0001: Adoption of Vitest, React Testing Library, and Axe-core for Characterization and Accessibility Testing

## Status
Approved (via Gate 0 Batch 1 Approval on 2026-10-20)

## Context
The project currently relies on `scripts/validate-questions.mjs` for data validation and `tsc && vite build` for compile-time checking. As we initiate a comprehensive visual and architectural redesign of the UI under AI-DLC and SDD, we require:
1. **Characterization Tests**: Automated regression tests locking in the behavioral contracts of the core state machine, quiz engine, storage layer, and countdown timer before making structural changes.
2. **Automated Accessibility Testing**: Direct programmatic verification of DOM nodes and glass surfaces against WCAG 2.2 AA standards (contrast, focusability, ARIA attributes).
3. **Seamless Integration**: Fast execution that reuses the existing Vite pipeline and `tsconfig.json` without adding runtime overhead to production bundles.

## Decision
We adopt the following developer dependencies:
- `vitest`: Fast, Vite-native test runner with built-in ESM, TypeScript, and dynamic import support.
- `@testing-library/react` and `@testing-library/jest-dom`: Standard DOM assertion utilities for React component characterization.
- `jsdom`: Lightweight DOM environment for fast headless component testing.
- `axe-core` and `vitest-axe`: Automated accessibility and WCAG contrast/attribute test suite.

These tools are strictly `devDependencies` and contribute **0 bytes** to the production client bundle.

## Consequences

### Positive
- Enables immediate authoring of characterization tests for `storage.ts`, `quizEngine.ts`, `Timer.tsx`, `LandingScreen.tsx`, and `QuizScreen.tsx`.
- Automated test suites can run in CI and local pre-commit hooks (`npm test`).
- Directly satisfies Constitution Principle 7 (WCAG 2.2 AA) and Principle 10 (Engineering Rigor).

### Negative
- Adds devDependencies to `package.json` (~25 MB installed in `node_modules`).
- Requires configuring `vitest.config.ts` or extending `vite.config.ts`.

## Compliance Check
- Constitution Principle 6 (ADR Required): Passed.
- Production Bundle Budget Impact: 0 bytes (development only).
