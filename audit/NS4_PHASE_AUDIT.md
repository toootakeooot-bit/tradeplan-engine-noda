# NS4 Phase Audit

Status: **PASS**

Upstream: NS3 Environment specification/audit.

Scope: `2-2 Phase` only.

## 1. Files reviewed

- `spec/PHASE_RULES.md`
- `schema/phase_state.schema.json`
- `tests/NS4_PHASE_CASES.md`
- `spec/NS2_FINAL_RULE_MATRIX.csv`
- `spec/NS2_R13_R30A_REREVIEW.md`
- NS3 Environment artifacts

## 2. Stage boundary audit

| Check | Result |
|---|---|
| Environment is the only stage dependency | PASS |
| Setup result used to resolve Phase | NO / PASS |
| Trigger result used to resolve Phase | NO / PASS |
| Entry/SL/TP/Wait logic introduced | NO / PASS |
| Formation promoted to mandatory R13 Phase gate | NO / PASS |
| R21-R27 HOLD used | NO / PASS |

## 3. R13 / R30-A regression audit

Verified:
- latest R13 rereview is controlling;
- structure, MA direction, and Fibonacci/Field-scale evidence paths remain separate;
- MA semantic role is fixed to Main-phase judgment in current Core;
- exact MA-direction detector remains TBD;
- `200%` alone does not cause higher-timeframe transition;
- known current-Field CH Break is the structural cue for possible broader-Field recheck;
- Formation responsibility remains R28/R29.

Result: **PASS**.

## 4. Aggregation audit

No unsupported aggregation logic was introduced.

Specifically absent:
- one-evidence-path automatically equals MAIN;
- 2-of-3 rule;
- weighted score;
- majority vote;
- mandatory MA+Break conjunction;
- mandatory Fibonacci threshold.

`phase_candidate` is separated from resolved `phase` so evidence can be retained without silently confirming a Phase.

Result: **PASS**.

## 5. Unknown-state audit

When Phase detector sufficiency is unresolved, `phase = UNKNOWN` is valid.

Detector absence is not converted to `FALSE` or another Phase.

Result: **PASS**.

## 6. Source-policy audit

No fixed timeframe map, MA perfect order, MA cross, slope threshold, pips threshold, generic TA Phase detector, TC/TradingCursor logic, or backtest-derived rule was added.

Result: **PASS**.

## 7. Static cases

P-01 through P-11 cover:
- unknown Phase;
- Early candidate;
- Main structure candidate;
- MA agreement/misalignment;
- Fibonacci without/with Field-scale cue;
- aligned evidence without invented scoring;
- evidence disagreement;
- Formation boundary;
- downstream backflow rejection.

Result: **PASS**.

## 8. Verdict

**NS4 COMPLETE — PASS**

PhaseState can be produced independently from EnvironmentState while preserving detector/aggregation TBDs and without consuming Setup/Trigger outputs.

NS5 Setup may proceed.
