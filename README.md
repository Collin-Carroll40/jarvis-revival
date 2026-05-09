> "AI killed cold email. So I revived Jarvis to automate the marketing channels that still work."

## What this is

A weekend build for AI Builder Day's "Give Yourself a Promotion" hackathon (May 2026).

Jarvis is the persistent Claude Code agent I run on a VPS. It already handled my daily life (calendar, todos, journaling, briefings). This weekend I extended it into a marketing operations layer for Caseread.ai, my AI legal research product.

The promotion I gave myself: I fired the version of me that was hand-drafting LinkedIn posts at 11pm and chasing competitive intel by browser tab. Jarvis does that work now. I review, edit, ship.

## The story

For most of 2025 and into early 2026, cold email worked. We ran an autonomous outreach pipeline against a list of solo and small-firm attorneys for Caseread (then called Lawless). It was the right channel for a while.

Then it wasn't. Bounce rates climbed past 30%. Reply rates collapsed under 0.25%. The mailbox providers got smarter, and cold email got drowned in AI-generated outreach noise. We paused the pipeline on May 1. The OutreachBot repo is archived. That channel is over for us.

The channels that still work for legal-tech founders are LinkedIn content and human-warmed connection campaigns through Dripify. Both demand voice. Both demand consistency. Both eat a founder's time. So I pointed Jarvis at them. The skills in this repo generate LinkedIn drafts in my voice three mornings a week, run a Friday content reflection, and pull a Sunday-evening competitive intel scan. They post nothing without me. I read everything on my phone via Telegram and ship what's worth shipping.

## What I built this weekend

- `linkedin-post` slash command, scheduled M/W/F 9 AM via cron. Generates 3 distinct LinkedIn drafts to Telegram with a diversity rule, a humanizer pass, a zero-em-dash policy, 9 structural templates, and a 23-post voice library as the tone anchor.
- `content-reflection` slash command, scheduled Fri 4 PM. Pulls the week's drafts, summarizes pillar / template / angle distribution, frames an engagement-learning prompt, saves the reflection to the vault.
- `competitive-intel` slash command, scheduled Sun 8 PM. WebSearches legal-AI news from the past 7 days, synthesizes a 3-paragraph Telegram brief on launches / people / funding, saves it to the vault.
- MCP watchdog (1-min cron) that alerts me directly via the Telegram Bot API if the MCP child process dies.
- Vault-search hook on `UserPromptSubmit`. Pre-loads relevant vault notes before each Jarvis response so context lookups don't burn a turn.
- Journal-append hook on `Stop`. Auto-appends decisions and actions from the conversation to today's daily journal.
- Dehumidifier ruleset, extracted out of `linkedin-post` into a reusable skill. Em-dash zero-tolerance, banned-vocabulary list (delve, leverage, transformative, robust, seamless, unlock, game-changer, revolutionize), no duplicate closers across variants, sentence-fragment injection.

## Pre-existing (Jarvis core, running since Feb 2026)

This repo extends a runtime I've been running for months. None of the following was built this weekend:

- Persistent Claude Code on a DigitalOcean VPS
- Telegram bot interface (`plugin:telegram:telegram` MCP)
- Memory vault at `~/vault/`, Obsidian-synced via GitHub
- Skill loader (Claude Code's built-in slash command system)
- Authenticated Gmail OAuth, originally wired for the OutreachBot cold-email pipeline, now repurposed
- 9 daily and weekly cron jobs that pre-date this weekend (cleanup, daily-brief, morning-digest, nighttime-ideas, weekly-checkin, weekly-growth, research-task, friday-review, calendar-sync)

## Time saved per week

| Task | Before | After | Saved |
|---|---|---|---|
| LinkedIn drafting (3 posts/week) | 4.5 hrs | 0.5 hrs (review only) | 4.0 hrs |
| Connection follow-up triage | 1.5 hrs | 0.25 hrs | 1.25 hrs |
| Competitive intel scanning | 3.0 hrs | 0.25 hrs | 2.75 hrs |
| Content reflection / planning | 1.0 hrs | 0.25 hrs | 0.75 hrs |
| **Total** | **~10 hrs** | **~1.25 hrs** | **~8.75 hrs** |

Roughly 10 hours back per week.

## Architecture

Telegram is the human approval layer. Cron-scheduled skills run inside Jarvis (Claude Code), pull from the memory vault, generate output, and ship it to me on Telegram for review. Webhooks (Dripify, future LinkedIn) flow back the same way. Full diagram and trust model in [ARCHITECTURE.md](./ARCHITECTURE.md).

(Note: the architecture diagram lives in `ARCHITECTURE.md` as ASCII. I didn't generate a PNG for the demo folder; the ASCII version is the source of truth.)

## Stack

- Claude Sonnet 4.6 (drafting + reasoning) and Claude Haiku 4.5 (cheap synthesis tasks)
- Python 3.11 + FastAPI for webhook handlers
- Telegram Bot API for the human-in-the-loop layer
- Dripify (planned) for LinkedIn relationship automation
- DigitalOcean VPS + Caddy for the always-on runtime

## Demo

90-second walkthrough in [DEMO.md](./DEMO.md).

## Repo notes

This repo is the new code from this weekend. Jarvis core (the runtime, the Telegram bot, the memory vault, the skill loader) lives separately as personal infrastructure and is not committed here. Treat this repo as a hackathon-build extension, not the whole stack.

## What's next

Sunday morning: sign up for Dripify and wire the connection-event webhook in `handlers/dripify_webhook.py`. After that, build the screenshot-ingestion mechanism so I can grow the style library by forwarding posts to Telegram. Schedule the topic radar cron once the news API budget settles. The LinkedIn auto-poster stays gated behind manual approval until I've earned the trust to flip the switch.

---

License: MIT. See [LICENSE](./LICENSE).
