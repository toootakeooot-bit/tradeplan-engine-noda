# NS2 Review Protocol

Status: **NS2-0 review baseline**

Repository: `toootakeooot-bit/tradeplan-engine-noda`

Branch: `feature/noda-v1`

## 1. Purpose

This protocol fixes how NS2-A and later work presents, checks, and confirms existing NODA rules. The key control is that AI classification alone cannot make a rule `CONFIRMED`.

## 2. Required review flow

```text
AI draft整理
  -> 日本語レビュー表
  -> user review
  -> OK / 修正 / 保留
  -> required source/image/original verification
  -> final整理
  -> audit
  -> CONFIRMED or unresolved
```

Before user review, use `DRAFT` or `REVIEW_REQUIRED`. Do not present that state as a confirmed rule classification.

## 3. Japanese review record

For each Rule ID, the user-facing review must be understandable without opening repository files. Include at least:

- Rule ID;
- Rule name;
- current baseline text;
- `正式定義` based on source evidence;
- `簡単に言うと` as an explanatory paraphrase;
- primary source;
- supplemental source;
- evidence level;
- candidate Primary Stage;
- candidate Secondary Stage;
- Observation dependencies;
- current interpretation / classification proposal;
- unresolved points;
- image-review need;
- AI confidence state;
- user judgment.

`簡単に言うと` is not itself a new NODA rule and must never override the sourced formal meaning.

## 4. User judgment states

### `OK`
The presented formal definition, explanatory paraphrase, source relationship, and classification proposal are accepted for the current review gate.

### `修正`
The user's understanding differs. Record the correction request, source basis if available, and return the item to review.

### `保留`
The item is not confirmable because source, image, context, or meaning is insufficient. Preserve it as unresolved.

User `OK` does not authorize inventing source-unsupported strategy logic. `docs/SOURCE_POLICY.md` remains controlling.

## 5. Image review levels

Each Rule may be assigned one of:

- `REQUIRED`
- `RECOMMENDED`
- `OPTIONAL`
- `NOT_REQUIRED`

The final level is assigned during the relevant NS2 block review, not in NS2-0.

Image review is especially useful where selection, location, scale, endpoints, or visual relationships matter, including significant highs/lows, turns, Dow scale, HL/TL/CH, line endpoints, zones, fields, and BR states.

## 6. Image evidence constraints

Images may verify how a text-defined rule appears on a chart. They may not by themselves establish:

- a new general rule;
- a threshold;
- candle-count requirement;
- price-distance requirement;
- timeframe requirement;
- a teacher's unstated intent;
- an Entry rule inferred from outcome hindsight.

If image and text do not align, record `IMAGE/TEXT CONFLICT` or OPEN ISSUE rather than forcing agreement.

## 7. Audio / transcript review

When teacher audio or a formal transcript is used, preserve where available:

- Source ID;
- file/title;
- segment/time range;
- statement location/text;
- surrounding context;
- evidence level.

A teacher statement and an AI interpretation of a video are different evidence objects.

## 8. Case evidence

Personal cases, other-student cases, and historical AI analyses are not standalone authority for general rules. They may support application review, boundary review, counterexample investigation, or source-discovery work only.

One case cannot be generalized into a new NODA rule.

## 9. Review granularity

Default NS2 blocks:

- NS2-A: R01-R10
- NS2-B: R11-R20
- NS2-C: R21-R30
- NS2-D: R31-R37 plus provisional hypotheses

Within a block, review may be reduced to 1-3 rules at a time, especially where image verification is required. User review must not be forced into one bulk approval.

## 10. Confirmation gate

A rule classification may become `CONFIRMED` only when, at minimum:

1. current Rule text is identified;
2. source is traceable;
3. Source Policy is satisfied;
4. Primary / Secondary Stage proposal has been reviewed;
5. Observation dependencies have been reviewed;
6. unresolved conflicts are absent or explicitly dispositioned;
7. any `REQUIRED` image review is completed;
8. user judgment is `OK`.

Management classification and strategy meaning are separate. Confirming a Stage mapping does not permit changing the underlying rule meaning.

## 11. AI confidence state

Use confidence as a review aid, not as evidence authority. Suggested states:

- `HIGH`: source and mapping appear direct;
- `MEDIUM`: source is present but classification or dependency requires judgment;
- `LOW`: source, boundary, or visual interpretation is unresolved.

A HIGH confidence score cannot replace user review or authoritative evidence.

## 12. Difference handling

If review suggests the baseline rule text may be wrong or incomplete, create a difference candidate containing:

- Rule ID;
- current baseline text;
- proposed issue/correction;
- source evidence;
- impact;
- user status;
- whether the proposal changes meaning.

Do not silently edit `02_野田式判断ルール台帳.md` during NS2 review.

## 13. Prohibitions

NS2 review must not:

- create strategy rules from images;
- infer teacher intent from drawing alone;
- use TC logic to fill a NODA gap;
- use generic TA to fill a NODA gap;
- treat one case as a universal rule;
- alter R01-R37 numbering;
- modify `trade-plan-a` or TC Engine;
- implement detector, strategy, adapter, sizing, or execution code.
