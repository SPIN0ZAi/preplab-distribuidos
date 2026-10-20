// src/components/primitives/ModalSheet.tsx
import React, { useEffect, useRef } from 'react';
import '../../styles/primitives/modal-sheet.css';
import { ModalSheetProps } from '../../types/modal';
import { IconButton } from './IconButton';
import { CloseIcon } from './Icons';

export const ModalSheet: React.FC<ModalSheetProps> = ({
  isOpen,
  onClose,
  title,
  subtitle,
  children,
  footer,
  maxWidth,
  className = '',
  'aria-label': ariaLabel,
}) => {
  const sheetRef = useRef<HTMLDivElement>(null);

  // Keyboard dismiss (Escape) & body scroll lock
  useEffect(() => {
    if (!isOpen) return;

    const originalOverflow = document.body.style.overflow;
    document.body.style.overflow = 'hidden';

    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.key === 'Escape') {
        e.preventDefault();
        onClose();
      }
    };

    window.addEventListener('keydown', handleKeyDown);

    return () => {
      document.body.style.overflow = originalOverflow;
      window.removeEventListener('keydown', handleKeyDown);
    };
  }, [isOpen, onClose]);

  if (!isOpen) return null;

  return (
    <div
      className="modal-backdrop"
      onClick={onClose}
      role="dialog"
      aria-modal="true"
      aria-label={ariaLabel || (typeof title === 'string' ? title : 'Modal Dialog')}
    >
      <div
        ref={sheetRef}
        className={`modal-sheet ${className}`}
        style={maxWidth ? { maxWidth } : undefined}
        onClick={(e) => e.stopPropagation()}
      >
        {/* Header */}
        <div className="modal-sheet__header">
          <div className="modal-sheet__titles">
            {typeof title === 'string' ? (
              <h2 className="modal-sheet__title">{title}</h2>
            ) : (
              title
            )}
            {subtitle && (
              typeof subtitle === 'string' ? (
                <p className="modal-sheet__subtitle">{subtitle}</p>
              ) : (
                subtitle
              )
            )}
          </div>

          <IconButton
            aria-label="Cerrar modal"
            variant="default"
            size="sm"
            shape="circle"
            onClick={onClose}
            icon={<CloseIcon size={16} />}
          />
        </div>

        {/* Body Content */}
        <div className="modal-sheet__body">
          {children}
        </div>

        {/* Optional Footer */}
        {footer && (
          <div className="modal-sheet__footer">
            {footer}
          </div>
        )}
      </div>
    </div>
  );
};
