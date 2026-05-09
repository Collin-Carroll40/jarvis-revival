# Demo — 90 second walkthrough

## The script (word-for-word)

> Hi. I'm Collin. I'm building Caseread.ai, an AI legal research product for solo and small-firm attorneys. For the last three months I've been running a Claude Code agent on a VPS that I talk to through Telegram. I call it Jarvis. It's my personal assistant. It runs my mornings, tracks my food and weight, captures my decisions, and as of this weekend, it runs my marketing.
>
> [Open Telegram on phone, scroll to today's morning thread.]
>
> Saturday morning, before I woke up, Jarvis sent me my daily digest, my market brief, and a Saturday-only weekly growth research synthesis. While I slept. Three back-to-back automated reports, all in my voice, all from cron jobs reading my memory vault and the legal-AI news cycle.
>
> [Scroll up to a LinkedIn-drafts thread from earlier this week.]
>
> Three mornings a week at 9 AM, Jarvis sends me three LinkedIn drafts. Different angles, different tones, different structural templates, all in my voice. The skill reads 23 of my own LinkedIn posts as a tone anchor and runs nine structural templates with a diversity rule on top. Em-dashes are banned. So is "delve", "leverage", "transformative". The audit fails the variant if any of those slip through.
>
> [Tap one variant, copy, paste into LinkedIn.]
>
> Done. Move on. The post that took me forty-five minutes at 11 PM last week takes me thirty seconds in the elevator now.
>
> [Show the time-saved table from `README.md`.]
>
> Adding all of these together, Jarvis saves me about fourteen hours a week. That's seven hundred twenty hours a year. Eighteen 40-hour workweeks. The promotion theme is literal.
>
> [Open `~/.claude/commands/` in the terminal, show one of the skill markdown files.]
>
> The whole reason this scaled so fast is that adding a new skill is one Markdown file plus one cron line. Not a Zapier workflow. Not an n8n flowchart. A markdown file. Friday at 11 PM I asked Jarvis to ship a Sentry monitor and a code-regression skill. Twenty-five minutes later, both were running on a Saturday-noon cron. That's the unlock.
>
> [Close on a beat.]
>
> This isn't a chatbot. It's an executive assistant that reads my code, makes changes, catches things I'd miss, and takes the wheel when I ask. I gave myself a promotion. I hired Jarvis.

## Click sequence

1. Open Telegram on phone, scroll to today's three back-to-back morning messages (digest + brief + weekly growth)
2. Scroll up to a recent `/linkedin-post` drafts thread, highlight the timestamp + the three labelled variants
3. Tap one variant, demo the copy-to-clipboard flow
4. Switch to laptop, open `README.md` time-saved section, point at the **~14.25 hrs/week saved** total
5. Open `~/.claude/commands/linkedin-post.md` in the terminal, show that the entire skill is a single Markdown file
6. Close on the **Why Claude Code specifically** section in `README.md` and read the closer line aloud: "I gave myself a promotion. I hired Jarvis."

If asked to go deeper, drill into:
- `ARCHITECTURE.md` for the data flow + trust model
- `dashboards/mission-control-health.jpg` for the secondary dashboard
- `handlers/dripify-sequence.jpg` for the Dripify campaign integration
- The `skills/dehumidifier.md` ruleset

## Time saved talking point

| Task | Before | After | Saved |
|---|---|---|---|
| LinkedIn drafting (3 posts/week) | 4.5 hrs | 0.5 hrs (review only) | 4.0 hrs |
| Connection follow-up triage | 1.5 hrs | 0.25 hrs | 1.25 hrs |
| Competitive intel scanning | 3.0 hrs | 0.25 hrs | 2.75 hrs |
| Content reflection / planning | 1.0 hrs | 0.25 hrs | 0.75 hrs |
| Codebase ground-truth audit | 1.0 hrs | 0.0 hrs (auto Sat 12 PM) | 1.0 hrs |
| Sentry error triage | 0.5 hrs | 0.0 hrs (auto Sat 12 PM) | 0.5 hrs |
| Ad-hoc agent dispatch (bug fixes, code edits, research scans) | 2.5 hrs | 0.5 hrs (review only) | 2.0 hrs |
| Health logging (food/weight via Telegram, voice memos transcribed + processed) | 1.0 hrs | 0.0 hrs | 1.0 hrs |
| Daily journal + decision capture (auto-append hook) | 0.5 hrs | 0.0 hrs | 0.5 hrs |
| Vault knowledge lookup (auto pre-loaded into every prompt) | 0.5 hrs | 0.0 hrs | 0.5 hrs |
| **Total** | **~16 hrs** | **~1.75 hrs** | **~14.25 hrs** |

Direct quote on stage: "I was spending about sixteen hours a week on operations work. LinkedIn drafting, follow-up triage, competitive scanning, codebase audits, error triage, food logging, journal capture. Jarvis handles all of it now. I review on my phone in the elevator and ship. The fourteen hours go back into product. That's eighteen workweeks a year I get back."

When the future-feature backlog ships (auto-newsletter, direct LinkedIn auto-post, Oura ring integration, multi-inbox triage), the projected total reaches **~21 hrs/week saved**, which is roughly half a full-time hire's annual capacity.

## Anticipated judge questions

### Q1. How much of this did you build at the hackathon vs. before?

Honest answer. Jarvis core (the Claude Code runtime, the Telegram bot interface, the memory vault, the skill loader, the Gmail OAuth, and 9 pre-existing daily / weekly cron jobs) has been running since February 2026. That's pre-existing personal infrastructure.

What I shipped this weekend: nine new skills and infrastructure pieces — `linkedin-post`, `content-reflection`, `competitive-intel`, `sentry-monitor`, `code-regression`, the dehumidifier ruleset extracted into a reusable skill, the MCP watchdog, and the two new hooks (vault-search on prompt submit, journal-append on stop). The README has the full breakdown under "What I built this weekend" vs. "Pre-existing".

The hackathon theme is "Give yourself a promotion." The work this weekend was promoting Jarvis from a personal-life agent to a full marketing-and-engineering operations agent. That extension is the build.

### Q2. What if the model goes down or hallucinates a bad post?

Two layers of defense.

**Layer 1: human approval.** Nothing posts to LinkedIn or any public surface without me tapping approve. The output goes to Telegram. I read it on my phone. I copy and paste. The auto-poster handler is scaffolded in the repo but gated behind a manual confirmation flow, and it's labeled stubbed.

**Layer 2: dehumidifier.** Before any draft reaches Telegram, it runs through the dehumidifier ruleset. Em-dash zero-tolerance audit fails the variant. Banned-vocabulary list (delve, leverage, transformative, robust, seamless, unlock, game-changer, revolutionize) fails the variant. Duplicate closers across variants fail the variant. The skill rewrites until it passes or returns an honest "couldn't draft this round, here's why" to Telegram.

If Anthropic's API itself is down, the cron fails loudly, the watchdog pings me on Telegram via direct Bot API curl, and I skip a day. The product I'm marketing is more important than hitting a posting cadence.

### Q3. Why not just use Buffer, Hootsuite, n8n, or Zapier?

Three reasons.

**Voice fidelity.** Buffer schedules. It doesn't write. Every social-scheduling tool I've evaluated either generates generic AI slop or asks me to write the post myself, which is the work I was trying to outsource. Jarvis writes in my voice because the prompt anchors on 23 of my actual posts and runs a humanizer pass that strips polish-tells until the draft reads like I typed it on my phone.

**Vault integration.** The drafts pull from my product memory, my decisions log, my competitive intel. A social tool can't do that. When Jarvis writes a post about Heppner v. Rakoff or about my schema-per-firm architecture, it's pulling from notes I wrote. The voice and the substance both come from inside.

**Build speed.** Adding a new Jarvis skill is one Markdown file plus one cron line — twenty-five minutes from "can we do this" to "it's running on schedule." The same job in n8n or Zapier is an afternoon of clicking through nodes plus debugging JSON-path expressions. Owned automation in the agent layer beats rented automation in the SaaS layer once you're running enough channels for it to compound.

### Q4. Could a non-technical person actually use this?

Yes — because writing a Jarvis skill is closer to writing a memo than writing code. The skill file is plain English describing the steps, the tools the agent is allowed to use, and where the output goes. Hot-reloaded by Claude Code. No build step, no deploy, no Docker, no DSL.

The "non-developers especially welcome" line in the hackathon brief points at exactly this. Jarvis lowers the bar from "I need to wire seven nodes together" to "I need to write a paragraph describing what I want done." That's the difference between an automation tool and an executive assistant.
