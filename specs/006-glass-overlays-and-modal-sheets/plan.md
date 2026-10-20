# Construction Plan: Unit 006 — Glass Overlays & Modal Sheets

## 1. Architectural Strategy
Create a reusable modal overlay primitive system in `src/components/primitives/ModalSheet.tsx` and upgrade `src/components/HistoryModal.tsx` to use Venus primitives and tokens.

```
src/
├── components/
│   ├── primitives/
│   │   └── ModalSheet.tsx (Reusable accessible glass dialog)
│   └── HistoryModal.tsx (Refactored modern attempt history)
├── styles/
│   ├── primitives/
│   │   └── modal-sheet.css (Optical backdrop & sheet styling)
│   └── components/
│       └── history-modal.css (Venus card-based table & stats)
└── types/
    └── modal.ts
```

## 2. Execution Phases
1. **Types & Contracts (`T023`)**: Define `ModalSheetProps` and event contracts in `src/types/modal.ts`.
2. **ModalSheet Primitive & Styles (`T024`)**: Implement `modal-sheet.css` and `src/components/primitives/ModalSheet.tsx` with focus trapping, Escape key dismiss, and scroll lock.
3. **Refactor HistoryModal Component (`T025`)**: Rebuild `HistoryModal.tsx` and author `history-modal.css`, integrating `SegmentedControl`, `Badge`, `IconButton`, and `Button`.
4. **Verification & Build Check (`T026`)**: Run `npm run build` and verify that no functional regressions exist in attempt calculation, clear history, or topic weaknesses.
