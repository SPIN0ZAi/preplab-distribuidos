// specs/001-design-tokens-and-theme/contracts/theme-tokens.ts

export type ThemeMode = 'light' | 'dark';

export interface VenusTokens {
  bgCanvas: string;
  cardBg: string;
  cardBgSubtle: string;
  cardBorder: string;

  primaryIndigo: string;
  primaryHover: string;
  primaryLight: string;
  secondaryPurple: string;
  accentCoral: string;
  gradientBrand: string;

  textHeadline: string;
  textBody: string;
  textMuted: string;
  textDisabled: string;

  success: string;
  successBg: string;
  danger: string;
  dangerBg: string;
  warning: string;
  warningBg: string;

  chartBarInactive: string;
  chartBarActive: string;

  shadowCard: string;
  shadowHover: string;
  shadowGlow: string;
}

export interface GlassTokens {
  blurThin: string;
  blurRegular: string;
  blurThick: string;
  blurMobile: string;

  saturate: string;

  fillThin: string;
  fillRegular: string;
  fillThick: string;

  border: string;
  edgeHighlight: string;
  edgeShade: string;
  sheen: string;

  shadow: string;
  shadowFloating: string;

  text: string;
  textMuted: string;

  fallbackFill: string;
  fallbackBorder: string;
}

export interface ThemeContract {
  theme: ThemeMode;
  venus: VenusTokens;
  glass: GlassTokens;
}
