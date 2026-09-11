# NS5 Setup Rules

Status: **NS5 specification — Setup responsibility fixed, Formation/selection detector TBDs preserved**

Upstream contracts:
- `schema/environment_state.schema.json`
- `schema/phase_state.schema.json`

Controlling baseline:
- `spec/NS2_FINAL_RULE_MATRIX.csv`
- `review/NS2_C_R28_R30_CONFIRMATION.md` for R28/R29 semantics
- `spec/RESPONSIBILITY.md`
- `docs/SOURCE_POLICY.md`
- NS3/NS4 specifications and audits

## 1. Responsibility

NS5 owns `2-3 Setup` only.

Setup answers:

> Given Environment and Phase context, is there a source-defined NODA setup candidate that should be watched for a later Trigger?

Setup is **not Entry** and is **not Trigger**.

A recognized Formation or line context does not authorize order placement, SL, TP, RR, sizing, or Wait/Invalidation strategy logic.

## 2. Rule mapping

### Setup-primary rules

| Rule | Setup responsibility | Open item |
|---|---|---|
| R08 | small-Dow line context used for small-structure BR / setup preparation | `LINE_SELECTION_TBD`; no Entry semantics |
| R28 | Reversal Formation recognition as reversal Setup candidate | `REVERSAL_FORMATION_DETECTION_TBD` |
| R29 | Continuation Formation recognition as continuation Setup candidate | `CONTINUATION_FORMATION_DETECTION_TBD` |

### Context rules

| Rule | Setup use |
|---|---|
| R12 | Early-phase / edge context can constrain where a setup is relevant; R12 does not become a Setup detector |
| R17 | intermediate TL / middle-Dow counter TL can be relevant line context; line concepts remain separate |
| R10 | Field/Action separation prevents an Action candidate from replacing broader Field context |

### Explicit exclusions

- R14-R16 are Trigger rules and are not used to declare Setup present.
- R19 remains Observation/Search Cue only.
- R20 may supply structural line/Break context but cannot alone create Setup or Entry.
- R21-R27 remain HOLD.
- R31-R37 remain Operational Control / HOLD.

## 3. Setup evaluation model

NS5 separates:

1. `setup_status` — whether a governed setup is present/absent/unknown;
2. `setup_type` — source-defined setup family when known;
3. `components` — line/Field/Phase context relevant to the setup;
4. `formation` — Formation family/pattern when a governed Formation recognition exists;
5. `wait_for_trigger` — local readiness state meaning a Setup exists but Trigger has not been evaluated/confirmed;
6. `unresolved[]` — detector/selection gaps.

`wait_for_trigger` is **not** the NS7/R21 strategy Wait decision. It is only a Setup-stage readiness flag and does not revive HOLD rules.

## 4. R08 small-Dow line context

R08 is Setup-primary because small-Dow lines are used to prepare/observe fine-structure BR opportunities.

NS5 may carry relevant R08 line references, but:
- exact line selection remains TBD;
- a small-Dow line by itself does not mean Setup is present unless the applicable source-defined setup context is satisfied;
- no Entry meaning is reintroduced into R08.

## 5. R28 Reversal Formation

Source-confirmed semantics:
- Reversal Formation indicates a possibility of structural reversal and is a Setup candidate;
- Formation recognition is separated from later Break/Action;
- Neckline/support-resistance Break/Action belongs to Trigger candidate handling, not Setup recognition;
- Formation presence alone does not confirm reversal or Entry.

Source-confirmed examples/catalog may include:
- `DOUBLE_TOP`;
- `DOUBLE_BOTTOM`;
- `TRIPLE_TOP`;
- `TRIPLE_BOTTOM`;
- `HEAD_AND_SHOULDERS`.

The list is a source-backed catalog, not a generic-TA extension license. New patterns require governed source addition.

Exact visual detector remains `REVERSAL_FORMATION_DETECTION_TBD`.

## 6. R29 Continuation Formation

Source-confirmed semantics:
- Continuation Formation indicates a possibility of current-trend continuation and is a Setup candidate;
- Formation forming inside its boundaries does not confirm continuation;
- continuation-side Break/Action is downstream Trigger candidate context;
- unresolved Formation direction does not authorize Entry.

Source-confirmed examples/catalog:
- `RECTANGLE` / Box;
- `TRIANGLE`;
- `FLAG`;
- `WEDGE`.

Exact visual detector remains `CONTINUATION_FORMATION_DETECTION_TBD`.

## 7. Formation type/pattern separation

To preserve extensibility without changing setup-family semantics:

- `formation_type` = `REVERSAL / CONTINUATION / NONE / UNKNOWN`;
- `formation_pattern` = a source-confirmed pattern identifier or `UNKNOWN`.

This separation does not itself add any Formation rule.

## 8. Setup status semantics

Allowed local setup states:
- `PRESENT` — a governed setup recognition is supplied/resolved;
- `ABSENT` — setup evaluation was possible and the source-defined setup is absent;
- `UNKNOWN` — available governed information cannot resolve setup;
- `NOT_EVALUATED` — prerequisites were not supplied or setup evaluation was intentionally not run.

If Formation detection is TBD and no pre-resolved Formation recognition is supplied, Formation-based setup is `UNKNOWN`, not `ABSENT`.

## 9. No future-stage dependency

NS5 must not consume `TriggerState`.

Formation boundary Break, Return, awareness revival, or other trigger action is not required to recognize Setup. If such downstream data is supplied, it cannot be used to retroactively manufacture Setup.

The allowed direction is:

`Environment -> Phase -> Setup -> Trigger`

not the reverse.

## 10. SetupState contract

Machine-readable contract: `schema/setup_state.schema.json`.

SetupState can carry:
- Phase/Environment references;
- setup status/type;
- direction candidate;
- Formation type/pattern;
- relevant line and Field references;
- setup components/evidence;
- `wait_for_trigger` local readiness flag;
- unresolved items.

## 11. Explicit TBD preservation

NS5 preserves at least:
- `LINE_SELECTION_TBD` where R08/R17 selection is needed;
- `REVERSAL_FORMATION_DETECTION_TBD`;
- `CONTINUATION_FORMATION_DETECTION_TBD`;
- any unresolved support/resistance/neckline selection required by a later Trigger.

No candle count, symmetry score, ATR threshold, pips tolerance, ML score, or generic Formation detector is introduced.

## 12. Completion condition

NS5 is complete at specification level when:
- Setup can be represented from Environment/Phase without Trigger;
- Formation recognition remains Setup, not Entry;
- R28/R29 family/pattern separation is preserved;
- absent vs unknown is distinguishable;
- `wait_for_trigger` does not revive formal Wait rules;
- detector/selection TBDs remain explicit;
- static cases and audit pass.
