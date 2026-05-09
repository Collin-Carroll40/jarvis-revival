# Demo — 90 second walkthrough

## The script (word-for-word)

> Hi. I'm Collin. I'm building Caseread.ai, an AI legal research product for solo and small-firm attorneys. For the last six months I've been running my life off a Claude Code agent on a VPS that I talk to through Telegram. I call it Jarvis.
>
> [Open Telegram on phone, scroll to the morning's draft thread.]
>
> This morning at 9 AM, Jarvis sent me three LinkedIn drafts. Different angles, different tones, different structural templates, all in my voice. They came from a skill that reads 23 of my own LinkedIn posts as a tone anchor and runs nine structural templates with a diversity rule on top. Em-dashes are banned. So is "delve", "leverage", "transformative". The audit fails the variant if any of those slip through.
>
> [Tap one variant, copy, paste into LinkedIn. Done. Move on.]
>
> Friday afternoon, Jarvis sends me a content reflection. Pillar mix this week, template mix, what angles haven't appeared in 30 days, three questions for me to sit with. Sunday evening, a competitive intel scan of legal AI hits my phone. Three paragraphs. Launches, hires, funding. With sources.
>
> [Show the architecture diagram from ARCHITECTURE.md.]
>
> The whole thing is cron jobs that talk to Claude Code that talks to my memory vault. Every action that touches a public channel comes through Telegram for me to approve. Nothing posts without me.
>
> Before this weekend, I was hand-drafting LinkedIn at 11 PM and chasing competitive intel by browser tab. About 10 hours a week of marketing-ops work. I gave that job to Jarvis. The promotion is mine.

## Click sequence

1. Open Telegram on phone, scroll to today's drafts message
2. Highlight the timestamp (9:00 AM) and the three labelled variants
3. Tap one variant, demo the copy-to-clipboard flow
4. Show the Friday content-reflection thread
5. Show the Sunday competitive-intel thread
6. Open `ARCHITECTURE.md` on laptop, walk the diagram top-to-bottom
7. Show the dehumidifier section in `skills/dehumidifier.md` and the banned-vocab list
8. Close on the time-saved table from `README.md`

## Time saved talking point

Direct quote: "I was spending about 10 hours a week on marketing operations work. Drafting LinkedIn, triaging follow-ups, scanning competitor news, planning my content calendar. Jarvis handles all of that now. I review and ship. The 10 hours go back into product."

| Task | Before | After | Saved |
|---|---|---|---|
| LinkedIn drafting (3 posts/week) | 4.5 hrs | 0.5 hrs (review only) | 4.0 hrs |
| Connection follow-up triage | 1.5 hrs | 0.25 hrs | 1.25 hrs |
| Competitive intel scanning | 3.0 hrs | 0.25 hrs | 2.75 hrs |
| Content reflection / planning | 1.0 hrs | 0.25 hrs | 0.75 hrs |
| **Total** | **~10 hrs** | **~1.25 hrs** | **~8.75 hrs** |

## Anticipated judge questions

### Q1. How much of this did you build at the hackathon vs. before?

Honest answer: Jarvis core (the Claude Code runtime, the Telegram bot interface, the memory vault, the skill loader, the Gmail OAuth, and 9 pre-existing daily / weekly cron jobs) has been running since February 2026. That's pre-existing personal infrastructure.

What I shipped this weekend: the three marketing-ops skills (`linkedin-post`, `content-reflection`, `competitive-intel`), the dehumidifier ruleset, the MCP watchdog, and the two new hooks (vault-search on prompt submit, journal-append on stop). The README has the full breakdown under "What I built this weekend" vs. "Pre-existing".

I didn't fake a from-scratch build. The promotion theme is "give yourself a promotion", and the work this weekend was promoting Jarvis from a personal-life agent to a marketing-operations agent. That extension is the build.

### Q2. What if the model goes down or hallucinates a bad post?

Two layers of defense.

**Layer 1: human approval.** Nothing posts to LinkedIn or any public surface without me tapping approve. The output goes to Telegram. I read it on my phone. I copy and paste. The auto-poster handler is scaffolded in the repo but gated behind a manual confirmation flow, and it's labeled stubbed.

**Layer 2: dehumidifier.** Before any draft reaches Telegram, it runs through the dehumidifier ruleset. Em-dash zero-tolerance audit fails the variant. Banned-vocabulary list (delve, leverage, transformative, robust, seamless, unlock, game-changer, revolutionize) fails the variant. Duplicate closers across variants fail the variant. The skill rewrites until it passes or returns an honest "couldn't draft this round, here's why" to Telegram.

If Anthropic's API itself is down, the cron fails loudly, the watchdog pings me on Telegram, and I skip a day. The product I'm marketing is more important than hitting a posting cadence.

### Q3. Why not just use Buffer or Hootsuite or some social-scheduling competitor?

Three reasons.

**Voice fidelity.** Buffer schedules. It doesn't write. Every social-scheduling tool I've evaluated either generates generic AI slop or asks me to write the post myself, which is the work I was trying to outsource. Jarvis writes in my voice because the prompt anchors on 23 of my actual posts and runs a humanizer pass that strips polish-tells until the draft reads like I typed it on my phone.

**Vault integration.** The drafts pull from my product memory, my decisions log, my competitive intel. A social tool can't do that. When Jarvis writes a post about Heppner v. Rakoff or about my schema-per-firm architecture, it's pulling from notes I wrote. The voice and the substance both come from inside.

**Ownership.** This is my agent. I run it. I extend it. The skills are markdown files I can edit on a flight without a vendor login. When a new channel matters next month (Discord communities, podcast outreach, whatever), I write a skill. I don't wait for a feature.

That's the bet. Owned automation in the agent layer beats rented automation in the SaaS layer once you're running enough channels for it to compound.
