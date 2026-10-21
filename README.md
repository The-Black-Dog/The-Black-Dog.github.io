# The-Black-Dog.github.io
Digital Skills Hub Student Practice Website

# ConnectUS Digital Skills Practice Site (Prototype)

A safe place for ConnectUS Digital Skills Hub (DSH) learners to practice everyday online tasks: filling out forms, searching a website, typing, and using a mouse or Chromebook trackpad. Nothing a learner types or clicks is saved or sent.

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

## Privacy

- No accounts, cookies, or browser storage. Progress and settings reset when the page is closed or reloaded.
- Forms never submit anywhere, and typed or pasted text is never logged.
- The page loads the Poppins font from Google Fonts, and GitHub Pages keeps standard server logs. Self-hosting the font is planned before production.
- The page asks search engines not to index it (`noindex`) during testing.

## Accessibility

Built to WCAG 2.2 Level AA: semantic HTML, full keyboard support, visible focus, screen reader announcements, reduced-motion support, and 44×44 px touch targets.

## Files

| File | Purpose |
| --- | --- |
| `index.html` | The whole site in one self-contained file (styles, scripts, and the learner photo are embedded) |
| `README.md` | This file |

The single-file format matches how the prototype is hosted on claude.ai. A modular source structure with a small build step is planned (see Roadmap).

## Run it locally

Open `index.html` in a browser, or use a local server such as the VS Code Live Server extension.

## Deploy to GitHub Pages

1. Create a repository (for example `connectus-practice-site`) and upload `index.html` and `README.md` to the main branch.
2. Go to **Settings › Pages**.
3. Under **Build and deployment**, set **Source** to **Deploy from a branch**, choose **main** and **/ (root)**, and save.
4. After a few minutes the site is live at `https://<account-name>.github.io/<repository-name>/`.

To update the site, upload a new `index.html` to the main branch. GitHub Pages republishes automatically.

Links to specific sections work by adding the section to the end of the URL, for example `.../#typing` or `.../#mouse/sort`.

## Giving feedback

Testers can share feedback with the ConnectUS program team. Helpful details: which activity, what device (Chromebook trackpad, mouse, other), what was confusing, and what they expected to happen.

## Roadmap

- Test with DSH learners on program Chromebooks.
- Add real-life challenges (sign-up, job application, and similar pages).
- Refactor into modular source files with a build step, automated tests (end-to-end and accessibility), and linting.
- Self-host fonts and add a Content-Security-Policy.
- Launch on the ConnectUS WordPress site, then add touch versions for iPads.

## Credits

Smart Columbus / ConnectUS Digital Skills Hub. Prototype built with Claude, based on designs from the ConnectUS design team. Learner photo used with permission (confirm media release before public launch).
