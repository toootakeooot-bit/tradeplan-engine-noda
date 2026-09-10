# NS2-A2 R04-R06 Confirmation

Repository: `toootakeooot-bit/tradeplan-engine-noda`

Branch: `feature/noda-v1`

Start HEAD: `a44aec2919bda754c1d0e4f8ef81c573ad375a27`

Scope: **R04-R06 user-review confirmation and R06 visual-review result only**

R01-R03 remain as already confirmed by NS2-A1. R07-R10 remain `REVIEW_REQUIRED`. NS2-B is not started.

## 1. R04 confirmation

### Rule
`R04｜大・中・小ダウを目的で分ける`

### Confirmed definition
大・中・小ダウは、値動きの構造尺度と分析目的によって使い分ける。

- 大ダウ：広範囲のフィールドと際を捉える。
- 中ダウ：大ダウ内の途中の構造・フィールドを捉える。
- 小ダウ：局面内の細かな構造とアクションを捉える。
- 大・中・小ダウを特定の時間足へ固定しない。

### User judgment
`OK / 修正反映済み`

### Change reason
`USER_REVIEW_APPROVED_CLARIFICATION`

### Stage
Primary Stage: `Environment` — CONFIRMED

### Source relation
- C01 supports the large/small Dow structural roles, turns, lines, field/edge context.
- C02 supports the middle-Dow viewpoint as an intermediate structure/field inside the large-Dow move.
- The user-approved clarification fixes the governing concept as `structural scale + analysis purpose`, not a fixed timeframe mapping.

### User-approved differences from prior draft / baseline wording
- Remove `小ダウ = Entry候補` from the R04 definition. Entry remains downstream.
- Do not redefine small Dow as `BR`. BR may use small-Dow structure later but is not the small-Dow definition.
- Do not map D1/H4/H1 or any other timeframe directly to large/middle/small Dow.

### Detection open item
`DOW_SCALE_DETECTION_TBD`

R04 rule semantics are confirmed. The following are not defined in NS2-A2:
- OHLC thresholds for large/middle/small Dow;
- candle-count thresholds;
- price-range thresholds;
- time-span thresholds;
- ATR or other generic-TA criteria;
- fixed timeframe mappings.

No new Dow-scale Observation ID is created here.

### Status
`CONFIRMED_RULE / DOW_SCALE_DETECTION_TBD`

## 2. R05 confirmation

### Rule
`R05｜ラインは「引けた」ではなく「目的で選ぶ」`

### Confirmed definition
ラインは、買い手・売り手の意識と現在のフィールドを視覚化する目的で選ぶ。

### User judgment
`OK`

### Stage
Primary Stage: `Environment` — CONFIRMED

### Source relation
S03 supports the role of lines as a means to visualize buyer/seller awareness and the active battlefield/field, and the principle of intentional line selection.

### Responsibility boundary
R05 fixes **why** lines are selected. It does not define:
- which two points must be chosen;
- start/end-point priority;
- large-Dow TL selection details;
- middle-Dow line details;
- small-Dow line details;
- any automatic candidate-ranking algorithm.

### Status
`CONFIRMED`

## 3. R06 confirmation

### Rule
`R06｜基本ライン`

### Confirmed basic definition
- HL：価格が反転している高値・安値に水平に引く。
- 上昇TL：切り上げた2点の安値で引く。
- 下降TL：切り下げた2点の高値で引く。
- CH：TLと平行に引く。上昇CHは直近高値側、下降CHは直近安値側へ合わせる。

### User judgment
`基本OK / 画像確認済み・選択規則TBD`

### Stage
Primary Stage: `Observation` — CONFIRMED BASIC

Secondary relation: `Environment`

### Source relation
- S03 directly defines the basic HL/TL/CH geometry.
- S06 `10 ラインの引き方例.txt`, `前回までのおさらい -> 1）ラインの種類`, restates the same HL/TL/CH basics.
- Teacher-corrected daily/H4/H1/wave-AB/final images were reviewed as A2 visual evidence.

### A2 visual-review result
The reviewed images support:
- the existence of multiple structural scales;
- the fact that different lines may be used on the same chart for different structural purposes;
- visual compatibility with the confirmed basic HL/TL/CH geometry.

The images do **not** by themselves establish a unique rule for selecting one pair of points from multiple valid-looking candidates. A2 evidence is treated as evidence of what was drawn, not as authority for unstated teacher intent.

### Visual selection open item
`VISUAL_SELECTION_TBD`

Unresolved items include:
- TL start/end-point priority when multiple candidates exist;
- which reaction high/low should be used for HL when multiple candidates exist;
- which counterpart point should be used for CH when multiple candidates exist.

The following are explicitly **not** introduced as candidate-selection rules:
- oldest two points;
- newest two points;
- outermost two points;
- maximum contact count;
- shallowest angle;
- candle-count thresholds;
- price-range thresholds;
- ATR or generic-TA criteria;
- machine-learning ranking.

### Status
`CONFIRMED_BASIC / VISUAL_SELECTION_TBD`

## 4. Responsibility routing from user review context

The following user-review context is preserved only for later review routing. It does not modify or confirm R07-R10 in NS2-A2.

### R07 handoff context — large-Dow TL
Candidate review context for R07:
- the outermost line that captures the broad trend structure is treated as an important large-Dow TL candidate;
- it is used to read the broad trend direction and the `際`;
- when price approaches it, reaction/reversal is treated as something to watch for;
- do not express this as an absolute `必ず反転する` rule.

`角度が緩やか` is not a defining condition.

R07 remains `REVIEW_REQUIRED` until its own user review.

### R10 handoff context — area/field partitioning
Candidate review context for R10:
- turn-spanning internal lines may partition the market into structural areas;
- line vicinity can be treated as a boundary where later phase/action review may become relevant;
- movement between such lines may be delegated to lower-timeframe/detail analysis where appropriate;
- this context is not inserted into R06 and does not yet change the formal R10 definition.

R10 remains `REVIEW_REQUIRED` until its own user review.

### R04 relation to middle-Dow context
The structural-scale aspect of the middle-Dow concept is already captured in R04. The detailed role of specific middle-Dow lines is not added to R06.

## 5. Observation relation

R06 relates to:
- `NO201 HL`
- `NO202 TL`
- `NO203 CH`

The source basis for their basic geometry is stronger after NS2-A2, but NS2-A2 does not promote NO201/NO202/NO203 to `FIXED`.

Reasons for keeping Observation governance separate include:
- multiple-candidate selection remains unresolved;
- Dow-scale relation remains unresolved at detector level;
- purpose-specific line selection is handled by later rule review.

No new Observation ID is created in NS2-A2.

## 6. NS1 open-issue impact

- NS1-OI-004 HL: stronger evidence for basic geometry; complete candidate selection still unresolved.
- NS1-OI-005 TL: stronger evidence for basic geometry; complete start/end-point selection still unresolved.
- NS1-OI-006 CH: stronger evidence for parallel/counterpart basic geometry; complete counterpart selection still unresolved.

These issues are not closed or promoted to FIXED by NS2-A2.

R01-R03 related NS1 open issues remain unchanged.

## 7. Scope protection

NS2-A2 does not:
- confirm or rewrite R07-R10;
- process R11+;
- start NS2-B;
- modify TC logic;
- modify `trade-plan-a`;
- add Entry/SL/TP logic;
- add generic-TA candidate-selection logic;
- create a new Observation ID;
- promote NS1 Observations to FIXED without governance.

The external baseline Rule Ledger is not directly overwritten by this confirmation record.