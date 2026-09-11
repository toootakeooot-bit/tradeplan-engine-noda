# NS2-C R21-R30 Draft / Partial Confirmation

Repository: `toootakeooot-bit/tradeplan-engine-noda`

Branch: `feature/noda-v1`

Start HEAD: `2678fb7ca8808ab4b79cd1382bbffd3350ef018b`

Status: **PARTIAL CONFIRMATION — R28 / R29 / R30-A CONFIRMED; R21-R27 REVIEW_REQUIRED; R30-B OUT_OF_NODA_CORE**

This document opens NS2-C without advancing into NS3. It preserves R01-R20 semantics and does not implement detector, strategy, sizing, Entry, SL, TP, adapter, or execution code.

## 1. Scope

NS2-C covers R21-R30 as a review block. This work only confirms:

- R28 Reversal Formation;
- R29 Continuation Formation;
- R30-A MA placement;
- R30-B Core exclusion.

R21-R27 remain `UNREVIEWED / REVIEW_REQUIRED` and are not automatically classified or confirmed by this work.

## 2. R21-R27 review queue

The following baseline rules remain queued for separate user review. Their external Rule Ledger text is not silently rewritten here.

| Rule | Baseline topic | NS2-C1 disposition |
|---|---|---|
| R21 | 待機は分析結果 | `REVIEW_REQUIRED` |
| R22 | Entry・SL・TPを同時決定 | `REVIEW_REQUIRED` |
| R23 | SLの狭い型 | `REVIEW_REQUIRED` |
| R24 | SLの広い型 | `REVIEW_REQUIRED` |
| R25 | 許容損失と取引量 | `REVIEW_REQUIRED` |
| R26 | TP | `REVIEW_REQUIRED` |
| R27 | RR | `REVIEW_REQUIRED` |

No R21-R27 Stage, RuleType, Owner, strategy meaning, or external/downstream ownership is confirmed in NS2-C1.

## 3. R28 — Reversal Formation

### Confirmed classification

- NODA Core: `YES`
- Primary Stage: `2-3 Setup`
- Secondary Stage: `2-4 Trigger`
- RuleType: `NODA_STRATEGY_CORE`
- Owner: `Setup`
- Status: `CONFIRMED_RULE / REVERSAL_FORMATION_DETECTION_TBD`

### Formal meaning

ダブルトップ／ボトム、トリプルトップ／ボトム、ヘッド＆ショルダーズ等、C04で反転Formationとして定義された形を、現在の構造が反転方向へ移行する可能性を示す `Setup候補` として認識する。

Formationの形状が見えるだけでは、反転確定またはEntry成立とはしない。

Formationに関係するNeckline、Support / Resistance等のBreakや、その後のSource-defined Actionは、Setup認識とは分離して `Trigger候補` として確認する。

```text
Formation recognition
  -> Setup candidate
  -> Break / Action
  -> Trigger candidate
```

### Source

- Primary: C04 `01_（補足資料４）フォーメーション.pdf`
- Supplemental: C03 `短期集中コース 3回目.pdf`

C03 explicitly places `小ダウの反転パターン` in the formation stage of the main-phase workflow. C04 defines reversal patterns as chart movement suggesting the possibility of trend reversal and gives Neckline / support-resistance role-change context.

### Open

`REVERSAL_FORMATION_DETECTION_TBD`

No fixed pips Break, candle count, symmetry score, confidence score, ML pattern detector, or generic-TA supplement is created.

## 4. R29 — Continuation Formation

### Confirmed classification

- NODA Core: `YES`
- Primary Stage: `2-3 Setup`
- Secondary Stage: `2-4 Trigger / 2-8 Wait`
- RuleType: `NODA_STRATEGY_CORE`
- Owner: `Setup`
- Status: `CONFIRMED_RULE / CONTINUATION_FORMATION_DETECTION_TBD`

### Formal meaning

Box / Rectangle、Triangle、Flag、Wedge等、C04で継続Formationとして定義された形を、現在のトレンドが継続する可能性を示す `Setup候補` として認識する。

Formation形成中だけでは継続方向を確定しない。

より広い構造のトレンド方向と整合し、Formationを継続方向へBreakするActionを確認した場合は `Trigger候補` とする。Formation内部に価格が残り、上下どちらにもBreakしていない間は `Wait候補` とする。

```text
Continuation Formation
  -> Setup
     |- Break not confirmed -> Wait
     `- continuation-side Break -> Trigger candidate
```

### Timeframe / scale boundary

C04の長期足文脈およびC03の大ダウ継続パターンは、固定時間足mappingには変換しない。

Formal representation uses:

- `より広い構造`
- `より細かな構造`

Existing R04 rule `Dow Scale != Fixed Timeframe` remains controlling.

### Source

- Primary: C04 `01_（補足資料４）フォーメーション.pdf`
- Supplemental: C03 `短期集中コース 3回目.pdf`

C03 explicitly places `大ダウの継続パターン` in the formation stage of the main-phase workflow. C04 defines continuation patterns as chart movement suggesting the possibility of trend continuation, highlights consolidation shape, and shows waiting for directional Break where continuation/reversal alternatives remain unresolved.

### Open

`CONTINUATION_FORMATION_DETECTION_TBD`

No fixed pips Break, candle count, ATR condition, pattern score, or generic-TA supplement is created.

## 5. R30 — split by responsibility without changing Rule ID

Rule ID `R30` remains unchanged. For NS2 responsibility purposes it is represented as two sub-rules:

- `R30-A` MA;
- `R30-B` RSI / Divergence / Elliott Wave / case-derived auxiliary indicators.

This is a management split, not an R-number renumbering.

## 6. R30-A — MA

### Confirmed classification

- NODA Core: `YES`
- Primary Stage: `2-1 Environment`
- Secondary Stage: `2-2 Phase`
- RuleType: `NODA_STRATEGY_CORE_AUXILIARY`
- Owner: `Environment / Phase`
- Status: `CONFIRMED_CORE / MAIN_PHASE_MA_ROLE_TBD`

### Formal meaning

MAは、高値・安値、Dow Structure、Field、際、TL / HL / CH等の価格構造を読み取った後に使用する補助情報とする。

特に、本格局面および現在の優勢方向を確認するための補助情報として使用する。

```text
Price Structure
  -> Environment
  -> Phase
  -> MA auxiliary confirmation
```

MA単独でDirection / Trigger / Entryを確定せず、NODA価格構造を上書きしない。

### Relationship to R13

- R13 owns `本格局面の確認`.
- R30-A owns `NODA全体でMAをどの位置に置くか`.

C03 explicitly shows 21 / 40 / 62 EMA as middle MA group and 200 SMA as long-term MA context. The exact mandatory/optional role remains unresolved under existing `MAIN_PHASE_MA_ROLE_TBD`.

No all-MA alignment mandatory gate, 200SMA mandatory gate, MA cross gate, angle threshold, distance threshold, or MA score is added.

## 7. R30-B — non-Core boundary

### Classification

- NODA Core: `NO`
- RuleType: `OUT_OF_NODA_CORE`
- Owner: `NONE / Future Validation`
- Status: `OUT_OF_NODA_CORE / FUTURE_VALIDATION_CANDIDATE`

RSI、Divergence、Elliott WaveおよびCase由来補助指標は、現時点ではNODA Core Strategy Ruleへ昇格させない。

They are not used as:

- Strategy Rule;
- Trigger;
- Entry condition;
- Phase condition;
- score bonus.

## 8. Responsibility connections

### R28

```text
Environment
  -> Phase
  -> Reversal Formation
  -> 2-3 Setup
  -> Break / Action
  -> 2-4 Trigger
```

### R29

```text
Environment
  -> Phase
  -> Continuation Formation
  -> 2-3 Setup
     |- no Break -> 2-8 Wait
     `- continuation Break -> 2-4 Trigger
```

### R30-A

```text
2-1 Environment
  -> Price Structure recognition
  -> 2-2 Phase
  -> MA auxiliary confirmation
```

No direct MA -> Trigger / Entry path is created.

## 9. Relationship to existing confirmed rules

- R13 remains `CONFIRMED_CORE / MA_ROLE_TBD / DETECTION_TBD`; Formation is not a mandatory main-phase gate.
- R14-R16 remain unchanged Trigger rules.
- R19 remains `Observation / Search Cue` only.
- R20 remains structural Line / BR context and is not replaced by Formation.
- R01-R20 semantics are regression protected.

## 10. Required visual/source verification completed

### C03

- p.4 visually confirms the workflow `相場環境認識 -> 中期MA群 -> フォーメーション -> エントリー`, with `小ダウの反転パターン` and `大ダウの継続パターン` placed in Formation.
- p.6 visually confirms 21/40/62EMA middle-MA group, 200SMA long-MA context, and main-phase judgment context.
- p.7 visually confirms large-Dow continuation Formation examples and small-Dow reversal Formation examples around the main-phase context.

### C04

- p.5 visually confirms Reversal Pattern as reversal-possibility context and Neckline support/resistance role-change context.
- p.32 visually summarizes reversal possibility, support-to-resistance confirmation, and target-value context.
- p.34 visually confirms Continuation Pattern as continuation-possibility context and consolidation / wider-trend context.
- p.36 visually confirms Box/Rectangle boundary Break and explicitly shows `どちらかに抜けるのを待つ` when continuation/reversal alternatives remain unresolved.
- p.55 visually summarizes continuation possibility and broader-trend context.

No image-only threshold, candle count, hidden teacher intent, or detector rule is invented.

## 11. NS2-C1 stop conditions

After this confirmation:

- R21-R27 remain `REVIEW_REQUIRED`;
- R31+ remain unprocessed;
- no new Observation ID is created;
- NS3+ is not started;
- no TC or `trade-plan-a` change is authorized.
