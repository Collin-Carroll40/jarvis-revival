"""
linkedin_poster.py — outbound LinkedIn post handler. GATED behind manual approval.

Status: STUBBED 2026-05-09. Logic to be filled by Collin once the trust gate
opens (target: ~30 days of stable drafts in production).

Pipeline role:
    The trust progression for this repo is:
      1. Today: Jarvis drafts. Collin copy/pastes. Nothing posts automatically.
      2. After ~30 days of stable drafts: Jarvis posts to a draft queue. Collin
         one-tap approves on Telegram. This handler runs the approved post.
      3. Eventually: Routine posts go out automatically inside guardrails.
         Anything weighty (case-law analysis, competitive callouts) still gates.

    This file is the queue executor. It only fires when the linkedin-post-generator
    has tagged a variant as approved AND Collin has confirmed via a Telegram
    reaction. Even then, the dehumidifier runs one more pass before publishing.

Depends on:
    - Env vars: LINKEDIN_OAUTH_CLIENT_ID, LINKEDIN_OAUTH_CLIENT_SECRET,
      LINKEDIN_OAUTH_REFRESH_TOKEN
    - External services: LinkedIn API v2 (Posts endpoint), the dehumidifier skill
    - Python deps: httpx, pydantic

Public surface:
    async def post_to_linkedin(draft_path: str, variant: str) -> dict
    async def confirm_then_post(chat_id: str, message_id: str, draft_path: str, variant: str) -> dict

TODO (when the gate opens, not Sunday):
    - Apply for LinkedIn API access (the Marketing Developer Platform is the
      relevant program; the personal /me/posts endpoint may suffice for solo use)
    - Implement OAuth refresh-token flow
    - Implement post_to_linkedin: read the draft file, extract the chosen variant,
      run the dehumidifier one more time, POST to LinkedIn, log the URL back to
      ~/projects/jarvis-revival/library/post-log.md
    - Implement confirm_then_post: wait for an explicit thumbs-up reaction on the
      Telegram approval message before posting. No silent ship.
    - Add a kill switch: an env flag LINKEDIN_AUTOPOST_ENABLED that defaults to
      false. The gate only opens when Collin flips it explicitly.
    - Log every post attempt (success or failure) to a vault audit trail
"""


async def post_to_linkedin(draft_path: str, variant: str) -> dict[str, str]:
    # TODO when the gate opens. Until then, this raises so accidental imports fail loud.
    raise NotImplementedError(
        "linkedin_poster is gated behind manual trust progression. "
        "Do not call until Collin explicitly enables autopost."
    )


async def confirm_then_post(
    chat_id: str, message_id: str, draft_path: str, variant: str
) -> dict[str, str]:
    # TODO when the gate opens.
    raise NotImplementedError("confirm_then_post is gated. See module docstring.")
