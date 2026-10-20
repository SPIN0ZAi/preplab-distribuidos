// src/components/Timer.tsx
import React, { useEffect, useState } from 'react';

interface TimerProps {
  initialDurationSeconds: number | null;
  timeRemainingSeconds: number | null;
  timerStartedAtTimestamp: number | null;
  isPaused?: boolean;
  onTimeExpired: () => void;
  onTick?: (remaining: number) => void;
}

export const Timer: React.FC<TimerProps> = ({
  initialDurationSeconds,
  timeRemainingSeconds,
  timerStartedAtTimestamp,
  isPaused = false,
  onTimeExpired,
  onTick,
}) => {
  // If timer is disabled (null or 0)
  if (!initialDurationSeconds || initialDurationSeconds <= 0) {
    return (
      <div className="timer-badge" title="Temporizador desactivado">
        <span>⏱️</span>
        <span>Sin límite</span>
      </div>
    );
  }

  const [currentRemaining, setCurrentRemaining] = useState<number>(() => {
    if (timerStartedAtTimestamp && initialDurationSeconds) {
      const elapsed = Math.floor((Date.now() - timerStartedAtTimestamp) / 1000);
      return Math.max(0, initialDurationSeconds - elapsed);
    }
    return timeRemainingSeconds ?? initialDurationSeconds;
  });

  useEffect(() => {
    if (isPaused || currentRemaining <= 0) return;

    const interval = setInterval(() => {
      let remaining = currentRemaining;
      if (timerStartedAtTimestamp && initialDurationSeconds) {
        const elapsed = Math.floor((Date.now() - timerStartedAtTimestamp) / 1000);
        remaining = Math.max(0, initialDurationSeconds - elapsed);
      } else {
        remaining = Math.max(0, currentRemaining - 1);
      }

      setCurrentRemaining(remaining);
      if (onTick) onTick(remaining);

      if (remaining <= 0) {
        clearInterval(interval);
        onTimeExpired();
      }
    }, 1000);

    return () => clearInterval(interval);
  }, [currentRemaining, isPaused, timerStartedAtTimestamp, initialDurationSeconds, onTimeExpired, onTick]);

  const minutes = Math.floor(currentRemaining / 60);
  const seconds = currentRemaining % 60;
  const formatted = `${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;
  const isWarning = currentRemaining <= 60 && currentRemaining > 0;

  return (
    <div
      className={`timer-badge ${isWarning ? 'warning' : ''}`}
      title={isWarning ? '¡Menos de 1 minuto restante!' : 'Tiempo restante'}
    >
      <span>⏱️</span>
      <span>{formatted}</span>
    </div>
  );
};
