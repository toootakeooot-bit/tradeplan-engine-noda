# NS7-B Scenario Renderer Static Cases

Status: **STATIC CONTRACT / REFERENCE RENDERER CASE SET**

This file tests rendering responsibility, not trading correctness.

## Common assertions

Every case must preserve:

- Scenario order `A -> B -> C`;
- supplied scenario meaning;
- supplied upstream references;
- `UNKNOWN != FALSE`;
- no Entry / SL / TP inference;
- no NODA rule creation;
- no TC / TradingCursor import;
- no geometry inference from chart pixels.

## Case matrix

| ID | Case | Expected panel | Expected overlay | Expected result |
|---|---|---|---|---|
| SR-01 | Main continuation | A/B/C shown | supplied A path/context | PASS |
| SR-02 | Alternative reversal | A/B/C shown | supplied B path distinguished | PASS |
| SR-03 | Wait | WAIT visible | supplied wait area/path only | PASS |
| SR-04 | Setup exists / Trigger waiting | `WAITING` preserved | no trigger mark unless supplied | PASS |
| SR-05 | Trigger resolved | supplied status/marker rendered | supplied marker/path | PASS |
| SR-06 | UNKNOWN-heavy | UNKNOWN retained | missing geometry not invented | PASS |
| SR-07 | Field-scale transition candidate | supplied field/CH shown | no automatic higher-timeframe inference | PASS |
| SR-08 | Continuation Formation | supplied scenario rendered | no Formation detector added | PASS |
| SR-09 | Reversal Formation | supplied scenario rendered | no Formation detector added | PASS |
| SR-10 | Insufficient evidence | unresolved text visible | no fabricated path | PASS |
| SR-11 | Missing optional geometry | panel renders | overlay limited to supplied primitives | PASS/PARTIAL |
| SR-12 | Wrong scenario order | blocked | blocked | BLOCKED |

## Reference executable case

Fixture:

`tests/fixtures/ns7b_scenario_renderer_main.json`

Command:

```bash
python tools/render_scenario_svg.py \
  tests/fixtures/ns7b_scenario_renderer_main.json \
  --out-dir rendered/ns7b
```

Expected artifacts:

- `rendered/ns7b/scenario_panel.svg`
- `rendered/ns7b/scenario_overlay.svg`

The fixture intentionally carries `MOCK_GEOMETRY`, so output status is `PARTIAL`. This represents unresolved coordinate provenance, not a false trading condition.

## SR-01 Main continuation

Scenario A is `MAIN / UP / WAITING` and an A path is supplied.

Expected:
- path rendered from supplied points only;
- renderer does not activate A;
- no Entry is created.

## SR-02 Alternative reversal

Scenario B remains `ALTERNATIVE` even when its path is supplied.

Renderer must not promote it to MAIN.

## SR-03 Wait

Scenario C remains visible even when A/B exist.

WAIT is not converted to neutral Entry.

## SR-04 Setup present / Trigger waiting

`WAITING` remains a display state.

Absent trigger geometry is not synthesized.

## SR-05 Trigger resolved

When producer supplies `ACTIVE` plus activation geometry, the renderer displays those supplied values only. It does not verify the Trigger.

## SR-06 UNKNOWN-heavy

UNKNOWN must remain UNKNOWN.

No default FALSE, INVALID, BUY, or SELL substitution is allowed.

## SR-07 Field-scale transition candidate

If upstream supplies CH/field geometry, the renderer displays it.

It must not infer `200% = higher timeframe` or select a broader Field by itself.

## SR-08 / SR-09 Formation

Formation semantics remain upstream R28/R29 responsibility.

Renderer may display supplied labels and paths but does not recognize chart patterns.

## SR-10 Insufficient evidence

`INSUFFICIENT_EVIDENCE` is renderable.

Missing activation/invalidation levels are not invented.

## SR-11 Missing optional geometry

Panel mode remains valid.

Overlay is limited to supplied primitives.

## SR-12 Invalid order

Input order `B/A/C`, duplicate IDs, or missing C must fail closed.

This protects fixed A/B/C visual identity from accidental reordering.
