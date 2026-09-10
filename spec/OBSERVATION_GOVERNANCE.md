# NS1 Observation Governance

Status: **NS1 governance baseline**

Repository: `toootakeooot-bit/tradeplan-engine-noda`

Branch: `feature/noda-v1`

## 1. Purpose

This document fixes how Market Facts and NODA Observations are identified, classified, sourced, extended, changed, and audited.

The governing principle is:

> Fix the container and controls now; add only source-supported content later.

Discovery of a new observation in NS2 or later must be handled as a governed addition, not as a reason to rebuild NS1 from zero.

## 2. Layer system

| Layer | Meaning | Examples at NS1 |
|---|---|---|
| L0 | Common Market Facts supplied without NODA strategy interpretation | OHLC, Timestamp, Symbol, Timeframe, Current Price, Raw Candle Series |
| L1 | NODA Primitive Observations directly recognized from L0 under NODA rules | NODA-significant High / Low, Swing |
| L2 | NODA Derived Observations based on governed NODA observations | HL / TL / CH |

Environment, Phase, Setup, Trigger, Entry, SL, TP, Wait and Invalidation are strategy-decision stages, not automatically observation layers.

## 3. Stable ID system

IDs are immutable once committed unless a documented repository corruption/collision requires exceptional correction.

- `MF001`–`MF999`: L0 Market Facts
- `NO101`–`NO199`: L1 NODA Primitive Observations
- `NO201`–`NO299`: L2 NODA Derived Observations

Future layers, if ever required, must be explicitly approved before a new prefix/range is introduced.

Rules:

1. New items take an unused ID.
2. Existing IDs are never renumbered for visual ordering.
3. Deleted/retired IDs are not recycled.
4. An ID identifies one semantic concept over its lifetime; a meaning-changing replacement should normally receive a new ID and deprecate the old one.

## 4. Specification status system

### `FIXED`

Definition, responsibility boundary, and source basis are sufficient to serve as the current specification baseline.

`FIXED` does not imply that code has been implemented.

### `PROVISIONAL`

The concept/structure is usable for planning, but one or more details still require confirmation before strict implementation.

### `TBD`

Definition, ownership, dependencies, source, or another essential specification element is not fixed.

### `UNKNOWN`

Runtime/case-level result meaning: available governed rules and inputs are insufficient to resolve a specific case.

`UNKNOWN` is primarily a runtime result state and must not be used to conceal a missing specification that should be marked `TBD` or `PROVISIONAL`.

## 5. Required record template

Every governed Fact/Observation record must be able to carry:

- `ID`
- `Name`
- `Layer`
- `Status`
- `Source`
- `Definition`
- `Input`
- `Output`
- `Dependencies`
- `Timeframe`
- `Determinism`
- `Example`
- `Counterexample`
- `Open Issue`
- `Notes`

Fields may contain `TBD` where the source does not support a fixed value.

## 6. Source traceability

`docs/SOURCE_POLICY.md` is controlling.

For NODA-specific observations, a transition to `FIXED` requires source traceability sufficient to show why the definition is NODA-specific and not an AI/generic-TA/TC substitution.

A source record should identify, when available:

- source title/file;
- section/page/time/location;
- rule ID or teacher statement reference;
- whether the evidence is direct or interpretive;
- any unresolved conflict.

Market Facts may be fixed at conceptual supplied-data level without teacher evidence because they are not NODA strategy rules. Transport/schema details still require the later common input contract.

## 7. Determinism and reproducibility

Target principle:

**same supplied input + same NODA rule version + same decision conditions = same Fact/Observation result**.

Determinism may only be asserted when the specification is sufficient to support it.

For `TBD` items, do not claim deterministic detection.

NS1 fixes the requirement only. It does not implement detectors or replay tests.

## 8. Addition procedure

When later work discovers a required Fact/Observation:

1. demonstrate that existing governed items cannot represent the requirement without semantic distortion;
2. determine candidate layer/ownership;
3. locate authoritative source if NODA-specific;
4. assign the next unused stable ID in the applicable range;
5. register definition, status, source, inputs, outputs, dependencies, timeframe, and open issues;
6. audit for overlap/conflict with existing items;
7. identify regression consumers that may be affected;
8. record change type and rationale in the change history/audit artifact.

If steps 2–5 cannot be completed, the item may still be registered as `TBD` when preserving the unresolved requirement is useful, but no trading behavior may be invented.

## 9. Change classes

Every substantive change should be classified as one of:

- `ADD` — add a new semantic item;
- `CLARIFY` — make wording more precise without changing meaning;
- `RECLASSIFY` — change layer/responsibility classification without changing sourced meaning;
- `SOURCE_CORRECTION` — correct source locator or source transcription;
- `DEPRECATE` — retire an item while preserving history.

A meaning-changing edit must not be mislabeled `CLARIFY`.

If meaning materially changes, prefer a new ID plus `DEPRECATE` of the old concept unless an audited source correction clearly proves that the old text was erroneous.

## 10. Stronger control for existing definitions

Changing an existing definition is a stronger event than adding a new item.

Before a definition change:

- identify the exact source reason;
- identify dependent observations/rules/tests;
- assess semantic drift;
- record regression scope;
- preserve the old definition in history;
- issue an audit verdict.

Performance improvement by itself is never sufficient justification.

## 11. Dependency rules

Dependencies must refer to stable IDs where practical.

No dependency is inferred merely because it appears logically convenient.

Circular dependencies are prohibited unless a later explicit architecture specification defines a valid iterative model and audits it.

Unknown dependencies remain `TBD`.

## 12. Timeframe rules

Do not assume cross-timeframe equivalence.

A rule that is sourced for one timeframe cannot be generalized to another without source support or an explicitly approved general rule.

Timeframe-independent definitions may be marked as such only when supported.

## 13. OPEN ISSUE governance

Each unresolved issue should carry:

- Open Issue ID;
- affected Fact/Observation ID(s);
- unresolved question;
- missing source/evidence;
- impact;
- whether NS2 is blocked;
- earliest intended resolution milestone.

The existence of an OPEN ISSUE does not automatically fail NS1. Failure is required only if the governance/boundary itself is unsafe or the next milestone cannot proceed without guessing.

## 14. Regression rule

When a later ADD/CLARIFY/RECLASSIFY/SOURCE_CORRECTION/DEPRECATE affects an existing consumer, the change must identify the regression scope.

Potential consumers include:

- Environment rules;
- Phase rules;
- Setup rules;
- Trigger rules;
- Entry/SL/TP rules;
- Wait/Invalidation rules;
- fixtures/tests;
- common output contracts.

NS1 does not implement these consumers.

## 15. Prohibited governance shortcuts

Do not:

- renumber IDs to make tables look tidy;
- fill TBD definitions using generic technical analysis;
- copy TC behavior into NODA;
- promote a teaching example into a universal rule without evidence;
- invent thresholds/timeframes/candle counts;
- rewrite R01–R37 meaning under the label of observation cleanup;
- modify `trade-plan-a` or TC Engine as part of observation governance;
- use backtest performance as source evidence.

## 16. NS1 freeze rule

NS1 is considered structurally complete when the layer/ID/status/source/change/reproducibility controls and minimum observation set are registered.

Later additions use this governance baseline and do not reopen NS1 wholesale unless a fundamental flaw in this governance model is discovered.
