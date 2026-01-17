import type { Config } from "tailwindcss";

const config: Config = {
  content: [
    "./src/pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/components/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      colors: {
        background: "#09090b",
        foreground: "#fafafa",
        primary: {
          DEFAULT: "#8b5cf6",
          foreground: "#ffffff",
        },
        card: {
          DEFAULT: "#18181b",
          border: "#27272a"
        }
      },
    },
  },
  plugins: [],
};
export default config;