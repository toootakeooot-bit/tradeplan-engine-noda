# NS2-A1 R01-R03 Confirmation

Repository: `toootakeooot-bit/tradeplan-engine-noda`

Branch: `feature/noda-v1`

NS2-A DRAFT baseline HEAD: `4ecf8f584e26a08f226ccaf9f99b8fed085b2529`

Scope: **R01-R03 user-review confirmation only**

## 1. R01 confirmation

### Rule
`R01｜高値・安値が土台`

### Confirmed definition
トレンド判断、ライン選択、トレードプランは、高値・安値の読み取りを土台にする。

### User judgment
`OK`

### Stage
Primary Stage: `Environment` — CONFIRMED

### Source relation
- S01 `04 トレンドの判断方法.txt`: high/low reading is the foundation for trend judgment and line selection.
- C01 `短期集中コース 1回目.pdf`: high/low progression is part of the initial visual-analysis flow.

### User-approved difference from baseline Rule Ledger
**Before**: high/low foundation sentence plus `インジケーターを先に見て方向を決めない`.

**After**: high/low foundation sentence only.

**Reason**: `USER_REVIEW_APPROVED_CLARIFICATION`

**User approved**: YES

**Source impact**: the confirmed definition remains supported by S01/C01. The removed sentence is not retained as a rule, note, OPEN ISSUE, Advanced condition, or separate candidate.

**Semantic impact**: narrows R01 to the user-approved core definition without adding new strategy logic.

## 2. R02 confirmation

### Rule
`R02｜トレンドの定義`

### Confirmed definition
- 上昇トレンド：高値と安値がともに切り上がって推移する。
- 下降トレンド：高値と安値がともに切り下がって推移する。
- それ以外：上昇トレンドでも下降トレンドでもない。

Trend definitions are two kinds only. For runtime representation, `UPTREND`, `DOWNTREND`, and `NOT_UP_OR_DOWN` may be used. `NOT_UP_OR_DOWN` is a negative result state, not a third trend type.

### User judgment
`OK / 修正反映済み`

### Stage
Primary Stage: `Environment` — CONFIRMED

### Source relation
S01 directly supports the rising/falling definitions based on both highs and lows.

### User-approved difference from baseline Rule Ledger
**Before**: non-matching cases were described as `方向未確定、レンジ、またはターン変化候補`.

**After**: non-matching cases are only `上昇トレンドでも下降トレンドでもない`.

**Reason**: `USER_REVIEW_APPROVED_CLARIFICATION`

**User approved**: YES

**Source impact**: no claim is made that a non-match is range, sideways, turn change, or another generic TA category.

**Semantic impact**: removes unsupported automatic sub-classification and preserves only the positive up/down definitions plus a negative result state.

## 3. R03 confirmation

### Rule
`R03｜ターンの区切り`

### Confirmed definition
#### 上昇側
N字が1つ形成された後に、そのN字を形成する区間の最安値が確定し、その最安値をターンの起点として遡って確定する。

#### 下降側
N字が1つ形成された後に、そのN字を形成する区間の最高値が確定し、その最高値をターンの起点として遡って確定する。

ターン起点は候補極値が出現した瞬間に確定するのではなく、N字形成後に遡及して確定する。概念上、`candidate` と `confirmed turn origin` を区別する。

### User judgment
`OK / 修正反映済み`

### Stage
Primary Stage: `Environment` — CONFIRMED

### Source relation
- S01 supports the general Turn concept as a change in the rhythm of highs/lows.
- C01 supports the small-/large-Dow Turn context and turn-boundary usage.
- The exact N-pattern retrospective-origin wording is recorded as a `USER_REVIEW_APPROVED_CLARIFICATION`; this record does not falsely attribute that exact wording to C01/S01.

### Status
`CONFIRMED_RULE / DETECTION_TBD`

Rule semantics are user-confirmed. The OHLC detector that determines when one N-pattern is complete is not defined here.

### Implementation open item
`N_PATTERN_DETECTION_TBD`

No candle-count rule, threshold, price-distance rule, timeframe rule, or generic-TA detector is invented.

### Swing relation
`NO103 Swing` is not merged with Turn.

Relationship: `RELATIONSHIP_TBD`

### User-approved difference from baseline Rule Ledger
**Before**: small-/large-Dow turn definitions based on change points and cycles.

**After**: the confirmed turn-origin semantics specify retrospective confirmation after one N-pattern, using the lowest point for the upward side and the highest point for the downward side.

**Reason**: `USER_REVIEW_APPROVED_CLARIFICATION`

**User approved**: YES

**Source impact**: source-supported Turn context is retained; exact N-pattern wording is explicitly labeled as user-confirmed clarification rather than quoted teacher text.

**Semantic impact**: clarifies how the turn origin is confirmed; detector implementation remains unresolved.

## 4. Explicitly rejected conditions

The following are completely excluded from the NS2 rule system for R03 and are not preserved as Advanced, Optional, OPEN ISSUE, candidate, note, or test condition:

1. break of the left turn's last return high / last push low;
2. retracement of 38% or more against the left turn.

They must not be reintroduced without a new explicit user instruction and the applicable source-governance process.

## 5. Observation relation

- R01: related to NO101 / NO102; exact significant-high/low detector remains unresolved.
- R02: uses high/low progression; exact NO101 / NO102 selection algorithm remains unresolved.
- R03: uses high/low structure and an N-pattern concept; no new Observation ID is added in NS2-A1.
- NO103 Swing remains separate and unresolved relative to Turn.

No NS1 Observation status is changed by this confirmation record.

## 6. Scope protection

R04-R10 are not reviewed or confirmed by NS2-A1. Their NS2-A DRAFT content and user judgments remain unchanged.

No TC Engine, Adapter, `trade-plan-a`, Entry/SL/TP logic, sizing, execution, or strategy implementation is modified here.