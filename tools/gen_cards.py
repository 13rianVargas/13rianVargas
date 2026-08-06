#!/usr/bin/env python3
"""Generate the custom SVG cards for the profile README.

One template per shape so every card shares the same gold/black language as the
hand-drawn badges in assets/. SMIL only — GitHub's camo proxy sandboxes CSS animation.
"""
import os

OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "assets")
GOLD, IVORY, BG0, BG1 = "#FFD700", "#FFF8DC", "#0D1117", "#161B22"
MONO = "'Fira Code', 'Courier New', monospace"

def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def card(uid, w, glyph, title, lines, meta, accent=None, pad_to=None):
    """A credential / award card: glyph + title + body lines + meta footer.

    Height is derived from the line count so the divider never collides with the
    body. pad_to forces a taller card so siblings in one table row line up.
    """
    n = max(len(lines), pad_to or 0)
    h = 140 + (n - 1) * 19
    body = "".join(
        f'<text x="26" y="{88 + i*19}" font-family="{MONO}" font-size="12.5" '
        f'fill="{IVORY}" fill-opacity="0.88">{esc(l)}</text>'
        for i, l in enumerate(lines)
    )
    badge = ""
    if accent:
        tw = len(accent) * 8.4 + 20
        badge = (
            f'<rect x="{w-tw-22}" y="19" width="{tw}" height="24" rx="6" fill="{GOLD}"/>'
            f'<text x="{w-tw/2-22}" y="35.5" font-family="{MONO}" font-size="12" font-weight="700" '
            f'fill="{BG0}" text-anchor="middle" letter-spacing="0.5">{esc(accent)}</text>'
        )
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
  <defs>
    <linearGradient id="bg{uid}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{BG0}"/><stop offset="100%" stop-color="{BG1}"/>
    </linearGradient>
    <linearGradient id="sh{uid}" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="{GOLD}" stop-opacity="0"/>
      <stop offset="50%" stop-color="{GOLD}" stop-opacity="0.9"/>
      <stop offset="100%" stop-color="{GOLD}" stop-opacity="0"/>
      <animateTransform attributeName="gradientTransform" type="translate"
        values="-{w} 0; {w} 0" dur="6s" repeatCount="indefinite"/>
    </linearGradient>
  </defs>

  <rect x="0.75" y="0.75" width="{w-1.5}" height="{h-1.5}" rx="12" fill="url(#bg{uid})" stroke="{GOLD}" stroke-width="1.5"/>
  <rect x="12" y="1" width="{w-24}" height="1.6" fill="url(#sh{uid})"/>

  <g transform="translate(28, 33)" stroke="{GOLD}" fill="none" stroke-width="1.8"
     stroke-linecap="round" stroke-linejoin="round">{glyph}</g>

  <text x="52" y="38" font-family="{MONO}" font-size="14" font-weight="700"
        fill="{GOLD}" letter-spacing="0.6">{esc(title)}</text>
  {badge}
  {body}

  <line x1="26" y1="{h-34}" x2="{w-26}" y2="{h-34}" stroke="{GOLD}" stroke-opacity="0.22" stroke-width="1"/>
  <text x="26" y="{h-15}" font-family="{MONO}" font-size="11.5" font-weight="700"
        fill="{GOLD}" fill-opacity="0.75" letter-spacing="1">{esc(meta)}</text>
</svg>
'''

def cat(uid, w, label):
    """A tech-stack category header: diamond + label + rule."""
    tw = len(label) * 9.6
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="34" viewBox="0 0 {w} 34">
  <polygon points="12,10 19,17 12,24 5,17" fill="{GOLD}">
    <animate attributeName="opacity" values="0.5;1;0.5" dur="3.2s" repeatCount="indefinite"/>
  </polygon>
  <text x="29" y="22" font-family="{MONO}" font-size="14" font-weight="700"
        fill="{GOLD}" letter-spacing="2.2">{esc(label)}</text>
  <line x1="{29+tw+14}" y1="17" x2="{w-10}" y2="17" stroke="{GOLD}" stroke-opacity="0.3" stroke-width="1"/>
</svg>
'''

# ── glyphs, drawn in the same stroke language as the existing badge icons ──
G_SHIELD = '<path d="M 0 -11 L 9 -7.5 V 1 C 9 6.5 4.8 10 0 11.5 C -4.8 10 -9 6.5 -9 1 V -7.5 Z"/><path d="M -4 0 L -1 3.5 L 4.5 -3" stroke-width="2"/>'
G_CLOUD  = '<path d="M -9 5 A 5 5 0 0 1 -8.4 -5 A 7 7 0 0 1 5 -6 A 5.2 5.2 0 0 1 9 5 Z"/>'
G_BOOK   = '<path d="M -9 -8 H -1 A 2.5 2.5 0 0 1 1 -6 V 9 A 2 2 0 0 0 -1 7 H -9 Z"/><path d="M 9 -8 H 1 A 2.5 2.5 0 0 0 -1 -6 V 9 A 2 2 0 0 1 1 7 H 9 Z"/>'
G_MEDAL  = '<circle cx="0" cy="4" r="6.5"/><path d="M -5.5 -1.5 L -8 -11 H 8 L 5.5 -1.5"/><path d="M -2 4 L -0.4 6 L 2.6 2" stroke-width="1.9"/>'
G_CODE   = '<path d="M -3.5 -8 L -10 0 L -3.5 8"/><path d="M 3.5 -8 L 10 0 L 3.5 8"/><path d="M 1 -9 L -1 9" stroke-opacity="0.6"/>'
G_CERT   = '<rect x="-9.5" y="-9" width="19" height="13" rx="2"/><path d="M -5 -4.5 H 5" stroke-opacity="0.55"/><path d="M -5 -0.5 H 1" stroke-opacity="0.55"/><path d="M 0 4 L -3.5 11 L 0 9 L 3.5 11 Z"/>'

CARDS = [
    # (uid, filename, width, glyph, title, body lines, meta, accent, pad_to)
    ("ccst", "cred-ccst.svg", 760, G_SHIELD, "CCST CYBERSECURITY", [
        "Official proctored 100-160 exam (Certiport). 700 is the minimum to pass.",
        "100% in network security, vulnerability assessment and incident handling.",
    ], "CISCO SYSTEMS  ·  05/2026", "974 / 1000", None),

    # los tres de abajo van en una misma fila -> misma altura (pad_to=4)
    ("cisco", "cred-cisco.svg", 370, G_CERT, "CISCO ACADEMY", [
        "Ethical Hacker · CCNA Switching,",
        "Routing & Wireless Essentials ·",
        "Intro to Cybersecurity ·",
        "NDG Linux Unhatched",
    ], "4 BADGES · 5 CERTS  ·  2024—2026", None, 4),

    ("gcp", "cred-gcloud.svg", 370, G_CLOUD, "GOOGLE CLOUD", [
        "Generative AI ·",
        "Data & Analytics ·",
        "Infrastructure & Operations",
    ], "16 COURSES & BADGES  ·  2026", None, 4),

    ("platzi", "cred-platzi.svg", 370, G_BOOK, "PLATZI", [
        "Java & Spring —",
        "the backend track,",
        "start to finish",
    ], "2 CERTIFICATES · 32 H  ·  02/2026", None, 4),

    # estos dos comparten fila -> pad_to=3
    ("awcisco", "award-cisco.svg", 430, G_MEDAL, "CISCO CYBER CHALLENGE", [
        "Won the voucher that paid for the CCST",
        "exam — which I then passed at 974/1000.",
    ], "CISCO SYSTEMS · BOGOTÁ D.C.  ·  04/2026", None, 3),

    ("awmar", "award-marathon.svg", 430, G_CODE, "PROGRAMMING MARATHON", [
        "University representative against ~120 teams,",
        "qualifier for the Latin American Regional.",
        "Solved in Java, Python and C++.",
    ], "KONRAD LORENZ  ·  2024", None, 3),
]

CATS = [("FRONTEND", 560), ("BACKEND & LANGUAGES", 560), ("DATABASES", 560), ("TOOLS & DEVOPS", 560)]

written = []
for uid, name, w, glyph, title, lines, meta, accent, pad in CARDS:
    p = os.path.join(OUT, name)
    open(p, "w", encoding="utf-8").write(card(uid, w, glyph, title, lines, meta, accent, pad))
    written.append((name, os.path.getsize(p)))

for label, w in CATS:
    name = "cat-" + label.split()[0].lower().replace("&", "") + ".svg"
    p = os.path.join(OUT, name)
    open(p, "w", encoding="utf-8").write(cat(label[:3].lower(), w, label))
    written.append((name, os.path.getsize(p)))

for n, s in written:
    print(f"  {n:24} {s:6} bytes")
