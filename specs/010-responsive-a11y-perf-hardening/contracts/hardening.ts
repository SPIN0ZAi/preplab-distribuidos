/**
 * Unit U10: Hardening, Responsive & Accessibility Contract
 */

export interface AccessibilityAuditSummary {
  contrastTextOnGlassMin: number;
  contrastTextOnCardMin: number;
  touchTargetMinPx: number;
  focusRingOffsetPx: number;
  maxMobileBlurPx: number;
  forcedColorsSupported: boolean;
  reducedMotionSupported: boolean;
  reducedTransparencySupported: boolean;
}

export const HARDENING_DEFAULTS: AccessibilityAuditSummary = {
  contrastTextOnGlassMin: 4.5,
  contrastTextOnCardMin: 7.0,
  touchTargetMinPx: 44,
  focusRingOffsetPx: 2,
  maxMobileBlurPx: 12,
  forcedColorsSupported: true,
  reducedMotionSupported: true,
  reducedTransparencySupported: true,
};
