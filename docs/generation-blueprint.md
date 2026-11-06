# 06 — Future Screenshot Generation Blueprint (Deliverables 9-E, 9)

Use this every time a new app comes in. Steps 1–5 produce a **storyboard for approval**. Nothing is rendered before the owner says yes.

## Step 1 — Application understanding (intake form)
```
App name / one-line purpose:
Category (App Store primary + secondary):
Target user (who, situation, trigger moment):
Top 3 jobs the user hires it for:
Differentiator vs top 2 competitors (name them):
Measurable outcome? (number, unit, source) or "none":
Brand: colours (HEX), fonts, logo, mascot? (y/n), voice:
UI theme: light / dark / both:
Proof available: rating (value + count + date), awards (name + year), press — or "none":
Markets / locales:
Hard no's (claims, features to hide, competitors not to mention):
```
If a field is empty, ask. Never fill it from imagination.

## Step 2 — Asset inspection
- Capture every candidate screen at 3× on the largest simulator (`goldie`, or a `simctl` screenshot). Use realistic, non-personal demo data (no real names, emails or faces).
- Record for each screen: what feature it proves, whether it reads at thumbnail size, and its dominant colour and theme.
- Reject screens that are paywalls, onboarding or splash screens (contract), or that show placeholder text.

## Step 3 — Archetype selection
Run the decision engine (`03-…md`, section B). Write the result as:
`Archetype: ARC-x (score n) · runner-up ARC-y (score m) · why: … · blended techniques: …`

## Step 4 — Creative direction (one page)
Palette (brand HEX + derived tokens) · type pair + sizes · alignment · field strategy · device style · decorative language (what is allowed and what is banned) · rhythm (layout ID sequence).
**Gate:** present 2 directions (the top two archetypes) as one rendered hero tile each. The owner picks one.

## Step 5 — Storyboard
### Sequence framework (value before features)
| Slot | Job | Typical layout |
|---|---|---|
| 1 | **Who it's for + the core promise.** Contains the category keyword. Proof if real. Brand name. | L1 / L6 / L9 |
| 2 | **The differentiator**: why this app and not the obvious alternative | L4 / L6 |
| 3 | **The primary action**: the thing users do daily | L2 / L4 |
| 4 | **The emotional or aspirational feature** | L3 / L5 |
| 5 | **Control / safety / trust** (history, privacy, sync) | L4 / L11 |
| 6 | **Mastery / insight / progress** | L7 / L2 |
| 7–10 | Secondary features, integrations, widgets, Watch/iPad | L10 / L8 |

Slots 1–3 are the search-result view: together they must answer **what it is, why it's different, and what you do**.

### Headline formulas (benefit first)
- **Outcome + context:** "Eat out smarter" · "Split bills fairly"
- **Verb + object + twist:** "Turn reps into screen time"
- **Contrast pair:** "Talk first. Reveal later."
- **Input → output:** "Any chat → clean PDF"
- **Numbered step:** "1. Find what you like"
- **Quantified:** "[real number] [unit] [benefit]", used only with a source

Rules: 2–6 words · one coloured key word · no feature jargon (say "fair splits", not "income-weighted allocation") · every claim maps to a real screen · `humanizer` pass.

### Storyboard table (fill one row per tile)
| # | Objective | Feature (real screen ID) | Headline | Key word | Sub | Layout | Field | Device (scale/crop/rot) | Callouts (real component IDs) | Decoration | Proof (source) |
|---|---|---|---|---|---|---|---|---|---|---|---|

## Step 6 — Production
Follow `05-production-workflow.md`. Render all tiles from tokens. No hand-tweaking outside tokens without writing it back into the token file.

## Step 7 — QA
`07-qa-checklist.md` + a contact sheet at thumbnail size, reviewed alongside the top 3 competitors' screenshots (do they stand apart?).

## Accuracy guardrails (non-negotiable)
- No invented features, screens, numbers, ratings, reviews, awards, download counts or "#1" claims.
- Callouts are crops of real UI. No retyped data that the app could not produce.
- Illustrative elements (3D objects, mascots) must not look like functionality. If ambiguous, drop them.
- No third-party logos unless the integration ships, and only within that brand's guidelines.
- No human faces: hands, masks, silhouettes or objects instead.
- Placeholder content is never in a final export without the owner's written OK.
