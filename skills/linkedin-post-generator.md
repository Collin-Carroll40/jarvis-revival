# Skill: linkedin-post-generator

Status: shipped this weekend.

## Purpose

Generate three distinct LinkedIn post variants for Caseread.ai every drafting day (M/W/F at 9 AM via cron). Output goes to Telegram for human review and copy/paste publishing. Nothing posts to LinkedIn automatically.

This is the engine of the marketing-ops layer. It replaces ~4 hours/week of hand-drafting with ~30 minutes of phone-based review.

## Inputs

- **Voice anchor:** `library/style-library.md` — the running 23-post voice analysis. Tone reference, opener patterns, ending patterns, what Collin does and doesn't do.
- **Archetypes:** `library/archetypes.md` — the 9 structural templates. Picks 3 different ones per run, rotated against the last 2 runs.
- **Pillar rotation:** the most recent draft's frontmatter `pillar:` value. Pick a different pillar this run.
- **Product ground truth:** vault notes on Caseread architecture, partnerships, current beta state. Anchors any product claim.
- **Inspiration files (optional):** up to 5 most recent files in `~/vault/04-projects/lawless-ai/linkedin/_inspiration/`.
- **News (Pillar C only):** 1-2 web searches scoped to the past 7 days.

## Outputs

- One markdown file at `~/vault/04-projects/lawless-ai/linkedin/lawless-linkedin-YYYY-MM-DD.md` with frontmatter (`date`, `pillar`, `sourceUrl`, `audience`, `brand`) and three labelled variants (Option A / B / C).
- One Telegram message to chat_id `8169002246` containing the full text of all three variants. Mobile-readable formatting, blank lines between sections.
- Silent best-effort git commit on the vault repo.

## Pillars (rotate each run)

- **A — Privilege & ethics.** ABA Rule 1.6, Heppner-style doctrine, schema-per-firm isolation. Cite a rule or case.
- **B — Beta-user patterns.** What solo / small-firm attorneys say out loud about research workflow. Anonymized. Patterns yes, fabricated anecdotes no.
- **C — Industry takes.** React to a legal-tech / legal-AI headline from the past 7 days. If nothing fresh surfaces, swap to A or B and note the swap.

## Tonal lenses (one per variant, order shuffles)

- **Professional & insightful.** Thought-leadership polish. Cites a doctrine or stat.
- **Conversational & personal.** First-person builder voice. Observation from running the beta.
- **Bold & opinionated.** Punchy hook, contrarian POV. Takes a stance the rest of legal-tech LinkedIn won't.

## Steps

1. **Date + pillar pick.** Get today's date. Read the most recent draft. Pick a different pillar than its frontmatter says. Default to Pillar A on first run.
2. **Pillar C news scan (only if Pillar C).** Run 1-2 WebSearch queries scoped to the past 7 days. If nothing substantive lands, swap to A or B and note the swap.
3. **Read references.** Voice samples (mandatory). Inspiration files (up to 5). Product ground-truth notes.
4. **Brainstorm 5+ angles within the chosen pillar, then pick the 3 most different.** Three variants must be three different posts, not three stylistic spins on the same point. Different throughline, different topic, different product tie-in.
5. **Draft three variants.** Each variant: 1,000-1,500 chars body (vary across the three), strong 2-line hook in the first ~210 chars, short paragraphs of varying length, end with a sharp implication or specific question (never "what do you think?"), 0-3 trailing hashtags from a small allowed set, 0-1 emoji.
6. **Run the dehumidifier.** Em-dash zero tolerance. Banned vocabulary scrubbed. Sentence-fragment injection. No duplicate closers across variants. See `skills/dehumidifier.md`.
7. **Self-audit.** Substance check (no "Lawless", no fabricated lawyers, no "hallucination-free" claims, no Sworn / BYU references, no shared throughline across variants). Rewrite anything that fails.
8. **Save the file.** Frontmatter + Hook/angle + three variants + Notes section (templates used, lengths, throughline, swap-notes).
9. **Send Telegram.** Full text of all three variants in the message body. Filename at the bottom.
10. **Git commit.** Best-effort, silent.

## Hard rules

- Never write "Lawless" anywhere. Brand is Caseread.ai.
- Never fabricate specific lawyers, firms, judges, quotes, or non-public case names.
- Never claim "zero hallucinations" or "hallucination-free". Soften to "verified" or "checked against source".
- Never reference Sworn.ai, BYU, or hackathons.
- Never auto-publish. Output goes to Telegram for Collin to copy/paste.

## Failure modes

- Web search empty for Pillar C: swap to A or B, note it.
- Voice samples missing: still draft, but flag in the Notes section that tone confidence is lower.
- Telegram fails: still write the vault file; log the failure to stderr.
- Dehumidifier audit can't find a clean pass after 3 rewrites: ship the closest variant with a Telegram note flagging which rule it failed on, so Collin can decide whether to ship anyway.
