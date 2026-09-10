# NS2-A R01-R10 Draft

Status: **R01-R05 CONFIRMED / R06 CONFIRMED_BASIC + VISUAL_SELECTION_TBD / R07-R09 CONFIRMED_RULE + selection TBD / R10 CONFIRMED**

Repository: `toootakeooot-bit/tradeplan-engine-noda`

Branch: `feature/noda-v1`

NS2-A DRAFT baseline HEAD: `4ecf8f584e26a08f226ccaf9f99b8fed085b2529`

This document records NS2-A1 confirmations for R01-R03, NS2-A2 confirmations for R04-R06, and NS2-A3 confirmations for R07-R10. The external baseline Rule Ledger `02_野田式判断ルール台帳.md` is not directly overwritten here. R11+ and NS2-B remain unprocessed.

## 1. Summary matrix

| Rule | Current category | Primary Stage | Secondary Stage | Observation dependency | Status |
|---|---|---|---|---|---|
| R01 | Environment | Environment | Observation relation | NO101, NO102 | CONFIRMED |
| R02 | Environment | Environment | Observation relation | NO101, NO102 | CONFIRMED |
| R03 | Environment | Environment | Observation relation | NO101, NO102; NO103=RELATIONSHIP_TBD | CONFIRMED_RULE / DETECTION_TBD |
| R04 | Environment | Environment | Phase / Setup relation | Turn/Dow scale governed later | CONFIRMED_RULE / DOW_SCALE_DETECTION_TBD |
| R05 | Line/Zone/Field | Environment | Observation relation | exact dependency TBD | CONFIRMED |
| R06 | Line/Zone/Field | Observation | Environment | NO201, NO202, NO203 | CONFIRMED_BASIC / VISUAL_SELECTION_TBD |
| R07 | Line/Zone/Field | Environment | Observation / Phase | NO201, NO202; Dow scale detector TBD | CONFIRMED_RULE / LINE_SELECTION_TBD |
| R08 | Line/Zone/Field | Setup | Environment / Observation | NO201, NO202, NO203 relation | CONFIRMED_RULE / LINE_SELECTION_TBD |
| R09 | Line/Zone/Field | Observation | Environment | NO202; TL Zone candidate | CONFIRMED_RULE / APPLICATION_SELECTION_TBD |
| R10 | Line/Zone/Field | Environment | Setup / Trigger | Field/Action representation TBD | CONFIRMED |

## 2. R01-R06 confirmed baseline preserved

### R01 | 高値・安値が土台
Confirmed definition: トレンド判断、ライン選択、トレードプランは、高値・安値の読み取りを土台にする。  
Status: `CONFIRMED`.

### R02 | トレンドの定義
- 上昇：高値と安値がともに切り上がる。  
- 下降：高値と安値がともに切り下がる。  
- それ以外：上昇でも下降でもない。  
`NOT_UP_OR_DOWN` は第三トレンドではない。  
Status: `CONFIRMED`.

### R03 | ターンの区切り
- 上昇側：N字形成後、その区間最安値を起点として遡及確定。  
- 下降側：N字形成後、その区間最高値を起点として遡及確定。  
Status: `CONFIRMED_RULE / DETECTION_TBD`.  
Open: `N_PATTERN_DETECTION_TBD`, Swing relation `RELATIONSHIP_TBD`.

### R04 | 大・中・小ダウ
大・中・小ダウは構造尺度と分析目的で使い分け、時間足へ固定しない。  
- 大：広範囲Fieldと際。  
- 中：大ダウ内の途中構造・Field。  
- 小：局面内の細かな構造とAction。  
Entryは定義から除外。BRも小ダウそのものの定義にしない。  
Status: `CONFIRMED_RULE / DOW_SCALE_DETECTION_TBD`.

### R05 | ラインを選ぶ目的
ラインは、買い手・売り手の意識と現在のFieldを視覚化する目的で選ぶ。  
Status: `CONFIRMED`.

### R06 | 基本ライン
- HL：反転高値・安値に水平。  
- 上昇TL：切り上げた2点の安値。  
- 下降TL：切り下げた2点の高値。  
- CH：TLと平行。上昇CHは直近高値側、下降CHは直近安値側。  
Status: `CONFIRMED_BASIC / VISUAL_SELECTION_TBD`.  
NO201/NO202/NO203は本工程ではFIXEDへ昇格しない。

## 3. NS2-A3 R07-R10 confirmation

### R07 | 大ダウのライン

**Baseline text**  
- 大ダウTL：選択時点で一度も抜かれていない線を基本とする。始点が絶対的な最安値・最高値でない場合もある。  
- 大ダウHL：一つの大きなターン中の最安値・最高値。  
- 用途：広範囲のフィールドと際。 `[C01]`

**Confirmed definition**  
大ダウラインは、広いトレンド構造の外側を捉え、広範囲のフィールドと際を認識するために使用する。

- 大ダウTL：選択時点で一度も抜かれていないラインを基本とする。始点は絶対的な最安値・最高値とは限らない。  
- 大ダウHL：一つの大きなターン中の最安値・最高値に置く。  
- 価格が大ダウの際へ接近した場合は、反応・反転の可能性を重要警戒する。

**User judgment**: `OK / LINE_SELECTION_TBD`  
**Stage**: Primary=`Environment`; Secondary=`Observation / Phase`  
**Dependencies**: NO201, NO202; Dow-scale detector remains TBD.  
**Open**: `LARGE_DOW_LINE_SELECTION_TBD`.  
**Constraint**: `必ず反転する` としない。最外側、最古/最新、最多接触、最緩角度、ATR、値幅、足数などを未出典の選択規則として導入しない。  
**Status**: `CONFIRMED_RULE / LINE_SELECTION_TBD`.

### R08 | 小ダウのライン

**Baseline text**  
一つの局面内、近い対称関係、値動きのクラスターに着目して引く。主用途は小ダウBRやEntryアクションで、全体フィールドの代用にはしない。 `[C01]`

**Confirmed definition**  
小ダウラインは、一つの局面内の細かな構造を捉えるために使用する。近い対称関係や値動きのクラスターに着目して選ぶ。小ダウBRを確認するために使用する場合が多い。大ダウ・中ダウが担う広いフィールド認識の代用にはしない。

**User judgment**: `OK / Entry削除 / Selection TBD`  
**User-approved difference**: Entry表現を正式定義から除外。BRは用途であり、小ダウラインそのものの定義ではない。  
**Stage**: Primary=`Setup`; Secondary=`Environment / Observation`. Existing NS2-A primary stage is preserved because the rule bridges recognized structure toward BR-oriented setup without defining Entry.  
**Dependencies**: NO201, NO202, NO203 relation possible; no Observation promotion here.  
**Open**: `SMALL_DOW_LINE_SELECTION_TBD`; 「近い」の距離、クラスター本数、反応回数、値幅、足数、時間幅等は未定義。  
**Status**: `CONFIRMED_RULE / LINE_SELECTION_TBD`.

### R09 | トレンドラインゾーン

**Baseline text**  
- 基本：始点ローソク足のヒゲから実体まで。  
- 応用1：CH側のゾーンから逆輸入。  
- 応用2：上昇TLは一段上、下降TLは一段下のローソク足実体まで。  
旧β運用文には基本形優先の制御があった。 `[S04]`

**Confirmed definition**  
トレンドラインは一本の線だけでなくゾーンとして扱う。

- 基本形：始点ローソク足のヒゲから実体までをゾーンとする。  
- 応用形1：チャネルライン側のゾーンから逆輸入する方法がある。  
- 応用形2：上昇TLでは一段上、下降TLでは一段下のローソク足実体まで広げる方法がある。

過去または途中で価格反応が確認できる場合、そのライン／ゾーンが市場で意識されている可能性を補強する材料とし、信頼度を高める要素として扱う。反応履歴は必須条件でも正解保証でもない。

**Source**: S04 `07 トレンドラインゾーンの取り方.txt` confirms the three zone methods and situational use of applications. User clarification governs `reaction history -> confidence reinforcement`.  
**User-approved difference**: β版の「基本形優先、応用は反応履歴と理由がある場合だけ」という独自制御文を正式R09から除外。  
**Stage**: Primary=`Observation`; Secondary=`Environment`.  
**Dependencies**: NO202; TL Zone may later need a governed Observation representation, but no new ID is added.  
**Open**: `TL_ZONE_APPLICATION_SELECTION_TBD`. No reaction-count, pips, wick/body-only, ATR, score or ML threshold is introduced.  
**Status**: `CONFIRMED_RULE / APPLICATION_SELECTION_TBD`.

### R10 | フィールドとアクションを分ける

**Baseline text**  
- フィールド：際から際までの「面」。大・中・小ダウの戦場。  
- アクション：フィールドの抜き差し、BR、意識の復活などの「変化」。 `[C02]`

**Confirmed definition**  
- Field：際から際までの戦場を「面」として捉える。大・中・小ダウの構造に応じ、ラインや際によって相場を複数のField / Areaとして捉える。  
- Action：そのFieldや際で発生する値動き、および買い手・売り手の力関係の変化を捉える。  
- Field内部：ラインや際の付近ではActionや反応を確認し、ライン間の内部値動きは必要に応じてより細かな構造で確認する。

**User judgment**: `OK / エリア分け・細部構造への引継ぎ追加`  
**Stage**: Primary=`Environment`; Secondary=`Setup / Trigger`.  
**Timeframe boundary**: `必ず下位足へ落とす` としない。R04の `Dow Scale != fixed timeframe` を維持する。  
**Responsibility boundary**: BR成立、Return成立、Entry、SL、TP、発注は後続Rule。  
**Open**: `FIELD_REPRESENTATION_TBD` — Fieldを独立Observationとして持つかEnvironment出力とするかは後続Governance。  
**Status**: `CONFIRMED`.

## 4. Source / governance notes

- R07/R08 primary source: C01 `短期集中コース 1回目.pdf`.  
- R09 primary source: S04 `07 トレンドラインゾーンの取り方.txt`.  
- R10 primary source: C02 `短期集中コース 2回目.pdf`.  
- User-confirmed clarifications are recorded as `USER APPROVED DIFFERENCE`; external baseline Rule Ledger is not overwritten here.  
- No new Observation ID is added. NO201/NO202/NO203 are not promoted to FIXED by NS2-A3.

## 5. Responsibility chain

`R04 Dow Scale` -> `R05 line purpose` -> `R06 HL/TL/CH basic geometry` -> `R07 large-Dow line / R08 small-Dow line / R09 TL Zone` -> `R10 Field=面 / Action=変化` -> later `Phase / BR / Return / Entry`.

R07-R10 do not introduce Entry, SL, TP or broker execution logic.

## 6. Stop condition

R01-R10 user-review results are recorded. R07/R08 line selection and R09 application selection remain TBD; R10 representation detail remains TBD. R11+ and NS2-B are not started.
