// src/components/primitives/Button.tsx
import React from 'react';
import '../../styles/primitives/button.css';
import { ButtonProps } from '../../types/primitives';
import { SpinnerIcon } from './Icons';

export const Button: React.FC<ButtonProps> = ({
  variant = 'primary',
  size = 'md',
  shape = 'rounded',
  isLoading = false,
  leftIcon,
  rightIcon,
  as: Component = 'button',
  className = '',
  children,
  disabled,
  ...restProps
}) => {
  const classes = [
    'btn',
    `btn--${variant}`,
    `btn--${size}`,
    `btn--${shape}`,
    isLoading ? 'btn--loading' : '',
    className,
  ]
    .filter(Boolean)
    .join(' ');

  const isButtonElement = Component === 'button';

  return (
    <Component
      className={classes}
      disabled={isButtonElement ? (disabled || isLoading) : undefined}
      aria-busy={isLoading ? 'true' : undefined}
      {...restProps}
    >
      {isLoading ? (
        <>
          <SpinnerIcon size={size === 'sm' ? 14 : size === 'lg' ? 20 : 16} />
          <span>{children}</span>
        </>
      ) : (
        <>
          {leftIcon && <span className="btn__icon-left">{leftIcon}</span>}
          {children && <span>{children}</span>}
          {rightIcon && <span className="btn__icon-right">{rightIcon}</span>}
        </>
      )}
    </Component>
  );
};
