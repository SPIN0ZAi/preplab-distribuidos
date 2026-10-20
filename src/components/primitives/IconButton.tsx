// src/components/primitives/IconButton.tsx
import React from 'react';
import '../../styles/primitives/button.css';
import { IconButtonProps } from '../../types/primitives';

export const IconButton: React.FC<IconButtonProps> = ({
  'aria-label': ariaLabel,
  variant = 'default',
  size = 'md',
  shape = 'circle',
  icon,
  as: Component = 'button',
  className = '',
  disabled,
  ...restProps
}) => {
  const variantClass = variant === 'primary' ? 'btn--primary' : variant === 'glass' ? 'btn--glass' : 'btn--secondary';
  const classes = [
    'btn',
    'btn--icon',
    `btn--circle`,
    `btn--${size}`,
    variantClass,
    className,
  ]
    .filter(Boolean)
    .join(' ');

  const isButtonElement = Component === 'button';

  return (
    <Component
      className={classes}
      aria-label={ariaLabel}
      disabled={isButtonElement ? disabled : undefined}
      {...restProps}
    >
      {icon}
    </Component>
  );
};
