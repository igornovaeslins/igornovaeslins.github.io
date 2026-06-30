# igornovaeslins.github.io

Personal academic website of **Igor Novaes Lins** — political scientist (criminal governance and politics in Latin America).

Live at **https://igornovaeslins.github.io**

Trilingual (EN / PT / ES), five pages each (About · Research · Publications · Writing · Consulting), generated from a single script.

## Edit / rebuild

Edit the content in `build.py` (the `T` dictionary and the `PUBS` / `OPEDS` lists) or the design in `style.css`, then run:

    python3 build.py

This regenerates all HTML, `sitemap.xml`, and `robots.txt`. Commit and push to `main` — GitHub Pages redeploys automatically.

## Design & SEO

- Economist-style sidebar layout · Bricolage Grotesque + Hanken Grotesk · editorial red `#E3120B`.
- Per-page `<title>` / `meta description`, `hreflang` alternates, Open Graph, Twitter cards, and schema.org `Person` structured data are built in.
- To verify the site in Google Search Console, paste the verification meta tag into the marked spot in `build.py` → `render_head` (`ADD-GOOGLE-VERIFICATION-HERE`), then rebuild and push.
