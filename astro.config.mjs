import { defineConfig } from "astro/config";

// The account serves Pages from a user-level custom domain, so canonical URLs
// resolve under dev.adityarajsingh.com rather than github.io. `base` is the
// repo path — drop it to "/" if this ever gets its own domain.
export default defineConfig({
  site: "https://dev.adityarajsingh.com",
  base: "/garuda-purana",
  outDir: "./dist",
});
