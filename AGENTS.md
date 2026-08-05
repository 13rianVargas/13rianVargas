# 13rianVargas · Agent Context

> Operational context and rules for AI agents working in this repository.

---

## Project Overview

This repository contains the **GitHub profile README** for Brian Vargas (`@13rianVargas`). It is displayed on the GitHub profile page at https://github.com/13rianVargas.

The README presents Brian's identity as a **Java Backend Developer | Full Stack** and K-Forge founder, with custom animated SVG banners, GitHub stats, and tech stack badges.

> **Source of truth:** the portfolio at <https://13rian-vargas.vercel.app> owns the bio, role, project list and tech stack. When they disagree, the portfolio wins and this README follows. Its content lives in `MyPortfolio/src/i18n/ui.ts` and `MyPortfolio/src/components/sections/`.

---

## Structure

```text
13rianVargas/
├── README.md                   # GitHub profile README (rendered at github.com/13rianVargas)
└── assets/
    ├── header-banner.svg       # 1200x400 · animated hero (deer mark, name, role, ID-card frame)
    ├── divider.svg             # 1200x6   · animated gold shimmer divider (between sections)
    ├── footer-banner.svg       # 1200x260 · animated footer (deer mark, signature, particles)
    ├── badge-fukl.svg          # 320x44   · university
    ├── badge-linkedin.svg      # 320x44   · LinkedIn
    ├── badge-kforge.svg        # 320x44   · K-Forge org
    ├── badge-kforge-link.svg   # 320x44   · K-Forge website
    ├── badge-portfolio.svg     # 320x44   · portfolio
    ├── badge-cv-en.svg         # 320x44   · CV download (English)
    ├── badge-cv-es.svg         # 320x44   · CV download (Spanish)
    ├── badge-repo.svg          # 100x32   · project repo pill
    ├── badge-live.svg          # 110x32   · project live pill
    ├── badge-wip.svg           # 100x32   · project WIP pill
    ├── badge-prototype.svg     # 130x32   · project prototype pill (demo, not production)
    └── badge-video-soon.svg    # 152x32   · project pill for a demo video not yet published
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

- **`header-banner.svg`** — 1200x400. Hex mesh background, floating particles, expanding rings, rotating diamonds, gradient text shimmer on name. Carries the **identity-card motif**: corner brackets, `ID: 000-013` and `BOGOTÁ D.C. · CO`, echoing the 3D flip card on the portfolio.
- **`divider.svg`** — 1200x6. Soft gold base + animated white shimmer that travels left-to-right (4s loop).
- **`footer-banner.svg`** — 1200x260. Hex mesh, rising particles, expanding rings from the top edge, gold signature.

### Deer mark

Both banners carry a **deer head** drawn as gold line art — the same logo as the portfolio favicon (`MyPortfolio/public/icons/deerhead.svg`), and the main visual link between the two properties.

Do **not** import the portfolio's file: it is a 248 KB traced silhouette that blows the size budget and clashes with the hand-drawn stroke style. The README version is a redrawn geometric path set (antlers, ears, head, eyes) living inline in each banner. Keep both copies in sync when editing.

When editing SVGs:
- Stick to SMIL only — CSS animations are sandboxed in GitHub camo.
- Keep file size reasonable (current files are <5KB each).
- Use the gold/black palette only.

---

## External Services Used

| Service | Purpose |
|---------|---------|
| `readme-typing-svg.demolab.com` | Animated typing roles |
| `ghchart.rshah.org` | Contribution heatmap — **no GitHub token**, so it cannot fail the way the widgets below did |
| `quotes-github-readme.vercel.app` | Random daily quote |
| `komarev.com` | Profile visitor counter |
| `img.shields.io` | Custom badges + `dynamic/json` stat strip off `api.github.com` |
| `raw.githubusercontent.com` | Custom SVG assets in `assets/` |

### Do not use these — verified dead

Free hobby instances of the popular readme widgets are being shut down. Probed and confirmed broken:

| Dead host | Status |
|-----------|--------|
| `github-readme-stats.vercel.app` | `503 DEPLOYMENT_PAUSED` |
| `github-profile-trophy.vercel.app` | `402 DEPLOYMENT_DISABLED` |
| `github-profile-summary-cards.vercel.app` | `500` |
| `github-contributor-stats.vercel.app` | `402` |
| `github-readme-stats.hackclub.dev` | `200`, but body renders `Something went wrong` |
| `github-readme-activity-graph.vercel.app` | intermittent — see below |

`github-readme-activity-graph.vercel.app` deserves its own note because it fails *sometimes*, which is worse than failing outright. It renders `Can't fetch any contribution. Please check your username 😬` on its own token's bad days, and camo then caches that error image, so the profile looks broken long after the service recovered. Probing it 12 times in a row returned 12 healthy responses while the profile was still showing the error. It was replaced with `ghchart.rshah.org`, which proxies GitHub's public contribution chart and needs no token at all — one less credential to expire.

**Rule of thumb: prefer widgets that need no GitHub token.** Every widget that broke on this profile broke at the token or the hosting bill, never at the rendering.

**Do not swap in a third-party mirror** — that is the same class of instance and it will die too. The replacement is self-hosting:

| Fork | Runtime | Env var | Live instance |
|------|---------|---------|---------------|
| `13rianVargas/github-readme-stats` | Node (`api/*.js`) | `PAT_1` | `github-readme-stats-nu-gilt-20.vercel.app` |

A `github-profile-trophy` fork existed briefly and was **deleted on 2026-08-05** — self-hosting it does not work (see below), so there was nothing to keep. Do not re-fork it without reading that section first.

If it is ever revived, its requirements differ from the stats project — verified in source, not assumed:

1. It is **Deno** (`vercel-deno@3.1.1`, pinned in its own `vercel.json`), not Node.
2. It reads `Deno.env.get("GITHUB_TOKEN1")` **and** `GITHUB_TOKEN2` in `src/Services/GithubApiService.ts:24-27`, then indexes `TOKENS[attempt]` on retry. Both must be set, to the same token. Naming either one `PAT_1` yields an unauthenticated instance.
3. **Vercel → Settings → Deployment Protection → Vercel Authentication → "Only Preview Deployments."** Left on the default, production returns 401 to anonymous traffic and the card renders blank through GitHub's camo proxy.
4. Token scopes: `read:user` + `public_repo` (only `repo` if private contributions should count).

### Trophy: a fresh deploy of `master` does not boot (verified 2026-08-05)

Doing all three of the above is **not enough**. A Vercel deploy of current `master` returns `500 FUNCTION_INVOCATION_FAILED` on **every** URL, including `/` with no query string. That path renders a static HTML form and never calls the GitHub API or reads a token, so the failure is at **module load, before any request logic**. Env vars are not the cause — do not chase them.

Proof, against a community instance running an older deploy:

| Instance | `/` with no username |
|---|---|
| ours, deployed 2026-08-05 from `master` | `500 FUNCTION_INVOCATION_FAILED` |
| `github-profile-trophy-orcin-eta.vercel.app` | `400` — the expected "username is required" page |

Likely cause: `deps.ts` imports over raw `https://deno.land/std@0.203.0/...` and `deno.land/x/...` URLs, while the pinned runtime `vercel-deno@3.1.1` has not shipped since **2024-07-16**. Upstream issue [#455](https://github.com/ryo-ma/github-profile-trophy/issues/455) and PRs #456/#457 propose migrating those imports to JSR; all three are still **open and unmerged**.

Rolling the fork back to an older commit is unlikely to help — `deps.ts` is unchanged across recent history, so what differs is Vercel's current build image, not the code.

**Decision (2026-08-05): the Trophies section is dropped.** It is gone from `README.md`, replaced by a comment explaining why. Do not re-add it — not self-hosted (does not boot), and **not** pointed at a community instance either: 6 of the 10 listed in the upstream README are already 404. Revisit only if #457 merges upstream.

**Current state:** the GitHub Stats section is live and self-hosted at `github-readme-stats-nu-gilt-20.vercel.app` (verified: 1219 commits, 52 PRs, 112 issues, plus top-langs). A `200` is not proof a widget works — grep the response body for real content (`Total Commits`, trophy titles) before trusting it.

---

## Conventions

- **Single file repo.** Only `README.md` and `assets/` matter.
- **GitHub-flavored markdown** with embedded HTML for layout.
- **Color discipline:** every new badge or widget must use the gold `#FFD700` + black `#0D1117` palette. No off-brand colors. (The portfolio's amber `#fbbf24` is the same family — no need to reconcile them.)
- **No contact data.** Never put an email, phone number, `mailto:` link or `wa.me` link in this repo. The CV badges link to the PDFs already published on the portfolio; that is the only contact route. A `badge-email.svg` used to exist and was deliberately deleted — do not restore it.
- **Projects follow the portfolio.** The list mirrors the portfolio's 5 projects: KApp, AMODEL, K-Forge, SpemTraductor, MyPortfolio. Add a project here only after it appears there. TiendaQ and Roastory were removed for this reason — they are real K-Forge work, but not on the portfolio.
- **K-Forge stacks:** K-Forge's own README stays authoritative for K-Forge project internals. KApp is Java + Spring Boot microservices — never React Native.
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
- **Verify every badge URL before committing** — broken images degrade the public profile. Sweep the whole file, do not spot-check:
  ```bash
  grep -oE 'https://[^"]+' README.md | sed 's/&amp;/\&/g' | sort -u \
    | while read -r u; do c=$(curl -s -o /dev/null -w '%{http_code}' --max-time 20 -L "$u"); [ "$c" = 200 ] || echo "[$c] $u"; done
  ```
  LinkedIn answering `999` is expected — that is their anti-bot gate, not a broken link. Anything else is a real failure.
- **Never hardcode the years of experience.** The portfolio computes it from `START_YEAR = 2023`, so it rolls over every January. Keep it as prose.
- **Keep tooling badges accurate:** npm, pnpm, Bun (3 distinct, no duplicates).
- **Custom SVG edits:** test rendering by viewing the raw URL after push — GitHub camo caches for ~5min.
- No automatic commits. Present changes for review first.


---

## Temporary Files

- `tmp/` is gitignored. Store one-off scripts and throwaway files there.
- Delete after use. Never commit anything from `tmp/`.