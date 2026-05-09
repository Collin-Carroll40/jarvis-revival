"""
morning_post.py — entrypoint for the M/W/F 9 AM linkedin-post-generator cron.

Status: STUBBED 2026-05-09. Logic to be filled by Collin Sunday morning.

Pipeline role:
    Cron triggers this file at 9:00 AM Mountain on Monday, Wednesday, Friday. The
    file invokes the linkedin-post-generator skill inside Claude Code on the VPS,
    which produces three LinkedIn post variants and ships them to Telegram for
    review. This file is the thin Python shim around the slash command call: it
    sets the right env, runs the skill, captures the exit code, and pings Collin
    if the run failed.

    Today the actual skill execution is handled by Claude Code's slash command
    runner inside Jarvis core (which lives outside this repo). This file is the
    documented entrypoint that the cron line points at, plus the failure-handling
    wrapper.

Depends on:
    - Env vars: ANTHROPIC_API_KEY (used by Claude Code), TELEGRAM_BOT_TOKEN,
      TELEGRAM_CHAT_ID
    - External services: Claude Code skill runner, Telegram Bot API,
      vault filesystem at ~/vault
    - Python deps: httpx, python-dotenv

Public surface:
    def main() -> int  (exit code; 0 = success, non-zero = failure caught by cron)

TODO Sunday:
    - Decide on the skill-invocation mechanism. Options:
      (a) shell out to the existing claude-code CLI with the slash command name
      (b) call the Anthropic API directly with the skill's system prompt loaded
      Option (a) keeps parity with the manual-run flow Collin already uses.
    - On failure, send a Telegram message to TELEGRAM_CHAT_ID with the exit code
      and the last 20 lines of stderr. Failure should be loud, not silent.
    - Add a guardrail: if the previous M/W/F run produced a draft file but the
      Notes section is missing required keys, exit 0 with a Telegram warning
      rather than retrying. The drafting cron should not double-post on a fix.
"""

import sys


def main() -> int:
    # TODO Sunday: invoke the linkedin-post-generator skill, handle failure paths.
    raise NotImplementedError(
        "morning_post.main not implemented yet. See module docstring TODO."
    )


if __name__ == "__main__":
    sys.exit(main())
