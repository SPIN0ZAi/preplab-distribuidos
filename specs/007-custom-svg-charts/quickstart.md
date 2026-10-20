# Quickstart: Unit 007 — Custom SVG Charts

## Usage Examples

### 1. Rounded Bar Chart (Figma Venus Aesthetic)
```tsx
import { RoundedBarChart } from './components/charts/RoundedBarChart';

<RoundedBarChart
  data={[
    { label: 'Lun', value: 45 },
    { label: 'Mar', value: 60 },
    { label: 'Mie', value: 85, highlighted: true }, // Electric Indigo active bar
    { label: 'Jue', value: 40 },
    { label: 'Vie', value: 70 },
  ]}
  height={180}
/>
```

### 2. Smooth Area Sparkline
```tsx
import { AreaSparkline } from './components/charts/AreaSparkline';

<AreaSparkline
  data={[
    { label: 'Test 1', value: 50 },
    { label: 'Test 2', value: 65 },
    { label: 'Test 3', value: 60 },
    { label: 'Test 4', value: 85 },
    { label: 'Test 5', value: 90 },
  ]}
  height={100}
/>
```

### 3. Circular Score Gauge
```tsx
import { CircularGauge } from './components/charts/CircularGauge';

<CircularGauge
  percentage={85}
  size={120}
  tone="dynamic" // Green if >= 50%, Red if < 50%
/>
```
