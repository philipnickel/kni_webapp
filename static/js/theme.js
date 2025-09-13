// DaisyUI Theme System
(function(){
  // Available themes (matching tailwind.config.js)
  const AVAILABLE_THEMES = [
    'light', 'corporate', 'business', 'emerald'
  ];

  function applyTheme(themeName) {
    const root = document.documentElement;
    
    // Validate theme name
    if (!AVAILABLE_THEMES.includes(themeName)) {
      console.warn(`Unknown theme: ${themeName}, falling back to light`);
      themeName = 'light';
    }
    
    // Apply theme by setting data-theme attribute
    root.setAttribute('data-theme', themeName);
    
    // Clear any stored user preferences to prevent override
    localStorage.removeItem('preferred-theme');
    
    // Dispatch custom event for theme change
    window.dispatchEvent(new CustomEvent('themechange', { 
      detail: { theme: themeName } 
    }));
  }

  function getSystemTheme() {
    if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
      return 'dark';
    }
    return 'light';
  }

  function initializeTheme() {
    // For business websites, server default takes priority
    const serverDefault = window.PREFERRED_THEME_DEFAULT;
    
    // Always use server default for business websites
    let themeToApply = serverDefault || getSystemTheme();
    
    applyTheme(themeToApply);
    
    console.log(`Theme applied: ${themeToApply} (server default: ${serverDefault})`);
  }

  // Listen for system theme changes
  if (window.matchMedia) {
    window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', (e) => {
      // Only apply system theme if no server default is set
      if (!window.PREFERRED_THEME_DEFAULT) {
        applyTheme(e.matches ? 'dark' : 'light');
      }
    });
  }

  // Initialize theme on page load
  initializeTheme();

  // Expose theme switching function globally
  window.switchTheme = applyTheme;
  window.getCurrentTheme = () => document.documentElement.getAttribute('data-theme');
  window.getAvailableThemes = () => [...AVAILABLE_THEMES];
})();