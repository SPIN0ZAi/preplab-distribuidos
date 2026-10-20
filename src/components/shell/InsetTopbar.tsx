// src/components/shell/InsetTopbar.tsx
import React, { useState, useEffect } from 'react';
import '../../styles/shell/inset-topbar.css';
import { GlassSurface } from '../GlassSurface';
import { InsetTopbarProps } from '../../types/shell';
import { IconButton } from '../primitives/IconButton';
import { SunIcon, MoonIcon } from '../primitives/Icons';
import { themeService, ThemeMode } from '../../services/theme';
import { Badge } from '../primitives/Badge';
import { Button } from '../primitives/Button';

export const InsetTopbar: React.FC<InsetTopbarProps> = ({
  currentScreen,
  title = 'Distributed Systems Exam Prep',
  subtitle,
  examInProgress = false,
  onQuitExam,
  className = '',
}) => {
  const [theme, setCurrentThemeState] = useState<ThemeMode>('light');

  useEffect(() => {
    setCurrentThemeState(themeService.getTheme());
    const handleThemeChange = (e: Event) => {
      const customEvent = e as CustomEvent<{ theme: ThemeMode }>;
      if (customEvent.detail?.theme) {
        setCurrentThemeState(customEvent.detail.theme);
      }
    };
    window.addEventListener('ds_theme_change', handleThemeChange);
    return () => window.removeEventListener('ds_theme_change', handleThemeChange);
  }, []);

  const handleToggleTheme = () => {
    const nextTheme = themeService.toggleTheme();
    setCurrentThemeState(nextTheme);
  };

  const getBreadcrumb = () => {
    switch (currentScreen) {
      case 'home':
        return 'Dashboard / Exam Overview';
      case 'quiz':
        return 'Active Session / Timed Quiz';
      case 'results':
        return 'Evaluation / Score Report';
      case 'history':
        return 'Analytics / Past Attempts';
      default:
        return 'Dashboard';
    }
  };

  return (
    <GlassSurface
      as="header"
      variant="regular"
      shape="rounded"
      className={`inset-topbar ${className}`}
      aria-label="Topbar Header"
    >
      <div className="topbar__left">
        <span className="topbar__breadcrumb">
          {getBreadcrumb()}
          {subtitle && ` • ${subtitle}`}
        </span>
        <h1 className="topbar__title">{title}</h1>
      </div>

      <div className="topbar__right">
        {examInProgress ? (
          <>
            <Badge tone="warning" dot size="md">
              Exam in Progress
            </Badge>
            <Button
              variant="danger"
              size="sm"
              shape="pill"
              onClick={onQuitExam}
            >
              Quit Exam
            </Button>
          </>
        ) : (
          <Badge tone="indigo" size="md">
            520 Verified Qs
          </Badge>
        )}

        <IconButton
          aria-label={`Switch to ${theme === 'dark' ? 'light' : 'dark'} mode`}
          variant="glass"
          size="md"
          shape="circle"
          className="topbar__theme-toggle"
          onClick={handleToggleTheme}
          icon={theme === 'dark' ? <SunIcon size={18} /> : <MoonIcon size={18} />}
        />
      </div>
    </GlassSurface>
  );
};
