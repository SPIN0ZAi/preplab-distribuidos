// src/services/theme.ts
export type ThemeMode = 'light' | 'dark';

const THEME_STORAGE_KEY = 'ds_quiz_theme_preference';

export const themeService = {
  getTheme(): ThemeMode {
    try {
      const stored = localStorage.getItem(THEME_STORAGE_KEY);
      if (stored === 'light' || stored === 'dark') {
        return stored;
      }
      return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
    } catch {
      return 'light';
    }
  },

  setTheme(theme: ThemeMode): void {
    try {
      localStorage.setItem(THEME_STORAGE_KEY, theme);
      document.documentElement.setAttribute('data-theme', theme);
      window.dispatchEvent(new CustomEvent('ds_theme_change', { detail: { theme } }));
    } catch (e) {
      console.error('Failed to save theme to localStorage', e);
    }
  },

  toggleTheme(): ThemeMode {
    const current = this.getTheme();
    const next: ThemeMode = current === 'dark' ? 'light' : 'dark';
    this.setTheme(next);
    return next;
  },

  init(): void {
    const theme = this.getTheme();
    document.documentElement.setAttribute('data-theme', theme);

    // Listen for OS theme changes if user hasn't explicitly overridden
    try {
      window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', e => {
        if (!localStorage.getItem(THEME_STORAGE_KEY)) {
          this.setTheme(e.matches ? 'dark' : 'light');
        }
      });
    } catch {
      // matchMedia listener not supported in legacy environment
    }
  },
};
