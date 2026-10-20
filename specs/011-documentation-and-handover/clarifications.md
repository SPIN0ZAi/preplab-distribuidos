# SDD Clarifications: 011-documentation-and-handover

## Resolved Decisions

### Q1: Where should design system and optical recipe documentation reside?
- **Decision**: In root-level markdown documents `DESIGN_SYSTEM.md` and `GLASS_MATERIAL_GUIDE.md`, with operations materials stored in `aidlc-docs/operations/`.
- **Rationale**: Root-level placement makes core architecture instantly discoverable for engineers and designers cloning the repository.

### Q2: What should be emphasized in the documentation regarding future feature work?
- **Decision**: Emphasize **Rule 10 (Glass Discipline)**: Content belongs on solid, high-contrast Venus cards; glass is reserved strictly for chrome, navigation, toolbars, and modal surfaces.
- **Rationale**: Preserves long-term legibility and prevents visual clutter or contrast degradation in future extensions.
