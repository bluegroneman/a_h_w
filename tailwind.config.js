/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './src/templates/**/*.html',
    './home/templates/**/*.html',
    './search/templates/**/*.html',
  ],
  theme: {
    extend: {
      colors: {
        'primary': '#9b7bb5',
        'primary-dark': '#7a5f91',
        't-black': "#333333",
				't-orange': "#feb358",
				't-blue': "#3c78e0",
				't-teal': "#50bec1",
      },
    },
  },
	plugins: [require("@tailwindcss/forms"), require("@tailwindcss/typography"), require("@tailwindcss/aspect-ratio")],
}
require
