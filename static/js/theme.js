// Admin-controlled theme system - no public theme switching
(function(){
  const THEMES = {
    forest: {
      '--color-primary': '#4d7a3a',
      '--color-primary-hover': '#3a5e2c',
      '--color-surface': '#ffffff',
      '--color-surface-soft': '#f6f8f4',
      '--color-surface-contrast': '#1f321a',
      '--color-text': '#1f2937',
      '--color-text-muted': '#6b7280',
      '--color-border': '#e5e7eb',
      '--color-footer-bg': '#3d251b',
      '--color-footer-text': '#e9e3d9',
      '--color-inverse': '#ffffff',
      '--color-inverse-muted': 'rgba(255,255,255,0.8)',
      '--color-hero-start': '#3a5e2c',
      '--color-hero-end': '#654e33',
      '--color-hero-overlay': 'rgba(0,0,0,0.45)'
    },
    wood: {
      '--color-primary': '#a67c52',
      '--color-primary-hover': '#8b5a3c',
      '--color-surface': '#ffffff',
      '--color-surface-soft': '#faf9f7',
      '--color-surface-contrast': '#3d251b',
      '--color-text': '#1f2937',
      '--color-text-muted': '#6b7280',
      '--color-border': '#e9e3d9',
      '--color-footer-bg': '#3d251b',
      '--color-footer-text': '#e9e3d9',
      '--color-inverse': '#ffffff',
      '--color-inverse-muted': 'rgba(255,255,255,0.85)',
      '--color-hero-start': '#6f4530',
      '--color-hero-end': '#654e33',
      '--color-hero-overlay': 'rgba(0,0,0,0.45)'
    },
    slate: {
      '--color-primary': '#475569',
      '--color-primary-hover': '#334155',
      '--color-surface': '#ffffff',
      '--color-surface-soft': '#f1f5f9',
      '--color-surface-contrast': '#0f172a',
      '--color-text': '#0f172a',
      '--color-text-muted': '#475569',
      '--color-border': '#e2e8f0',
      '--color-footer-bg': '#0f172a',
      '--color-footer-text': '#e2e8f0',
      '--color-inverse': '#e2e8f0',
      '--color-inverse-muted': 'rgba(226,232,240,0.8)',
      '--color-hero-start': '#1e293b',
      '--color-hero-end': '#334155',
      '--color-hero-overlay': 'rgba(0,0,0,0.35)'
    }
  };

  function applyTheme(name){
    const theme = THEMES[name];
    if (!theme) return;
    const root = document.documentElement;
    Object.entries(theme).forEach(([k,v]) => root.style.setProperty(k, v));
    root.setAttribute('data-theme', name);
  }

  // Apply server-defined theme only (no user override)
  const serverTheme = window.PREFERRED_THEME_OVERRIDE || window.PREFERRED_THEME_DEFAULT || 'forest';
  applyTheme(serverTheme);
})();
