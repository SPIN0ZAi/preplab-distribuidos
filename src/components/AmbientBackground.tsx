// src/components/AmbientBackground.tsx
import React from 'react';
import '../styles/ambient-background.css';

interface AmbientBackgroundProps {
  className?: string;
}

export const AmbientBackground: React.FC<AmbientBackgroundProps> = ({ className = '' }) => {
  return (
    <div
      className={`ambient-background ${className}`.trim()}
      aria-hidden="true"
      tabIndex={-1}
    >
      <div className="ambient-orb ambient-orb-1" />
      <div className="ambient-orb ambient-orb-2" />
      <div className="ambient-orb ambient-orb-3" />
    </div>
  );
};
