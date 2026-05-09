"""
topic_radar.py — hourly news scan and newsworthiness filter for Pillar C drafts.

Status: STUBBED 2026-05-09. Logic to be filled later (planned, not Sunday).

Pipeline role:
    Runs every hour, weekdays 7 AM to 7 PM Mountain. Pulls the latest legal-tech
    / legal-AI news, filters to fresh + relevant items, scores each candidate
    via Claude Haiku against the rubric in prompts/topic_evaluation.md, and pings
    Collin on Telegram only if a story scores >= 7. On thumbs-up reaction, the
    telegram_handler writes the inspiration file that the next M/W/F drafting
    run picks up.

    The whole point is to surface hot stories ahead of the M/W/F drafting cycle
    so Pillar C posts are timely, without pinging Collin on dead hours.

Depends on:
    - Env vars: ANTHROPIC_API_KEY (Haiku calls), TELEGRAM_BOT_TOKEN,
      TELEGRAM_CHAT_ID
    - External services: Claude API (Haiku), some news/search source (likely
      WebSearch via the Claude Code runtime in Jarvis core)
    - Python deps: anthropic, httpx, python-dotenv

Public surface:
    def main() -> int
    async def evaluate_candidate(headline: str, url: str, snippet: str, recent_history: list[str]) -> dict

TODO (later, not Sunday):
    - Decide news source: use Claude Code's WebSearch via skill invocation,
      or wire a dedicated news API (NewsAPI, GDELT, Google News RSS)
    - Implement evaluate_candidate: load prompts/topic_evaluation.md as the
      system prompt, call Haiku with the candidate, parse the JSON response
    - Implement deduplication against the last 14 days of Pillar C draft
      throughlines from ~/vault/04-projects/lawless-ai/linkedin/
    - Implement Telegram alert format with thumbs-up / thumbs-down ask
    - Add a daily cap: max 3 alerts per day, even if more candidates clear
      threshold. Quiet > spammy.
    - Cost-monitor wrapper: track Haiku spend per day, alert if it crosses $0.50
"""

import sys


def main() -> int:
    # TODO (later, not Sunday): run the hourly radar.
    raise NotImplementedError(
        "topic_radar.main not implemented yet. Skill is planned. See docstring."
    )


async def evaluate_candidate(
    headline: str, url: str, snippet: str, recent_history: list[str]
) -> dict[str, object]:
    # TODO: load topic_evaluation.md, call Haiku, parse JSON.
    raise NotImplementedError("evaluate_candidate not implemented.")


if __name__ == "__main__":
    sys.exit(main())
