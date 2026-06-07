# Memory — html-slides-advanced

Append-only log of process lessons from QA runs and user sessions. Newest on top. 2–3 sentences per entry. Content rules and spec live in `SKILL.md` — this file is for improving the skill itself.

Before each session: read all entries, scan for any lesson that suggests a missing rule, recurring fix, or better default in `SKILL.md`. If found, flag each one to the user in one sentence before doing anything else.

---

## 2026-06-07

The style-picker Q5 flow needed all 49 systems accessible by number, not a partial list. `style-picker.html` added as a companion tool — share it with the user at Q5. Card numbers must live in the card body (not overlaid on the swatch strip) to stay readable on dark-first palettes.

The bottom metadata row on style-picker cards was ambiguous — scheme dot and formality word appeared as two ends of one bar, implying a spectrum between them. Fixed by splitting into two clearly labeled rows: `Scheme` and `Formality` each on their own line.

