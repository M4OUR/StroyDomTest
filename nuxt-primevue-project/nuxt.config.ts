export default defineNuxtConfig({
  css: [
    'primevue/resources/themes/saga-blue/theme.css',
    'primevue/resources/primevue.min.css',
    'primeicons/primeicons.css'
  ],

  build: {
    transpile: ['primevue']
  },

  compatibilityDate: '2025-01-18'
})