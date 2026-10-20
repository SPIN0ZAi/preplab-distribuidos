// specs/005-inset-app-shell/contracts/app-shell.ts
import React from 'react';

export type ScreenId = 'home' | 'quiz' | 'results' | 'history' | 'review';

export interface NavItemConfig {
  id: string;
  label: string;
  icon: React.ReactNode;
  badge?: string | number;
  badgeTone?: 'neutral' | 'indigo' | 'success' | 'warning' | 'danger';
  screen?: ScreenId;
  onClick?: () => void;
  disabled?: boolean;
}

export interface InsetSidebarProps {
  currentScreen: ScreenId;
  onNavigate: (screen: ScreenId) => void;
  examInProgress?: boolean;
  onQuitExam?: () => void;
  totalQuestions?: number;
  className?: string;
}

export interface InsetTopbarProps {
  currentScreen: ScreenId;
  onNavigate: (screen: ScreenId) => void;
  title?: string;
  subtitle?: string;
  examInProgress?: boolean;
  className?: string;
}

export interface MobileNavPillProps {
  currentScreen: ScreenId;
  onNavigate: (screen: ScreenId) => void;
  examInProgress?: boolean;
  className?: string;
}

export interface AppShellProps {
  currentScreen: ScreenId;
  onNavigate: (screen: ScreenId) => void;
  examInProgress?: boolean;
  onQuitExam?: () => void;
  title?: string;
  children: React.ReactNode;
}
