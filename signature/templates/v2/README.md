# Capstone email signature — template v2

Navy card, single animated GIF (works the same in Outlook, Gmail, Apple Mail, light & dark mode).

Layout
- Left column (aligned to logo edge): animated Capstone logo · WhatsApp + number · Instagram / LinkedIn / Facebook / X / YouTube · capstoneproperty.com
  (number row and icon row are justified to the exact width of the website line)
- Right column (aligned to name): Name (25px, cap-height = "Capstone") · Title (baseline = "PROPERTY") · pin + Marina Way 27 / Porto Arabia / The Pearl, Qatar
- Card trimmed to content with equal 28px margins on all sides, 18px rounded corners, rows on a 30px grid
- Shown at 420px wide in email, rendered at 2x for retina

Make one for a person
1. python3 render.py <slug> "<Full Name>" "<Job Title>" <8-digit WhatsApp>   -> people/<slug>/card.gif
2. Rename card.gif to card-<YYYYMMDDHHMM>.gif and point build_page.py at it (cache-busting), then
   python3 build_page.py <slug> "<Full Name>" "<Job Title>" <WhatsApp>       -> people/<slug>/index.html
3. Commit and push; page goes live at /decks/signature/people/<slug>/

Example: people/raniel-ponesto/  (preview.png in this folder)
