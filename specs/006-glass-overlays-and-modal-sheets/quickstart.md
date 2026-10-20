# Quickstart: Unit 006 — Glass Overlays & Modal Sheets

## Usage Example

```tsx
import { ModalSheet } from './components/primitives/ModalSheet';
import { Button } from './components/primitives/Button';

<ModalSheet
  isOpen={isModalOpen}
  onClose={() => setIsModalOpen(false)}
  title="Historial de Intentos"
  subtitle="Resultados de simulacros anteriores y debilidades por tema"
  footer={
    <div style={{ display: 'flex', justifyContent: 'flex-end', gap: '12px' }}>
      <Button variant="secondary" onClick={() => setIsModalOpen(false)}>Cerrar</Button>
    </div>
  }
>
  <div className="modal-body-content">
    {/* Content */}
  </div>
</ModalSheet>
```
