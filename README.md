# ConnectUS Digital Skills Practice Site (Prototype)

A safe place for ConnectUS Digital Skills Hub (DSH) learners to practice everyday online tasks: filling out forms, searching a website, typing, and using a mouse or Chromebook trackpad. Nothing a learner types or clicks is saved or sent.

**Live prototype:** https://the-black-dog.github.io/
**Status:** Prototype for user testing. Not the final production site.

## What's included

**Practice home page**
- Orientation and safety message, with hint bubbles that explain each part of the page (can be turned off).
- Site search that only searches this site, with an explanation of site search versus search engines.
- A four-step checkout form (Cart, Billing, Shipping, Payment) with teaching-style error messages and a pretend payment card.
- Header controls (menu, settings, more options) with tips, plus text size and high-contrast settings.
- Practice email sign-up in the footer.

**Typing practice** (`#typing`)
- Three levels (words, sentences, real-life entries), each with a rotating list of practice lines.
- Live words-per-minute counter (can be hidden), accuracy, and a per-visit average and best speed.

**Mouse and trackpad skills** (`#mouse`)
- Hub with progress and stars for the current visit.
- Getting comfortable (warm-up), Close the pop-ups, Open the folders, Sort the groceries, Highlight and copy, Find the hidden star, Two-finger click, and a bonus puzzle.
- Every activity has a "Show me how" demo, multiple levels, and a keyboard path. Dragging activities also offer "click to pick up, click to place."
- Written for Chromebook trackpads first, with mouse tips as a backup.

Link to a section by adding it to the end of the address, for example `https://the-black-dog.github.io/#typing` or `https://the-black-dog.github.io/#mouse/sort`.

## Files

| File | Purpose |
| --- | --- |
| `index.html` | The whole site in one self-contained file (styles, scripts, fonts, and the learner photo are embedded) |
| `404.html` | Friendly "page not found" page with a link back home |
| `og-image.png` | Preview image shown when the link is shared in texts, email, or social media |
| `apple-touch-icon.png` | Icon used when the site is saved to a phone or tablet home screen |
| `robots.txt` | Asks search engines not to crawl the site during testing |
| `.nojekyll` | Tells GitHub Pages to serve the files as-is instead of building them with Jekyll |
| `tools/update_csp_hashes.py` | Keeps the security policy in sync after editing scripts (see below) |
| `LICENSE` | MIT license for the source code |
| `licenses/Poppins-OFL.txt` | License for the Poppins font |

## Privacy

- No accounts, cookies, or browser storage. Progress and settings reset when the page is closed or reloaded.
- Forms never submit anywhere, and typed or pasted text is never logged.
- The page makes no requests to outside services: fonts and images are built into the page.
- GitHub Pages keeps standard server logs (such as visitors' IP addresses), as most web hosts do.
- The page asks search engines not to index it (`noindex` and `robots.txt`) during testing.

## Security

`index.html` includes a Content-Security-Policy that blocks the page from loading anything from other sites, sending data anywhere, or submitting forms. Its scripts are allowed by exact fingerprints (hashes).

**Important:** after editing anything inside a `<script>` block in `index.html`, run this from the repository folder before committing:

```
python3 tools/update_csp_hashes.py
```

Otherwise the browser blocks the edited script and the page's buttons stop working. The browser's developer console shows a Content-Security-Policy error if this happens.

## Accessibility

Built to WCAG 2.2 Level AA: semantic HTML, full keyboard support, visible focus, screen reader announcements, reduced-motion support, and 44×44 px touch targets.

## Run it locally

Open `index.html` in a browser, or use a local server such as the VS Code Live Server extension.

## Updating the live site

This repository is named after the account (`<account-name>.github.io`), so GitHub Pages serves it at the root address.

1. Upload changed files to the `main` branch (keep `index.html` at the top level, not in a folder).
2. GitHub Pages republishes automatically. Watch the **Actions** tab for a green check, then reload with Ctrl + Shift + R.

Pages settings: **Settings › Pages › Build and deployment**, Source **Deploy from a branch**, branch **main**, folder **/ (root)**.

If the site moves to a custom domain, update the `og:url` and `og:image` addresses near the top of `index.html`.

## Giving feedback

Testers can share feedback with the ConnectUS program team. Helpful details: which activity, what device (Chromebook trackpad, mouse, other), what was confusing, and what they expected to happen.

## Roadmap

- Test with DSH learners on program Chromebooks.
- Add real-life challenges (sign-up, job application, and similar pages).
- Refactor into modular source files with a build step, automated tests (end-to-end and accessibility), and linting.
- Add a plain-language privacy note on the site.
- Launch on the ConnectUS WordPress site, then add touch versions for iPads.

## License and credits

- Source code: MIT License (see `LICENSE`).
- Poppins font: SIL Open Font License 1.1 (see `licenses/Poppins-OFL.txt`).
- The learner photograph and the ConnectUS and Smart Columbus names and branding are not covered by the MIT License. Confirm the photo's media release before public launch.

Smart Columbus / ConnectUS Digital Skills Hub. Prototype built with Claude, based on designs from the ConnectUS design team.
