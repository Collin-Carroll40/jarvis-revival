# Skill: intel-synthesis

Status: shipped this weekend.

## Purpose

Run a Sunday-evening competitive intelligence scan of the legal-tech / legal-AI market. Send a 3-paragraph brief to Telegram so Collin walks into Monday morning with a picture of the past week before he plans.

Replaces ~3 hours/week of browser-tab competitor scanning with ~15 minutes of phone reading.

Scheduled Sunday 8 PM via cron.

## Inputs

- **Time window:** past 7 days.
- **Target competitors and orbit:** OpenCase, Westlaw, LexisNexis, Harvey AI, Hebbia, Eve Legal, Spellbook, Paxton AI, Casetext (Thomson Reuters), Vincent AI, ABA tech committee, Stanford RegLab, hallucination-sanction case law.
- **Caseread.ai positioning context:** AI legal research for solo / small / mid-market attorneys. Wedge is Hallucination Shield + schema-per-firm privilege isolation.

## Outputs

- One markdown brief at `~/vault/01-daily/competitive-intel/intel-YYYY-MM-DD.md` with frontmatter, three sections (launches & products, people & hiring, funding & deals), bottom line, sources, and a search log.
- One Telegram brief to chat_id `8169002246`, three paragraphs plus a 1-2 sentence bottom line, with sources listed at the bottom.
- Silent best-effort git commit.

## Steps

1. **Set up.** Get today's date. Compute the "7 days ago" date string for query phrasing.
2. **Run 4-6 WebSearch queries.** Vary phrasing across topic clusters: OpenCase, Westlaw / Lexis announcements, Harvey funding / hiring, legal AI startup launches, AI hallucination sanctions, ABA AI guidance. Cap at ~8 queries total.
3. **Capture results.** For each useful hit: headline, source URL, date (must be in the last 7-14 days, older = skip), why it matters for Caseread's wedge.
4. **Optional WebFetch for depth.** Only if a search snippet leaves a critical gap (funding amount, lead investor, specific roles). Skip paywalled sites and aggregators.
5. **Synthesize three paragraphs.**
   - Launches & products: who shipped what, what's competitively interesting for solo / small firms.
   - People & hiring: who got hired, what the role profile signals (CISO = security pressure; ex-Big Four = benchmarking investment; model-eval lead = roadmap).
   - Funding & deals: amounts, valuations, lead investors, what segment of legal AI is getting attention (research vs drafting vs eDiscovery vs intake).
6. **Write a 1-2 sentence bottom line.** Specific to Caseread's solo/small-firm wedge: what to accelerate, deprioritize, or defend against.
7. **Save vault file.** Brief + sources + search log (each query and which results it produced).
8. **Send Telegram.** Mobile-readable, 3 paragraphs tight at 3-5 sentences each, sources at the bottom, vault path last.
9. **Git commit.** Best-effort, silent.

## Hard rules

- Never write "Lawless". Brand is Caseread.ai.
- Never reference Sworn.ai, BYU, hackathons, or any other Collin project.
- Source every claim. Include URLs.
- Be honest about a quiet week. Don't pad. Say so plainly and suggest what a quiet week is good for (shipping, content, beta-user calls).
- No em-dashes as drama beats. No banned vocabulary.

## Failure modes

- All web searches fail: send Telegram message acknowledging the failure. Suggest manual re-run. Write vault file with the search log so the failure is debuggable.
- Some queries return, others don't: synthesize from what you have. Note the gap.
- WebFetch fails: synthesize from search snippets only.
- Telegram fails: still write vault. Log to stderr.

Always send Telegram. Always write vault. Never exit silently.
