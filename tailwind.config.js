/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html",
    "./apps/**/*.html",
    "./static/**/*.js",
    "./node_modules/flowbite/**/*.js",
    "./node_modules/preline/**/*.js",
    "./node_modules/tw-elements/js/**/*.js"
  ],
  darkMode: "class",
  theme: {
    extend: {
      fontFamily: {
        'body': ['Inter', 'sans-serif'],
      },
    },
  },
  plugins: [
    require('flowbite/plugin'),
    require('preline/plugin'),
    require('tw-elements/plugin.cjs'),
    require('@tailwindcss/typography'),
    require('@tailwindcss/forms'),
  ],
}
