# ROADMAP

What's running today, what's in flight, and what's next for Jarvis as it grows from "marketing automation for caseread.ai" into a full personal-AI infrastructure layer.

The honest line: anything labeled **shipped** runs on the VPS today. Anything **planned** has a real plan and a stub or a doc, but the live behavior is pending one or two prerequisites (an account, a webhook URL, a token, a few hours of code).

---

## Engineering

### 1. `code-regression` — weekly codebase audit
**Status: shipped, runs Sat 12 PM MT.**
Read-only crawl of the caseread codebase. Diffs against last Saturday's snapshot. Flags new routes, migrations, version drift, deleted-but-referenced files, stubs promoted to shipped. Mirrors my hand-written ground-truth doc format.

### 2. `sentry-monitor` — weekly error digest
**Status: shipped, runs Sat 12 PM MT, env-var pending.**
Pulls the past 7 days of Sentry issues, groups by severity, surfaces hot errors and new-this-week regressions. Cleanly emits "not configured" if `SENTRY_AUTH_TOKEN` is unset, so the cron is safe to leave running until the caseread Sentry account is provisioned. The API call path is real, not stubbed.

### 3. `pr-preflight` — pre-PR ground-truth lint
**Status: planned.**
Before I open a PR, runs the codebase ground-truth crawler, lints against `CLAUDE.md` rules, checks for the QC-self-flag bug class history, and surfaces edits to make before review wastes Rey's time. Triggered by a git pre-push hook.

### 4. `regression-sentinel` — recurring-bug class detection
**Status: planned.**
Reads recent diffs, flags patterns that historically introduced bugs. The two known classes today: (a) `claude -p` subprocess invocations missing `TELEGRAM_NO_KILL=1` (the calendar-sync.sh / vault-dump.sh class — three live incidents), and (b) regex-extraction running against rendered output rather than structured input (the QC-self-flagging-template-copy class). Adds new patterns to the watch list as they surface.

---

## Sales / customer

### 5. `customer-onboarding` — beta tester pre-meeting brief
**Status: planned.**
When a beta tester signs up, Jarvis auto-researches them (firm size, practice area, recent cases via OpenLaws + public docket scrapes), drafts a personalized welcome email, and posts a pre-meeting brief to Telegram before the Calendly call.

### 6. `compliance-oracle` — engagement-letter / privilege Q&A draft
**Status: planned.**
Attorney emails asking about caseread's privilege posture, schema-per-firm isolation, ABA Rule 1.6 compliance, or vendor-disclosure language get auto-drafted answers using ABA rules in the vault + the live codebase as ground truth. Drafts to Telegram for approval before reply.

### 7. `customer-feedback-synth` — weekly product-signal digest
**Status: planned.**
Beta feedback from Gmail, Telegram, and the in-app feedback button aggregates to vault. Weekly synthesis: top 3 patterns, prioritized backlog suggestion, and copy that fits the next LinkedIn post. Closes the build → ship → learn loop without me reading 30 inbox threads on Sunday night.

---

## Operations / strategy

### 8. `revenue-pulse` — daily MRR + usage health digest
**Status: planned.**
5-line morning digest: Stripe MRR delta, Supabase usage stats, Vercel deploy frequency, recent Sentry errors. Catches churn spikes, usage anomalies, and deploy regressions before manual review. Predates the Stripe wire-up — this skill ships dormant and activates the moment paid customers exist.

### 9. `cofounder-sync-prep` — auto-prep for Rey calls
**Status: planned.**
Before each scheduled Collin / Rey sync, Jarvis assembles agenda from open Mission Control todos, recent decisions in vault, blocked tasks, and yesterday's git activity. Drops it in a shared doc. Replaces the "what should we cover" pre-call dance.

### 10. `investor-prep` — pre-investor-call briefing
**Status: planned.**
Each scheduled investor call, Jarvis reads the investor's portfolio (from public sources), drafts pre-meeting brief: their thesis, what to emphasize, likely questions, recent portfolio news. Saves 1-2 hours of prep per meeting.

---

## Personal

### 11. `burnout-monitor` — early-warning pattern detection
**Status: shipped (input side), planned (output side).**
The food, weight, and sleep-pattern data already lands in Mission Control daily via the existing `/food` and `/weight` skills. The detection layer (3-day patterns of sub-1500 cal + sub-6h sleep + 2 AM commits triggering a "take tomorrow morning slow" Telegram ping) is planned. Predates the auto-publish trust line: this skill always pings me, never auto-cancels meetings.

---

## Already running (Jarvis core, since Feb 2026)

These predate the hackathon. Listed for completeness so the difference between weekend work and standing infrastructure is visible:

- `daily-brief` — 9:03 AM MT, market intel + status delta
- `morning-digest` — 7:35 AM MT, calendar + top todos + weight + habits
- `nighttime-ideas` — 9:00 PM MT, creative options menu for tomorrow
- `weekly-checkin` — Sun 6:07 PM MT, cross-domain pattern analysis
- `weekly-growth` — Sat 10:00 AM MT, marketing/growth research
- `research-task` — weekday noon, rotating growth topics
- `friday-review` — Fri 5 PM MT, week-over-week summary
- `cleanup` — 3:03 AM MT daily, VPS maintenance
- `calendar-sync` — every 4 hours, Google Calendar to Mission Control
- `mcp-watchdog` — every minute, alerts on Telegram MCP death

---

## How priorities get set

I add a feature when one of three things happens: I notice myself doing the same manual workflow three weeks in a row, a beta tester surfaces a need that isn't a product-feature ask, or a bug recurs and the pattern becomes a class. Speculative builds wait. The repo doesn't grow faster than the lessons do.
