# NS6 Trigger Rules

Status: **NS6 specification — Trigger responsibility fixed, Break/Return/awareness/Formation detectors TBD**

Upstream contracts:
- `schema/environment_state.schema.json`
- `schema/phase_state.schema.json`
- `schema/setup_state.schema.json`

Controlling baseline:
- `spec/NS2_FINAL_RULE_MATRIX.csv`
- NS2-B confirmed semantics for R14-R20
- R28/R29 confirmed Setup/Trigger boundary
- `spec/RESPONSIBILITY.md`
- `docs/SOURCE_POLICY.md`
- NS3-NS5 specifications and audits

## 1. Responsibility

NS6 owns `2-4 Trigger` only.

Trigger answers:

> Given Environment, Phase, and Setup context, has a source-defined NODA activation Action been resolved strongly enough to proceed to later Entry consideration?

Trigger does **not** mean Entry is valid.

NS6 does not determine:
- Entry price/zone;
- SL;
- TP;
- RR;
- position size;
- broker execution;
- formal Wait/Invalidation outcome.

## 2. Rule mapping

### Trigger-primary rules

| Rule | Trigger responsibility | Open item |
|---|---|---|
| R14 | small-Dow BR: large-Dow edge context -> final phase -> small-Dow TL/HL -> Break -> Return -> next Early-phase candidate action | `SMALL_DOW_BR_DETECTION_TBD` |
| R15 | small awareness revival: counter-trend small-Dow line Break then return-side Action as awareness-revival candidate | `SMALL_AWARENESS_REVIVAL_DETECTION_TBD` |
| R16 | large awareness revival: previously broken large-Dow line / main-trend return context with small-Dow cycle relation | `SMALL_DOW_CYCLE_DETECTION_TBD`; line-return detector TBD |

### Trigger-context rules

| Rule | Trigger use |
|---|---|
| R19 | Return Move remains Observation/Search Cue only; it may locate relevant return context but is not a standalone Trigger |
| R20 | known TL/CH Break carries structural meaning; TL/CH BR alone is not Entry and is not automatically a standalone Trigger |
| R28 | Reversal Formation recognition is Setup; source-defined neckline/support-resistance Break/Action may be Trigger candidate context |
| R29 | Continuation Formation recognition is Setup; continuation-side Formation Break may be Trigger candidate context |

## 3. TriggerState model

NS6 separates:

1. `trigger_status` — `TRUE / FALSE / UNKNOWN / NOT_EVALUATED`;
2. `trigger_type` — source-defined activation family when known;
3. `break_state` / `return_state` — Action evidence state;
4. `awareness_revival` — R15/R16 candidate state;
5. `formation_break` — R28/R29 downstream Break context;
6. `return_move_observation` — R19 search cue, explicitly not Trigger;
7. `tl_ch_break_context` — R20 structural meaning, explicitly not Entry;
8. `evidence[]` and `unresolved[]`.

## 4. R14 small-Dow BR

Confirmed semantics:

`large-Dow edge -> final phase -> small-Dow TL or HL -> Break -> Return -> next Early-phase candidate Action`

NS6 may set `trigger_type = SMALL_DOW_BR` only when R14 trigger evidence itself is supplied/resolved according to governed semantics.

NS6 does not invent:
- Break candle-close rule;
- Return distance/touch tolerance;
- pips threshold;
- fixed timeframe;
- line-selection detector.

If required Break/Return evidence is unresolved, trigger result is `UNKNOWN`, not `FALSE`.

## 5. R15 small awareness revival

Confirmed semantics:
- in Main or Final phase context, a counter-trend small-Dow line is broken;
- price/action returns toward that line;
- this is a candidate for revival of the preceding small-Dow turn awareness.

R15 is not equivalent to R19 Return Move.

R19 may serve as a search cue, but R15 requires its own source-defined semantic context and detector remains TBD.

## 6. R16 large awareness revival

Confirmed semantics:
- a previously broken large-Dow line remains the relevant structural context;
- a return toward main-trend direction is observed as a large awareness-revival candidate;
- small-Dow up/down cycle relation is relevant;
- exact cycle and line-return detection remain TBD.

NS6 does not reduce R16 to a simple line touch.

## 7. R19 Return Move boundary

R19 remains:

`Observation / Search Cue`

It may be represented in TriggerState because Trigger evaluation may need to know whether a Return Move observation is available, but:
- `R19 = TRUE` does not imply `trigger_status = TRUE`;
- R19 is not a subtype of R15;
- R19 alone cannot authorize Entry.

## 8. R20 TL/CH Break boundary

Known R20 semantics may be carried:
- TL Break -> trend-turn/change candidate context;
- CH Break -> continuation/acceleration candidate context.

R20 does not define standalone Entry.

NS6 must not convert R20 meaning into:
- `TL Break => sell/buy Entry`;
- `CH Break => continuation Entry`;
- fixed Break thresholds.

The relevant Trigger rule must still be source-defined (R14/R15/R16 or R28/R29 Action context).

## 9. Formation Break context

R28/R29 remain Setup owners.

NS6 owns only the downstream Action candidate:
- Reversal Formation: source-defined neckline/support-resistance Break/Action candidate;
- Continuation Formation: continuation-side boundary Break candidate.

Formation recognition alone does not make Trigger TRUE.

Exact Formation-boundary and Break detectors remain TBD.

## 10. Trigger truth semantics

`TRUE`:
- a governed Trigger rule/action has been evaluated and resolved as present.

`FALSE`:
- the applicable Trigger rule has been evaluated with sufficient governed information and is not present.

`UNKNOWN`:
- required governed evidence/detector is insufficient or conflicting.

`NOT_EVALUATED`:
- prerequisite Setup/context was not supplied or this trigger path was not run.

Missing detector capability must never be represented as `FALSE`.

## 11. No Entry promotion

Even when `trigger_status = TRUE`:
- Entry remains a later-stage decision;
- R22 and other Entry/SL/TP rules remain HOLD;
- no price, order, SL, TP, RR, lot, sizing, or execution field is generated.

The maximum NS6 conclusion is:

> A source-defined Trigger has been resolved and the case may proceed to later Entry evaluation when that stage is governed.

## 12. TriggerState contract

Machine-readable contract: `schema/trigger_state.schema.json`.

It can carry:
- upstream references;
- trigger status/type;
- Break/Return states;
- awareness revival state;
- Formation Break state;
- R19 observation cue;
- R20 structural Break context;
- evidence/unresolved items.

## 13. Explicit TBD preservation

NS6 preserves at least:
- `SMALL_DOW_BR_DETECTION_TBD`;
- `SMALL_AWARENESS_REVIVAL_DETECTION_TBD`;
- `SMALL_DOW_CYCLE_DETECTION_TBD`;
- line-return detector TBD;
- `RETURN_MOVE_DETECTION_TBD`;
- `BR_DETECTION_TBD`;
- `REVERSAL_FORMATION_DETECTION_TBD` / Formation-boundary Break details;
- `CONTINUATION_FORMATION_DETECTION_TBD` / Formation-boundary Break details.

No candle counts, pips thresholds, generic Break definition, pattern score, or fixed timeframe is added.

## 14. Completion condition

NS6 is complete at specification level when:
- Trigger consumes only upstream Environment/Phase/Setup plus governed Action evidence;
- R19 remains observation/search cue;
- R20 remains structural Break meaning/context;
- R14-R16 and R28/R29 Action boundaries are preserved;
- Trigger TRUE is not Entry TRUE;
- unknown vs false is explicit;
- detector TBDs are preserved;
- static cases and audit pass.
