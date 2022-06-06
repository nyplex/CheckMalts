module.exports = {
  content: ['./**/templates/**/*.{html,js}', './node_modules/flowbite/**/*.js'],
  theme: {
    extend: {
      fontFamily: {
        barlow: ['Barlow', 'sans-serif'],
      },
      colors: {
        secondaryColor: '#E3A008',
        secondaryHoverDarker: '#C27803',
        secondaryHoverLighter: '#FACA15',
        primaryColor: '#fff',
        contrastColor: '#000',
      }
    },
    screens: {
      'xxs': '340px',
      'mobile': '450px',
      'sm': '640px',
      'md': '768px',
      'lg': '1024px',
      'xl': '1280px',
      '2xl': '1536px',
    }
  },
  plugins: [
    require('flowbite/plugin')
  ],
  darkMode: 'media',
}
