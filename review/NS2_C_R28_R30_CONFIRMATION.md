# NS2-C1 R28 / R29 / R30-A Confirmation

Repository: `toootakeooot-bit/tradeplan-engine-noda`

Branch: `feature/noda-v1`

Start HEAD: `2678fb7ca8808ab4b79cd1382bbffd3350ef018b`

Scope: **R28, R29, R30-A, and R30-B Core boundary only**. R21-R27 remain review-required. R31+, NS3+, TC, and `trade-plan-a` are out of scope.

## 1. Confirmation summary

| Item | NODA Core | Primary | Secondary | RuleType | Owner | Status |
|---|---:|---|---|---|---|---|
| R28 Reversal Formation | YES | `2-3 Setup` | `2-4 Trigger` | `NODA_STRATEGY_CORE` | `Setup` | `CONFIRMED_RULE / REVERSAL_FORMATION_DETECTION_TBD` |
| R29 Continuation Formation | YES | `2-3 Setup` | `2-4 Trigger / 2-8 Wait` | `NODA_STRATEGY_CORE` | `Setup` | `CONFIRMED_RULE / CONTINUATION_FORMATION_DETECTION_TBD` |
| R30-A MA | YES | `2-1 Environment` | `2-2 Phase` | `NODA_STRATEGY_CORE_AUXILIARY` | `Environment / Phase` | `CONFIRMED_CORE / MAIN_PHASE_MA_ROLE_TBD` |
| R30-B RSI / Divergence / Elliott Wave etc. | NO | Core外 | Future validation only | `OUT_OF_NODA_CORE` | `NONE / Future Validation` | `OUT_OF_NODA_CORE / FUTURE_VALIDATION_CANDIDATE` |

## 2. R28 confirmed content

### Formal meaning

ダブルトップ／ボトム、トリプルトップ／ボトム、ヘッド＆ショルダーズ等、C04で反転Formationとして定義された形を、現在の構造が反転方向へ移行する可能性を示すSetup候補として認識する。

Formationの存在だけでは反転確定・Entry成立とはしない。

Formationに関係するNeckline、Support / Resistance等のBreakや、その後のSource-defined Actionは、Formation認識と分離してTrigger候補として確認する。

```text
Formation recognition
  -> Setup candidate
  -> Break / Action
  -> Trigger candidate
```

### Source basis

C04 explicitly defines reversal patterns as chart movement suggesting the possibility of trend reversal. It identifies Neckline thinking and support/resistance role change as important context. C03 places `小ダウの反転パターン` in the Formation step of its main-phase workflow.

### Image verification

- C03 p.4: workflow visually places Environment -> middle MA group -> Formation -> Entry and lists small-Dow reversal pattern under Formation.
- C03 p.7: small-Dow reversal examples are visually separated from large-Dow continuation examples.
- C04 p.5: reversal possibility and Neckline role-change relation are visually explicit.
- C04 p.32: reversal summary visually reiterates reversal possibility, support-to-resistance confirmation, and target context.

No image/text conflict was found.

### Open

`REVERSAL_FORMATION_DETECTION_TBD`

No pips threshold, candle-count threshold, symmetry score, confidence score, ML detector, or generic-TA Formation is introduced.

## 3. R29 confirmed content

### Formal meaning

Box / Rectangle、Triangle、Flag、Wedge等、C04で継続Formationとして定義された形を、現在のトレンドが継続する可能性を示すSetup候補として認識する。

Formation形成中だけでは継続方向を確定しない。

より広い構造のトレンド方向と整合し、Formationを継続方向へBreakするActionを確認した場合はTrigger候補とする。Formation内部に価格が残り、上下どちらにもBreakしていない間はWait候補とする。

```text
Continuation Formation
  -> Setup
     |- Break not confirmed -> Wait
     `- continuation-side Break -> Trigger candidate
```

### Source basis

C04 explicitly defines continuation patterns as chart movement suggesting the possibility of trend continuation and emphasizes consolidation shape. C04's Box/Rectangle example states that when direction is unresolved and reversal alternatives remain possible, waiting for one side to Break is better. C03 places `大ダウの継続パターン` in the Formation step of the main-phase workflow.

### Image verification

- C03 p.4: large-Dow continuation pattern appears under Formation in the workflow.
- C03 p.7: Rectangle, Triangle, Flag, Wedge are visually grouped as large-Dow continuation examples.
- C04 p.34: continuation possibility and broader-trend context are visually explicit.
- C04 p.36: Box/Rectangle boundaries and waiting for directional Break are visually explicit.
- C04 p.55: continuation summary visually reiterates continuation possibility and broader-trend context.

No fixed D1/H4/H1 mapping is inferred. Formal wording uses `より広い構造 / より細かな構造`.

### Open

`CONTINUATION_FORMATION_DETECTION_TBD`

No pips threshold, candle-count threshold, ATR condition, pattern score, or generic-TA supplement is introduced.

## 4. R30-A confirmed content

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

### Source basis

C03 places middle MA group after market-environment recognition and before Formation / Entry in its workflow. C03 p.6 states that MA conditions are added to main-phase judgment, shows 21/40/62EMA as middle MA group and 200SMA as long MA, and visually relates them to small-Dow / large-Dow directional context.

### R13 boundary

R13 remains the rule for `本格局面の確認`.

R30-A is the NODA-wide placement / priority rule for MA.

Existing `MAIN_PHASE_MA_ROLE_TBD` is retained. This work does not create:

- mandatory alignment of 21/40/62EMA;
- mandatory 200SMA gate;
- MA-cross gate;
- angle threshold;
- MA-distance threshold;
- MA score.

### Image verification

- C03 p.4: visually confirms the order Environment -> middle MA group -> Formation -> Entry.
- C03 p.6: visually confirms 21/40/62EMA, 200SMA and their main-phase / directional-context placement.

No mandatory MA rule is inferred from drawing alone.

## 5. R30-B Core boundary

RSI、Divergence、Elliott Wave、その他Case由来補助指標は、現時点ではNODA Coreへ組み込まない。

Classification:

- `RuleType = OUT_OF_NODA_CORE`
- `Owner = NONE / Future Validation`
- `Status = OUT_OF_NODA_CORE / FUTURE_VALIDATION_CANDIDATE`

They are not promoted to Strategy, Phase, Trigger, Entry, or score rules.

## 6. Relationship to existing confirmed rules

- R13: Formation is still not a mandatory main-phase gate; MA exact role remains TBD.
- R14-R16: existing Trigger semantics remain unchanged.
- R19: remains `Observation / Search Cue` only.
- R20: remains Line / BR structural context.
- R01-R20: no semantic rewrite is authorized by NS2-C1.

## 7. R21-R27 status

R21-R27 remain `UNREVIEWED / REVIEW_REQUIRED`.

No NS2-C1 confirmation or ownership inference is applied to them.

## 8. Governance / implementation boundary

- no new Observation ID;
- no detector implementation;
- no Entry / SL / TP implementation;
- no sizing / execution implementation;
- no NS3+ start;
- no TC change;
- no `trade-plan-a` change.

## 9. User-approved classification

The following is explicitly user-approved:

- `R28 Reversal Formation -> NODA Core -> 2-3 Setup -> 2-4 Trigger`
- `R29 Continuation Formation -> NODA Core -> 2-3 Setup -> 2-4 Trigger / 2-8 Wait`
- `R30-A MA -> NODA Core Auxiliary -> 2-1 Environment / 2-2 Phase`
- `R30-B -> OUT_OF_NODA_CORE / Future Validation`

This confirmation does not modify the external Drive `02_野田式判断ルール台帳.md`.
