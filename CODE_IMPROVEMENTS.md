## Quick Review Checklist — Silva Automation Landing

Done now
- **Shared layout:** Added `includes/header.html` and `includes/footer.html`; pages now load them via placeholders and the loader script.
- **Accessibility:** Added skip link, aria-expanded/aria-hidden updates on menu toggle buttons, deferred script loading.
- **Performance:** Lazy-loaded tab images with dimensions; deferred JS; fixed missing asset reference; removed redundant header file.
- **SEO/meta:** Added canonical + Open Graph + theme-color to index/contact/legal pages.
- **Fixes:** Valid `.vscode/launch.json`; added `assets/css/legal.css`; removed `Archive.zip` backup file.

Still recommended
1. **Optimize media:** Compress `assets/videos/hero.mp4` / `hero.webm` and large images or serve from a CDN.
2. **Structured data:** Add JSON-LD for local business/contact if desired.
3. **CSP & security:** Consider a Content Security Policy tailored to required origins (fonts.googleapis.com, calendly, etc.) and obfuscate email to reduce scraping.
4. **Testing/CI:** Add an automated HTML/Lighthouse check in CI to catch regressions.
5. **Cache headers:** Ensure hosting sets strong caching for static assets and cache-busting for updates.

If you want, I can tackle media compression, add JSON-LD, or wire up a lightweight CI (HTML validation + Lighthouse) next.
