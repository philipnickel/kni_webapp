/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html",
    "./apps/**/*.py",
    "./apps/**/*.html",
  ],
  theme: {
    extend: {
      colors: {
        // Wood construction business palette - warm, natural, craftsmanship
        'wood': {
          50: '#fdfcf8',   // Lightest cream
          100: '#f8f4ed',  // Pale wood
          200: '#f1e8d6',  // Light natural
          300: '#e7d4b8',  // Warm beige
          400: '#d4b896',  // Natural wood tone
          500: '#b8956f',  // Rich wood
          600: '#9d7a54',  // Medium brown
          700: '#826343',  // Dark wood
          800: '#654e33',  // Deep brown
          900: '#4a3626',  // Dark walnut
        },
        'craft': {
          50: '#faf9f7',   // Off-white
          100: '#f3f0eb',  // Warm white
          200: '#e9e3d9',  // Light tan
          300: '#dbc9b8',  // Soft brown
          400: '#c8a882',  // Warm tan
          500: '#a67c52',  // Craftsman brown
          600: '#8b5a3c',  // Rich brown
          700: '#6f4530',  // Deep craft
          800: '#583528',  // Dark chocolate
          900: '#3d251b',  // Espresso
        },
        'forest': {
          50: '#f6f8f4',   // Lightest sage
          100: '#ecf2e8',  // Pale green
          200: '#d8e6d1',  // Light sage
          300: '#b8d0a8',  // Soft green
          400: '#8fb577',  // Natural green
          500: '#6b9654',  // Forest green
          600: '#4d7a3a',  // Deep sage
          700: '#3a5e2c',  // Dark forest
          800: '#2d4722',  // Deep wood green
          900: '#1f321a',  // Darkest green
        }
      },
      fontFamily: {
        'sans': ['system-ui', '-apple-system', 'BlinkMacSystemFont', 'Segoe UI', 'Roboto', 'Helvetica Neue', 'Arial', 'sans-serif'],
        'display': ['Georgia', 'Cambria', 'Times New Roman', 'serif'],
        'craft': ['Georgia', 'Cambria', 'serif'], // For headings - more traditional, trustworthy
      },
      spacing: {
        '18': '4.5rem',
        '88': '22rem',
      },
      boxShadow: {
        'construction': '0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05)',
        'construction-lg': '0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04)',
      }
    },
  },
  plugins: [
    require('@tailwindcss/forms'),
    require('@tailwindcss/typography'),
  ],
}