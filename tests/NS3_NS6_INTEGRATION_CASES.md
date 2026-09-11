# NS3-NS6 Integrated Regression Cases

Purpose: verify one-way behavior across:

`Environment -> Phase -> Setup -> Trigger`

without implementing HOLD rules or unresolved detectors.

These cases are symbolic and rely on pre-resolved governed observations/evidence where a detector remains TBD.

## I-01 — Environment only

Input:
- governed structural highs/lows/lines available;
- no Phase evidence supplied.

Expected:
- Environment resolves available structure;
- Phase = UNKNOWN;
- Setup/Trigger are NOT_EVALUATED;
- no downstream backfill.

Result: PASS.

## I-02 — Environment -> Phase resolved/candidate

Input:
- Environment structure available;
- governed Phase evidence sufficient for a Phase result or source-supported candidate;
- no Setup recognition.

Expected:
- PhaseState produced;
- Setup absent/unknown according to actual evaluation;
- Trigger not inferred from Phase alone.

Result: PASS.

## I-03 — Phase present, Setup absent

Input:
- valid Environment and Phase;
- applicable Setup path is actually evaluated and absent.

Expected:
- `setup_status = ABSENT`;
- Trigger = NOT_EVALUATED;
- no Entry conclusion.

Result: PASS.

## I-04 — Setup present, Trigger waiting

Input:
- valid Environment/Phase;
- governed Reversal or Continuation Formation setup supplied;
- no resolved downstream Action.

Expected:
- Setup PRESENT;
- local `wait_for_trigger = TRUE`;
- Trigger UNKNOWN/NOT_EVALUATED;
- formal R21 Wait is not invoked.

Result: PASS.

## I-05 — Trigger resolved

Input:
- valid upstream states;
- governed R14/R15/R16 or Formation Action evidence resolves Trigger TRUE.

Expected:
- Trigger TRUE;
- pipeline stops at Trigger;
- no Entry/SL/TP/Wait plan is produced.

Result: PASS.

## I-06 — Detector TBD creates UNKNOWN mid-pipeline

Input:
- raw facts exist;
- a required upstream NODA detector remains TBD with no pre-resolved observation.

Expected:
- affected stage returns UNKNOWN;
- downstream stages do not convert UNKNOWN to FALSE or invent missing data;
- unresolved codes propagate as context where relevant.

Result: PASS.

## I-07 — Source/evidence insufficiency

Input:
- source-governed inputs do not support the requested decision.

Expected:
- relevant stage stops at UNKNOWN/NOT_EVALUATED;
- no generic TA or TC/TradingCursor substitution;
- no new rule generated.

Result: PASS.

## I-08 — Field-scale transition candidate

Input:
- Environment contains a known current-Field CH Break context;
- R13 Fibonacci/Field evidence available;
- Field transition detector remains TBD.

Expected:
- Phase may set `higher_scale_recheck_required = TRUE`;
- no automatic timeframe is chosen;
- `200%` alone is not used as transition condition;
- downstream Setup/Trigger remain independent.

Result: PASS.

## I-09 — Continuation Formation path

Input:
- Environment/Phase support relevant context;
- Continuation Formation recognition supplied;
- no boundary Break initially.

Expected first pass:
- Setup PRESENT;
- Trigger not TRUE.

Then supply governed continuation-side Break evidence.

Expected second pass:
- Setup remains unchanged;
- Trigger may become TRUE as `CONTINUATION_FORMATION_BREAK`;
- no Entry conclusion.

Result: PASS.

## I-10 — Reversal Formation path

Input:
- Environment/Phase context available;
- Reversal Formation recognition supplied;
- source-defined neckline/support-resistance Action later supplied.

Expected:
- Setup = Reversal Formation candidate;
- Trigger becomes TRUE only when downstream Action itself is resolved;
- Formation presence alone never equals Trigger/Entry.

Result: PASS.

## I-11 — R19 Return Move does not short-circuit pipeline

Input:
- Return Move observation supplied;
- no applicable source-defined Trigger Action resolved.

Expected:
- R19 is carried as search cue;
- Trigger not TRUE solely from Return Move;
- Entry unavailable.

Result: PASS.

## I-12 — R20 CH Break semantics do not create Entry

Input:
- known CH Break context.

Expected:
- Environment/Trigger context can record continuation/acceleration candidate meaning;
- no standalone Trigger TRUE unless a Trigger rule is satisfied;
- no Entry.

Result: PASS.

## I-13 — evidence conflict at Phase

Input:
- R13 structure and MA evidence disagree;
- no source-defined aggregation/tie-break rule.

Expected:
- Phase unresolved unless independently supplied;
- Setup/Trigger do not rewrite Phase to proceed;
- no vote/score.

Result: PASS.

## I-14 — HOLD rule intrusion

Input:
- R21-R27 or R31-R37 is proposed as missing Stage logic.

Expected:
- rejected for NS3-NS6 strategy semantics;
- current unresolved state remains.

Result: PASS.

## I-15 — downstream-to-upstream mutation attempt

Input:
- Trigger result is changed after upstream Environment/Phase/Setup were produced.

Expected:
- Environment/Phase/Setup do not mutate retroactively unless their own upstream evidence changes;
- stage dependency remains one-way.

Result: PASS.

## Integrated regression verdict

All required integration scenarios are representable with the four stage contracts and preserve uncertainty/HOLD boundaries.
