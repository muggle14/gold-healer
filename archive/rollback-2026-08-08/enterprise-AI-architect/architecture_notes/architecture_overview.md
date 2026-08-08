# Architecture overview

## In plain English

The website is a digital brochure and booking doorway. Visitors learn about Garima,
review active offerings, build trust, and move to WhatsApp, telephone, email, or
Instagram to arrange a session.

## Technically

The Experience layer is a static HTML, inline CSS, and vanilla JavaScript site hosted
by GitHub Pages at `thecosmicalchemy.com`. Brand assets and the pinned Lucide 1.30.0
runtime are served from the repository; Google Fonts remains external. There is no application backend,
database, authentication, analytics service, or server-side form processing.

## Eight-layer footprint

- Experience: implemented through the website and external contact links.
- Agent: not implemented.
- Context or retrieval-augmented generation: not implemented.
- Evaluation: automated publication validation plus responsive, interaction, link,
  metadata, and accessibility-oriented browser checks.
- Safety: medical disclaimer, confidentiality wording, no draft testimonial invention.
- LLMOps: not implemented.
- Platform: GitHub repository, GitHub Pages, custom domain, static assets.
- Governance: Git history, checkpoint commit, ADR, noindex staging page, policy pages.
