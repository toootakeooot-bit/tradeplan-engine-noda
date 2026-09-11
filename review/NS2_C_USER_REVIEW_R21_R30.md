# NS2-C User Review R21-R30

Repository: `toootakeooot-bit/tradeplan-engine-noda`

Branch: `feature/noda-v1`

Start HEAD: `2678fb7ca8808ab4b79cd1382bbffd3350ef018b`

Status: **PARTIAL CONFIRMATION — R28 / R29 / R30-A CONFIRMED; R21-R27 REVIEW_REQUIRED; R30-B OUT_OF_NODA_CORE**

## 1. User-reviewed items

| Rule | User judgment | NODA Core | Primary Stage | Secondary Stage | Status |
|---|---|---:|---|---|---|
| R28 Reversal Formation | OK | YES | `2-3 Setup` | `2-4 Trigger` | `CONFIRMED_RULE / REVERSAL_FORMATION_DETECTION_TBD` |
| R29 Continuation Formation | OK | YES | `2-3 Setup` | `2-4 Trigger / 2-8 Wait` | `CONFIRMED_RULE / CONTINUATION_FORMATION_DETECTION_TBD` |
| R30-A MA | OK | YES | `2-1 Environment` | `2-2 Phase` | `CONFIRMED_CORE / MAIN_PHASE_MA_ROLE_TBD` |
| R30-B RSI / Divergence / Elliott Wave etc. | Core exclusion approved | NO | `OUT_OF_NODA_CORE` | Future validation only | `OUT_OF_NODA_CORE / FUTURE_VALIDATION_CANDIDATE` |

## 2. R28 review result

### Current baseline

現行Rule Ledger R28は、Double Top / Bottom、Triple Top / Bottom、Head & Shoulders等について、Necklineと支持・抵抗の役割変化を確認して反転候補とし、形が似ているだけでは確定しないとしている。

### Accepted formal definition

反転Formationは、現在の構造が反転方向へ移行する可能性を示す `Setup候補` として認識する。

Formationの存在だけでは反転確定・Entry成立とはしない。Formationに関係するNeckline、Support / Resistance等のBreakや、その後のSource-defined Actionは、別途 `Trigger候補` として確認する。

### 簡単に言うと

`形を見つける = Setup`、`Break / Actionを見る = Trigger候補`。

### Source

- Primary: C04 `01_（補足資料４）フォーメーション.pdf`
- Supplemental: C03 `短期集中コース 3回目.pdf`

### Image review

`REQUIRED_COMPLETED`

C03 p.4/p.7 and C04 p.5/p.32 were visually checked. No image/text conflict found.

### Open

`REVERSAL_FORMATION_DETECTION_TBD`

## 3. R29 review result

### Current baseline

現行Rule Ledger R29は、Box、Triangle、Flag、Wedgeについて、より広いトレンド方向と保ち合いBreakを組み合わせて継続候補とし、上下どちらへも抜けていない間は待機するとしている。

### Accepted formal definition

継続Formationは、現在のトレンドが継続する可能性を示す `Setup候補` として認識する。

Formation内部に価格が残り、方向Breakが未成立なら `Wait候補`。より広い構造のトレンド方向と整合し、Formationを継続方向へBreakするActionを確認した場合は `Trigger候補` とする。

### 簡単に言うと

`Formation中 = Setup`、`まだ抜けない = Wait`、`継続方向へ抜ける = Trigger候補`。

### Source

- Primary: C04 `01_（補足資料４）フォーメーション.pdf`
- Supplemental: C03 `短期集中コース 3回目.pdf`

### Image review

`REQUIRED_COMPLETED`

C03 p.4/p.7 and C04 p.34/p.36/p.55 were visually checked. C04 p.36 explicitly supports waiting when directional resolution is not yet known. No fixed timeframe mapping is created.

### Open

`CONTINUATION_FORMATION_DETECTION_TBD`

## 4. R30-A review result

### Current baseline

現行Rule Ledger R30はMAとRSI / Divergence / Elliott Wave等を同じRule内で扱っている。

### Accepted formal definition

MAは、高値・安値、Dow Structure、Field、際、TL / HL / CH等の価格構造を読み取った後に使用する補助情報とする。

特に、本格局面および現在の優勢方向を確認するための補助情報として使用する。

`Price Structure -> Environment -> Phase -> MA auxiliary confirmation`

MA単独でDirection / Trigger / Entryを確定しない。

### R13 boundary

R13は本格局面確認そのものを扱う。R30-AはNODA全体におけるMAの配置・優先順位を扱う。

既存 `MAIN_PHASE_MA_ROLE_TBD` を維持し、21/40/62EMA全一致必須、200SMA必須、MA Cross、角度、乖離率、Score等を新規作成しない。

### Source

Primary: C03 `短期集中コース 3回目.pdf`

### Image review

`REQUIRED_COMPLETED`

C03 p.4/p.6 were visually checked. p.4 places middle MA group between Environment and Formation; p.6 shows 21/40/62EMA, 200SMA and main-phase judgment context. No mandatory MA gate is inferred from the image alone.

## 5. R30-B review result

RSI、Divergence、Elliott Wave、その他Case由来補助指標は現時点のNODA Coreに含めない。

They remain:

`OUT_OF_NODA_CORE / FUTURE_VALIDATION_CANDIDATE`

They are not promoted to Strategy, Phase, Trigger, Entry, or scoring rules.

## 6. R21-R27 remain open

| Rule | Review state |
|---|---|
| R21 | `REVIEW_REQUIRED` |
| R22 | `REVIEW_REQUIRED` |
| R23 | `REVIEW_REQUIRED` |
| R24 | `REVIEW_REQUIRED` |
| R25 | `REVIEW_REQUIRED` |
| R26 | `REVIEW_REQUIRED` |
| R27 | `REVIEW_REQUIRED` |

No user confirmation is inferred for these rules from the R28-R30 review.

## 7. Regression protection

R01-R20 semantics remain unchanged.

R13 retains Formation as non-mandatory reinforcement context and MA role as partly unresolved.

R14-R16 remain Trigger rules; R19 remains Observation / Search Cue; R20 remains Line / BR structural context.

## 8. User-approved management classification

- R28: `RuleType=NODA_STRATEGY_CORE`, `Owner=Setup`
- R29: `RuleType=NODA_STRATEGY_CORE`, `Owner=Setup`
- R30-A: `RuleType=NODA_STRATEGY_CORE_AUXILIARY`, `Owner=Environment / Phase`
- R30-B: `RuleType=OUT_OF_NODA_CORE`, `Owner=NONE / Future Validation`

Existing R01-R20 are not retrofitted with RuleType / Owner in this work.
