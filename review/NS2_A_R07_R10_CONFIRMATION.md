# NS2-A3 R07-R10 Confirmation

Repository: `toootakeooot-bit/tradeplan-engine-noda`

Branch: `feature/noda-v1`

Start HEAD: `5df66410340f277811a58a3e636164e41b4ea10e`

Scope: **R07-R10 user-review confirmation only**

R01-R06 remain as previously confirmed. R11+ and NS2-B are not started.

## 1. R07 confirmation

### Rule
`R07｜大ダウのライン`

### Confirmed definition
大ダウラインは、広いトレンド構造の外側を捉え、広範囲のフィールドと際を認識するために使用する。

- 大ダウTL：選択時点で一度も抜かれていないラインを基本とする。始点は絶対的な最安値・最高値とは限らない。
- 大ダウHL：一つの大きなターン中の最安値・最高値に置く。
- 価格が大ダウの際へ接近した場合は、反応・反転の可能性を重要警戒する。

### User judgment
`OK / LINE_SELECTION_TBD`

### Stage
Primary: `Environment`

Secondary: `Observation / Phase`

### Source
C01 `短期集中コース 1回目.pdf` supports large-Dow TL/HL, broad field and edge roles. User clarification adds the explicit non-guaranteed reaction/reversal watch wording.

### Selection open item
`LARGE_DOW_LINE_SELECTION_TBD`

The role of broad outer structure / edge is confirmed. A mechanical choice among multiple valid candidates is not fixed.

Not introduced:
- outermost always wins;
- oldest/newest line;
- most touches;
- shallowest angle;
- longest duration;
- ATR;
- price-range threshold;
- candle-count threshold;
- generic-TA line priority.

### User-approved difference
Reaction/reversal at the edge is a high-priority watch, not an absolute `必ず反転する` rule.

### Status
`CONFIRMED_RULE / LINE_SELECTION_TBD`

## 2. R08 confirmation

### Rule
`R08｜小ダウのライン`

### Confirmed definition
小ダウラインは、一つの局面内の細かな構造を捉えるために使用する。近い対称関係や値動きのクラスターに着目して選ぶ。小ダウBRを確認するために使用する場合が多い。大ダウ・中ダウが担う広いフィールド認識の代用にはしない。

### User judgment
`OK / Entry削除 / Selection TBD`

### Stage
Primary: `Setup`

Secondary: `Environment / Observation`

The existing NS2-A Primary Stage is retained. R08 uses recognized small-Dow structure to frame BR-oriented setup context but does not define Entry.

### Source
C01 `短期集中コース 1回目.pdf` supports one-phase scope, nearby symmetry, price clusters, and frequent small-Dow BR use.

### User-approved difference
`Entry` is removed from the formal R08 definition. Small-Dow line is not an Entry line. BR is a common use of the line, not the definition of the line itself.

### Selection open item
`SMALL_DOW_LINE_SELECTION_TBD`

Not defined:
- pips threshold for `near`;
- minimum cluster count;
- reaction-count threshold;
- price-range threshold;
- candle-count threshold;
- time-span threshold;
- automatic score;
- generic-TA criteria.

### Status
`CONFIRMED_RULE / LINE_SELECTION_TBD`

## 3. R09 confirmation

### Rule
`R09｜トレンドラインゾーン`

### Confirmed definition
トレンドラインは一本の線だけでなくゾーンとして扱う。

1. 基本形：始点ローソク足のヒゲから実体までをゾーンとする。
2. 応用形1：チャネルライン側のゾーンから逆輸入する方法がある。
3. 応用形2：上昇TLでは一段上、下降TLでは一段下のローソク足実体まで広げる方法がある。

過去または途中で価格反応が確認できる場合、そのライン／ゾーンが市場で意識されている可能性を補強する材料とし、信頼度を高める要素として扱う。

Reaction history is `confidence reinforcement`; it is neither mandatory nor proof of correctness.

### User judgment
`OK / β独自制御削除 / 反応履歴追加 / Selection TBD`

### Stage
Primary: `Observation`

Secondary: `Environment`

### Source
S04 `07 トレンドラインゾーンの取り方.txt` explicitly presents the basic form and two application forms, and discusses situational application and checking whether a zone is being respected. User clarification fixes reaction history as a confidence-reinforcement concept.

### User-approved differences
The prior β operational sentence requiring basic-form priority and limiting applications to cases with reaction-history/reason explanation is removed from the formal R09 definition. The three sourced methods remain.

### Application open item
`TL_ZONE_APPLICATION_SELECTION_TBD`

The existence of the three methods is confirmed, but the automatic choice among them is not fixed.

Not introduced:
- reaction-count threshold;
- pips distance for a reaction;
- wick-only/body-only rule;
- reaction-rate threshold;
- reversal-size threshold;
- ATR criterion;
- touch-count score;
- confidence numeric score;
- ML score;
- generic-TA zone scoring.

### Observation relation
R09 relates to `NO202 TL`. `TL Zone` may later require governed representation, but NS2-A3 creates no new Observation ID.

### Status
`CONFIRMED_RULE / APPLICATION_SELECTION_TBD`

## 4. R10 confirmation

### Rule
`R10｜フィールドとアクションを分ける`

### Confirmed definition
- **Field**: 際から際までの戦場を「面」として捉える。大・中・小ダウの構造に応じ、ラインや際によって相場を複数のField / Areaとして捉える。
- **Action**: そのFieldや際で発生する値動き、および買い手・売り手の力関係の変化を捉える。
- **Inside a Field**: ラインや際の付近ではActionや反応を確認し、ライン間の内部値動きは必要に応じてより細かな構造で確認する。

### User judgment
`OK / エリア分け・細部構造への引継ぎ追加`

### Stage
Primary: `Environment`

Secondary: `Setup / Trigger`

### Source
C02 `短期集中コース 2回目.pdf` supports Field as battlefield area and Action as movement / change in buyer-seller force. User clarification adds explicit Area partition and finer-structure handoff.

### Timeframe boundary
Do not define `always drop to a lower timeframe`. R04's rule remains: `Dow Scale != fixed timeframe`. The confirmed wording is `より細かな構造で確認する`.

### Responsibility boundary
R10 does not define:
- BR confirmation;
- Return confirmation;
- Entry;
- SL;
- TP;
- broker execution.

### Representation open item
`FIELD_REPRESENTATION_TBD`

Whether Field later becomes an independent governed Observation or remains Environment output is not determined here.

### Status
`CONFIRMED`

## 5. User-approved differences from external baseline Rule Ledger

The external `02_野田式判断ルール台帳.md` is not directly overwritten in NS2-A3.

| Rule | User-approved difference |
|---|---|
| R07 | reaction/reversal is an important watch, not a guaranteed reversal |
| R08 | remove Entry from formal definition; BR remains common use, not identity |
| R09 | remove β operational restriction; keep three sourced zone methods; reaction history becomes confidence reinforcement; application selection remains TBD |
| R10 | add Field/Area partitioning and handoff of internal movement to finer structural analysis |

These are recorded as `USER APPROVED DIFFERENCE` for later governed Rule Ledger synchronization.

## 6. Observation / NS1 impact

- R07 relates to NO201/NO202; line selection remains unresolved.
- R08 may relate to NO201/NO202/NO203; use-specific selection remains unresolved.
- R09 relates to NO202; no TL-Zone Observation ID is added.
- R10 Field/Action representation remains `FIELD_REPRESENTATION_TBD`.
- NO201/NO202/NO203 are not promoted to FIXED by NS2-A3.

## 7. Responsibility chain

`R04 Dow Scale` -> `R05 line purpose` -> `R06 HL/TL/CH basic geometry` -> `R07 large-Dow line / R08 small-Dow line / R09 TL Zone` -> `R10 Field=面 / Action=変化` -> later `Phase / BR / Return / Entry`.

## 8. Scope protection

NS2-A3 does not:
- alter R01-R06 rule semantics;
- process R11+;
- start NS2-B;
- add new Entry/SL/TP rules;
- add new Observation IDs;
- promote NO201/NO202/NO203 to FIXED;
- modify TC logic or repository;
- modify `trade-plan-a`.
