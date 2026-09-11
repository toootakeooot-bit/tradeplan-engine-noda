# NS3 Environment Rules

Status: **NS3 specification — Environment responsibility fixed, detector/selection TBDs preserved**

Repository: `toootakeooot-bit/tradeplan-engine-noda`

Branch: `feature/noda-v1`

Baseline: NS2 Final Audit HEAD `da5a2925a53d7f571e786db41b0803b7183dfabc`

Controlling documents:
- `spec/NS2_FINAL_RULE_MATRIX.csv`
- `audit/NS2_FINAL_AUDIT.md`
- `spec/RESPONSIBILITY.md`
- `docs/SOURCE_POLICY.md`
- `spec/OBSERVATION_GOVERNANCE.md`
- `spec/MARKET_FACTS.md`
- `spec/NODA_OBSERVATIONS.md`

## 1. Responsibility

NS3 owns `2-1 Environment` only.

Environment answers:

> What NODA market structure and structural context are currently available from governed Market Facts / NODA Observations, without deciding Phase, Setup, Trigger, Entry, SL, TP, Wait, or Invalidation?

Environment must be independently evaluable. It may return unresolved fields when required observations or detectors are not available.

Environment does **not**:
- decide `EARLY / MAIN / FINAL` Phase;
- declare a Setup candidate from a Formation;
- declare a Trigger true;
- declare Entry;
- determine SL / TP / RR / sizing;
- fill missing NODA observations with generic TA;
- call a later stage to resolve an earlier-stage field.

## 2. Inputs

Allowed upstream input classes:

1. L0 Market Facts (`MF001`–`MF006`) as supplied;
2. governed NODA Observations (`NO101`–`NO203`) when available;
3. source-traceable structural evidence already resolved outside NS3;
4. unresolved markers when a detector/selection remains TBD.

NS3 does not create a detector for `NO101` / `NO102` / `NO103` / `NO201` / `NO202` / `NO203`.

A missing NODA observation is not equivalent to a negative observation.

## 3. Rule mapping

### Primary Environment rules

| Rule | Environment responsibility | Unresolved carried forward |
|---|---|---|
| R01 | significant high/low are the structural foundation | NO101/NO102 detector TBD |
| R02 | upward/downward/undetermined trend semantics from governed structural highs/lows | input high/low recognition may be TBD |
| R03 | Turn structural concept | Turn detector / NO103 relationship TBD |
| R04 | separate large/middle/small Dow by purpose | `DOW_SCALE_DETECTION_TBD` |
| R05 | select/use lines by structural purpose, not line abundance | dependency/selection details TBD |
| R07 | large-Dow line as broad Field / edge context | `LINE_SELECTION_TBD` |
| R10 | separate Field (area) and Action (change) | Field representation TBD |
| R17 | intermediate TL and middle-Dow counter TL are separate structural line concepts | line selection / Break detector TBD |
| R18 | after supplied/known Break context, use new structural high/low to redraw TL/CH and remap Field | high/low and line selection TBD; Break detection not owned here |
| R20 | TL/CH purpose difference and structural meaning of their Break when Break evidence is supplied | `BR_DETECTION_TBD`; no standalone Entry |

### Observation-primary / Environment-context rules

| Rule | Use in NS3 |
|---|---|
| R06 | carry HL / TL / CH structural observations; visual selection remains TBD |
| R09 | carry TL Zone context; application selection remains TBD |

### Later-stage rules referenced only as boundary guards

- R08 is Setup-primary and must not be promoted to an Environment decision.
- R11–R13 / R30-A belong to Phase and are not evaluated in NS3.
- R14–R16 belong to Trigger and are not evaluated in NS3.
- R19 is an Observation/Search Cue and is not required to complete Environment.
- R28/R29 belong to Setup.
- R21–R27 are HOLD and unavailable for NS3 semantics.
- R31–R37 are Operational Control / HOLD and are not NODA strategy authority.

## 4. Environment evaluation protocol

This protocol defines responsibility flow only; it does not invent detectors.

1. Preserve supplied L0 facts exactly at the Market Fact boundary.
2. Accept NODA-significant highs/lows only when supplied/resolved under governed NODA observation logic. Raw candle highs/lows are not promoted.
3. If significant highs/lows are available, R02 may express the sourced trend relationship. If they are not available, trend result is `UNKNOWN`, not `FALSE`.
4. If Turn / Dow-scale evidence is unavailable because the detector is TBD, the corresponding result remains `UNKNOWN`.
5. HL/TL/CH/Zone objects are carried only when their governed observation/selection evidence exists; NS3 does not manufacture line candidates.
6. Field / edge context is assembled from available structural objects. Missing edge/Field representation remains unresolved.
7. R17 line concepts are represented separately. `intermediate_tl` must not alias `middle_dow_counter_tl`.
8. R18 Field remap is evaluated only when post-Break structural evidence is already available. NS3 does not invoke NS6 Trigger to obtain a Break.
9. R20 may attach the sourced semantic context of a known TL Break or CH Break. It does not detect Break and does not create Entry.
10. Every unresolved requirement is emitted in `unresolved[]` with the governing Rule/TBD code where practical.

## 5. No circular dependency rule

Environment cannot depend on Phase, Setup, or Trigger output.

For R18/R20, `Break` is treated as supplied/resolved structural evidence when present. If no governed Break evidence is available, those sub-results are `NOT_EVALUATED` or `UNKNOWN`. This prevents the prohibited cycle:

`Environment -> Phase -> Setup -> Trigger -> Environment`.

## 6. EnvironmentState contract semantics

The machine-readable contract is `schema/environment_state.schema.json`.

Important semantics:

- `KNOWN`: the field is resolved from governed input/rules.
- `UNKNOWN`: available governed information is insufficient to resolve the case.
- `NOT_EVALUATED`: the sub-rule was not applicable or the prerequisite evidence was not supplied.

These are runtime transport states, not new trading rules.

`FALSE` is used only for an evaluated condition that is actually false. Missing detector capability must not become `FALSE`.

## 7. Required structural outputs

EnvironmentState can carry:

- significant high / low references;
- Trend;
- Turn references;
- Dow-scale classifications;
- HL / TL / CH / TL Zone objects;
- broad/current Field context;
- edge references when governed evidence exists;
- `intermediate_tl`;
- `middle_dow_counter_tl`;
- supplied Break context;
- post-Break Field-remap result;
- R20 TL/CH Break semantic context;
- evidence references;
- unresolved items.

The presence of a field in the schema does not imply that its detector is implemented.

## 8. Explicit TBD preservation

NS3 preserves at least:

- `NO101/NO102_DETECTION_TBD`;
- `TURN_DETECTION_TBD` / NO103 relationship;
- `DOW_SCALE_DETECTION_TBD`;
- `VISUAL_SELECTION_TBD` for basic lines;
- `LINE_SELECTION_TBD`;
- `APPLICATION_SELECTION_TBD` for TL Zone;
- `FIELD_REPRESENTATION_TBD`;
- `HIGH_LOW_DETECTION_TBD`;
- `BR_DETECTION_TBD`.

No candle counts, pips, ATR, MA, generic swing formula, or fixed timeframe mapping are introduced.

## 9. Independence completion condition

NS3 is complete at specification level when:

- Environment accepts only upstream facts/observations/evidence;
- Environment can return a valid state without Phase/Setup/Trigger;
- unresolved detector/selection work is explicit;
- R18/R20 do not create a dependency on Trigger;
- later-stage decisions are absent;
- static cases pass;
- NS3 audit passes.
