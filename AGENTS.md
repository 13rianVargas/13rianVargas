# 13rianVargas · Agent Context

> Operational context and rules for AI agents working in this repository.

---

## Project Overview

This repository contains the **GitHub profile README** for Brian Vargas (`@13rianVargas`). It is displayed on the GitHub profile page at https://github.com/13rianVargas.

The README presents Brian's identity as a Full Stack Developer and K-Forge founder, with custom animated SVG banners, GitHub stats, and tech stack badges.

---

## Structure

```text
13rianVargas/
├── README.md                   # GitHub profile README (rendered at github.com/13rianVargas)
└── assets/
    ├── header-banner.svg       # Animated hero banner (name + role + particles)
    ├── divider.svg             # Animated gold shimmer divider (between sections)
    └── footer-banner.svg       # Animated wave footer (closing tag + waves)
```

---

## Brand Identity

- **Primary:** Gold `#FFD700`
- **Highlight:** Ivory `#FFF8DC`
- **Background:** Black `#0D1117` (matches GitHub dark theme)
- **Typography:** Fira Code (monospace) for headers and code-style text
- **Visual motif:** `◈` diamond bullets for section headers
- **Style:** Dark + gold accents, terminal/code aesthetic

This palette is intentionally distinct from the K-Forge brand (purple `#8B5CF6`). Brian's personal identity is gold; K-Forge sections within the README reference K-Forge but stay in gold to keep the page coherent.

---

## Animated SVG Banners

The three custom SVGs in `assets/` use SMIL animations (`<animate>`, `<animateTransform>`) which work through GitHub's camo image proxy. They are referenced from the README via raw URLs:

```
https://raw.githubusercontent.com/13rianVargas/13rianVargas/main/assets/<file>.svg
```

- **`header-banner.svg`** — 1200x320. Animated grid background, floating particles, dashed border lines, glowing brackets, gradient text shimmer on name, blinking terminal cursor.
- **`divider.svg`** — 1200x6. Soft gold base + animated white shimmer that travels left-to-right (4s loop).
- **`footer-banner.svg`** — 1200x160. Animated wave layers (3 layers at different speeds) with gradient closing tag.

When editing SVGs:
- Stick to SMIL only — CSS animations are sandboxed in GitHub camo.
- Keep file size reasonable (current files are <5KB each).
- Use the gold/black palette only.

---

## External Services Used

| Service | Purpose |
|---------|---------|
| `readme-typing-svg.demolab.com` | Animated typing roles |
| `github-readme-stats.vercel.app` | Stats card + top languages |
| `github-readme-streak-stats.herokuapp.com` | Contribution streak |
| `github-profile-summary-cards.vercel.app` | Profile details, repos-per-language, productive time |
| `github-readme-activity-graph.vercel.app` | Contribution graph |
| `github-profile-trophy.vercel.app` | Trophies |
| `skillicons.dev` | Animated tech stack icons |
| `quotes-github-readme.vercel.app` | Random daily quote |
| `komarev.com` | Profile visitor counter |
| `img.shields.io` | Custom badges (gold-on-black palette) |

---

## Conventions

- **Single file repo.** Only `README.md` and `assets/` matter.
- **GitHub-flavored markdown** with embedded HTML for layout.
- **Color discipline:** every new badge or widget must use the gold `#FFD700` + black `#0D1117` palette. No off-brand colors.
- **K-Forge references:** when listing K-Forge projects, the stack descriptions must match the K-Forge ecosystem (K-Forge Web, KApp, TiendaQ, Roastory). KApp is Java + Spring Boot microservices — never React Native.
- **Tooling badges:** keep npm + pnpm + Bun as three separate badges (no duplicates).
- **Commits:** Conventional Commits, English, lowercase.
  ```
  docs: update tech stack badges
  feat(assets): add animated header banner
  fix(readme): resolve duplicate pnpm badge
  ```

---

## AI Agent Instructions

- Modify `README.md` and files inside `assets/`.
- **Maintain the gold/black aesthetic.** Do not introduce purple, blue, or other accent colors.
- **Maintain story consistency with K-Forge ecosystem.** Project list and stacks must match `K-Forge/.github/profile/README.md`.
- **Verify badge URLs work** before committing — broken images degrade the public profile.
- **Keep tooling badges accurate:** npm, pnpm, Bun (3 distinct, no duplicates).
- **Custom SVG edits:** test rendering by viewing the raw URL after push — GitHub camo caches for ~5min.
- No automatic commits. Present changes for review first.
