/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,jsx,ts,tsx}",
  ],
  theme: {
    extend: {
      animation: {
        'fade-in': 'fadeIn 0.5s ease-out',
        'scale-up': 'scaleUp 0.6s ease-out',
        'pulse-slow': 'pulse 2s cubic-bezier(0.4, 0, 0.6, 1) infinite',
      },
      keyframes: {
        fadeIn: {
          '0%': { opacity: '0' },
          '100%': { opacity: '1' },
        },
        scaleUp: {
          '0%': { transform: 'scale(0.95)' },
          '100%': { transform: 'scale(1)' },
        },
      },
      boxShadow: {
        neon: '0 0 10px rgba(99, 102, 241, 0.7), 0 0 20px rgba(99, 102, 241, 0.4)',
      },
      textShadow: {
        DEFAULT: '0 0 5px rgba(255, 255, 255, 0.3)',
      },
    },
  },
  plugins: [],
};