// src/components/primitives/SegmentedControl.tsx
import React, { useRef } from 'react';
import '../../styles/primitives/segmented-control.css';
import { SegmentedControlProps } from '../../types/primitives';

export function SegmentedControl<T extends string = string>({
  options,
  value,
  onChange,
  size = 'md',
  className = '',
  'aria-label': ariaLabel,
}: SegmentedControlProps<T>) {
  const containerRef = useRef<HTMLDivElement>(null);

  const handleKeyDown = (e: React.KeyboardEvent, index: number) => {
    let nextIndex = index;
    if (e.key === 'ArrowRight' || e.key === 'ArrowDown') {
      e.preventDefault();
      nextIndex = (index + 1) % options.length;
    } else if (e.key === 'ArrowLeft' || e.key === 'ArrowUp') {
      e.preventDefault();
      nextIndex = (index - 1 + options.length) % options.length;
    }

    if (nextIndex !== index && !options[nextIndex].disabled) {
      onChange(options[nextIndex].id);
      const buttons = containerRef.current?.querySelectorAll<HTMLButtonElement>('button');
      buttons?.[nextIndex]?.focus();
    }
  };

  return (
    <div
      ref={containerRef}
      className={`segmented-control segmented-control--${size} ${className}`}
      role="radiogroup"
      aria-label={ariaLabel}
    >
      {options.map((option, index) => {
        const isSelected = option.id === value;
        return (
          <button
            key={option.id}
            type="button"
            role="radio"
            aria-checked={isSelected}
            tabIndex={isSelected ? 0 : -1}
            disabled={option.disabled}
            className={`segmented-control__item ${isSelected ? 'segmented-control__item--active' : ''}`}
            onClick={() => !option.disabled && onChange(option.id)}
            onKeyDown={(e) => handleKeyDown(e, index)}
          >
            {option.icon && <span className="segmented-control__icon">{option.icon}</span>}
            <span>{option.label}</span>
            {option.badge !== undefined && (
              <span className="segmented-control__badge">{option.badge}</span>
            )}
          </button>
        );
      })}
    </div>
  );
}
