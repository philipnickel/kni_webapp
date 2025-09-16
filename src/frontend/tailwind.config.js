/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html",
    "./**/templates/**/*.html",
    "./**/*.py",
    "./static/**/*.js",
    "./static/src/**/*.js",
    "./node_modules/preline/dist/*.js"
  ],
  darkMode: "class",
  theme: {
    extend: {
      fontFamily: {
        'body': ['Inter', 'sans-serif'],
      },
      height: {
        '120': '30rem', // 480px - equivalent to h-120
      },
    },
  },
  plugins: [
    require('preline/plugin'),
    require('@tailwindcss/typography'),
    require('@tailwindcss/forms'),
  ],
}
