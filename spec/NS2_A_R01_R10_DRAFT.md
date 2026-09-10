# NS2-A R01-R10 Draft

Status: **R01-R05 CONFIRMED / R06 CONFIRMED_BASIC + VISUAL_SELECTION_TBD / R07-R10 REVIEW_REQUIRED**

Repository: `toootakeooot-bit/tradeplan-engine-noda`

Branch: `feature/noda-v1`

NS2-A DRAFT baseline HEAD: `4ecf8f584e26a08f226ccaf9f99b8fed085b2529`

This document records NS2-A1 user-confirmed results for R01-R03 and NS2-A2 user-confirmed results for R04-R06. R07-R10 remain at the original NS2-A review state. The external baseline Rule Ledger `02_野田式判断ルール台帳.md` is not directly edited here.

## 1. Summary matrix

| Rule | Current category | Primary Stage | Secondary Stage | Observation dependency | Image review | Status |
|---|---|---|---|---|---|---|
| R01 | Environment | Environment (CONFIRMED) | Observation relationship retained | NO101, NO102; detector detail TBD | OPTIONAL for rule definition | CONFIRMED |
| R02 | Environment | Environment (CONFIRMED) | Observation relationship retained | NO101, NO102; detector detail TBD | OPTIONAL for rule definition | CONFIRMED |
| R03 | Environment | Environment (CONFIRMED) | Observation relationship retained | NO101, NO102; NO103=RELATIONSHIP_TBD | Detector verification later | CONFIRMED_RULE / DETECTION_TBD |
| R04 | Environment | Environment (CONFIRMED) | Phase / Setup relationship retained | Turn/Dow scale representation governed later | Detector verification later | CONFIRMED_RULE / DOW_SCALE_DETECTION_TBD |
| R05 | Line/Zone/Field | Environment (CONFIRMED) | Observation relationship retained | exact dependency TBD | OPTIONAL | CONFIRMED |
| R06 | Line/Zone/Field | Observation (CONFIRMED BASIC) | Environment | NO201, NO202, NO203 | Basic reviewed; candidate selection unresolved | CONFIRMED_BASIC / VISUAL_SELECTION_TBD |
| R07 | Line/Zone/Field | Environment | Observation / Phase | NO201, NO202; Dow-scale dependency TBD | REQUIRED | REVIEW_REQUIRED / IMAGE_REVIEW_PENDING |
| R08 | Line/Zone/Field | Setup | Environment / Observation | NO201, NO202, NO203; small-Dow dependency TBD | REQUIRED | REVIEW_REQUIRED / IMAGE_REVIEW_PENDING |
| R09 | Line/Zone/Field | Observation | Environment | NO202; OBSERVATION_CANDIDATE: TL Zone | REQUIRED | REVIEW_REQUIRED / IMAGE_REVIEW_PENDING |
| R10 | Line/Zone/Field | Environment | Setup / Trigger | field/action concepts; exact observation dependency TBD | RECOMMENDED | REVIEW_REQUIRED |

R01-R06 Primary Stage assignments are confirmed at the rule-semantics level. R06's multiple-candidate line selection remains unresolved. R07-R10 assignments remain `PROPOSED`, not final.

## 2. Source locator results

| Rule | Ledger source label | Verified source/location in NS2-A | Source/review result |
|---|---|---|---|
| R01 | S01, C01 | S01 `04 トレンドの判断方法.txt`: high/low foundation section. C01 `短期集中コース 1回目.pdf`: pp.13-15 area. | User-approved clarification removes the indicator sentence from the confirmed definition. |
| R02 | S01 | S01: `★★動画の重要ポイント★★` -> `1）トレンドの定義` and `2）トレンドの判断方法`. | User-approved clarification: only rising/falling trend definitions; non-match is not auto-classified as range/sideways/turn change. |
| R03 | C01, S01 | S01: `3）ターンの概念`. C01: pp.14-15 `2. ターンの区切り`, small-Dow and large-Dow turn context. | User-confirmed clarification adds retrospective N-pattern origin semantics. Existing sources are not claimed to contain that exact N-pattern wording. |
| R04 | C01, C02 | C01: pp.13-17, large/small Dow high/low, turn, large/small Dow line purposes. C02: pp.14-15, Field/Action and middle-Dow role. | User-approved clarification fixes structural scale + analysis purpose, removes Entry candidate from R04 definition, and explicitly avoids fixed timeframe mapping. |
| R05 | S03 | S03 `06 ラインの種類、引き方.txt`: preface immediately before `ラインの種類と性質`, line purpose is visualizing buyer/seller awareness and the active field. | User confirmed core purpose wording. |
| R06 | S03, S06 | S03: `１）ラインの種類`. S06 `10 ラインの引き方例.txt`: `前回までのおさらい -> 1）ラインの種類`, directly restating HL/TL/CH basics. A2 teacher-corrected images were also reviewed for visual selection context. | Basic geometry confirmed. The inspected images do not establish a unique multiple-candidate selection rule; keep `VISUAL_SELECTION_TBD`. |
| R07 | C01 | C01 p.16 `3. 大ダウのライン`: TL not broken at selection; HL at turn extreme; purpose is broad field / edge. | None found |
| R08 | C01 | C01 p.17 `4. 小ダウのライン`: within one trend phase; often for small-Dow BR; nearby symmetry/cluster focus. | None found |
| R09 | S04 | S04 `07 トレンドラインゾーンの取り方.txt`: `ゾーンの取り方`, basic = wick to body of starting candle; application variants also stated. | None found |
| R10 | C02 | C02 p.14 `1. ラインの活用法の違い`: Field = battlefield edge-to-edge; Action = change in buyer/seller balance / field insertion-removal. | None found |

## 3. Rule-by-rule state

### R01 | 高値・安値が土台

**Baseline text**  
トレンド判断、ライン選択、トレードプランは、安値・高値の読み取りを土台にする。インジケーターを先に見て方向を決めない。 `[S01, C01]`

**Confirmed definition**  
トレンド判断、ライン選択、トレードプランは、高値・安値の読み取りを土台にする。

**User judgment**: `OK`  
**Change reason**: `USER_REVIEW_APPROVED_CLARIFICATION`  
**Stage**: Primary=`Environment (CONFIRMED)`  
**Dependencies**: NO101, NO102. Exact significant-high/low recognition remains TBD.  
**NS1 OI**: NS1-OI-001/002 remain partial; importance and usage are supported, detector rules are not fixed.  
**Image**: not required for Rule Definition confirmation.

**User-approved difference**  
The indicator sentence is excluded from the confirmed R01 definition and is not retained as an auxiliary rule, note, OPEN ISSUE, Advanced condition, or separate rule candidate.

### R02 | トレンドの定義

**Baseline text**  
- 上昇トレンド：安値と高値が切り上がって推移  
- 下降トレンド：安値と高値が切り下がって推移  
- どちらも揃わない場合：方向未確定、レンジ、またはターン変化候補  
`[S01]`

**Confirmed definition**  
- 上昇トレンド：高値と安値がともに切り上がって推移する。  
- 下降トレンド：高値と安値がともに切り下がって推移する。  
- それ以外：上昇トレンドでも下降トレンドでもない。

The trend definitions are two kinds only. Runtime output may use `UPTREND`, `DOWNTREND`, or `NOT_UP_OR_DOWN`; the third is a negative state, not a third trend type.

**User judgment**: `OK / 修正反映済み`  
**Change reason**: `USER_REVIEW_APPROVED_CLARIFICATION`  
**Stage**: Primary=`Environment (CONFIRMED)`  
**Dependencies**: NO101, NO102; exact selection algorithm remains TBD.  
**NS1 OI**: NS1-OI-001/002 remain partial.  
**Image**: not required for Rule Definition confirmation.

**User-approved difference**  
Do not automatically classify a non-match as range, sideways, turn change, a separate uncertain-market structure, or any generic-TA category.

### R03 | ターンの区切り

**Baseline text**  
- 小ダウのターン：一つの上げまたは下げの中で、小ダウ推移が変化した起点  
- 大ダウのターン：小ダウのターンを複数跨ぎ、最低でも上げ・下げの1サイクルを含む変化の起点  
`[C01, S01]`

**Confirmed definition**  
- 上昇側：N字が1つ形成された後に、そのN字を形成する区間の最安値が確定し、その最安値をターンの起点として遡って確定する。  
- 下降側：N字が1つ形成された後に、そのN字を形成する区間の最高値が確定し、その最高値をターンの起点として遡って確定する。

The candidate extreme is not an immediately confirmed turn origin. After one N-pattern has formed, the origin is confirmed retrospectively as `confirmed turn origin`.

**User judgment**: `OK / 修正反映済み`  
**Change reason**: `USER_REVIEW_APPROVED_CLARIFICATION`  
**Stage**: Primary=`Environment (CONFIRMED)`  
**Dependencies**: NO101, NO102. NO103 Swing relationship=`RELATIONSHIP_TBD`.  
**Rule semantics**: USER CONFIRMED.  
**Detection implementation**: `N_PATTERN_DETECTION_TBD`.  
**Image**: Rule Definition confirmed; visual detector verification deferred.

**Explicitly not adopted**  
The left-turn last-return-high / last-push-low break condition and the 38% retracement condition are not registered anywhere in the NS2 rule system, notes, candidates, OPEN ISSUE, or tests.

### R04 | 大・中・小ダウを目的で分ける

**Baseline text**  
- 大ダウ：広範囲のフィールドと際を捉える  
- 中ダウ：大ダウのトレンド中で発生する途中のフィールドを捉える  
- 小ダウ：一つの局面内のアクション、BR、Entry候補を捉える  
小さな波を詳細に見たことを、大ダウ分析の代用にしない。 `[C01, C02]`

**Confirmed definition**  
大・中・小ダウは、値動きの構造尺度と分析目的によって使い分ける。

- 大ダウ：広範囲のフィールドと際を捉える。  
- 中ダウ：大ダウ内の途中の構造・フィールドを捉える。  
- 小ダウ：局面内の細かな構造とアクションを捉える。  
- 大・中・小ダウを特定の時間足へ固定しない。

**User judgment**: `OK / 修正反映済み`  
**Change reason**: `USER_REVIEW_APPROVED_CLARIFICATION`  
**Stage**: Primary=`Environment (CONFIRMED)`  
**Dependencies**: governed Turn/Dow-scale representation may be required later; no Observation ID added here.  
**Detection implementation**: `DOW_SCALE_DETECTION_TBD`.  
**Image**: rule semantics confirmed; machine scale-selection verification deferred.

**User-approved difference**  
R04 no longer defines small Dow through `Entry候補`. Entry remains a downstream responsibility. BR is also not made a defining condition of small Dow. The large/middle/small distinction is structural scale + analysis purpose, not a fixed timeframe map.

### R05 | ラインは「引けた」ではなく「目的で選ぶ」

**Baseline text**  
ラインの第一目的は、買い手と売り手の意識、現在の戦場のフィールドを視覚化すること。価格を当てるために無目的に増やさない。 `[S03]`

**Confirmed definition**  
ラインは、買い手・売り手の意識と現在のフィールドを視覚化する目的で選ぶ。

**User judgment**: `OK`  
**Change reason**: `USER_REVIEW_APPROVED_CLARIFICATION`  
**Stage**: Primary=`Environment (CONFIRMED)`  
**Dependencies**: exact governed line-observation dependency remains later work.  
**Image**: not required for rule-definition confirmation.  
**Open point**: implementation criteria for choosing among multiple line candidates are not defined by R05 itself.

### R06 | 基本ライン

**Baseline text**  
- HL：価格が反転している高値・安値に水平に引く  
- 上昇TL：切り上げた2点の安値で引く  
- 下降TL：切り下げた2点の高値で引く  
- CH：TLと平行にし、上昇CHは直近高値、下降CHは直近安値へ合わせる  
`[S03, S06]`

**Confirmed basic definition**  
- HL：価格が反転している高値・安値に水平に引く。  
- 上昇TL：切り上げた2点の安値で引く。  
- 下降TL：切り下げた2点の高値で引く。  
- CH：TLと平行にし、上昇CHは直近高値、下降CHは直近安値へ合わせる。

**User judgment**: `基本OK / 画像確認済み・選択規則TBD`  
**Stage**: Primary=`Observation (CONFIRMED BASIC)`; Secondary=`Environment`.  
**Dependencies**: NO201 HL, NO202 TL, NO203 CH.  
**NS1 OI**: NS1-OI-004/005/006 receive stronger source evidence for basic geometry, but the complete candidate-selection rule remains unresolved. No Observation status is promoted here.  
**Source locator update**: S06 exact supporting section is now captured as `前回までのおさらい -> 1）ラインの種類`, which restates HL/TL/CH basics.  
**Visual review**: teacher-corrected daily, H4, H1, wave-AB, and final images were reviewed as A2 visual evidence. The drawings support the existence of different structural scales, but do not by themselves establish a unique rule for selecting among multiple valid-looking line candidates.  
**Open point**: `VISUAL_SELECTION_TBD` — exact priority for selecting TL start/end points, HL reaction points, and CH counterpart points when multiple candidates exist.

**Responsibility routing**  
User-provided context about the outermost large-Dow TL, turn-spanning middle-Dow lines, and area/field partitioning is not inserted into R06. The large-Dow TL role is deferred to the R07 user review; area partitioning and Field/Action semantics are deferred to R10. R07-R10 are not modified or confirmed by NS2-A2.

### R07 | 大ダウのライン

**Baseline text**  
- 大ダウTL：選択時点で一度も抜かれていない線を基本とする。始点が絶対的な最安値・最高値でない場合もある  
- 大ダウHL：一つの大きなターン中の最安値・最高値  
- 用途：広範囲のフィールドと際  
`[C01]`

**Formal interpretation for review**  
C01 p.16 directly describes large-Dow TL/HL and states the purpose is to capture the broad field and its edge.

**Plain Japanese**  
大ダウのラインは、細かいEntry用ではなく大きな戦場と際を見るために選ぶ。TLは選択時点で抜かれていないこと、HLは大きなターンの極値が基準になる。

**Stage**: Primary=`Environment (PROPOSED)`; Secondary=`Observation / Phase (PROPOSED)`  
**Dependencies**: NO201, NO202; Dow-scale dependency TBD.  
**Image**: REQUIRED / IMAGE_REVIEW_PENDING.  
**Open point**: visual confirmation is needed for allowed non-extreme TL starting points.

### R08 | 小ダウのライン

**Baseline text**  
一つの局面内、近い対称関係、値動きのクラスターに着目して引く。主用途は小ダウBRやEntryアクションであり、全体フィールドの代用にしない。 `[C01]`

**Formal interpretation for review**  
C01 p.17 states small-Dow lines are selected inside one trend phase, often for small-Dow BR, and focus on nearby symmetry / price clusters.

**Plain Japanese**  
小ダウのラインは大きな相場全体を見る線ではなく、局面の中でBRやEntryにつながる近い値動きを見るための線。

**Stage**: Primary=`Setup (PROPOSED)`; Secondary=`Environment / Observation (PROPOSED)`  
**Dependencies**: NO201, NO202, NO203; small-Dow scale dependency TBD.  
**Image**: REQUIRED / IMAGE_REVIEW_PENDING.  
**Open point**: exact boundary between a small-Dow line and a larger-scale line is visual/source dependent.

### R09 | トレンドラインゾーン

**Baseline text**  
- 基本：始点ローソク足のヒゲから実体までをゾーンとする  
- 応用1：CH側のゾーンから逆輸入  
- 応用2：上昇TLは一段上、下降TLは一段下のローソク足実体まで広げる候補  
β版の通常判断は基本形を優先し、応用は反応履歴と理由を説明できる場合だけ使う。 `[S04]`

**Formal interpretation for review**  
S04 explicitly gives three TL-zone methods: basic wick-to-body at the starting candle, channel-side reverse import, and one-candle-level body extension. S04 recommends practicing the basic form first; the baseline's β operational restriction should be reviewed as operational wording rather than silently treated as teacher-universal semantics.

**Plain Japanese**  
TLは一本の細い線だけでなくゾーンとして見る。基本は始点ローソク足のヒゲから実体までで、応用形もある。

**Stage**: Primary=`Observation (PROPOSED)`; Secondary=`Environment (PROPOSED)`  
**Dependencies**: NO202 TL; `TL Zone` = OBSERVATION_CANDIDATE.  
**Image**: REQUIRED / IMAGE_REVIEW_PENDING.  
**Open point**: exact governance status of the baseline β restriction versus sourced teaching recommendation.

### R10 | フィールドとアクションを分ける

**Baseline text**  
- フィールド：際から際までの「面」。大・中・小ダウの戦場  
- アクション：フィールドの抜き差し、BR、意識の復活などの「変化」  
アクション単独で上位フィールドを無視しない。 `[C02]`

**Formal interpretation for review**  
C02 p.14 directly separates Field, used to grasp the battlefield edge-to-edge, from Action, used to grasp changes in buying/selling force and field interaction.

**Plain Japanese**  
フィールドは「どこからどこまでが戦場か」、アクションは「その戦場で何が変わったか」。この2つを混ぜない。

**Stage**: Primary=`Environment (PROPOSED)`; Secondary=`Setup / Trigger (PROPOSED)`  
**Dependencies**: exact governed Observation dependency TBD; Field/Action remain later strategy concepts under NS0/NS1 boundary.  
**Image**: RECOMMENDED.  
**Open point**: whether Field requires a separate governed observation representation or remains Environment output is not decided here.

## 4. NS1 open-issue linkage

| NS1 issue | NS2-A2 state | Status |
|---|---|---|
| NS1-OI-001 Significant High | R01-R03 confirm structural need; no universal detector fixed | PARTIAL |
| NS1-OI-002 Significant Low | R01-R03 confirm structural need; no universal detector fixed | PARTIAL |
| NS1-OI-003 Swing | R03 Turn semantics confirmed; Swing=Turn not established | UNRESOLVED / RELATIONSHIP_TBD |
| NS1-OI-004 HL | R06 basic HL geometry source-confirmed/user-approved; candidate point selection remains unresolved | PARTIAL / stronger evidence |
| NS1-OI-005 TL | R06 basic TL geometry source-confirmed/user-approved; multiple-candidate selection remains unresolved | PARTIAL / stronger evidence |
| NS1-OI-006 CH | R06 basic CH relation source-confirmed/user-approved; counterpart selection in ambiguous cases remains unresolved | PARTIAL / stronger evidence |

No NS1 Observation is promoted to FIXED in NS2-A2.

## 5. Observation / detector candidates

No new Observation ID is added in NS2-A2. `DOW_SCALE_DETECTION_TBD` and `VISUAL_SELECTION_TBD` are implementation/open-review states, not new trading rules.

## 6. User-approved differences

R01-R03 differences are recorded in `review/NS2_A_R01_R03_CONFIRMATION.md`. R04-R06 differences and review dispositions are recorded in `review/NS2_A_R04_R06_CONFIRMATION.md`. The external Rule Ledger is not directly overwritten.

## 7. Stop condition

R01-R05 are confirmed at the Rule-semantics level. R06 basic definition is confirmed while multiple-candidate visual selection remains `VISUAL_SELECTION_TBD`. R07-R10 remain unconfirmed and unchanged in review status. NS2-B must not begin until further user instruction.