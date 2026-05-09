"""
telegram_handler.py — inbound Telegram event router for jarvis-revival surfaces.

Status: STUBBED 2026-05-09. Logic to be filled by Collin Sunday morning.

Pipeline role:
    Most Telegram traffic is handled by the existing plugin:telegram:telegram MCP
    inside Jarvis core, which is shared infrastructure (not part of this repo).
    This file only handles the marketing-ops-specific Telegram surfaces that
    jarvis-revival owns: thumbs-up reactions on topic-radar alerts, screenshot
    forwards meant for the screenshot-ingester skill, and approval reactions on
    auto-poster drafts (once the auto-poster comes off the gate). Inbound events
    here are pushed to the appropriate skill or vault path.

Depends on:
    - Env vars: TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID
    - External services: Telegram Bot API
    - Python deps: python-telegram-bot, fastapi, pydantic

Public surface:
    app: FastAPI
    POST /webhook/telegram  (handler: telegram_update)
    async def telegram_update(update: TelegramUpdate) -> dict
    async def route_reaction(chat_id: str, message_id: str, emoji: str) -> None
    async def route_image(chat_id: str, message_id: str, file_id: str, caption: str | None) -> None

TODO Sunday:
    - Decide whether to keep this as a webhook (recommended once the topic radar
      ships) or stay on the MCP polling model. The MCP covers everything today.
    - Define the TelegramUpdate pydantic shape (use python-telegram-bot's Update
      schema as the reference)
    - Implement the reaction router: thumbs-up on a topic-radar alert writes the
      inspiration file at ~/vault/04-projects/lawless-ai/linkedin/_inspiration/
      so the next M/W/F draft run picks up the seed
    - Implement the image router: forwards the file_id to the screenshot-ingester
      skill, which downloads the attachment, runs Claude vision, and appends to
      library/style-library.md
    - Add deduplication so the same reaction event doesn't trigger twice
"""

from typing import Any

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="jarvis-revival telegram handler")


class TelegramUpdate(BaseModel):
    """Placeholder. Real schema lifted from python-telegram-bot's Update."""

    update_id: int
    message: dict[str, Any] | None = None
    message_reaction: dict[str, Any] | None = None


@app.post("/webhook/telegram")
async def telegram_update(update: TelegramUpdate) -> dict[str, str]:
    # TODO Sunday: dispatch to route_reaction or route_image based on update shape.
    raise NotImplementedError(
        "telegram_update router not implemented yet. See module docstring TODO."
    )


async def route_reaction(chat_id: str, message_id: str, emoji: str) -> None:
    # TODO Sunday: thumbs-up on a topic-radar alert -> write inspiration file.
    raise NotImplementedError("route_reaction not implemented.")


async def route_image(
    chat_id: str, message_id: str, file_id: str, caption: str | None
) -> None:
    # TODO Sunday: forward file_id into the screenshot-ingester skill.
    raise NotImplementedError("route_image not implemented.")
