/**
 * Unit U9: Interaction Polish & Motion Contract
 */

export interface MotionConfig {
  springEase: string;
  bounceEase: string;
  smoothEase: string;
  durationFast: number; // ms
  durationNormal: number; // ms
  durationDeliberate: number; // ms
}

export const DEFAULT_MOTION_CONFIG: MotionConfig = {
  springEase: 'cubic-bezier(0.16, 1, 0.3, 1)',
  bounceEase: 'cubic-bezier(0.34, 1.56, 0.64, 1)',
  smoothEase: 'cubic-bezier(0.4, 0, 0.2, 1)',
  durationFast: 140,
  durationNormal: 240,
  durationDeliberate: 420,
};

export type MotionPreset = 'spring' | 'bounce' | 'smooth' | 'instant';

export interface InteractiveElementMotion {
  hoverLift?: boolean;
  activePress?: boolean;
  celebrate?: boolean;
}
