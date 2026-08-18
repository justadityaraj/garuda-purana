import { defineConfig } from "astro/config";

// GitHub Pages serves at /<repo>/ — drop `base` to "/" when a custom domain lands.
export default defineConfig({
  site: "https://justadityaraj.github.io",
  base: "/garuda-purana",
  outDir: "./dist",
});
