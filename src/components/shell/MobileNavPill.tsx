// src/components/shell/MobileNavPill.tsx
import React from 'react';
import '../../styles/shell/mobile-nav-pill.css';
import { GlassSurface } from '../GlassSurface';
import { MobileNavPillProps } from '../../types/shell';
import {
  SparklesIcon,
  ClockIcon,
  FlameIcon,
} from '../primitives/Icons';

export const MobileNavPill: React.FC<MobileNavPillProps> = ({
  currentScreen,
  onNavigate,
  examInProgress = false,
  onOpenHistory,
  className = '',
}) => {
  return (
    <GlassSurface
      as="nav"
      variant="regular"
      shape="pill"
      className={`mobile-nav-pill ${className}`}
      aria-label="Mobile Bottom Navigation"
    >
      <button
        type="button"
        className={`mobile-nav__item ${currentScreen === 'home' ? 'mobile-nav__item--active' : ''}`}
        onClick={() => onNavigate('home')}
      >
        <span className="mobile-nav__icon">
          <SparklesIcon size={20} />
        </span>
        <span>Practice</span>
      </button>

      <button
        type="button"
        className={`mobile-nav__item ${currentScreen === 'quiz' ? 'mobile-nav__item--active' : ''}`}
        onClick={() => onNavigate('quiz')}
        disabled={!examInProgress && currentScreen !== 'quiz'}
      >
        <span className="mobile-nav__icon">
          <ClockIcon size={20} />
        </span>
        <span>{examInProgress ? 'Active' : 'Exam'}</span>
      </button>

      <button
        type="button"
        className={`mobile-nav__item ${currentScreen === 'history' ? 'mobile-nav__item--active' : ''}`}
        onClick={() => {
          if (onOpenHistory) {
            onOpenHistory();
          } else {
            onNavigate('history');
          }
        }}
      >
        <span className="mobile-nav__icon">
          <FlameIcon size={20} />
        </span>
        <span>History</span>
      </button>
    </GlassSurface>
  );
};
