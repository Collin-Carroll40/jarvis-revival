# Skill: topic-radar

Status: planned.

## Purpose

Hourly news scan for legal-AI / legal-tech stories that have a real angle for Caseread.ai's wedge. Evaluate newsworthiness via Haiku (cheap), and only ping Telegram if the story is actually hot enough to post about. The goal is to feed timely Pillar C drafts without forcing Collin to refresh news sites.

Think of it as the precursor to the linkedin-post-generator's Pillar C run. Topic radar surfaces a candidate story; if Collin gives it a thumbs-up reaction in Telegram, the next M/W/F drafting run uses that story as the Pillar C seed.

## Inputs

- **Schedule:** every hour, weekdays 7 AM to 7 PM Mountain.
- **News sources:** the same WebSearch surface intel-synthesis uses (legal AI, legal tech, ABA, court rulings on AI sanctions, competitor announcements).
- **Recent Pillar C history:** the last 14 days of Pillar C drafts in `~/vault/04-projects/lawless-ai/linkedin/`. Avoid pinging on a story that's already been drafted.
- **Newsworthiness rubric (passed to Haiku):** 0-10 score on (a) freshness (last 24-48 hrs), (b) angle for solo/small firms, (c) substance (real reporting vs press release rewrite), (d) novelty (not already in the recent draft history).

## Outputs

- If a story scores >= 7 across the rubric: a Telegram alert to chat_id `8169002246` with the headline, the source URL, the Haiku-generated angle hook ("the take a solo attorney post would lead with"), and a thumbs-up / thumbs-down ask.
- If Collin reacts with thumbs-up: a vault file at `~/vault/04-projects/lawless-ai/linkedin/_inspiration/topic-radar-YYYY-MM-DD-HHMM.md` containing the story summary + the angle hook. The next linkedin-post-generator run picks this up as a Pillar C seed.
- If nothing scores >= 7: silent. No Telegram noise on quiet hours.

## Steps (planned)

1. **Run a small set of WebSearch queries** scoped to the last 24-48 hours.
2. **Filter to fresh + relevant.** Skip aggregators, paywalled premium, tweet threads.
3. **For each candidate, Haiku-evaluate against the rubric.** One Haiku call per candidate, ~$0.001 each, batch where possible.
4. **Compare against recent Pillar C draft history.** If the same topic was drafted in the last 14 days, skip.
5. **Pick the top-scoring candidate above the threshold.** If nothing clears it, exit silently.
6. **Send Telegram alert.** Headline, source, one-line angle hook, prompt for thumbs-up / thumbs-down reaction.
7. **On thumbs-up reaction:** write the inspiration file. The next M/W/F drafting run picks it up automatically.
8. **On thumbs-down or no reaction within 4 hours:** discard. The drafting cron picks its own pillar.

## Cost control

The whole reason this skill exists is to use Haiku for the cheap newsworthiness filter so Sonnet only gets called when a story is actually worth drafting. Estimated cost: <$1/month for the radar itself. No live news API needed since WebSearch is already wired in.

## Hard rules

- Never auto-draft. The radar surfaces. Collin approves. The drafting cron drafts.
- Never spam. One alert per hour max, only when threshold cleared.
- Never overlap with the linkedin-post-generator's own Pillar C news scan. The drafting cron always runs its own scan; the radar's job is to feed candidates into the inspiration directory ahead of time.

## Why it matters

Pillar C posts are the highest-impression posts in Collin's voice samples (Westlaw monopoly = 4,479 impressions). But Pillar C is also the hardest to keep fresh because it requires reacting to news, and the linkedin-post-generator's own news scan only fires on M/W/F. Topic radar's job is to make sure that when M/W/F arrives, the news angle is already queued.

## Status notes

Not built this weekend. The drafting cron's own Pillar C news scan covers the baseline case fine. Topic radar is a quality-of-life upgrade for hot weeks (e.g., new sanction ruling drops on a Tuesday, would otherwise sit unused until Friday). Schedule for build once the news API budget settles and the Dripify webhook is in place.
