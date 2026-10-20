# Data Model: Unit 004 — UI Component Primitives

## Entity Definitions

### 1. Button Variants & Props
- `variant`: `'primary' | 'secondary' | 'glass' | 'danger' | 'ghost'`
- `size`: `'sm' | 'md' | 'lg'`
- `shape`: `'rounded' | 'pill' | 'circle'`
- `isLoading`: `boolean`
- `leftIcon`: `React.ReactNode`
- `rightIcon`: `React.ReactNode`
- `disabled`: `boolean`

### 2. Badge / Pill Variants
- `tone`: `'neutral' | 'indigo' | 'success' | 'warning' | 'danger' | 'glass'`
- `size`: `'sm' | 'md'`
- `dot`: `boolean` (optional glowing status dot)

### 3. SegmentedControl Option
- `id`: `string`
- `label`: `string`
- `icon`: `React.ReactNode` (optional)
- `badge`: `string | number` (optional)
- `disabled`: `boolean` (optional)

### 4. TextInput Props
- `value`: `string`
- `onChange`: `(value: string) => void`
- `placeholder`: `string`
- `icon`: `React.ReactNode` (optional left prefix icon)
- `onClear`: `() => void` (optional clear action)
- `error`: `string` (optional validation error message)
