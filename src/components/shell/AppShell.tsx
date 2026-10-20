// src/components/shell/AppShell.tsx
import React from 'react';
import '../../styles/shell/app-shell.css';
import { AppShellProps } from '../../types/shell';
import { InsetSidebar } from './InsetSidebar';
import { InsetTopbar } from './InsetTopbar';
import { MobileNavPill } from './MobileNavPill';

export const AppShell: React.FC<AppShellProps> = ({
  currentScreen,
  onNavigate,
  examInProgress = false,
  onQuitExam,
  title = 'Distributed Systems Exam Prep',
  subtitle = 'Lab 1 & Lab 2 Exam Simulator',
  activeLab = 'all',
  onSelectLab,
  onOpenHistory,
  children,
}) => {
  return (
    <div className="app-shell">
      <div className="app-shell__container">
        {/* Desktop / Tablet Floating Inset Sidebar */}
        <InsetSidebar
          currentScreen={currentScreen}
          onNavigate={onNavigate}
          examInProgress={examInProgress}
          onQuitExam={onQuitExam}
          activeLab={activeLab}
          onSelectLab={onSelectLab}
        />

        {/* Main Content Area */}
        <div className="app-shell__main">
          <InsetTopbar
            currentScreen={currentScreen}
            onNavigate={onNavigate}
            title={title}
            subtitle={subtitle}
            examInProgress={examInProgress}
            onQuitExam={onQuitExam}
          />

          <main className="app-shell__content" id="main-content">
            {children}
          </main>
        </div>
      </div>

      {/* Mobile Floating Bottom Nav Pill */}
      <MobileNavPill
        currentScreen={currentScreen}
        onNavigate={onNavigate}
        examInProgress={examInProgress}
        onOpenHistory={onOpenHistory}
      />
    </div>
  );
};
