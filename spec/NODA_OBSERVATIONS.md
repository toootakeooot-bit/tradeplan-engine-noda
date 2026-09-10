# NS1 NODA Observations

Status: **NS1 baseline**

Repository: `toootakeooot-bit/tradeplan-engine-noda`

Branch: `feature/noda-v1`

## 1. Purpose

This document registers the minimum NODA Observation set needed to support later NS work while preserving the NS0 source and responsibility boundaries.

NS1 deliberately does **not** invent the formal trading meaning or detection algorithm for any NODA-specific observation whose authoritative source has not yet been verified.

## 2. Layer model

### L1 — NODA Primitive Observations

Direct NODA-native observations derived from raw Market Facts under authoritative NODA rules.

### L2 — NODA Derived Observations

NODA-native structural observations that depend on L1 or other formally governed observations.

Layer assignment in NS1 is a management classification, not an implementation algorithm. If later authoritative material contradicts a provisional layer assignment, a governed `RECLASSIFY` change is required.

## 3. Minimum L1 set

| ID | Name | Layer | Status | Source | Definition | Input | Output | Dependencies | Timeframe | Determinism | Open issue |
|---|---|---|---|---|---|---|---|---|---|---|---|
| NO101 | NODA-significant High | L1 | TBD | Authoritative NODA source required | Exact selection rule is not fixed in NS1. It is explicitly distinct from a raw candle High. | Candidate: L0 candle data | TBD | TBD | TBD | Not asserted | NS1-OI-001 |
| NO102 | NODA-significant Low | L1 | TBD | Authoritative NODA source required | Exact selection rule is not fixed in NS1. It is explicitly distinct from a raw candle Low. | Candidate: L0 candle data | TBD | TBD | TBD | Not asserted | NS1-OI-002 |
| NO103 | Swing | L1 | TBD | Authoritative NODA source required | Exact NODA meaning and recognition rule are not fixed in NS1. Generic swing definitions are prohibited as substitutes. | Candidate: L0 and/or significant High/Low | TBD | TBD | TBD | Not asserted | NS1-OI-003 |

## 4. Minimum L2 set

| ID | Name | Layer | Status | Source | Definition | Input | Output | Dependencies | Timeframe | Determinism | Open issue |
|---|---|---|---|---|---|---|---|---|---|---|---|
| NO201 | HL | L2 | TBD | Authoritative NODA source required | Exact NODA definition, relationship, and recognition rule are not fixed in NS1. | TBD | TBD | TBD | TBD | Not asserted | NS1-OI-004 |
| NO202 | TL | L2 | TBD | Authoritative NODA source required | Exact NODA definition, relationship, and recognition rule are not fixed in NS1. | TBD | TBD | TBD | TBD | Not asserted | NS1-OI-005 |
| NO203 | CH | L2 | TBD | Authoritative NODA source required | Exact NODA definition, relationship, and recognition rule are not fixed in NS1. | TBD | TBD | TBD | TBD | Not asserted | NS1-OI-006 |

## 5. Status interpretation

The `TBD` status above is intentional.

It means NS1 has registered the concept and its management identity, but has **not** established an authoritative formal definition sufficient for implementation.

`TBD` must not be read as:

- a placeholder that developers may fill using common technical analysis;
- permission to copy TradingCursor behavior;
- permission to infer candle counts, thresholds, price distances, timeframes, or hierarchy;
- permission to implement a provisional detector and later treat its output as teacher evidence.

## 6. Explicit exclusions from NS1 Observation scope

The following are not promoted into the NS1 observation ledger merely to make later work easier:

- 大ダウ;
- 小ダウ;
- Trend judgment;
- Field judgment;
- 際;
- 先行局面 / 本格局面 / 最終局面;
- Phase;
- BR candidate;
- Setup judgment;
- Break / Return judgment;
- support/resistance conversion judgment;
- Entry;
- SL;
- TP;
- Wait / Invalidation.

They remain candidates for later Environment / Phase / Setup / Trigger / Entry / SL / TP / Wait-Invalidation work according to authoritative sources.

## 7. Dependencies policy

Dependencies are not guessed.

Where a dependency looks intuitive but is not source-confirmed, the field remains `TBD`.

Later NS work may add or clarify dependencies through the governed change procedure without renumbering the observation ID.

## 8. Timeframe policy

NS1 does not assume that the same observation rule applies identically to D1, H4, H1, M15, or any other timeframe.

Any timeframe-specific rule must be sourced. Until then, `Timeframe = TBD`.

## 9. Example / counterexample policy

NS1 does not fabricate canonical examples or counterexamples for TBD observations.

Examples may be added later only when their role is clear:

- sourced teaching example;
- regression fixture;
- explanatory non-authoritative illustration clearly marked as such.

An example must not be silently converted into a universal rule.

## 10. Extension principle

This file is intentionally extensible.

NS2 and later work may identify additional observation requirements. Such items are added under `spec/OBSERVATION_GOVERNANCE.md` with new stable IDs, source traceability, dependency registration, and audit history.

NS1 does not need to be rerun from zero merely because a new observation is discovered.
