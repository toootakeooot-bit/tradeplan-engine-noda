# NS7-B Scenario Visual Renderer

Status: **SPECIFICATION + REFERENCE SVG RENDERER BASELINE**

Repository: `toootakeooot-bit/tradeplan-engine-noda`

Branch: `feature/noda-v1`

Baseline: NS3-NS6 Final Audit HEAD `0a1ec61503d34f28db2e6cba31b865340d2357c7`

## 1. Purpose

NS7-B converts already-composed Scenario A / B / C data into visual artifacts for fast field review.

It is a **renderer**, not a strategy engine and not a scenario generator.

Input chain:

`EnvironmentState + PhaseState + SetupState + TriggerState + ScenarioComposer output + source chart image(s)`

Output:

- `scenario_panel_image`
- `scenario_overlay_image` when chart geometry is supplied

The renderer must preserve upstream uncertainty and must never infer a missing NODA rule, price level, chart coordinate, Entry, SL, TP, or Trigger.

## 2. Responsibility boundary

NS7-B owns:

- visual layout;
- visual distinction of Scenario A / B / C;
- rendering of supplied current-position, line, zone, path, activation and invalidation annotations;
- compact display of premise, activation, invalidation, next action, evidence summary and status;
- display of `UNKNOWN`, `INSUFFICIENT_EVIDENCE`, `WAIT_FOR_MORE_STRUCTURE`, or `NOT_EVALUATED`.

NS7-B does not own:

- scenario generation or ranking;
- NODA rule interpretation beyond displaying supplied data;
- new Trigger evaluation;
- Entry / SL / TP / RR;
- broker or execution logic;
- TC / TradingCursor comparison;
- filling TBD/HOLD definitions.

## 3. NS7-A dependency

The final Scenario Composer schema is not yet frozen.

Therefore NS7-B defines an **adapter-facing renderer input contract** that captures only the fields required for visualization. A future NS7-A producer may map into this contract without changing renderer semantics.

This is not permission for NS7-B to create or repair scenario meaning.

If Scenario A / B / C are absent or structurally incomplete, rendering must fail closed or surface an unresolved state.

## 4. Input contract

`schema/scenario_renderer_input.schema.json` is controlling.

Required high-level data:

- `render_request_id`;
- `source_chart_images[]`;
- upstream state references;
- exactly three scenarios ordered A, B, C;
- optional `visual_annotations`.

Each scenario carries:

- `scenario_id`: `A`, `B`, or `C`;
- `scenario_label`;
- `scenario_type`: `MAIN | ALTERNATIVE | WAIT`;
- `premise`;
- `direction`;
- `activation_conditions[]`;
- `invalidation_conditions[]`;
- `next_action`;
- `evidence_refs[]`;
- `priority`;
- `confidence`;
- `current_status`.

`confidence` is descriptive only. NS7-B does not calculate or rescore it.

## 5. Visual coordinates

Overlay geometry is never inferred from text.

All geometry must be supplied explicitly as normalized coordinates in `[0,1]`:

- `x=0` = left edge;
- `x=1` = right edge;
- `y=0` = top edge;
- `y=1` = bottom edge.

Supported annotation primitives:

- `marker`;
- `line`;
- `zone`;
- `path`.

A renderer may scale normalized coordinates to the output viewport.

If required geometry is missing, the renderer may still produce the three-panel summary but must not invent overlay geometry.

## 6. Output modes

### 6.1 Panel mode

One image with three scenario columns:

- left: Scenario A;
- center: Scenario B;
- right: Scenario C.

Required visible information:

- scenario label/type;
- direction;
- current status;
- premise;
- activation;
- invalidation;
- next action;
- evidence summary.

A simplified path is drawn only when `visual_annotations.paths` supplies one.

### 6.2 Overlay mode

The first eligible source chart image is used as the background.

Only supplied annotation geometry may be drawn.

Overlay may include:

- current-position marker;
- TL / CH / HL / edge / zone / field boundaries;
- Scenario A/B/C paths;
- activation markers;
- invalidation markers;
- supplied labels.

No chart recognition occurs inside NS7-B.

## 7. Visual grammar

The reference renderer uses stable visual roles, not strategy meaning:

- solid path: supplied scenario path;
- dashed boundary: supplied line/boundary;
- translucent rectangle: supplied zone;
- circle marker: supplied current/activation point;
- cross marker: supplied invalidation point;
- label: short supplied text.

Scenario identity must remain visually distinguishable in monochrome as well as color-capable displays by combining label + dash/marker patterns.

The renderer must not rely on color alone.

## 8. Unknown and insufficient states

The renderer preserves uncertainty.

Allowed scenario/runtime labels include:

- `ACTIVE`;
- `WAITING`;
- `INVALID`;
- `UNKNOWN`;
- `INSUFFICIENT_EVIDENCE`;
- `NOT_EVALUATED`.

Unknown is not converted to false.

Missing geometry is not interpreted as absence of a line, zone, or scenario.

## 9. Reference renderer

`tools/render_scenario_svg.py` is a dependency-light reference implementation.

It:

1. reads one JSON input;
2. validates renderer-critical structural constraints;
3. writes `scenario_panel.svg`;
4. writes `scenario_overlay.svg` when a source chart URI is present;
5. never evaluates NODA rules;
6. never calculates market prices;
7. never changes scenario ordering or meaning.

SVG is used because it is directly viewable, machine-generated, text-auditable, and supports raster chart backgrounds plus vector annotations.

A future PNG/JPEG rasterizer may consume SVG downstream without changing NS7-B strategy responsibility.

## 10. Fail-closed rules

The reference renderer refuses the request when:

- scenarios are not exactly A/B/C in that order;
- required scenario fields are absent;
- normalized coordinates fall outside `[0,1]`;
- an annotation refers to an unknown scenario;
- source chart URI is empty for overlay rendering.

For non-critical missing optional visual data, the panel remains renderable and the omission is surfaced in metadata/unresolved notes.

## 11. Prohibitions

NS7-B must not:

- invent price levels;
- infer line/zone geometry from screenshot pixels;
- infer a trend path not supplied by Scenario Composer;
- reinterpret `MAIN`, `ALTERNATIVE`, or `WAIT`;
- change A/B/C order;
- turn WAIT into BUY/SELL;
- turn UNKNOWN into FALSE;
- infer Entry / SL / TP;
- import TC/TradingCursor logic;
- resolve any NS2/NS3-NS6 TBD/HOLD;
- add a NODA strategy rule.

## 12. Static cases

`tests/NS7B_SCENARIO_RENDERER_CASES.md` covers:

1. Main continuation;
2. Alternative reversal;
3. Wait;
4. Setup present / Trigger waiting;
5. Trigger resolved;
6. UNKNOWN-heavy;
7. Field-scale transition candidate;
8. Continuation Formation;
9. Reversal Formation;
10. insufficient evidence;
11. missing geometry;
12. invalid scenario ordering.

## 13. Completion definition

NS7-B is complete at the renderer-contract/reference-implementation level when:

- panel SVG can be generated from valid A/B/C input;
- overlay SVG can be generated using a supplied chart image and supplied normalized geometry;
- no visual element requires new NODA semantics;
- uncertainty is preserved;
- Entry / SL / TP boundaries are preserved;
- audit passes.

This milestone does **not** claim automatic chart-image recognition or automatic scenario composition.
