/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html",
    "./apps/**/*.html",
    "./static/**/*.js",
    "./node_modules/flowbite/**/*.js"
  ],
  safelist: [
    'lg:hidden',
    'hidden',
    'lg:flex',
    'flex'
  ],
  theme: {
    extend: {
      fontFamily: {
        'craft': ['Playfair Display', 'serif'],
        'body': ['Inter', 'sans-serif'],
      },
      colors: {
        // Carpenter theme colors
        carpenter: {
          50: '#faf5f0',
          100: '#f3e8d9',
          200: '#e6ceb0',
          300: '#d6ad7d',
          400: '#c28a4f',
          500: '#b56f34',
          600: '#a25a28',
          700: '#864724',
          800: '#6d3a23',
          900: '#58301e',
          950: '#2f180e',
        },
        primary: {
          50: '#eff6ff',
          100: '#dbeafe',
          200: '#bfdbfe',
          300: '#93c5fd',
          400: '#60a5fa',
          500: '#3b82f6',
          600: '#2563eb',
          700: '#1d4ed8',
          800: '#1e40af',
          900: '#1e3a8a',
          950: '#172554',
        }
      },
    },
  },
  plugins: [
    require('flowbite/plugin'),
    require('@tailwindcss/typography'),
  ],
}
