# NS5 Setup Static Cases

Purpose: verify Setup responsibility without inventing Formation/line detectors or consuming Trigger output.

## Case S-01 — Reversal Formation supplied as recognized

Input:
- Environment/Phase context available;
- governed Reversal Formation recognition supplied;
- no Break/Action supplied.

Expected:
- `setup_status = PRESENT`;
- `setup_type = REVERSAL_FORMATION`;
- Formation family/pattern retained;
- `wait_for_trigger = TRUE` or equivalent local readiness state;
- no Trigger/Entry conclusion.

Result: PASS.

## Case S-02 — Continuation Formation supplied as recognized

Input:
- broader/current trend context available;
- governed Continuation Formation recognition supplied;
- boundary Break not supplied.

Expected:
- `setup_status = PRESENT`;
- `setup_type = CONTINUATION_FORMATION`;
- `wait_for_trigger = TRUE`;
- continuation is not yet confirmed as Trigger/Entry.

Result: PASS.

## Case S-03 — Formation detector unavailable

Input:
- chart/market facts available;
- `REVERSAL_FORMATION_DETECTION_TBD` / `CONTINUATION_FORMATION_DETECTION_TBD` unresolved;
- no pre-resolved Formation recognition supplied.

Expected:
- Formation-based setup is `UNKNOWN`, not `ABSENT`;
- no generic-TA Formation detector is substituted.

Result: PASS.

## Case S-04 — small-Dow line context only

Input:
- governed small-Dow line reference supplied;
- no source-defined Formation or other complete setup candidate.

Expected:
- line is preserved as Setup component/context;
- line presence alone does not automatically set a Formation setup;
- Entry remains outside scope.

Result: PASS.

## Case S-05 — intermediate TL and middle-Dow counter TL context

Input:
- both R17 line types supplied.

Expected:
- separate line roles retained;
- no aliasing;
- Setup may reference either/both as context without redefining them.

Result: PASS.

## Case S-06 — Formation recognized plus downstream Break accidentally supplied

Input:
- recognized Formation;
- external Break/Trigger datum also supplied.

Expected:
- Setup remains based on Formation/context;
- downstream Break is not required to justify setup recognition;
- NS5 does not emit Trigger true.

Result: PASS.

## Case S-07 — evaluated absence

Input:
- a governed Formation detector/result is supplied as evaluated and absent;
- prerequisites are sufficient.

Expected:
- `setup_status = ABSENT` for the evaluated setup path;
- absence is allowed only because evaluation actually occurred.

Result: PASS.

## Case S-08 — incomplete upstream Phase

Input:
- Environment known;
- Phase is `UNKNOWN`;
- Formation recognition supplied.

Expected:
- Setup may preserve the Formation candidate but records Phase context as unresolved where relevant;
- it does not fabricate a Phase to make Setup valid;
- overall setup may remain `UNKNOWN` if the source-defined setup requires unresolved Phase context.

Result: PASS.

## Case S-09 — source catalog enforcement

Input:
- a pattern name not present in the currently source-confirmed catalog is proposed by generic TA.

Expected:
- not promoted into `formation_pattern` as a NODA rule;
- requires governed source addition/review before use.

Result: PASS.

## Case S-10 — formal Wait rule leakage

Input:
- Setup present but Trigger not evaluated;
- R21 remains HOLD.

Expected:
- NS5 may set local `wait_for_trigger = TRUE`;
- it does not claim formal NODA Wait decision under R21;
- no R21 semantics are revived.

Result: PASS.

## Case S-11 — conflicting setup evidence

Input:
- governed context does not permit a unique setup conclusion.

Expected:
- `setup_status = UNKNOWN`;
- evidence retained;
- no vote/score/tie-break invented.

Result: PASS.

## Static-case verdict

All NS5 cases are satisfiable under `spec/SETUP_RULES.md` while preserving Formation and line-selection TBDs and stage boundaries.
