# Skill: dehumidifier

Status: shipped this weekend (extracted from linkedin-post-generator).

## Purpose

A standalone, reusable text-rewriting skill that strips AI tells from any draft. Originally embedded inside the linkedin-post-generator, extracted out so any other skill (intel-synthesis Telegram brief, content-reflection digest, future caseread-blog drafter, future cold-DM templates) can run drafts through the same audit.

If a model produces a polished-but-AI-shaped draft, the dehumidifier is the second layer of defense before it reaches Telegram.

## Inputs

- A block of text (the draft).
- Optional context: the previous 1-2 variants in the same run, used to enforce the "no duplicate closers" rule across a multi-variant set.

## Outputs

- A rewritten block of text that has cleared the audit, OR
- A failure object with: which rule(s) failed, which sentence(s), the suggested rewrite. The caller decides whether to ship the closest variant with a flag, or to retry.

## Rules

### 1. Em-dash zero tolerance

Every `—` in the body fails the audit. Replace with one of:

- A period (start a new sentence).
- A comma.
- Parentheses.

Examples of the rewrite move:

- Before: `Sullivan & Cromwell — a top-25 firm — announced...`
- After: `Sullivan & Cromwell, a top-25 firm, announced...`
- Or: `Sullivan & Cromwell (a top-25 firm) announced...`
- Or: `Sullivan & Cromwell announced... It's a top-25 firm.`

Run a literal `grep '—'` against the draft before declaring it passes. If any `—` remains, it fails.

### 2. Banned vocabulary

Strip and rephrase every occurrence of:

- delve
- leverage
- transformative
- robust
- seamless
- unlock
- game-changer
- revolutionize
- synergy
- "in today's fast-paced / rapidly evolving / digital age"
- "Here's the thing."
- "I've been thinking a lot about..."
- "It's not just X, it's Y."

Hedge words that soften when Collin doesn't hedge:

- perhaps
- arguably
- potentially
- notably
- particularly
- fundamentally

### 3. No duplicate closers across variants

When called with multiple variants in one run, the dehumidifier checks that no two variants share their final sentence or use the same closer pattern. If two variants close on, say, "Onward." or "That's the door legal tech needs to walk through.", at least one of them rewrites.

This rule fires at the variant-set level, not the per-draft level. The caller passes the previous variants in for context.

### 4. Sentence-fragment injection

A real human typing on a phone uses sentence fragments. A polished AI draft doesn't. If a draft has zero standalone fragments (sentences without verbs), inject 1-2 where they earn their spot.

Example move:

- Before: `That's not a product. That's a liability.`  (already has a fragment-feeling rhythm; no change needed.)
- Before: `The architecture is what matters most about the product, and that's where the model alone cannot help.`
- After: `The architecture is what matters. Not the model.`  (second clause is a fragment; rhythm sharpens.)

### 5. Anti-symmetry check

Strip the polish-tells of perfect parallelism:

- Three-item parallel rhythm lists ("faster, smarter, safer") unless enumerating real distinct items.
- Every paragraph being exactly 2 sentences.
- Every paragraph starting with a capital-letter declarative.
- Topic-sentence / support / conclusion structure in every paragraph.
- All sentences the same length.

If any of these symmetries appear consistently, break one of them deliberately. Vary syntax. Mix a 1-sentence paragraph in with a 3-sentence paragraph. Start a paragraph with "But" or "And".

### 6. Conversational contractions

AI-polished prose under-uses contractions. If the draft has zero "it's", "don't", "won't", "we're", "I'm", inject them where they read naturally. Don't force.

### 7. Generic closer ban

Replace any of these:

- "What do you think?"
- "Let me know your thoughts."
- "Drop your thoughts below."
- "Like and share."
- "Just my two cents."

With either: a sharp specific question worth answering, or a quiet implication, or a single-line punch. Collin's signature closes: implication, conviction, or a specific URL / next-action. Never a generic engagement-bait line.

## Steps (programmatic flow)

1. Read draft.
2. Run em-dash grep. If any `—`, queue rewrites.
3. Run banned-vocab grep against the list. Queue rewrites.
4. Compare closers across variants if multiple passed in. Queue rewrites for any duplicates.
5. Check fragment count. If zero, mark for fragment injection.
6. Check symmetry. Mark for syntactic break if too uniform.
7. Apply rewrites in one pass. Keep the original throughline intact.
8. Re-run em-dash grep on the rewrite to make sure the rewrite didn't introduce new ones.
9. Return the rewrite, or return failure with the unfixable rules and let the caller decide.

## Hard rule

The dehumidifier never adds content. It rewrites or shortens. If the rewrite would require fabricating a fact, it returns failure and asks the caller to pass in more substance.

## Why a standalone skill

Originally these rules lived inside the linkedin-post-generator's Step 4.5 and Step 5. The intel-synthesis Telegram brief needs the same audit (no em-dashes, no banned vocab). The future caseread-blog skill will need it. Cold-DM templates from Dripify reply triage will need it. Extracting out into one skill means one place to update the banned list, one place to add a new rule, and one consistent voice across every channel Jarvis touches.
