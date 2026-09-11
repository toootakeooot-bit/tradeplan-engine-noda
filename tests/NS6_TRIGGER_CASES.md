# NS6 Trigger Static Cases

Purpose: verify Trigger responsibility and search-cue/context separation without implementing TBD detectors or Entry logic.

## Case T-01 — R14 small-Dow BR resolved

Input:
- upstream Environment/Phase/Setup context is available;
- governed R14 Break + Return Action is supplied/resolved.

Expected:
- `trigger_status = TRUE`;
- `trigger_type = SMALL_DOW_BR`;
- no Entry/SL/TP field is generated.

Result: PASS.

## Case T-02 — R14 detector unavailable

Input:
- relevant setup/context exists;
- Break/Return detector evidence is unresolved.

Expected:
- `trigger_status = UNKNOWN`;
- missing detector is not treated as `FALSE`;
- unresolved includes `SMALL_DOW_BR_DETECTION_TBD`.

Result: PASS.

## Case T-03 — R15 awareness revival small

Input:
- Main/Final phase context supplied;
- counter-trend small-Dow line Break/return-side awareness-revival evidence supplied as governed R15 Action.

Expected:
- `trigger_type = AWARENESS_REVIVAL_SMALL`;
- awareness revival scope = SMALL;
- R19 Return Move is not treated as identical to R15.

Result: PASS.

## Case T-04 — R19 Return Move only

Input:
- Return Move observation is known;
- no R14/R15/R16/Formation Action is resolved.

Expected:
- `return_move_observation.state = TRUE`;
- `trigger_status` is not set TRUE solely from R19;
- result is `UNKNOWN`, `FALSE`, or `NOT_EVALUATED` only according to whether an applicable Trigger path was actually evaluated.

Result: PASS.

## Case T-05 — R16 awareness revival large unresolved cycle

Input:
- relevant large-Dow line context exists;
- small-Dow cycle detection is unresolved.

Expected:
- R16 trigger remains `UNKNOWN`;
- no simple-touch shortcut is used;
- unresolved includes cycle/line-return TBD.

Result: PASS.

## Case T-06 — known TL Break context only

Input:
- known TL Break supplied under R20;
- no source-defined Trigger rule resolves true.

Expected:
- R20 meaning may record `TURN_CANDIDATE`;
- TL Break alone does not set `trigger_status = TRUE` or Entry.

Result: PASS.

## Case T-07 — known CH Break context only

Input:
- known CH Break supplied under R20;
- no source-defined Trigger rule resolves true.

Expected:
- R20 meaning may record `CONTINUATION_ACCELERATION_CANDIDATE`;
- CH Break alone does not set Entry or standalone Trigger true.

Result: PASS.

## Case T-08 — Reversal Formation action candidate

Input:
- SetupState contains recognized Reversal Formation;
- source-defined neckline/support-resistance Action evidence is supplied/resolved.

Expected:
- `trigger_type = REVERSAL_FORMATION_ACTION` may be TRUE;
- Formation recognition itself remains Setup evidence;
- Entry remains outside scope.

Result: PASS.

## Case T-09 — Continuation Formation without boundary Break

Input:
- recognized Continuation Formation setup;
- continuation-side Break not resolved.

Expected:
- Formation setup remains present upstream;
- Trigger is `UNKNOWN` or `NOT_EVALUATED`, not TRUE;
- NS6 does not convert Setup presence into Trigger.

Result: PASS.

## Case T-10 — Continuation Formation with supplied continuation-side Break

Input:
- recognized Continuation Formation setup;
- governed continuation-side boundary Break supplied/resolved.

Expected:
- `trigger_type = CONTINUATION_FORMATION_BREAK` may be TRUE;
- no Entry/SL/TP conclusion.

Result: PASS.

## Case T-11 — evaluated negative Trigger

Input:
- applicable trigger path is fully evaluable under governed evidence;
- required Action is absent.

Expected:
- `trigger_status = FALSE` is permitted;
- FALSE is used only because evaluation was actually possible.

Result: PASS.

## Case T-12 — conflicting Trigger evidence

Input:
- governed trigger evidence is inconsistent and no tie-break rule exists.

Expected:
- `trigger_status = UNKNOWN`;
- unresolved records case-evidence conflict;
- no majority vote/score is invented.

Result: PASS.

## Case T-13 — Entry logic offered downstream

Input:
- upstream states plus external proposed Entry price/SL/TP.

Expected:
- NS6 ignores/rejects Entry/SL/TP for Trigger derivation;
- Trigger output contains no Entry plan.

Result: PASS.

## Case T-14 — HOLD rule offered to complete Trigger

Input:
- R21-R27 text proposed to fill a missing Trigger condition.

Expected:
- rejected;
- HOLD remains HOLD;
- Trigger unresolved if current source rules are insufficient.

Result: PASS.

## Static-case verdict

All NS6 cases are satisfiable under `spec/TRIGGER_RULES.md` while preserving Trigger/Entry separation and unresolved detector states.
