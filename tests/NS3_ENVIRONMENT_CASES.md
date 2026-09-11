# NS3 Environment Static Cases

Purpose: verify responsibility and uncertainty behavior without implementing TBD detectors.

These are symbolic static cases. They do not define candle counts, pips, timeframes, or generic TA detectors.

## Case E-01 — resolved structural input

Input:
- governed significant highs/lows are already supplied;
- their sequence satisfies sourced R02 upward-trend semantics;
- governed TL/CH references are supplied;
- no Phase/Setup/Trigger input.

Expected:
- `EnvironmentState.trend = UP`;
- supplied structural objects are retained;
- no Phase/Setup/Trigger field is produced;
- result may be `KNOWN` for resolved fields.

Result: PASS.

## Case E-02 — raw OHLC only, significant-high/low detector unavailable

Input:
- MF001/MF006 supplied;
- NO101/NO102 not supplied;
- significant-high/low detection remains TBD.

Expected:
- raw candle highs/lows are not promoted to NODA-significant highs/lows;
- `trend.resolution = UNKNOWN`;
- unresolved records identify significant-high/low detector dependency;
- no generic swing rule is used.

Result: PASS.

## Case E-03 — Dow scale unresolved

Input:
- structural highs/lows and lines available;
- `DOW_SCALE_DETECTION_TBD` unresolved.

Expected:
- line/structure evidence may be carried;
- Dow scale is `UNKNOWN`;
- absence of a resolved scale is not interpreted as `SMALL` or `LARGE` by convenience.

Result: PASS.

## Case E-04 — intermediate TL vs middle-Dow counter TL

Input:
- two separately sourced line references, one identified as intermediate TL and one as middle-Dow counter TL.

Expected:
- both are represented as separate line types;
- no alias/merge occurs;
- line selection remains separately unresolved if not supplied.

Result: PASS.

## Case E-05 — post-Break Field remap with supplied Break evidence

Input:
- a governed/supplied Break context exists;
- a new structural high/low and redraw evidence are already available;
- no Trigger output is supplied.

Expected:
- R18 may produce/record Field-remap context;
- Environment does not call Trigger;
- no Entry conclusion is created.

Result: PASS.

## Case E-06 — post-Break logic without Break detector/evidence

Input:
- current Field and lines exist;
- no governed Break evidence is available;
- BR detector remains TBD.

Expected:
- `break_context` is `UNKNOWN` or `NOT_EVALUATED`;
- `field_remap` is not forced false;
- no future Trigger result is requested.

Result: PASS.

## Case E-07 — TL Break / CH Break meaning only

Input:
- Break type is supplied as known TL Break or CH Break.

Expected:
- TL Break may be annotated as `TURN_CANDIDATE` context;
- CH Break may be annotated as `CONTINUATION_ACCELERATION_CANDIDATE` context;
- neither result is an Entry or standalone Trigger decision.

Result: PASS.

## Case E-08 — conflicting case evidence

Input:
- available governed evidence is internally inconsistent for a requested Environment field;
- no Source conflict is asserted.

Expected:
- affected field resolves to `UNKNOWN`;
- `unresolved[]` records a case-evidence conflict;
- AI does not average/vote/invent a tie-break rule.

Result: PASS.

## Case E-09 — downstream data accidentally supplied

Input:
- Environment inputs plus an external `trigger=true` field.

Expected:
- NS3 ignores/rejects the downstream Trigger datum for Environment derivation;
- Environment output is unchanged by Trigger.

Result: PASS.

## Case E-10 — HOLD rule offered as authority

Input:
- R21-R27 or R31-R37 text is offered to fill a missing Environment detector.

Expected:
- rejected as Environment strategy authority;
- unresolved remains unresolved.

Result: PASS.

## Static-case verdict

All NS3 cases are satisfiable under `spec/ENVIRONMENT_RULES.md` without new NODA semantics or detector implementation.
