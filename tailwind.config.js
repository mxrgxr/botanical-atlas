/** @type {import('tailwindcss').Config} */

module.exports = {
  content: ["./**/*.{html,js}"],
  theme: {
    colors: {
      'sage': '#a2bd84',
      'cool-blue': '#89b6cd',
      'dark-blue': '#243342',
      'forest-green': '#183227'
    },
    fontFamily: {
      'header': ['Roboto Slab', 'serif'],
      'body': ['Montserrat', 'sans-serif'],
    },
    extend: {},
  },
  plugins: [
    require('@tailwindcss/forms'),
    require('@tailwindcss/container-queries'),
  ],
};