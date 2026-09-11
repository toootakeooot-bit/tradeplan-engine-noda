# NS4 Phase Static Cases

Purpose: verify Phase responsibility, R13/R30-A rereview semantics, and UNKNOWN behavior without inventing Phase detectors or evidence aggregation rules.

## Case P-01 — Environment known, Phase detector unresolved

Input:
- valid EnvironmentState;
- no governed Phase classification;
- `PHASE_DETECTION_TBD` unresolved.

Expected:
- `phase = UNKNOWN`;
- environment fields remain available as evidence;
- no Setup/Trigger output.

Result: PASS.

## Case P-02 — source-supported Early candidate

Input:
- broad-structure edge context available;
- current final-phase context supplied/resolved;
- fine-structure/action evidence supports transition toward next Early phase;
- exact edge/action detector remains partially unresolved.

Expected:
- `phase_candidate = EARLY`;
- `phase` may remain `UNKNOWN` if final detector sufficiency is not established;
- no Entry conclusion.

Result: PASS.

## Case P-03 — Main candidate from R13 Method A

Input:
- large-Dow edge context known;
- source-governed last push-low/return-high Break evidence supplied;
- no MA direction evidence.

Expected:
- R13 price-structure evidence recorded as `SUPPORTS`;
- `phase_candidate = MAIN` is permitted;
- no invented rule that one evidence path automatically resolves `MAIN`;
- `phase` remains `UNKNOWN` unless the case includes an already-resolved Phase judgment.

Result: PASS.

## Case P-04 — MA confirmation evidence

Input:
- middle MA group direction supplied as all upward;
- long MA direction supplied as upward;
- exact slope detector is not evaluated inside NS4.

Expected:
- R13 MA evidence records upward agreement;
- evidence may reinforce Main-phase candidate;
- MA does not define Early/Final;
- no perfect-order, MA-cross, angle, distance, or score condition appears.

Result: PASS.

## Case P-05 — MA mixed direction

Input:
- middle MA group is mixed or unresolved;
- long MA is upward.

Expected:
- no bullish MA agreement is asserted;
- MA evidence is `DOES_NOT_SUPPORT` or `UNKNOWN` according to supplied state;
- mixed MA is not converted into another Phase by inference.

Result: PASS.

## Case P-06 — Fibonacci level without Field CH Break

Input:
- continuation distance is around 200% of the relevant sourced reference scale;
- no known current-Field CH Break.

Expected:
- `higher_scale_recheck_required` is not set TRUE merely because 200% was observed;
- no automatic higher timeframe/Field switch;
- Fibonacci remains continuation-distance evidence.

Result: PASS.

## Case P-07 — current-Field CH Break and broader-Field recheck

Input:
- known current-Field CH Break evidence supplied;
- Field transition detector itself remains TBD.

Expected:
- higher-scale recheck may be marked `TRUE` as the user-approved structural cue;
- current Phase is not automatically replaced;
- no fixed timeframe is selected.

Result: PASS.

## Case P-08 — multiple aligned Main evidence paths

Input:
- R13 structure evidence supports Main candidate;
- MA-direction evidence supports same direction;
- Fibonacci/Field evidence is compatible.

Expected:
- all evidence paths are preserved;
- no numeric confidence score or `2-of-3` rule is created;
- resolved Phase requires governed sufficiency; otherwise `phase_candidate = MAIN`, `phase = UNKNOWN`.

Result: PASS.

## Case P-09 — evidence disagreement

Input:
- source-governed structural evidence points toward a Main candidate;
- MA evidence does not align;
- no teacher-defined tie-break rule exists.

Expected:
- no vote/average/tie-break is invented;
- `phase = UNKNOWN` unless an independently resolved Phase is supplied;
- conflict/unresolved note is preserved.

Result: PASS.

## Case P-10 — Formation supplied to Phase

Input:
- a Reversal or Continuation Formation candidate is supplied;
- Phase evidence otherwise unresolved.

Expected:
- Formation is not used as a mandatory R13 gate or a standalone Phase detector;
- R28/R29 responsibility remains Setup;
- Phase remains based on R11/R12/R13/R30-A semantics.

Result: PASS.

## Case P-11 — downstream Trigger accidentally supplied

Input:
- EnvironmentState plus `trigger=true` from an external caller.

Expected:
- Trigger is ignored/rejected for Phase resolution;
- no backflow.

Result: PASS.

## Static-case verdict

All NS4 cases are satisfiable without inventing Phase thresholds, evidence aggregation, detector logic, or later-stage dependencies.
