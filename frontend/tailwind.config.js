/** @type {import('tailwindcss').Config} */
module.exports = {
    content: [
      "./src/**/*.{js,jsx,ts,tsx}", // Scan all source files for Tailwind classes
      "./public/index.html"
    ],
    theme: {
      extend: {
        colors: {
          primary: "#4F46E5",  // Indigo-600, adjust to your brand color
          secondary: "#3B82F6", // Blue-500
          accent: "#F59E0B",    // Amber-500
        },
        fontFamily: {
          sans: ["Inter", "ui-sans-serif", "system-ui"],
          serif: ["Georgia", "serif"],
          mono: ["Menlo", "monospace"],
        },
        spacing: {
          128: "32rem",
          144: "36rem",
        },
      },
    },
    plugins: [
      require('@tailwindcss/forms'),  // For better form styling
      require('@tailwindcss/typography'), // For prose styling
      require('@tailwindcss/aspect-ratio'), // For aspect ratios on images/videos
    ],
    darkMode: 'class',  // Enable class-based dark mode toggling
  }

  
  