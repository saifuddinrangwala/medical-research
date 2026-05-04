# Medical research

Working folder for **medical admissions research** (India + abroad). Use **`@`-mentions** on this folder in Cursor so assistants load shared context.

## Layout

| Path | Purpose |
|------|---------|
| [references/official-sources.md](./references/official-sources.md) | Authoritative portals only (NTA, MCC, Gujarat ACPUGMEC, NMC, etc.) |
| [profiles/candidate-a/](./profiles/candidate-a/) | Facts, academics, aspirations, ops notes for **Candidate A (de-identified)** |

## Profiles

| Person | Folder |
|--------|--------|
| Candidate A (de-identified) | [`profiles/candidate-a/README.md`](./profiles/candidate-a/README.md) · [Gujarat](./profiles/candidate-a/gujarat-colleges.md) · [Fee/living/intl matrix](./profiles/candidate-a/fee-living-reputation-matrix.md) · [Mumbai–Pune–Bengaluru](./profiles/candidate-a/mbbs-mumbai-pune-bengaluru.md) · [Egypt Cairo](./profiles/candidate-a/egypt-cairo-medical-colleges.md) |

Add new students under `profiles/<slug>/` using the same file pattern (`profile.md`, `academics.md`, `goals-and-options.md`, `operating-notes.md`).

## Primary documents (outside this repo)

- Gujarat HSC PDF: `[REDACTED_LOCAL_PATH]/hsc-result.pdf` (confirm with printed marksheet)

## Private personalized data (local only)

- Store sensitive candidate identity data under `private/` (git-ignored).
- Use that folder only for personalized report generation; keep `profiles/` de-identified.

## Changelog

- **2026-05-04** — Migrated pack into `medical-research/` with `references/` + `profiles/candidate-a/`.
- **2026-05-04** — Gujarat + Mumbai/Pune/Bengaluru lists: **Google Maps** links on every row; Phone/Email partly filled (remainder `—`, confirm on official sites). ACPUGMEC `ug/contact.aspx` linked from `official-sources.md`.
- **2026-05-04** — Egypt Cairo metro medical faculties note + NMC “valid in India” framing; WDOMS bookmark in `official-sources.md`.
- **2026-05-04** — Candidate A: **English-medium only** for overseas MBBS screening (see `profiles/candidate-a/goals-and-options.md`).
- **2026-05-04** — Candidate A matrix expanded: all **Gujarat MBBS + BDS**, **Mumbai/Pune/Bengaluru** researched MBBS rows, **Egypt** faculties — see `profiles/candidate-a/fee-living-reputation-matrix.md`.
