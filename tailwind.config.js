/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./*.html",
    "./assets/js/main.js"
  ],
  theme: {
    extend: {
      backgroundImage: {
        // The fill-opacity has been changed from 0.1 to 0.3 to make the dots darker and more visible
        'hero-pattern': "url(\"data:image/svg+xml,%3Csvg width='20' height='20' viewBox='0 0 20 20' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='%2327272a' fill-opacity='0.3' fill-rule='evenodd'%3E%3Ccircle cx='3' cy='3' r='1'/%3E%3Ccircle cx='13' cy='13' r='1'/%3E%3C/g%3E%3C/svg%3E\")",
      }
    },
  },
  plugins: [
    require('@tailwindcss/typography'),
  ],
}

