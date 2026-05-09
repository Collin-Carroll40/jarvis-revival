<p align="center">
  <img src="./jarvis-logo.png" alt="Jarvis" width="220">
</p>

<h1 align="center">Jarvis</h1>

<p align="center"><em>My personal assistant. Automates the daily tasks that have to get done so I can spend my time on the work that doesn't yet.</em></p>

<p align="center">
  <img alt="Built for AI Builder Day 2026" src="https://img.shields.io/badge/AI%20Builder%20Day-2026-2b6cb0?style=flat-square">
  <img alt="Powered by Claude" src="https://img.shields.io/badge/Powered%20by-Claude%20Sonnet%204.6-d97706?style=flat-square">
  <img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-22c55e?style=flat-square">
</p>

---

## What this is

A weekend build for AI Builder Day's "Give Yourself a Promotion" hackathon (May 2026).

Jarvis is the persistent Claude Code agent I've been running on a DigitalOcean VPS since February. It's been my chief of staff for months: morning digest at 7:35 AM with calendar + priorities + weight, daily brief at 9:05 AM with market intel and action items, weekly growth research, nighttime ideas, food and weight tracking, vault knowledge capture, code regression scans. The picture below is a real Saturday morning conversation — not a demo, just three back-to-back Jarvis messages I read on my phone before coffee.

<p align="center">
  <img src="./dashboards/jarvis-telegram-morning.jpg" alt="A real Saturday morning with Jarvis on Telegram" width="380">
</p>

This weekend I extended Jarvis into a marketing operations layer for Caseread.ai, my AI legal research product. Same architecture, new skills. The same Jarvis that wakes me up with a digest and tracks my deficit days now also drafts my LinkedIn posts, runs Friday content reflections, pulls Sunday-evening competitive intel, monitors Sentry, and audits the codebase for regressions.

The promotion I gave myself: I fired the version of me that was hand-drafting LinkedIn posts at 11pm and chasing competitive intel by browser tab. Jarvis does that work now. I review, edit, ship. ~10 hours back per week.

> "AI killed cold email. So I revived Jarvis to automate the marketing channels that still work."

## The story

For most of 2025 and into early 2026, cold email worked. We ran an autonomous outreach pipeline against a list of solo and small-firm attorneys for Caseread (then called Lawless). It was the right channel for a while.

Then it wasn't. Bounce rates climbed past 30%. Reply rates collapsed under 0.25%. The mailbox providers got smarter, and cold email got drowned in AI-generated outreach noise. We paused the pipeline on May 1. The OutreachBot repo is archived. That channel is over for us.

The channels that still work for legal-tech founders are LinkedIn content and human-warmed connection campaigns through Dripify. Both demand voice. Both demand consistency. Both eat a founder's time. So I pointed Jarvis at them. The skills in this repo generate LinkedIn drafts in my voice three mornings a week, run a Friday content reflection, and pull a Sunday-evening competitive intel scan. They post nothing without me. I read everything on my phone via Telegram and ship what's worth shipping.

## What I built this weekend

- `linkedin-post` slash command, scheduled M/W/F 9 AM via cron. Generates 3 distinct LinkedIn drafts to Telegram with a diversity rule, a humanizer pass, a zero-em-dash policy, 9 structural templates, and a 23-post voice library as the tone anchor.
- `content-reflection` slash command, scheduled Fri 4 PM. Pulls the week's drafts, summarizes pillar / template / angle distribution, frames an engagement-learning prompt, saves the reflection to the vault.
- `competitive-intel` slash command, scheduled Sun 8 PM. WebSearches legal-AI news from the past 7 days, synthesizes a 3-paragraph Telegram brief on launches / people / funding, saves it to the vault.
- `sentry-monitor` slash command, scheduled Sat 12 PM. Pulls the past 7 days of Sentry issues, groups by severity, surfaces hot errors and new-this-week regressions, writes the report to the vault and sends a mobile digest to Telegram. Status: shipped this weekend, env-var pending Caseread Sentry account integration. Falls back gracefully to a "not configured" message until the token is set.
- `code-regression` slash command, scheduled Sat 12 PM. Read-only crawl of the Caseread codebase (routes, migrations, stack versions, commits, deletions). Diffs against last Saturday's snapshot to flag new routes shipped, migrations added, version drift, deleted-but-still-referenced files, and stubs that got promoted to shipped. Output mirrors the existing hand-written `ground-truth-2026-05-06.md` format. Status: shipped this weekend, functional immediately.
- MCP watchdog (1-min cron) that alerts me directly via the Telegram Bot API if the MCP child process dies.
- Vault-search hook on `UserPromptSubmit`. Pre-loads relevant vault notes before each Jarvis response so context lookups don't burn a turn.
- Journal-append hook on `Stop`. Auto-appends decisions and actions from the conversation to today's daily journal.
- Dehumidifier ruleset, extracted out of `linkedin-post` into a reusable skill. Em-dash zero-tolerance, banned-vocabulary list (delve, leverage, transformative, robust, seamless, unlock, game-changer, revolutionize), no duplicate closers across variants, sentence-fragment injection.

## How Jarvis actually runs

Jarvis is a single Claude Code agent process living in a `tmux` session named `jarvis` on a DigitalOcean droplet. The tmux session is the durability layer — when my SSH connection drops, when I close my laptop, when the network blips, Jarvis keeps running. I attach back when I need to talk to it directly.

Everything else clusters around that one process:

- **Telegram bot interface** — the primary input/output. Claude Code's plugin system (MCP) connects the agent to a Bot API channel I run on my own bot token. Inbound messages arrive as channel events the agent reacts to. Outbound replies go through the same channel. I read and write from my phone.
- **Tailscale** — the dashboard, vault, and SSH access live behind a Tailscale VPN. Mission Control at `100.78.49.99:3333` isn't on the public internet. Only my devices can reach it. No port forwards, no exposed services.
- **Memory vault** — `~/vault/` on the VPS, synced bidirectionally to a private GitHub repo (`second-brain-vault`). My phone runs Obsidian against the same repo. Whatever Jarvis writes to the vault — daily briefs, decisions, vault-search results, journal entries — shows up on my phone within seconds.
- **Skill loader** — every slash command (`/linkedin-post`, `/competitive-intel`, `/code-regression`, etc.) is a single Markdown file in `~/.claude/commands/`. Add a file, get a skill. Hot-reloaded by Claude Code. No build step, no deploy.
- **Cron + sandboxed subprocesses** — scheduled work fires through `cron`, which spawns a short-lived `claude -p "Run /skill"` subprocess. Each subprocess gets its own MCP server lifecycle. The long-running Jarvis poller and the cron-spawned ones coexist via a `TELEGRAM_NO_KILL=1` env var on the cron lines (a fix I patched in May 1 after a bug class where cron-spawned MCP children kept killing the persistent poller's connection).
- **Hooks** — Claude Code fires hooks on `UserPromptSubmit`, `Stop`, `PostCompact`, and `SessionEnd`. The vault-search hook greps the vault for keywords from my prompt and pre-loads the top 5 most-relevant excerpts as context before the agent responds. The journal-append hook appends decisions and action items to today's daily journal automatically. The watchdog hook on `MCP-down` fires a direct Telegram Bot API call (bypassing the dead MCP) so I find out within 60 seconds.
- **MCP watchdog** — a one-minute cron that checks `/proc/<bot.pid>/cwd` to verify the telegram MCP is alive. If it dies (the cron-bug class I patched), the watchdog uses `curl` directly against the Telegram Bot API to alert me. Self-healing was tested in production — it caught the May 6 incident before I would have noticed.
- **Stack** — Claude Sonnet 4.6 for drafting and reasoning, Claude Haiku 4.5 for cheap synthesis tasks (topic evaluation, classification). Python 3.11 + FastAPI for webhook handlers. Bun for Mission Control's React dashboard. Caddy for HTTPS termination on the few exposed surfaces. SQLite for Mission Control's local state.

A technical judge can read this section as the architectural answer to "what makes this more than a chatbot wrapper." It's a real always-on system with backpressure handling, durability, and self-healing — built incrementally over three months and extended this weekend.

## Why Claude Code specifically

Most "AI assistants" are wrappers around a chat API. They can talk about code. They can't see it. They can suggest fixes. They can't apply them. For a technical founder, that gap is the entire difference between a toy and a real assistant.

Jarvis runs on Claude Code, which is structurally different:

- **It can read my code.** Caseread.ai's repo is on the same VPS. The `code-regression` skill walks routes, migrations, package versions, and recent commits every Saturday. It sees what shipped, what broke, what got renamed, what's stale — because the agent has filesystem access, not just an OpenAPI spec.
- **It can change my code.** When I found a false-positive in the outreach pipeline's quality-check layer at 11pm last week, I described it on Telegram. A subagent forked, read the file, identified the regex bug, refactored it, ran the smoke tests, committed, pushed. I approved the diff before the push. The whole loop took 7 minutes.
- **It catches things I'd miss.** The May 1 cron-vs-MCP bug class (where cron-spawned subprocesses kept killing the persistent telegram poller) was diagnosed by a Jarvis investigator agent that crawled the session JSONL, traced the orphaned-PID pattern, and reported back with the exact root cause. I would have burned half a day chasing that one manually.
- **It takes the wheel when I ask.** Telegram message before bed: *"Build the cron, push to GitHub, the hackathon's tomorrow."* I went to sleep. I woke up to a working repo with three commits, a smoke-tested cron, and a Telegram summary. Real subprocess execution, real filesystem, real git operations, real autonomy. Not a chatbot. An operator.

That's where this stops being an LLM in a chat window and starts being an executive assistant. The "Give Yourself a Promotion" hackathon theme stops being a metaphor at that point. Hiring this executive assistant *was* my promotion.

## Mission Control — the secondary dashboard

Telegram is the primary control plane. Mission Control is the secondary one — a self-hosted Bun + React dashboard (Tailscale-only) that visualizes the data Jarvis writes and reads. Health, tasks, calendar, messages, outreach metrics, all in one place, populated from the same source of truth that the cron jobs pull from.

The Health tab below shows live data: 30-day weight trend, 14-day calorie bar chart against the 2,000-cal target, 14-day protein chart against the 150g target. Every food entry logged via `/food` lands here. Every reading from `/weight` lands here. The morning digest cron pulls from this same database.

<p align="center">
  <img src="./dashboards/mission-control-health.jpg" alt="Mission Control — Health tab" width="380">
</p>

Mission Control is part of Jarvis core (pre-existing). Weekend skills write to the same vault and database it reads from, so anything new the LinkedIn / intel / regression skills generate shows up next to the older food and weight data without extra wiring.

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
| Codebase ground-truth audit | 1.0 hrs | 0.0 hrs (auto Sat 12 PM) | 1.0 hrs |
| Sentry error triage | 0.5 hrs | 0.0 hrs (auto Sat 12 PM) | 0.5 hrs |
| **Total** | **~11.5 hrs** | **~1.25 hrs** | **~10.25 hrs** |

### Why this number actually matters

10 hours a week is **520 hours a year** — thirteen 40-hour workweeks. That's the headline.

What it really means: I no longer draft LinkedIn posts at 11pm. I no longer spend Sunday morning catching up on legal-AI news through 30 browser tabs. I no longer burn an hour every Friday trying to remember what I posted that week. The cognitive switching tax — flipping out of "founder building product" mode into "marketer drafting content" mode 12 times a week — is gone. Jarvis owns those shifts. I review on my phone in the elevator and ship.

For a solo founder, the 10 hours isn't the win. The win is having those 10 hours fall in coherent, focused, unbroken blocks. That's what makes the difference between shipping product and shipping content. With Jarvis I get to ship both.

## Architecture

Telegram is the human approval layer. Cron-scheduled skills run inside Jarvis (Claude Code), pull from the memory vault, generate output, and ship it to me on Telegram for review. Webhooks (Dripify, future LinkedIn) flow back the same way. Full diagram and trust model in [ARCHITECTURE.md](./ARCHITECTURE.md).

## Dripify integration

The LinkedIn relationship layer runs through Dripify. The campaign sequence below is the production flow Caseread uses for solo-and-small-firm attorney outreach. Jarvis hooks into the connection-accepted, message-replied, and follow-up-due events and writes them to the memory vault, where the EOD digest cron synthesizes the day into a single Telegram digest.

### Why a third-party SaaS for the actual LinkedIn actions

LinkedIn aggressively flags accounts that look automation-heavy. Direct API automation, headless browser scripts on a VPS, and most homegrown approaches get the account restricted or banned. Dripify exists specifically as a protection layer — they run the connection requests, follows, and messages through their own residential-proxy infrastructure with the rate-limiting and behavioral patterns that keep accounts in good standing.

So I deliberately drew the line: Dripify owns the LinkedIn-touching surface. Jarvis owns content generation, event handling, and the EOD digest. Trying to build the LinkedIn dance into Jarvis directly would have put my actual LinkedIn account at risk. The webhook integration in [`handlers/dripify_webhook.py`](./handlers/dripify_webhook.py) is the bridge between the two.

<p align="center">
  <img src="./handlers/dripify-sequence.jpg" alt="Dripify campaign sequence" width="700">
</p>

The flow:
- Send invite. Branch on Accepted / Still not accepted.
- Accepted path: 1-hour delay, then a 4-message cascade (1 hr / 2 days / 5 days / no-delay branch on viewed-message).
- Not-accepted path: 14-day wait, view profile, 19-day wait, withdraw invite, follow, second invite attempt at 15 days.
- Email-fallback branch when LinkedIn fails: find email, 3 send-email steps with 7-day and 14-day spacing.

The webhook handler that consumes these events lives in [`handlers/dripify_webhook.py`](./handlers/dripify_webhook.py). Currently stubbed — fills in Sunday morning once the Dripify account is provisioned.

## Demo

90-second walkthrough in [DEMO.md](./DEMO.md).

## Repo notes

This repo is the new code from this weekend. Jarvis core (the runtime, the Telegram bot, the memory vault, the skill loader) lives separately as personal infrastructure and is not committed here. Treat this repo as a hackathon-build extension, not the whole stack.

---

License: MIT. See [LICENSE](./LICENSE).
