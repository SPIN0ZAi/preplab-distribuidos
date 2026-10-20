# Atomic Tasks: Unit 006 — Glass Overlays & Modal Sheets

## Dependency Graph
```
T023 [Contracts & Types] ──> T024 [ModalSheet Component & CSS] ──> T025 [HistoryModal Modernization] ──> T026 [Verification & Build]
```

---

## Detailed Tasks Matrix

### T023: Author Modal Contracts & Types
- **File**: `src/types/modal.ts`
- **Requirement Link**: `FR-001`, `FR-006`, `NFR-011`
- **Estimated Effort**: 20 mins
- **Description**: Define TypeScript types for `ModalSheetProps` and confirmation dialog structures.
- **Definition of Done**: Clean TypeScript compilation with zero type errors.

### T024: Build Polymorphic `ModalSheet.tsx` & `modal-sheet.css`
- **Files**: `src/styles/primitives/modal-sheet.css`, `src/components/primitives/ModalSheet.tsx`
- **Requirement Link**: `FR-001`, `NFR-003`, `NFR-006`, `NFR-008`
- **Estimated Effort**: 45 mins
- **Description**: Implement glass modal overlay with dimmed blurred backdrop, spring entry animation, body scroll lock, Escape key dismiss, and focus management.
- **Definition of Done**: Modal opens smoothly, dismisses on backdrop click or Escape, and traps focus cleanly.

### T025: Modernize `HistoryModal.tsx` & Build `history-modal.css`
- **Files**: `src/styles/components/history-modal.css`, `src/components/HistoryModal.tsx`
- **Requirement Link**: `FR-001`, `FR-002`, `FR-006`, `NFR-006`
- **Estimated Effort**: 60 mins
- **Description**: Upgrade `HistoryModal` to use `ModalSheet`, `SegmentedControl` for tab switching ("Historial de Exámenes" vs "Debilidades por Tema"), `Badge` for scores and lab types, and `Button` for clear actions and confirmation.
- **Definition of Done**: All historical data, attempt percentages, and topic weaknesses display accurately in Venus soft-UI tables.

### T026: Production Build & Characterization Verification
- **Files**: Workspace-wide
- **Requirement Link**: `FR-006`, `NFR-009`
- **Estimated Effort**: 30 mins
- **Description**: Run `npm run build` and verify that history storage functions, clearing history works, and bundle budget remains $< 200\text{ KB}$ gzipped.
- **Definition of Done**: Build passes with 0 errors; 520 questions verified.
