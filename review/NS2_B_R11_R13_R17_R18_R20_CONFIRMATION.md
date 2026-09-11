# NS2-B2 R11-R13 / R17 / R18 / R20 Confirmation

Repository: `toootakeooot-bit/tradeplan-engine-noda`

Branch: `feature/noda-v1`

Start HEAD: `1e46eabd19207ce583aa93fe334b77df58a60986`

Scope: **R11-R13, R17, R18, R20 only**. R14-R16 and R19 remain regression-protected from NS2-B1. R21+ and NS2-C are out of scope.

## 1. Confirmation summary

| Rule | User result | Primary Stage | Status |
|---|---|---|---|
| R11 | OK | Phase | `CONFIRMED_RULE / PHASE_DETECTION_TBD` |
| R12 | OK | Phase | `CONFIRMED_RULE / EDGE_PROXIMITY_TBD` |
| R13 | OK / Core confirmed | Phase | `CONFIRMED_CORE / MA_ROLE_TBD / DETECTION_TBD` |
| R17 | OK / user clarification reflected | Environment | `CONFIRMED_RULE / LINE_SELECTION_TBD` |
| R18 | OK / user clarification reflected | Environment | `CONFIRMED_RULE / HIGH_LOW_DETECTION_TBD / LINE_SELECTION_TBD` |
| R20 | OK / user clarification reflected | Environment | `CONFIRMED_RULE / BR_DETECTION_TBD` |

## 2. R11 confirmed content

### Formal meaning

トレンドは `先行期 / 本格局面 / 最終局面` の3局面として捉える。

- 先行期：トレンドが形成され始める初期局面。
- 本格局面：トレンドの力が強く進行する主要局面。
- 最終局面：トレンド自体は継続しているが値動きが軟化していく終盤局面。

野田式では大きい構造・小さい構造の両方にこの3局面を適用する。

### Source / clarification

S02 explicitly states three phases, applies the interpretation to trends of different scales, and notes that consolidation can still be judged as inside the main phase. Therefore `本格局面 = always steep` is not mechanized.

The sentence `局面名称だけでEntryしない` is kept only as an operational/downstream boundary, not part of the phase-definition semantics.

No D1/H4/H1/M15 scale mapping is fixed.

### Open

`PHASE_DETECTION_TBD`

Includes boundary detection, phase start/end, nested phase representation.

## 3. R12 confirmed content

### Formal meaning

先行期を捉えるときは、まず広い構造の際を探す。その際付近で現在の最終局面から次の先行期へ切り替わる小さな構造・Actionを確認する。

`広い構造の際 -> 現在の最終局面 -> 細かな構造 / Action -> 次の先行期候補`

S07 weekly/daily examples remain examples only. No fixed timeframe mapping is added.

The S07 explanation that edge trading facilitates stop placement is retained as rationale only. No SL calculation or SL-position rule is added to R12.

### Open

`EDGE_PROXIMITY_TBD`

Includes proximity distance, pips, zone relation, touch/approach boundary, candle/time constraints.

## 4. R13 confirmed content

### Structural core

大ダウの際へ到達後、本格局面入りを確認する際は、最後の押し安値または戻し高値のBreakを重要な構造確認として見る。

### MA

C03 explicitly puts 21/40/62 EMA conditions into main-phase judgment and shows 200SMA as long-term direction context. Their relevance is confirmed, but exact required/optional status is not fixed.

`MAIN_PHASE_MA_ROLE_TBD`

No all-MA alignment gate, 200SMA mandatory gate, MA-cross rule, generic-TA supplement, or MA score is created.

### Formation

C03 wording `形成してくると入りやすくなる` is retained as reinforcement / easier-to-read context. Formation is not a mandatory main-phase gate.

### Finer structure

H4/H1 examples remain examples. Formal wording is `必要に応じて、より細かな構造でActionを確認する`.

## 5. R17 confirmed content

R17 contains two **separate** line concepts.

### R17-A 中間TL

Source core from C01 p.21:
- drawn across turns;
- endpoint around the point before the large-Dow extreme is shown;
- start/end need not always be absolute extremes.

User-approved clarification:
- long/middle-term viewpoint;
- drawn from past structure;
- reference line for BR on small-Dow/finer structure;
- treated as more reliable than a purely local short-term line because it carries longer-lived structural awareness;
- usable from short to medium horizon;
- particularly useful for early-phase / premonitory-change observation.

`信頼性が高い` remains qualitative only. No score is introduced.

### R17-B 中ダウカウンターTL

Source core from C03 p.13:
- counter TL is opposite the large-Dow trend direction;
- middle-Dow counter TL spans turns.

User-approved clarification:
- within small-Dow structure, spans turns;
- opposite the larger trend;
- local / near-term usage;
- BR reference for small-Dow/finer structure;
- commonly useful in the main phase.

### Relationship

The concepts share a practical role as BR reference lines for small/finer structure, but are not synonyms, aliases, or a fixed parent/child relation.

`中間TL != 中ダウカウンターTL`

### Open

`LINE_SELECTION_TBD` and Break detector TBD.

## 6. R18 confirmed content

### Formal meaning

ラインBreak後はEntry判断より先に新しい高値・安値の形成を確認し、その高安を使ってTLを引き直し、TL/CHおよび現在のFieldを再把握する。

S05 directly supports:
- post-Break next high/low check;
- new endpoint candidate;
- rising/falling two-point geometry;
- TL/CH redraw;
- Field remapping.

The rule does not require two entirely new points; existing start + new endpoint is explicitly compatible with the source example.

### User-approved structural-priority clarification

Break後に形成された外側の新高安は無視できず、当該TL更新文脈では以前の対応高安より構造上の優先度が上がる。

`Break -> new outer high/low -> higher structural priority -> TL/CH update -> Field remap`

This priority statement is recorded as user-approved clarification, not silently attributed as direct S05 wording.

### R19 boundary

R19 Return Move is not a TL-update condition.

`R19 -> TL redraw` is prohibited.

### Open

`HIGH_LOW_DETECTION_TBD`

`LINE_SELECTION_TBD`

Exact redraw timing and CH reset selection remain TBD.

## 7. R20 confirmed content

R20 is a structural-context rule for TL/CH properties and Break meaning, not a standalone Entry Trigger.

### TL property

Source core from S06: TL is commonly used as a new-entry reference.

User-approved clarification:
- new-entry / participation reference;
- participation decision is concentrated around a relatively clear level;
- zone tends to be relatively narrow;
- therefore TL has relatively stronger line meaning than CH.

`strong` is qualitative only; no numeric score.

### TL BR

S06 describes active prior-trend participants starting to withdraw, prior-trend force weakening and opposite force appearing more easily; this is kept as trend-change Action **candidate/context**, not reversal confirmation.

`TL BR != reversal confirmed`

### CH property

Source core from S06: CH is commonly used as a profit-taking target.

User-approved clarification:
- profit-taking / withdrawal reference;
- withdrawal may happen before arrival, at arrival, at Break, after Break, or after Return;
- behavioral timing has greater freedom and is less concentrated at one exact level;
- therefore CH has relatively weaker line meaning than TL.

`weak` is qualitative only; no numeric score.

### CH BR

S06 describes existing same-direction participants being favored and new same-direction entries appearing more easily; this is kept as continuation/acceleration Action **candidate/context**, not continuation confirmation.

`CH BR != continuation confirmed`

### Responsibility

R20 does not independently establish Entry, buy/sell confirmation, Phase, reversal or continuation.

**Primary Stage**: `Environment`

**Secondary**: `Observation / Trigger`

### Open

`BR_DETECTION_TBD`

## 8. Required source / visual review

R11:
- S02 original text checked for three phases, multi-scale application and consolidation note.
- C01/C03 practical visuals checked only for phase/scale context.

R12:
- S07 original text checked for edge -> final phase -> small-Dow line/action sequence.
- C01 edge / small-Dow BR visuals checked for location/scale relationship.

R13:
- C03 p.5: edge + last push-low/return-high Break.
- C03 p.6: 21/40/62 EMA and 200SMA context.
- C03 p.7: formation context.
- C03 pp.9-10: finer-structure examples.

R17:
- C01 p.21 intermediate TL visual checked.
- C03 p.13 counter TL visual checked.

R18:
- S05 original text checked. The registered source has no embedded static still. No image-only endpoint rule is invented; detector/selection remains TBD.

R20:
- S06 original text checked for TL=new-entry reference, CH=profit-target reference, TL-BR change Action and CH-BR continuation/acceleration Action.

No source image/text was used to invent a pips threshold, candle-count rule, fixed timeframe mapping, hidden teacher intent, or Entry rule.

## 9. Source vs user-approved difference ledger

The following items are explicitly marked as user-approved clarification rather than direct source quotation:

- R17 usage horizon, phase tendency, and qualitative reliability distinction between intermediate TL and middle-Dow counter TL.
- R18 higher structural priority of the post-Break outer high/low.
- R20 qualitative TL-vs-CH strength / zone-concentration interpretation derived from participant-purpose differences.

These are not silently written back to the external `02_野田式判断ルール台帳.md`.

## 10. Regression protection

R14 remains `CONFIRMED_RULE / DETECTION_TBD`.

R15 remains `CONFIRMED_RULE / DETECTION_TBD`.

R16 remains `CONFIRMED_RULE / DETECTION_TBD`.

R19 remains `CONFIRMED_RULE / RETURN_DETECTION_TBD`, Primary Stage `Observation`, Search Cue only.

No NS2-B2 semantic change to R14-R16 or R19.

## 11. NS2-B completion

R11-R20 rule semantics have now completed user review and confirmation. Remaining gaps are detector / selection / representation issues only.

`NS2-B: COMPLETE at rule-semantics level`

Stop before R21 / NS2-C.
