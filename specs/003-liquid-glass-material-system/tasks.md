# Atomic Tasks: Unit 003 — Liquid Glass Material System & Fallbacks

## Task Dependency Ordering

```
T010 [Liquid Glass CSS Recipe] ──> T011 [GlassSurface React Component] ──> T012 [Contrast & Fallback Verification]
```

---

## Detailed Tasks Matrix

### T010: Author `glass-surface.css` Stylesheet
- **File**: `src/styles/glass-surface.css`
- **Requirement Link**: `FR-001`, `NFR-003`, `NFR-005`, `NFR-006`, `NFR-013`, `NFR-017`
- **Estimated Effort**: 45 mins
- **Description**: Formulate the base `.glass-surface` optical layering recipe (backdrop blur + saturate, tinted fill, specular highlight inset, bottom shade inset, diagonal sheen pseudo-element `::before`, outer shadows). Implement variants: `.glass-surface--thin`, `.glass-surface--regular`, `.glass-surface--thick`, `.glass-surface--accent`, and shapes (`--rounded`, `--pill`, `--circle`). Implement `@supports not` fallback and mobile blur reduction.
- **Definition of Done**: CSS classes compile cleanly; optical layers render correctly in browser.

### T011: Build Polymorphic `GlassSurface.tsx` Component
- **Files**: `src/components/GlassSurface.tsx`, `src/types/glass.ts`
- **Requirement Link**: `FR-001`, `NFR-017`
- **Estimated Effort**: 45 mins
- **Description**: Implement polymorphic React component `<GlassSurface as="div" variant="regular" tone="default" shape="rounded">` supporting custom tags, classes, and full HTML attributes with TypeScript safety.
- **Definition of Done**: Component renders specified HTML tag with corresponding glass classes and children.

### T012: Build Verification & Automated Contrast Proof
- **Files**: Workspace-wide
- **Requirement Link**: `NFR-001`, `NFR-006`, `NFR-009`
- **Estimated Effort**: 30 mins
- **Description**: Run `npm run build` to confirm 0 compilation errors. Verify text contrast $\ge 4.5:1$ across all variants and fallback behaviors under reduced transparency.
- **Definition of Done**: Build passes with 0 warnings; initial bundle stays $< 200\text{ KB}$ gzipped.
