# Skill: sentry-monitor

Status: shipped this weekend (env-var pending Caseread Sentry account integration).

## Where this fits in Jarvis

Jarvis is a chief-of-staff layer over Caseread.ai. It already drafts LinkedIn copy, runs the Friday content reflection, and pulls a Sunday competitive scan. This skill closes the loop on the engineering side. Sentry sees production errors. Jarvis pulls them weekly, groups them, picks out what's hot, and writes a mobile-friendly digest to Telegram. The full report lands in the vault next to every other Caseread artifact, which means LinkedIn drafts, growth research, and reliability data all live in one searchable tree.

The skill is wired and shippable. Caseread's Sentry account integration is the last mile. Setting `SENTRY_AUTH_TOKEN` in the Telegram channel env file flips it from "not configured" to fully live without any code change.

## Cron

```
0 12 * * 6 cd /home/claude && TELEGRAM_NO_KILL=1 /home/claude/.nvm/versions/node/v22.22.1/bin/claude -p "Run /sentry-monitor" --allowedTools "Bash,Read,Write,Glob,Grep,WebFetch,mcp__plugin_telegram_telegram__reply" 2>&1 >> /home/claude/logs/sentry-monitor.log
```

Saturday 12:00 PM MT.

## Purpose

Run a weekly Sentry error scan for the Caseread.ai (still labeled `lawless-ai` in code) production app. Surface what broke this week, what's hot, and what's new vs ongoing. Send a concise digest to Telegram and save the full report to the vault.

## Inputs

- **`SENTRY_AUTH_TOKEN`** (env var, required to fetch live data). If unset, the skill skips API work and sends a one-line "not configured" message.
- **`SENTRY_ORG_SLUG`** (env var, optional). Default: `caseread`.
- Today's date in MT.

## Outputs

- One markdown report at `~/vault/04-projects/lawless-ai/sentry/sentry-YYYY-MM-DD.md` with frontmatter, headline, severity breakdown, hot errors, new-this-week section, and a recommendation block.
- One Telegram digest to chat_id `8169002246`, mobile-first, 8-12 lines max.
- Silent best-effort git commit.

## Steps

1. **Token check.** If `SENTRY_AUTH_TOKEN` is empty, send a single Telegram message ("Sentry monitor: SENTRY_AUTH_TOKEN not configured. Skill shipped + ready to wire.") and exit 0. No vault write.
2. **Fetch.** `GET https://sentry.io/api/0/organizations/{org}/issues/?statsPeriod=7d&query=is:unresolved&limit=100` with `Authorization: Bearer $SENTRY_AUTH_TOKEN`. Org from `SENTRY_ORG_SLUG`, default `caseread`.
3. **Parse + group.** Pull `id`, `shortId`, `title`, `culprit`, `permalink`, `level`, `count`, `userCount`, `firstSeen`, `lastSeen`, `status`, `isUnhandled`. Group by severity. Identify hot (>100 events 7d), new-this-week (firstSeen inside window), and ongoing.
4. **Build digest.** Headline + severity breakdown + top 3 hot + new-this-week list + recommendation. 8-12 lines.
5. **Recommendation rules** (priority order):
   - Any `fatal` with count >50 → "Fatal hot. Investigate <shortId> first."
   - Any `error` with count >500 → "High-volume error <shortId>. Likely user-facing."
   - 5+ new-this-week issues → "5+ regressions surfaced this week. Worth a sweep."
   - Otherwise → "Nothing urgent. Backlog grooming optional."
6. **Save vault file** at `~/vault/04-projects/lawless-ai/sentry/sentry-YYYY-MM-DD.md` with frontmatter (date, window, org, total_events, unresolved_issues, new_this_week) and full sections (headline, severity, hot, new, ongoing, recommendation, notes).
7. **Send Telegram.**
8. **Git commit** the vault dir, best-effort.

## AI tells (same as `/linkedin-post`)

Em-dash zero tolerance. Banned vocab: `delve`, `leverage`, `transformative`, `robust`, `seamless`, `unlock`, `game-changer`, `revolutionize`, `synergy`. No three-item parallel rhetorical lists. No marketing voice. Plain ops report.

## Hard rules

1. If `SENTRY_AUTH_TOKEN` is unset, send the "not configured" Telegram message and exit 0. Never fabricate Sentry data.
2. Never include the raw token in any output.
3. Always send Telegram, even on a clean week.
4. Honor the AI-tells blacklist in vault and Telegram output.

## Failure modes

- Token unset: graceful skip with the "not configured" message. Honest by design.
- Sentry API error: send Telegram with status code, write a stub vault file with the failure recorded, exit 0.
- Vault dir missing: `mkdir -p`.
- Git fails: log to stderr, don't block.

## Honest accounting

The skill is shipped this weekend, runs this Saturday, and will send the "not configured" message until the env var is set. Once Caseread's Sentry account is provisioned and the token lands in `~/.claude/channels/telegram/.env`, the next Saturday cron flips to live data. No code change required at that point.
