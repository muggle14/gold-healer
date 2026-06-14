# The Cosmic Alchemy — by Garima

A single-page website for **The Cosmic Alchemy**, a solo spiritual practice offering
**Dragon Healing**, Reiki, Akashic Records, Automatic Writing, Tarot, Astrology,
Numerology, Violet Flame & Inner Child Healing, Personalized Healing, Candle Magic,
Vaastu Aroma Therapy, plus **Pendulum** and **Lecher Antenna** readings.

Built as a static HTML/CSS/JS site, no build step, deployable to GitHub Pages.

**Design:** light "soft-gold / ivory / oak-yellow" palette with dark-copper metallic
headings, elegant serif (Cormorant Garamond) + clean sans (Inter), and line-art icon
service cards inspired by the Dragon Healing reference artwork.

---

## Repository layout

```
.
├── index.html              ← all markup + inline CSS/JS, the entire site
├── privacy.html            ← Privacy Policy (light-luxe styled)
├── terms.html              ← Terms & Conditions (light-luxe styled)
├── 404.html                ← styled fallback for GitHub Pages
├── robots.txt              ← search-engine directives
├── sitemap.xml             ← lists the in-page sections
├── .nojekyll               ← tells GitHub Pages to skip Jekyll
├── assets_gold_v2/         ← legacy offering illustrations (kept, no longer referenced)
├── banners_gold/           ← legacy banners + OG share image
└── branding/               ← logo and portrait of Garima (used in hero/about)
```

> **Note:** the service cards now use inline line-art icons (via [Lucide](https://lucide.dev)),
> so the heavy PNGs in `assets_gold_v2/` are no longer loaded by the page — a large
> page-speed win. They're retained in the repo in case you want to switch back to
> photographic cards.

## Page sections (journey)

`Hero → Quick actions → Pillars → About → Services → Tools & Readings → Why Choose Us → Feedback → Booking → FAQ → Contact → Footer`

Anchors: `#home`, `#about`, `#services`, `#tools`, `#why`, `#feedback`, `#book`, `#faq`, `#contact`.

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

1. Push to GitHub.
2. Repository **Settings → Pages**:
   - **Source:** *Deploy from a branch*
   - **Branch:** `main` (or `redesign/dark-luxe` while reviewing)
   - **Folder:** `/ (root)`
3. Save. After ~1 minute the site is live at
   <https://muggle14.github.io/gold-healer/>.

> ⚠️ GitHub Pages on a *private* repository requires a paid plan. On the Free plan,
> switch the repo to **Public** or Pages will fail to build.

### Custom domain (e.g. `thecosmicalchemy.com`)

1. Add a `CNAME` file at the repo root containing only the domain.
2. At your DNS registrar: a `CNAME` from `www` → `muggle14.github.io`, plus four A
   records for the apex pointing at GitHub's IPs
   (185.199.108.153, .109.153, .110.153, .111.153).
3. In **Settings → Pages**, set the custom domain and tick **Enforce HTTPS**.
4. Update the canonical/OG URLs in `index.html` and the URLs in `sitemap.xml`,
   `robots.txt`, `privacy.html`, `terms.html`, and the JSON-LD schema block.

---

## What to update when content changes

All copy lives inside `index.html`. Use *Find* in your editor.

| What                       | Search for / find in                                   | Notes |
| -------------------------- | ------------------------------------------------------ | ----- |
| **Contact email**          | `thecosmicalchemy1111@gmail.com`                       | Appears in head schema, hero, quickbar, services CTA, booking, FAQ, contact, footer, sticky bar, JS handler, privacy/terms. |
| **Instagram link**         | `instagram.com/thecosmicalchemy_garima`               | Profile URL used for every "Contact on Instagram" / feedback CTA and the footer icon. |
| **Booking link**           | `mailto:thecosmicalchemy1111@gmail.com?subject=Booking` | Currently a pre-filled `mailto:`. Replace with a Calendly / Cal.com / TidyCal URL when ready. |
| **Service cards**          | `class="svc-card"`                                     | Each modality. Icon is `data-lucide="…"`; copy is in `<h4>` + `<p>`. |
| **Tools / readings**       | `class="tool-card"`                                    | Pendulum Reading and Lecher Antenna Reading. |
| **Feedback / testimonials**| `class="t-card"`                                       | Three placeholder cards — replace quotes, names, and the service tag with real Instagram feedback. |
| **Why Choose Us**          | `class="why-card"`                                     | Trust pillars (Calm & Safe, Intuitive, Personalised, Confidential). |
| **FAQs**                   | `class="faq-item"`                                     | Add / remove items; mirror changes in the FAQ JSON-LD block in `<head>`. |
| **SEO description/keywords** | `<meta name="description">` / `<meta name="keywords">` | In `<head>`. |
| **JSON-LD schema**         | `application/ld+json`                                  | `ProfessionalService` + `FAQPage`; keep `serviceType`, `email`, and `sameAs` in sync. |
| **Site URL (canonical/OG)**| `https://muggle14.github.io/gold-healer/`             | Rewrite to your custom domain after DNS is live. |
| **Footer year**            | `&copy; 2026`                                          | Update annually. |
| **Favicon / logo**         | `branding/brand_v3.png`                                | Swap the PNG to change the icon site-wide. |

---

## What changed in this redesign

- **New light-luxe palette** — ivory / soft-gold / oak-yellow background, dark-copper
  metallic headings, copper/gold gradient buttons. (Replaced the previous dark theme.)
- **Line-art icon service cards** (Lucide) replacing ~3 MB photographic PNGs — much
  faster load.
- **Content:** removed *Quantum Healing*; added **Dragon Healing** (Energy Healing);
  added a **Tools & Readings** section with **Pendulum Reading** and **Lecher Antenna
  Reading**.
- **Contact:** email is now `thecosmicalchemy1111@gmail.com`; Instagram links point to
  the provided post URL.
- **Conversion:** "Book a Session", "Contact on Instagram", and "Email Me" CTAs in the
  hero, quick bar, services, booking, footer, and a sticky mobile CTA bar.
- **New sections:** "Why Choose Us" trust pillars and an Instagram-sourced Feedback
  section.
- **SEO:** rewritten title/description/keywords (Dragon/Reiki/Angel/Crystal/Sound +
  Pendulum/Lecher + spiritual/energy/intuitive healing), `FAQPage` schema added,
  updated `ProfessionalService` schema, refreshed `sitemap.xml`, light `theme-color`.
- **Legal:** added `privacy.html` and `terms.html` (previously broken footer links).

---

## Known follow-ups (need real data)

- [ ] Booking link — Calendly / Cal.com / TidyCal URL (currently `mailto:`).
- [ ] Real testimonials — replace the three placeholders with consented Instagram quotes/screenshots.
- [ ] Pricing — published per offering or as an "investment" sheet.
- [ ] Payment method — UPI handle / bank details to share at booking confirmation.
- [x] Instagram link — set to the profile `https://www.instagram.com/thecosmicalchemy_garima/`.
- [ ] A dedicated 1200×630 Open-Graph share image (currently reuses a banner crop).
- [ ] Optional: artwork for Dragon / Angel / Crystal / Sound if you ever want photographic cards again.

---

## Credits

Design and original implementation by the upstream author at
[maand3silva/garima-website](https://github.com/maand3silva/garima-website).
Cleanup, accessibility, SEO, the light-luxe redesign, and packaging on this branch.
