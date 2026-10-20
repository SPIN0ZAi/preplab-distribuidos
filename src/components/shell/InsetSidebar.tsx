// src/components/shell/InsetSidebar.tsx
import React from 'react';
import '../../styles/shell/inset-sidebar.css';
import { GlassSurface } from '../GlassSurface';
import { InsetSidebarProps } from '../../types/shell';
import {
  SparklesIcon,
  BookOpenIcon,
  ClockIcon,
  FlameIcon,
} from '../primitives/Icons';
import { Badge } from '../primitives/Badge';

export const InsetSidebar: React.FC<InsetSidebarProps> = ({
  currentScreen,
  onNavigate,
  examInProgress = false,
  onQuitExam,
  activeLab = 'all',
  onSelectLab,
  className = '',
}) => {
  const handleNav = (screen: 'home' | 'quiz' | 'results' | 'history', lab?: 'all' | 'lab1' | 'lab2') => {
    if (examInProgress && screen !== 'quiz') {
      const confirmLeave = window.confirm(
        'An exam session is currently active. Are you sure you want to leave? Your answers will be saved in history.'
      );
      if (!confirmLeave) return;
      onQuitExam?.();
    }
    if (lab && onSelectLab) {
      onSelectLab(lab);
    }
    onNavigate(screen);
  };

  return (
    <GlassSurface
      as="aside"
      variant="regular"
      shape="rounded"
      className={`inset-sidebar ${className}`}
      aria-label="Primary Navigation"
    >
      {/* Brand Header */}
      <div className="sidebar__brand">
        <div className="sidebar__logo-badge">
          <SparklesIcon size={22} />
        </div>
        <div className="sidebar__brand-text">
          <span className="sidebar__brand-title">DISTRIBUIDOS</span>
          <span className="sidebar__brand-subtitle">Lab 1 & Lab 2 Prep</span>
        </div>
      </div>

      {/* Navigation Sections */}
      <nav className="sidebar__nav">
        <div className="sidebar__section-title">Exam Practice</div>

        <button
          type="button"
          className={`sidebar__nav-item ${currentScreen === 'home' && activeLab === 'all' ? 'sidebar__nav-item--active' : ''}`}
          onClick={() => handleNav('home', 'all')}
        >
          <div className="sidebar__nav-item-content">
            <span className="sidebar__nav-item-icon">
              <SparklesIcon size={18} />
            </span>
            <span>All Questions</span>
          </div>
          <Badge tone="indigo" size="sm">520</Badge>
        </button>

        <button
          type="button"
          className={`sidebar__nav-item ${currentScreen === 'home' && activeLab === 'lab1' ? 'sidebar__nav-item--active' : ''}`}
          onClick={() => handleNav('home', 'lab1')}
        >
          <div className="sidebar__nav-item-content">
            <span className="sidebar__nav-item-icon">
              <BookOpenIcon size={18} />
            </span>
            <span>Lab 1 Focus</span>
          </div>
          <Badge tone={currentScreen === 'home' && activeLab === 'lab1' ? 'indigo' : 'neutral'} size="sm">260</Badge>
        </button>

        <button
          type="button"
          className={`sidebar__nav-item ${currentScreen === 'home' && activeLab === 'lab2' ? 'sidebar__nav-item--active' : ''}`}
          onClick={() => handleNav('home', 'lab2')}
        >
          <div className="sidebar__nav-item-content">
            <span className="sidebar__nav-item-icon">
              <BookOpenIcon size={18} />
            </span>
            <span>Lab 2 Focus</span>
          </div>
          <Badge tone={currentScreen === 'home' && activeLab === 'lab2' ? 'warning' : 'neutral'} size="sm">260</Badge>
        </button>

        <div className="sidebar__section-title" style={{ marginTop: '12px' }}>Simulation</div>

        <button
          type="button"
          className={`sidebar__nav-item ${currentScreen === 'quiz' ? 'sidebar__nav-item--active' : ''}`}
          onClick={() => handleNav('quiz')}
          disabled={!examInProgress && currentScreen !== 'quiz'}
        >
          <div className="sidebar__nav-item-content">
            <span className="sidebar__nav-item-icon">
              <ClockIcon size={18} />
            </span>
            <span>Active Exam</span>
          </div>
          {examInProgress && <Badge tone="warning" dot size="sm">Live</Badge>}
        </button>

        <button
          type="button"
          className={`sidebar__nav-item ${currentScreen === 'history' ? 'sidebar__nav-item--active' : ''}`}
          onClick={() => handleNav('history')}
        >
          <div className="sidebar__nav-item-content">
            <span className="sidebar__nav-item-icon">
              <FlameIcon size={18} />
            </span>
            <span>Exam History</span>
          </div>
        </button>
      </nav>

      {/* Footer Widget */}
      <div className="sidebar__footer">
        <div className="sidebar__stat-pill">
          <span className="sidebar__stat-pill-label">Bank Coverage</span>
          <span className="sidebar__stat-pill-value">100% (520 Qs)</span>
        </div>
      </div>
    </GlassSurface>
  );
};
