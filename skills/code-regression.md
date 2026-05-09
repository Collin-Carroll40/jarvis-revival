# Skill: code-regression

Status: shipped this weekend, functional immediately.

## Where this fits in Jarvis

Jarvis already keeps a hand-written ground-truth file at `~/vault/04-projects/lawless-ai/ground-truth-2026-05-06.md`. That file was useful, and stale within a week. This skill replaces the hand-write with an automatic Saturday crawl. It walks the Caseread codebase, snapshots routes / migrations / stack versions / commit themes, and diffs against the prior week's snapshot. The diff catches new routes shipped, new migrations, version drift, deletions, and stub-to-shipped promotions.

The point is keeping Jarvis honest about the product's actual state. LinkedIn posts can quietly drift to claiming features that aren't shipped. Competitive intel needs a real picture of what's in the codebase. This skill is the read-only ground-truth feed every other skill can lean on.

Same vault format as the May 6 hand-written snapshot, so the historical record stays consistent.

## Cron

```
0 12 * * 6 cd /home/claude && TELEGRAM_NO_KILL=1 /home/claude/.nvm/versions/node/v22.22.1/bin/claude -p "Run /code-regression" --allowedTools "Bash,Read,Write,Glob,Grep,mcp__plugin_telegram_telegram__reply" 2>&1 >> /home/claude/logs/code-regression.log
```

Saturday 12:00 PM MT.

## Purpose

Crawl the Caseread.ai codebase, write a ground-truth snapshot, diff against last week, and surface what shipped, what broke, and what drifted.

## Inputs

- **Codebase root:** `~/projects/Lawless.ai/` by default. Prefers `~/projects/caseread.ai/` if it exists (post-rebrand directory rename).
- **Reference format:** `~/vault/04-projects/lawless-ai/ground-truth-2026-05-06.md` for section structure.
- **Previous snapshot:** most recent `~/vault/04-projects/lawless-ai/code-regression/regression-*.md`.

## Outputs

- One markdown snapshot at `~/vault/04-projects/lawless-ai/code-regression/regression-YYYY-MM-DD.md` with frontmatter (date, window, codebase_root, prev_snapshot) and full sections.
- One Telegram digest to chat_id `8169002246`, 5-8 lines, mobile-first.
- Silent best-effort git commit.

## Steps

1. **Set up.** Get today's date. Resolve codebase root. `mkdir -p` the regression dir. Find the most recent prior `regression-*.md`.
2. **Crawl.**
   - Top-level `CLAUDE.md` (line count, mtime).
   - `package.json` (`name`, `version`, key deps and pinned versions).
   - `supabase/migrations/*.sql` (count, newest filename + mtime, last 5).
   - `src/app/` walk. Build a sorted route list (page paths and API routes).
   - `git log --since="7 days ago"` (one-liners, total commits, files changed).
   - Deletions/renames in last 7 days.
3. **Diff.** Compare against the previous snapshot file:
   - New routes shipped (in this week, not in last).
   - Removed routes.
   - New migrations (filename order).
   - Stack version drift (per dep).
   - Deleted/renamed files + grep for lingering references in still-active code.
   - Promoted-from-stub-to-shipped (heuristic, conservative).
4. **Build digest.** 5-8 lines, headline + 1-2 most significant changes with file refs + concern line + file path.
5. **Save vault file** mirroring the `ground-truth-2026-05-06.md` section structure.
6. **Send Telegram.**
7. **Git commit** the regression dir, best-effort.

## First-run behavior

No previous snapshot to diff against. Skill writes a baseline file and Telegram digest reads "First snapshot. Baseline written. Diff begins next Saturday." This is correct behavior, not a failure.

## AI tells (same as `/linkedin-post`)

Em-dash zero tolerance. Banned vocab: `delve`, `leverage`, `transformative`, `robust`, `seamless`, `unlock`, `game-changer`, `revolutionize`, `synergy`. No three-item parallel rhetorical lists. Plain ops voice.

## Hard rules

1. Read-only on the codebase. Never modify source files.
2. Always write the vault file. Always send Telegram, even on a quiet week.
3. If the codebase root doesn't exist, send Telegram error and exit 0.
4. First snapshot is valid output. Don't pad with fake diffs.
5. Honor the AI-tells blacklist in vault and Telegram output.

## Failure modes

- Codebase root missing: Telegram error, exit 0.
- `package.json` malformed: record "unparseable", continue.
- `git log` fails: skip commit-themes section.
- Previous-week file missing: mark "first snapshot", write baseline.
- Vault git commit fails: log to stderr, don't block.

## Honest accounting

Functional immediately. First Saturday run is a baseline. Second Saturday onward is the real diff. The skill cross-references deletions against still-active code with `grep`, which is a heuristic rather than a static analyzer, so the "lingering references" call-out is best-effort. Anything flagged needs a human read before action.
