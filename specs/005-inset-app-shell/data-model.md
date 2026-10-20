# Data Model: Unit 005 — Inset App Shell

## Navigation Items & State
```typescript
export type ScreenId = 'home' | 'quiz' | 'results' | 'history' | 'review';

export interface NavItem {
  id: ScreenId | string;
  label: string;
  icon: React.ReactNode;
  badge?: string | number;
  action: () => void;
  isActive: boolean;
  disabled?: boolean;
}

export interface AppShellProps {
  currentScreen: ScreenId;
  onNavigate: (screen: ScreenId) => void;
  activeLab?: 'all' | 'lab1' | 'lab2';
  onSelectLab?: (lab: 'all' | 'lab1' | 'lab2') => void;
  examInProgress?: boolean;
  onQuitExam?: () => void;
  children: React.ReactNode;
}
```
