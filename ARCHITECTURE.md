# Architecture

## Diagram

```
                            +----------------------+
                            |    Collin (mobile)   |
                            +----------+-----------+
                                       |
                                       | Telegram (read / approve / reply)
                                       |
                            +----------v-----------+
                            |  Telegram Bot API    |
                            |  (human approval)    |
                            +----------+-----------+
                                       |
                                       | plugin:telegram:telegram MCP
                                       |
+----------------+        +------------v------------+        +------------------+
|  Cron Jobs     +------->+  Jarvis (Claude Code)   +<-------+  Webhooks (in)   |
|                |        |  on DigitalOcean VPS    |        |                  |
|  M/W/F 9AM     |        |                         |        |  - Dripify       |
|   linkedin-    |        |  +-------------------+  |        |    /webhook/...  |
|   post         |        |  |  Skill loader     |  |        |    (planned)     |
|                |        |  |  (.claude/        |  |        |                  |
|  Fri 4PM       |        |  |   commands/*)     |  |        |                  |
|   content-     |        |  +---------+---------+  |        +------------------+
|   reflection   |        |            |            |
|                |        |  +---------v---------+  |        +------------------+
|  Sun 8PM       |        |  |  Memory vault     |  |        |  External APIs   |
|   competitive- |        |  |  ~/vault/         |  |        |                  |
|   intel        |        |  |  (Obsidian / git) |  |        |  - Anthropic     |
|                |        |  +-------------------+  |        |  - WebSearch     |
|  Every 1m      |        |                         |        |  - Gmail OAuth   |
|   mcp-watchdog |        |  +-------------------+  |        |  - LinkedIn      |
|                |        |  |  Hooks            |  |        |    (planned)     |
|                |        |  |  - UserPrompt     |  |        |                  |
+----------------+        |  |    Submit (vault  |  |        +--------+---------+
                          |  |    pre-search)    |  |                 ^
                          |  |  - Stop (journal  |  |                 |
                          |  |    append)        |  |                 |
                          |  +-------------------+  |                 |
                          |                         +-----------------+
                          |  +-------------------+  |    outbound: drafts,
                          |  |  Dehumidifier     |  |    intel, reports
                          |  |  (text rewrite)   |  |
                          |  +-------------------+  |
                          +-------------------------+
```

## Data flow

Cron triggers a slash command inside Claude Code. The command runs through the skill loader, reads from the memory vault, and may call WebSearch or other tools. The output gets passed through the dehumidifier ruleset and shipped to me on Telegram.

For inbound events (Dripify webhooks, Telegram replies), the same loop runs in reverse. A FastAPI endpoint or the Telegram MCP receives the event, normalizes it, writes a vault entry, and either pings me or queues work for the next scheduled cron.

The vault is the single source of truth. Everything Jarvis does either reads from or writes to `~/vault/`. The vault is git-synced to GitHub, which makes the same notes available in Obsidian on my phone and laptop.

## Trust model

Nothing is auto-published. Every outbound action that touches a public surface (LinkedIn, email, marketing copy) goes through Telegram for human approval first. The Dripify and LinkedIn auto-post integrations are scaffolded in `handlers/` but gated behind explicit confirmation flows. The trust progression looks like:

1. **Today**: Jarvis drafts. I copy / paste / publish.
2. **After ~30 days of stable drafts**: Jarvis posts to a draft queue. I one-tap approve in Telegram.
3. **Eventually**: Routine posts go out automatically inside guardrails. Anything weighty (case-law analysis, competitive callouts) still gates on me.

The dehumidifier ruleset is the second layer of defense. Even if a model produces a polished-but-wrong draft, the dehumidifier strips the AI tells and an em-dash audit fails the variant before it reaches Telegram.

## Where each component lives

**This repo (jarvis-revival):**
- `skills/` — all slash command definitions (linkedin-post, content-reflection, competitive-intel, dehumidifier, screenshot-ingester, topic-radar, intel-synthesis)
- `prompts/` — system prompts the skills compose at runtime
- `library/` — voice anchors, archetypes, post log, intel log
- `handlers/` — webhook endpoints (FastAPI) for Dripify + LinkedIn
- `crons/` — scheduled job entrypoints
- `demo/` — submission walkthrough

**Jarvis core (lives separately as personal infra, not in this repo):**
- The Claude Code runtime on the VPS
- The plugin:telegram:telegram MCP server
- The memory vault at `~/vault/`
- The 9 pre-existing cron jobs (cleanup, daily-brief, etc.)
- The Gmail OAuth credentials and refresh-token store
