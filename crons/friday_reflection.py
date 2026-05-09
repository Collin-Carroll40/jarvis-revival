"""
friday_reflection.py — entrypoint for the Friday 4 PM content-reflection cron.

Status: STUBBED 2026-05-09. Logic to be filled by Collin Sunday morning.

Pipeline role:
    Cron triggers this file at 4:00 PM Mountain on Friday. Invokes the
    content-reflection skill inside Claude Code, which walks the last 7 / 14 / 30
    days of LinkedIn drafts, builds the pillar / template / angle distribution,
    identifies cold templates and cold angles, and ships a 12-15 line digest
    to Telegram. The output also lands in ~/vault/04-projects/lawless-ai/
    linkedin/_reflections/.

    Closes the loop on the M/W/F drafting cycle. Without this, the drafting
    cron drifts into the same pillar / template combinations week after week.

Depends on:
    - Env vars: ANTHROPIC_API_KEY, TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID
    - External services: Claude Code skill runner, Telegram Bot API, vault
    - Python deps: httpx, python-dotenv

Public surface:
    def main() -> int

TODO Sunday:
    - Mirror morning_post.py's invocation pattern (shell out to claude-code
      with /content-reflection)
    - On failure, send Telegram message with exit code + stderr
    - Special-case the quiet-week branch: if the skill reports zero drafts in
      the last 7 days, don't treat that as a failure. The skill already handles
      the honest-quiet-week message. Just exit 0.
"""

import sys


def main() -> int:
    # TODO Sunday: invoke content-reflection skill, handle failure.
    raise NotImplementedError(
        "friday_reflection.main not implemented yet. See module docstring TODO."
    )


if __name__ == "__main__":
    sys.exit(main())
