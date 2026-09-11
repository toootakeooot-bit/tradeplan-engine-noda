# NS7-B Scenario Renderer Audit

Status: **PASS — renderer contract + reference SVG implementation complete**

Repository: `toootakeooot-bit/tradeplan-engine-noda`

Branch: `feature/noda-v1`

Baseline: NS3-NS6 Final Audit HEAD `0a1ec61503d34f28db2e6cba31b865340d2357c7`

## 1. Scope

Audited scope:

- Scenario A/B/C visualization only;
- three-panel visual output;
- source-chart overlay output using supplied geometry;
- renderer input/output contracts;
- reference SVG implementation;
- static mock cases.

Out of scope:

- Scenario Composer semantics;
- chart-image recognition;
- automatic coordinate extraction;
- Entry / SL / TP / RR;
- TC / TradingCursor comparison.

## 2. Artifacts

Created before this audit:

- `spec/SCENARIO_RENDERER_RULES.md`
- `schema/scenario_renderer_input.schema.json`
- `schema/scenario_renderer_output.schema.json`
- `tools/render_scenario_svg.py`
- `tests/fixtures/ns7b_scenario_renderer_main.json`
- `tests/NS7B_SCENARIO_RENDERER_CASES.md`
- `examples/ns7b_scenario_panel_sample.svg`
- `examples/ns7b_scenario_overlay_sample.svg`

Repository comparison from the NS3-NS6 baseline showed exactly these eight added files and no modification of NS0-NS6 governing semantic files.

## 3. Boundary audit

| Check | Result |
|---|---|
| Renderer generates scenario semantics | NO / PASS |
| Renderer changes A/B/C ordering | NO / PASS |
| Renderer creates Entry / SL / TP | NO / PASS |
| Renderer evaluates Trigger | NO / PASS |
| Renderer imports TC logic | NO / PASS |
| Renderer fills HOLD/TBD | NO / PASS |
| Renderer can show UNKNOWN | YES / PASS |

## 4. Scenario Composer dependency

NS7-A final output schema is not yet fixed.

NS7-B therefore defines a narrow **adapter-facing visualization contract** rather than defining Scenario Composer semantics.

This is safe because:

- the renderer requires only display-ready fields;
- it does not define how A/B/C are generated;
- it does not manufacture a missing scenario;
- future NS7-A may map its output into this renderer contract;
- missing or invalid A/B/C data fails closed.

The stop condition `scenario input undefined and rendering impossible` was not triggered because the visualization contract can be specified and executable using a mock producer fixture without settling any scenario-generation rule.

Result: **PASS**.

## 5. Image output audit

Panel mode:

- renders exactly three scenario columns;
- preserves label/type/direction/status;
- displays premise/activation/invalidation/next/evidence;
- only renders path geometry when supplied.

Overlay mode:

- accepts a supplied source chart URI as image background;
- scales normalized coordinates to the output viewport;
- renders only supplied line/zone/path/marker primitives;
- performs no screenshot/pixel/chart interpretation.

Result: **PASS**.

## 6. Visual grammar audit

Scenario distinction does not depend on color alone:

- A uses a solid path;
- B uses a long-dash path;
- C uses a short/dotted path;
- explicit A/B/C labels are always retained.

Current/activation/invalidation can be represented with distinct supplied marker roles.

Result: **PASS**.

## 7. Uncertainty audit

The contract supports:

- `ACTIVE`;
- `WAITING`;
- `INVALID`;
- `UNKNOWN`;
- `INSUFFICIENT_EVIDENCE`;
- `NOT_EVALUATED`.

Missing geometry does not mean condition false.

Unknown scenario evidence is not converted into a visual prediction.

Result: **PASS**.

## 8. Reference implementation verification

The reference fixture was executed against the same `tools/render_scenario_svg.py` implementation before repository audit.

Observed:

- process return code: `0`;
- critical structural validation: PASS;
- `scenario_panel.svg`: generated;
- `scenario_overlay.svg`: generated;
- output status: `PARTIAL` because the fixture intentionally carries `MOCK_GEOMETRY`;
- Scenario order: A/B/C preserved.

The committed sample SVGs demonstrate the two output styles without claiming real chart-derived coordinates.

Result: **PASS**.

## 9. Fail-closed audit

Reference implementation blocks or rejects:

- scenario count other than three;
- scenario order other than A/B/C;
- required scenario field omission;
- coordinate outside `[0,1]`;
- unknown scenario reference in visual path/marker;
- empty source chart URI.

It does not replace these failures with inferred values.

Result: **PASS**.

## 10. Source Policy / NODA audit

No new NODA rule is created.

No generic technical-analysis detector is added.

No source chart is interpreted by the renderer.

No price level is invented.

No NS2 or NS3-NS6 TBD/HOLD is resolved.

No R21-R27 rule is reactivated.

No R31-R37 operational control is promoted to strategy semantics.

Result: **PASS**.

## 11. Stop-condition audit

Requested stop conditions were checked:

1. Scenario input impossible to define without scenario semantics: **NO** — adapter-facing display contract was sufficient.
2. Source vs Scenario conflict: **NONE**.
3. Upstream State shortage forcing responsibility violation: **NONE**.
4. Scenario regeneration required inside Renderer: **NO**.
5. New NODA Rule required for visualization: **NO**.

Therefore work could proceed without user interruption.

## 12. Completion gate

| Condition | Result |
|---|---|
| Scenario A/B/C visual output supported | PASS |
| three-panel SVG output supported | PASS |
| chart-overlay SVG output supported | PASS |
| current/branch/invalidation primitives representable | PASS |
| UNKNOWN / insufficient state preserved | PASS |
| scenario meaning not supplemented | PASS |
| Entry / SL / TP boundary preserved | PASS |
| new NODA Rule | NONE / PASS |
| Audit | PASS |

## 13. Verdict

**NS7-B: COMPLETE — PASS at renderer-contract/reference-implementation level.**

Meaning:

> Once a producer supplies Scenario A/B/C plus optional display geometry, NS7-B can generate field-reviewable SVG panel and chart-overlay artifacts without changing strategy meaning.

This milestone does **not** claim:

- automatic scenario composition;
- screenshot recognition;
- automatic line/price coordinate extraction;
- Entry / SL / TP calculation.

Those responsibilities remain outside NS7-B.
