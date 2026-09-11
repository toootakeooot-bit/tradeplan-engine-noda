# NS4 Phase Rules

Status: **NS4 specification — Phase responsibility fixed, detector/aggregation TBDs preserved**

Upstream contract: `schema/environment_state.schema.json`

Controlling baseline:
- `spec/NS2_FINAL_RULE_MATRIX.csv`
- `spec/NS2_R13_R30A_REREVIEW.md`
- `spec/RESPONSIBILITY.md`
- `docs/SOURCE_POLICY.md`
- NS1 governance
- NS3 Environment specification/audit

## 1. Responsibility

NS4 owns `2-2 Phase` only.

Phase answers:

> Given an EnvironmentState and any governed Phase evidence, what Phase can be resolved without using Setup, Trigger, Entry, SL, TP, Wait, or Invalidation?

The NODA Phase vocabulary is:
- `EARLY` — 先行期;
- `MAIN` — 本格局面;
- `FINAL` — 最終局面;
- `UNKNOWN` — available governed information is insufficient to resolve the case.

NS4 does not create a Phase detector that NS2 left TBD.

## 2. Rule mapping

### Primary Phase rules

| Rule | Phase responsibility | Unresolved carried forward |
|---|---|---|
| R11 | three-phase semantics: Early / Main / Final | `PHASE_DETECTION_TBD`, boundaries/nesting TBD |
| R12 | Early-phase context: broad-structure edge -> current final phase -> fine structure/action -> next early-phase candidate | `EDGE_PROXIMITY_TBD`; no fixed TF mapping |
| R13 | Main-phase confirmation through multiple evidence paths | `PHASE_DETECTION_TBD`, `MA_DIRECTION_DETECTION_TBD`, `FIELD_TRANSITION_DETECTION_TBD` |
| R30-A | MA belongs to Main-phase judgment in current NODA Core | exact MA-direction detector TBD |

### Upstream Environment context

R01-R10/R17/R18/R20 can be consumed only through EnvironmentState / governed evidence. NS4 does not rewrite Environment semantics.

### Explicit exclusions

- R14-R16 are Trigger rules and cannot be used to back-solve Phase.
- R28/R29 are Setup rules. Formation may be adjacent/downstream evidence but is not made a mandatory R13 Phase gate.
- R21-R27 remain HOLD.
- R31-R37 remain Operational Control / HOLD.

## 3. Phase evaluation model

Because exact Phase detection/aggregation remains TBD, NS4 separates:

1. `phase` — resolved Phase only when governed rule evidence is sufficient;
2. `phase_candidate` — a source-supported candidate suggested by available evidence;
3. `evidence[]` — evidence paths and their evaluation state;
4. `unresolved[]` — detector/aggregation gaps preventing a resolved Phase.

This separation prevents a candidate from being silently promoted to a final Phase.

## 4. R11 semantics

R11 defines the three Phase meanings but does not supply a complete OHLC detector.

If the case lacks enough source-governed evidence to distinguish Phase, output:

- `phase = UNKNOWN`;
- optionally `phase_candidate` when a source-supported candidate exists;
- unresolved code referencing `PHASE_DETECTION_TBD`.

No fixed D1/H4/H1 mapping is created.

## 5. R12 Early-phase handling

NS4 may identify `EARLY` as a candidate when governed evidence expresses the sourced sequence:

`broad-structure edge -> current final phase -> fine structure/action -> next early-phase candidate`

However:
- exact edge proximity remains TBD;
- small-structure action detection may depend on unresolved downstream/observation evidence;
- R12 alone does not authorize Entry.

When prerequisites are incomplete, candidate/evidence can be emitted while `phase` remains `UNKNOWN`.

## 6. R13 Main-phase handling

`spec/NS2_R13_R30A_REREVIEW.md` is controlling.

R13 has multiple evidence paths and **no numeric evidence-count or score aggregation rule is invented**.

### Method A — structure

Source-confirmed evidence:
- large-Dow edge context;
- last push-low / return-high Break;
- candidate transition beyond Early phase toward Main phase.

Exact Break/Phase detector remains TBD.

### Method B — MA direction

Source-confirmed role:
- middle MA group `21 / 40 / 62 EMA` -> small-Dow directional context;
- long MA `200 SMA` -> large-Dow directional context;
- bullish confirmation: both groups upward;
- bearish confirmation: both groups downward.

`MA_DIRECTION_DETECTION_TBD` remains open. No perfect order, MA-cross rule, angle threshold, distance threshold, or score is added.

R30-A limits MA use in current NODA Core to Main-phase judgment. MA is not used by NS4 to define Early or Final phase.

### Method C — Fibonacci / Field scale

Source-confirmed core:
- Fibonacci Expansion observes trend-continuation levels;
- small-Dow N-wave or larger-Dow N-wave may be used as the relevant 100% scale according to sourced context;
- `100 / 161.8 / 200 / 261.8%` are source-shown continuation levels.

User-approved clarification:
- `100%–161.8%` may be used as one Main-phase volume/distance observation within the current Field;
- Fibonacci ratio alone does not trigger higher-timeframe transition;
- current-Field CH Break is the structural cue for possible move to a broader Field / higher-scale re-observation;
- `200% / 261.8%` remain continuation levels and do not automatically mean higher timeframe.

`FIELD_TRANSITION_DETECTION_TBD` remains open.

## 7. No hidden aggregation rule

NS4 must not create any of the following without later approval:
- `1 of 3 evidence paths = MAIN`;
- `2 of 3 = MAIN`;
- weighted confidence score;
- mandatory MA + Break conjunction;
- mandatory Fibonacci threshold;
- majority vote.

If multiple evidence paths align, they may be recorded as reinforcing evidence. Exact final aggregation remains governed by `PHASE_DETECTION_TBD` unless a resolved case explicitly supplies the Phase classification.

## 8. Higher-scale recheck

`higher_scale_recheck_required` is a Phase-context flag, not a timeframe-switch command.

It may be `TRUE` only when governed evidence supports the user-approved Field-scale interpretation, such as a known current-Field CH Break that indicates possible transition to a broader Field.

It does not mean:
- `200% reached`;
- automatically select D1/H4/H1;
- automatically replace the current Phase.

## 9. PhaseState contract semantics

Machine-readable contract: `schema/phase_state.schema.json`.

Allowed resolution states:
- `KNOWN`;
- `UNKNOWN`;
- `NOT_EVALUATED`.

Evidence state is represented independently from Phase resolution.

A detector gap is `UNKNOWN`, not `FALSE`.

## 10. Completion condition

NS4 is complete at specification level when:
- EnvironmentState is the only stage input;
- Phase output is independent of Setup/Trigger;
- R13 latest semantics are controlling;
- MA role is no longer marked semantically TBD, only detection remains TBD;
- no evidence aggregation threshold is invented;
- `UNKNOWN` is valid when Phase cannot be resolved;
- static cases and audit pass.
