// src/components/primitives/TextInput.tsx
import React from 'react';
import '../../styles/primitives/text-input.css';
import { TextInputProps } from '../../types/primitives';
import { CloseIcon } from './Icons';

export const TextInput: React.FC<TextInputProps> = ({
  value,
  onChange,
  icon,
  onClear,
  error,
  placeholder,
  className = '',
  disabled,
  ...restProps
}) => {
  return (
    <div className="text-input-container">
      <div
        className={`text-input-wrapper ${error ? 'text-input-wrapper--error' : ''} ${className}`}
      >
        {icon && <span className="text-input__icon">{icon}</span>}
        <input
          type="text"
          value={value}
          onChange={(e) => onChange(e.target.value)}
          placeholder={placeholder}
          disabled={disabled}
          className="text-input__field"
          {...restProps}
        />
        {value && onClear && !disabled && (
          <button
            type="button"
            className="text-input__clear-btn"
            onClick={onClear}
            aria-label="Clear input"
          >
            <CloseIcon size={14} />
          </button>
        )}
      </div>
      {error && <p className="text-input__error-msg">{error}</p>}
    </div>
  );
};
