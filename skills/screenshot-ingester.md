# Skill: screenshot-ingester

Status: planned for week 1 of caseread launch.

## Purpose

Let Collin grow the LinkedIn style library by forwarding posts as Telegram screenshots. The skill reads the screenshot with Claude vision, parses the post text and structure, classifies the move (opener type, rhythm, ending pattern), and appends a dated entry to `library/style-library.md`.

This closes the loop on voice fidelity. The drafting cron only stays in voice if the style library keeps growing as Collin's taste evolves.

## Inputs

- A Telegram message with `attachment_kind="image"` from chat_id `8169002246`. Usually a screenshot of someone's LinkedIn post (or one of Collin's own that performed well).
- Optional caption text on the Telegram message: a one-line note from Collin like "love the opener" or "the foil takedown move".
- The current `library/style-library.md` so the skill doesn't duplicate an entry.

## Outputs

- One appended dated entry in `library/style-library.md` under a new "## YYYY-MM-DD — curated additions" subsection.
- Telegram confirmation to chat_id `8169002246`: short "added pattern: <one-line label>" message with a checkmark reaction on the original.
- Silent best-effort git commit on the repo.

## Steps (planned)

1. **Receive the Telegram image event.** Download the attachment via the plugin:telegram:telegram MCP.
2. **Read the image with Claude vision.** Use a Sonnet call with the image attached. Prompt: extract the post text verbatim, plus structural metadata (opener type, paragraph rhythm, use of arrow bullets, ending pattern, hashtag count).
3. **Classify the move.** Map the post to one of the 9 structural archetypes (or flag as a new archetype candidate). Identify what's distinctive about it.
4. **Check for duplicates.** If a near-identical pattern already exists in `style-library.md`, skip with a Telegram note.
5. **Append the entry.** New subsection with date, the verbatim post (quoted), the classified archetype, the one-line "what makes this move work" lesson, Collin's caption note if present.
6. **Reply on Telegram.** Confirm the add with the pattern label.
7. **Git commit.** `library: style-lib add YYYY-MM-DD <label>`.

## Inputs from Collin (manual flow)

Collin forwards a LinkedIn screenshot to the bot. Optional one-line caption. That's the entire UX.

## Hard rules

- Never include the original poster's name or photo content in the entry. Keep it about the structural move, not the person.
- Never auto-publish anywhere. The library is internal.
- If vision OCR gets less than ~80% of the post text cleanly, ask Collin to paste the text manually. Don't fabricate.

## Why it matters

The drafting cron's voice fidelity is downstream of the style library. If the library stays static at 23 posts, the drafts plateau. If Collin can feed it 1-2 patterns a week from the wild, the voice keeps sharpening.

## Status notes

Not built this weekend. The drafting and reflection skills work fine without it for now, since the seed library has 23 posts of voice data which is a strong tone anchor on its own. Screenshot ingestion becomes urgent once Collin's taste outruns the seed library, expected around week 1 of the public Caseread launch when posting cadence ramps.
