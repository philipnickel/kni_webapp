/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html",
    "./apps/**/*.html",
    "./static/**/*.js",
    "./node_modules/flowbite/**/*.js",
  ],
  safelist: [
    'lg:hidden',
    'hidden',
    'lg:flex',
    'flex'
  ],
  theme: {
    extend: {
      colors: {
        primary: {
          DEFAULT: '#8B5A2B',
          light: '#A0522D',
          dark: '#5C3317',
        },
        secondary: {
          DEFAULT: '#C2A878',
          light: '#D1B892',
          dark: '#A3835B',
        },
        accent: {
          DEFAULT: '#556B2F',
          light: '#6B8E23',
          dark: '#3A4B1E',
        },
      },
      fontFamily: {
        'craft': ['Playfair Display', 'serif'],
        'body': ['Inter', 'sans-serif'],
      },
    },
  },
  plugins: [
    require('flowbite/plugin'),
    require('@tailwindcss/typography'),
  ],
}
