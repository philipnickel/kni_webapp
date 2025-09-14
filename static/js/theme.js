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
    
    // Store preference in localStorage
    localStorage.setItem('preferred-theme', themeName);
    
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
    // Priority order: server override > localStorage > server default > system preference
    const serverOverride = window.PREFERRED_THEME_OVERRIDE;
    const storedTheme = localStorage.getItem('preferred-theme');
    const serverDefault = window.PREFERRED_THEME_DEFAULT;
    
    let themeToApply = serverOverride || storedTheme || serverDefault || getSystemTheme();
    
    applyTheme(themeToApply);
  }

  // Listen for system theme changes
  if (window.matchMedia) {
    window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', (e) => {
      // Only apply system theme if no user preference is stored
      if (!localStorage.getItem('preferred-theme') && !window.PREFERRED_THEME_DEFAULT) {
        applyTheme(e.matches ? 'dark' : 'light');
      }
    });
  }

  // Initialize theme on page load
  initializeTheme();

  // Theme preview functionality
  let originalTheme = null;
  let previewTimeout = null;

  function previewTheme(themeName) {
    // Clear any existing timeout
    if (previewTimeout) {
      clearTimeout(previewTimeout);
    }
    
    // Store original theme if not already stored
    if (originalTheme === null) {
      originalTheme = document.documentElement.getAttribute('data-theme');
    }
    
    // Apply preview theme
    document.documentElement.setAttribute('data-theme', themeName);
    
    // Add preview indicator
    document.documentElement.classList.add('theme-preview');
  }

  function restoreTheme() {
    // Clear any existing timeout
    if (previewTimeout) {
      clearTimeout(previewTimeout);
    }
    
    // Add small delay to prevent flickering when moving between options
    previewTimeout = setTimeout(() => {
      if (originalTheme !== null) {
        document.documentElement.setAttribute('data-theme', originalTheme);
        document.documentElement.classList.remove('theme-preview');
        originalTheme = null;
      }
    }, 100);
  }

  // Expose theme switching function globally
  window.switchTheme = applyTheme;
  window.getCurrentTheme = () => document.documentElement.getAttribute('data-theme');
  window.getAvailableThemes = () => [...AVAILABLE_THEMES];
  window.previewTheme = previewTheme;
  window.restoreTheme = restoreTheme;
})();