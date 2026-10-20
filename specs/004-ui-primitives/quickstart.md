# Quickstart: Unit 004 — UI Component Primitives

## Usage Examples

### 1. Primary & Glass Buttons
```tsx
import { Button } from './components/primitives/Button';
import { SparklesIcon } from './components/primitives/Icons';

// Primary Action Button (Venus Electric Indigo)
<Button variant="primary" size="lg" shape="rounded" rightIcon={<SparklesIcon />}>
  Start Timed Exam
</Button>

// Glass Action Button (Liquid Glass Material)
<Button variant="glass" size="md" shape="pill">
  View Lab 1 Review
</Button>
```

### 2. Segmented Control for Mode Selection
```tsx
import { SegmentedControl } from './components/primitives/SegmentedControl';

<SegmentedControl
  value={selectedLab}
  onChange={setSelectedLab}
  options={[
    { id: 'all', label: 'All Questions', badge: 520 },
    { id: 'lab1', label: 'Lab 1', badge: 260 },
    { id: 'lab2', label: 'Lab 2', badge: 260 },
  ]}
/>
```

### 3. Badges & Status Indicators
```tsx
import { Badge } from './components/primitives/Badge';

<Badge tone="success" dot>Answered (45)</Badge>
<Badge tone="warning">Flagged (12)</Badge>
<Badge tone="indigo">Easy</Badge>
```
