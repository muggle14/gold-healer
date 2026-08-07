# Security notes

## Current controls

- The site is static and has no server-side credential or payment storage.
- External links opening new tabs use `noopener` and, where appropriate, `noreferrer`.
- The staged page uses `noindex,nofollow` and is not the GitHub Pages source branch.
- Medical and mental-health disclaimers remain visible.
- Unverified testimonial drafts are excluded from the staged publication.

## Gaps

- Google Fonts and the unpinned Lucide CDN receive normal web requests from visitors.
- The contact form opens the visitor's mail client and does not provide backend delivery
  assurance or abuse controls.
- WhatsApp, Instagram, email, and telephone handling depend on third-party platforms and
  the owner's operating practices.
- Policy copy is an implementation-consistency update, not a substitute for legal review.

