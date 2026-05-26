# The Cosmic Alchemy — by Garima Sharma

A single-page website for **The Cosmic Alchemy**, a solo spiritual practice offering
Akashic Records readings, Automatic Writing, Tarot, Astrology, Numerology, Reiki,
Quantum Healing, Violet Flame Healing, Candle Magic, Inner Child Healing and
Vaastu Aroma Therapy.

Built as a static HTML/CSS/JS site, no build step, deployable to GitHub Pages.

---

## Repository layout

```
.
├── index.html              ← all markup + inline CSS/JS, the entire site
├── 404.html                ← styled fallback for GitHub Pages
├── robots.txt              ← search-engine directives
├── sitemap.xml             ← lists the in-app sections
├── .nojekyll               ← tells GitHub Pages to skip Jekyll
├── assets_gold_v2/         ← offering-card illustrations
├── banners_gold/           ← hero, page-header, CTA banners
└── branding/               ← logo and portrait of Garima
```

## Branches

| Branch  | Purpose                                                                |
| ------- | ---------------------------------------------------------------------- |
| `master`| **Pristine base** — exact clone of the upstream source, untouched.     |
| `main`  | **Active site** — cleanup, SEO, accessibility, schema, README, 404 etc.|

If you need to compare against the original or roll back a regression, `master`
is the safety net.

---

## Run locally

The site is plain static HTML. Any static server will do:

```bash
# Python (no install needed on macOS)
python3 -m http.server 8000

# or Node
npx serve .

# or just open the file
open index.html
```

Then visit <http://localhost:8000>.

---

## Deploy via GitHub Pages

1. Push to GitHub (already done for branches `master` and `main`).
2. Repository **Settings → Pages**:
   - **Source:** *Deploy from a branch*
   - **Branch:** `main`
   - **Folder:** `/ (root)`
3. Save. After ~1 minute the site is live at
   <https://muggle14.github.io/gold-healer/>.

> ⚠️ **Important — repo visibility.** GitHub Pages on a *private* repository
> requires a paid plan (Pro / Team / Enterprise). On the Free plan, switch the
> repo to **Public** (Settings → General → Danger Zone → Change visibility) or
> Pages will fail to build.

### Custom domain (e.g. `thecosmicalchemy.com`)

1. Add a file named `CNAME` at the repo root containing only the domain:
   ```
   www.thecosmicalchemy.com
   ```
2. At your DNS registrar, create:
   - A CNAME record from `www` → `muggle14.github.io`
   - Four A records for the apex pointing at GitHub's IPs (185.199.108.153, 185.199.109.153, 185.199.110.153, 185.199.111.153)
3. In **Settings → Pages**, fill in the custom domain and tick **Enforce HTTPS**.
4. Also update the canonical/OG URLs inside `index.html` and the URLs in
   `sitemap.xml`, `robots.txt`, and the JSON-LD schema block.

---

## What to update when content changes

All copy lives inside `index.html`. Use *Find* in your editor to jump to each item.

| What                          | Search for / find in                                                    | Notes                                                                                            |
| ----------------------------- | ----------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| **Booking link**              | `id="primaryBookingCta"`                                                | Currently a `mailto:`. Replace `href` with a Calendly / Cal.com / TidyCal URL when ready.        |
| **Contact email**             | `hello@thecosmicalchemy.com`                                            | Appears in 8 places: head schema, footer, contact section, FAQ, booking CTA, JS form handler.    |
| **Social links**              | `class="foot-social"`                                                   | Update Instagram / Facebook / YouTube / WhatsApp URLs in the footer.                             |
| **WhatsApp number**           | `https://wa.me/`                                                        | Append the international number (e.g. `https://wa.me/919876543210`).                             |
| **Testimonials (home)**       | `<blockquote>"Garima holds such a powerful…`                            | Replace the home-page quote and `<cite>` attribution.                                            |
| **Testimonials (page)**       | `class="testi-grid"`                                                    | Three `<div class="t-card">` blocks — edit quote and `who`.                                       |
| **Offering names / blurbs**   | `class="off-card"` (home carousel) and `class="off-service"` (detail)   | Each modality has both a card on the home page and a long-form entry on the Offerings page.      |
| **Duration / pricing**        | `class="duration"`                                                      | Inside each `.off-service` block.                                                                |
| **FAQs**                      | `class="faq-wrap"`                                                      | Add / remove `<div class="faq-item">` blocks.                                                    |
| **Booking page note**         | `class="book-note"`                                                     | The italic paragraph below the booking button.                                                   |
| **About / Story copy**        | `<div class="page" id="about">`                                         | About page content.                                                                              |
| **SEO description / keywords**| `<meta name="description">` / `<meta name="keywords">`                  | In `<head>`.                                                                                     |
| **OG preview image**          | `<meta property="og:image">`                                            | Defaults to `banners_gold/sun_banner_peacock.png`. Use a 1200×630 image for best results.        |
| **Site URL (canonical, OG)**  | `https://muggle14.github.io/gold-healer/`                               | Rewrite to your custom domain after DNS is live.                                                 |
| **Footer year**               | `&copy; 2026`                                                           | Update annually.                                                                                 |
| **Favicon / logo**            | `branding/brand_v3.png`                                                 | Swap the PNG in `branding/` to change the icon site-wide.                                        |

### How to swap the booking CTA for Calendly

In `index.html`, find:

```html
<a class="btn-gold" id="primaryBookingCta" href="mailto:hello@thecosmicalchemy.com?...">Book a Session +</a>
```

Replace `href="mailto:…"` with your Calendly URL:

```html
<a class="btn-gold" id="primaryBookingCta" href="https://calendly.com/thecosmicalchemy/intro" target="_blank" rel="noopener">Book a Session +</a>
```

You may also want to update the four secondary `Book a Session +` buttons in
the hero, about, philosophy, and testimonials sections, plus all `Book Session →`
links inside each offering card. Search for `showPage('book')` to find them.

---

## What was changed in `main` (vs. `master`)

- Added full `<head>` SEO suite: `<title>`, `description`, `keywords`, `canonical`, `robots`, `theme-color`, Open Graph, Twitter cards, favicons, Google Fonts preconnect.
- Added JSON-LD `ProfessionalService` schema with services and contact point.
- Fixed `WhatsAp` → `WhatsApp` typo on the booking page.
- Removed the `Replace the Calendly URL above…` developer placeholder.
- Filled in the `Answer TBD.` FAQ ("How do I reschedule?") and added a safety-disclaimer FAQ.
- Standardised all CTAs to `Book a Session +`.
- Replaced footer `href="#"` social and policy links with real URLs (placeholder Instagram / FB / YT / WhatsApp and `privacy.html` / `terms.html` targets — create those pages when ready).
- Converted the contact form's fake `<a>` "Send Message" into a real `<form>` with validation that opens a pre-filled `mailto:`.
- Newsletter form now shows an inline polite message instead of silently doing nothing.
- Promoted the wrapping `<div class="nav">` to a `<nav>` element; mobile burger menu is a real `<button>` with `aria-expanded` / `aria-controls`.
- Added `aria-expanded` toggling for every FAQ accordion, `aria-label` for all icon-only buttons (carousel arrows, mobile toggle, social icons, slider dots), and `aria-current="page"` on the active nav link.
- Added visible focus rings (`:focus-visible`) and an `.sr-only` utility class.
- Added `loading="lazy"`, `decoding="async"`, and `width`/`height` to all 22 below-fold images.
- Closed the previously unclosed `.carousel-track` / `.carousel-outer` wrappers.
- Hash-routing: visiting `/#about` etc. opens the right section; browser back/forward now works.
- Added `404.html`, `robots.txt`, `sitemap.xml`, `.nojekyll`.

The visual identity — palette, typography, banners, ornaments — is unchanged.

---

## Known follow-ups (need real data)

- [ ] Booking link — Calendly / Cal.com / TidyCal URL (currently `mailto:`).
- [ ] Real testimonials with names and first-line consent.
- [ ] Pricing — published either per offering, or as an "investment" sheet.
- [ ] Payment method — UPI handle / bank details / wire instructions to share at booking confirmation.
- [ ] Privacy Policy and Terms & Conditions pages (`privacy.html`, `terms.html`).
- [ ] Real Instagram / Facebook / YouTube / WhatsApp URLs.
- [ ] A 1200 × 630 Open-Graph image (a dedicated share card looks cleaner than a banner crop).
- [ ] Optional: Google Business Profile + link from the JSON-LD `sameAs` array.

---

## Credits

Design and original implementation by the upstream author at
[maand3silva/garima-website](https://github.com/maand3silva/garima-website).
Cleanup, accessibility, SEO and packaging on `main`.
