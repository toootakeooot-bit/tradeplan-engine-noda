# NS2-B R11-R20 Draft

Status: **PARTIAL CONFIRMATION — R14-R16 / R19 CONFIRMED AT RULE-SEMANTICS LEVEL; R11-R13 / R17-R18 / R20 REVIEW_REQUIRED**

Repository: `toootakeooot-bit/tradeplan-engine-noda`

Branch: `feature/noda-v1`

NS2-B start HEAD: `b92dac35b625f81f86c71bdab2265f15c49b1ef7`

NS2-B1 start HEAD: `00532261164dca16232c2357a2801ae6b97cd501`

Scope: **R11-R20 only**. R01-R10 remain as confirmed in NS2-A1/A2/A3. R21+ are out of scope. This file does not modify the external Rule Ledger.

## 1. Review control

NS2-B follows `spec/NS2_REVIEW_PROTOCOL.md`:

`AI draft -> Japanese user review -> OK/修正/保留 -> required source/image verification -> final整理 -> audit -> CONFIRMED or unresolved`

NS2-B1 confirms only R14, R15, R16 and R19 at the requested rule-semantics level. R11-R13, R17-R18 and R20 remain `REVIEW_REQUIRED`.

## 2. Summary matrix

| Rule | Name | Primary Stage | Secondary Stage | Main dependency / relation | Image review | AI confidence | Status |
|---|---|---|---|---|---|---|---|
| R11 | 3つの局面 | Phase | Environment | R02/R04/R07/R10; Phase representation TBD | REQUIRED | HIGH semantics / MEDIUM detector | REVIEW_REQUIRED |
| R12 | 先行期を狙う前提 | Phase | Setup | R07 edge, R08 small-Dow line, R10 Field/Action | REQUIRED | HIGH semantics | REVIEW_REQUIRED |
| R13 | 本格局面の確認 | Phase | Setup | NO101/NO102; large-Dow edge; MA/formation auxiliary handling | REQUIRED | MEDIUM | REVIEW_REQUIRED |
| R14 | 小ダウBR | Trigger | Phase / Setup | R07/R08; NO201/NO202; `SMALL_DOW_BR_DETECTION_TBD` | REQUIRED | HIGH semantics / MEDIUM detector | CONFIRMED_RULE / DETECTION_TBD |
| R15 | 意識の復活（小） | Trigger | Phase | small-Dow structure; Turn; `SMALL_AWARENESS_REVIVAL_DETECTION_TBD` | REQUIRED | HIGH semantics / MEDIUM detector | CONFIRMED_RULE / DETECTION_TBD |
| R16 | 意識の復活（大） | Trigger | Phase / Environment | large-Dow line; `SMALL_DOW_CYCLE_DETECTION_TBD` | REQUIRED | HIGH semantics / MEDIUM detector | CONFIRMED_RULE / DETECTION_TBD |
| R17 | 中間TL・カウンターTL | Environment | Observation / Setup | NO202; Dow scale; Turn | REQUIRED | HIGH semantics / MEDIUM selection | REVIEW_REQUIRED |
| R18 | ラインブレイク後は地図を更新 | Environment | Observation | NO101/NO102/NO202/NO203; Field remap | REQUIRED | HIGH | REVIEW_REQUIRED |
| R19 | リターンムーブ | Observation | Downstream search context only | NO202; `RETURN_MOVE_DETECTION_TBD`; R14/R15 downstream search relation only | RECOMMENDED | HIGH semantics / MEDIUM detector | CONFIRMED_RULE / RETURN_DETECTION_TBD |
| R20 | TL BRとCH BRの意味 | Trigger | Environment | NO202/NO203; trend-change/continuation interpretation | RECOMMENDED | HIGH | REVIEW_REQUIRED |

## 3. Source locator baseline

External baseline: `02_野田式判断ルール台帳.md` β0.3-A限定運用版.

| Rule | Ledger source | Verified locator used for NS2-B draft |
|---|---|---|
| R11 | S02, C01, C03 | S02 `05 トレンドの3つの局面.txt`: `★★動画の重要ポイント★★` and annotation on applying phases to large/small trends. C01/C03 provide practical phase context. |
| R12 | S07, C01 | S07 `16 《練習》先行期を狙ったエントリー.txt`: points 1-3 (`際`, final phase, small-Dow TL). C01 overall flow / large-Dow edge / small-Dow BR. |
| R13 | C03 | C03 `短期集中コース 3回目.pdf`: pp.4-11 area, especially p.5 last push-low/return-high break, p.6 MA group, p.7 formation, pp.9-10 finer-timeframe action examples. |
| R14 | C01, S07 | C01 p.18 `小ダウのBR`; S07 point 3, final-phase small-Dow TL and break-return context. |
| R15 | C01 | C01 p.19 `意識の復活（小）`. |
| R16 | C01 | C01 p.20 `意識の復活（大）`. |
| R17 | C01, C03 | C01 p.21 `中間トレンドライン`; C03 p.13 `カウンターTL`. |
| R18 | S05 | S05 `08 ラインをブレイクした時の対処法.txt`: post-break next high/low, redraw, and Field remapping sections. |
| R19 | S03, S06 | S06 `10 ラインの引き方例.txt`: `ラインのブレイク後は【リターンムーブ】が発生しやすい` section. S03 provides support/resistance and line-break context. User review restricts R19 to observation/cue responsibility. |
| R20 | S06 | S06 `10 ラインの引き方例.txt`: `トレンド転換` vs `トレンド続伸（加速）` section. |

## 4. Rule-by-rule draft

### R11 | 3つの局面

**Current baseline text**
- 先行期：先行参加者が仕込み、一般参加者はまだ悲観的な時期
- 本格局面：角度と勢いが強い主要トレンドの進行期
- 最終局面：一般参加者が遅れて入り、トレンドは続くが値動きが軟化する時期
- 野田式では大小のトレンドにもこの考え方を適用する。局面はチャート上の条件で仮分類し、名称だけでEntryしない。

**Source-grounded draft interpretation**
S02 directly defines three phases and explicitly states NODA applies the concept not only to the main trend but also to trends viewed at larger/smaller scale. S02 also notes that consolidation can still be judged as inside a main phase, so `本格局面 = always steep movement at every moment` must not be over-literalized.

**Plain Japanese**
トレンドを先行期・本格局面・最終局面の3段階で見る。大小のトレンドでも同じ考え方を使う。

**Primary Stage proposal**: `Phase`

**Secondary**: `Environment`

**Observation/Rule relation**: R02 trend, R04 Dow scale, R07 edge, R10 Field/Action. No new Observation ID is added.

**Image review**: `REQUIRED` — actual phase boundaries and nested scale use are visual.

**Open issues**
- exact chart conditions for phase boundary detection;
- whether the baseline sentence `名称だけでEntryしない` is retained as a rule or treated as a review/operational guard;
- how to represent nested phases across structural scales without fixed timeframe mapping.

**User judgment**: `未確認`

### R12 | 先行期を狙う前提

**Current baseline text**
先行期は「際で勝負する」発想である。上位足の大ダウライン・ゾーンなどの際を見つけ、その付近で最終局面から次の先行期へ移る小ダウアクションを待つ。際から離れたEntryはSLが遠くなり、損切りが増えやすい。

**Source-grounded draft interpretation**
S07 directly says targeting the early phase is equivalent to `際で勝負する`, that an edge makes stop placement easier, and that one searches for the final phase near a larger-scale edge before looking for a small-Dow line/action. S07 uses weekly/daily as an example, but NS2-B must not convert this example into a fixed timeframe mapping.

**Plain Japanese**
まず大きい構造の際を探し、その付近で最終局面から次の先行期へ切り替わる細かな動きを待つ。

**Primary Stage proposal**: `Phase`

**Secondary**: `Setup`

**Relation**: R07 large-Dow edge, R08 small-Dow line, R10 Field/Action, R14 BR.

**Image review**: `REQUIRED`.

**Open issues**
- exact visual boundary of `際付近`;
- whether `際から離れるとSLが遠い/損切りが増えやすい` belongs in R12 semantics or later risk/entry explanation;
- no fixed higher/lower timeframe mapping may be introduced.

**User judgment**: `未確認`

### R13 | 本格局面の確認

**Current baseline text**
大ダウの際へ到達後、反対側の最後の押し安値または戻し高値のブレイクを確認する。中期MA群（21・40・62EMA）の方向、長期MA（200SMA）、フォーメーションを補助にし、必要なら4時間足・1時間足へ下げて波形を確認する。

**Source-grounded draft interpretation**
C03 directly states that after reaching a large-Dow edge, the last push-low / return-high break is checked. It also adds the 21/40/62 EMA group to judging whether the main phase is entering, shows 200 SMA as long-term direction context, and says formations can make entry easier. C03 gives H4/H1 as practical examples when daily action is too straight to read. These examples must not automatically become fixed timeframe requirements.

**Plain Japanese**
大ダウの際から本格局面へ入ったかを、最後の押し安値/戻し高値のブレイクを中心に確認し、MAやフォーメーションは補助情報として見る、という整理候補。

**Primary Stage proposal**: `Phase`

**Secondary**: `Setup`

**Image review**: `REQUIRED`.

**Open issues / review-critical**
- whether last push-low / return-high break is necessary, sufficient, or one major confirmation condition;
- exact role of 21/40/62 EMA and 200 SMA: `required condition` vs `auxiliary confidence/context`;
- exact role of formations: C03 wording is `形成してくると入りやすくなる`, which does not by itself prove a mandatory gate;
- H4/H1 must remain examples unless user/source explicitly fixes them.

**User judgment**: `未確認`

### R14 | 小ダウBR

**Confirmed formal definition**
大ダウの際へ到達した後、最終局面内の小ダウラインを用いてBreakとReturnを確認し、次の先行期へ切り替わるActionを捉える。

対象ライン:
- `TL`: 最終局面内で現在のトレンド方向に引いた小ダウTL。
- `HL`: 最終局面内の最後の押し安値・戻し高値に置いた小ダウHL。

構造順序は、`大ダウの際 -> 最終局面 -> 小ダウTL/HL -> Break -> Return -> 次の先行期候補`。

**Responsibility boundary**
R14はTrigger構造を扱う。Entry価格、注文、SL、TP、Lot、Position Size、発注は扱わない。

**Primary Stage**: `Trigger`

**Secondary**: `Phase / Setup`

**Source**: C01 p.18 / S07.

**Detector status**: `SMALL_DOW_BR_DETECTION_TBD`.

**Detector must not invent**: pips threshold, candle-close requirement, wick rule, Return tolerance, candle count, elapsed-time condition.

**Status**: `CONFIRMED_RULE / DETECTION_TBD`

**User judgment**: `OK`

### R15 | 意識の復活（小）

**Confirmed formal definition**
本格局面または最終局面内で、反対トレンド方向へ引いた小ダウラインが一度Breakされた後、再びそのライン側へ戻るActionを、直前の小ダウターンの意識が復活する候補として捉える。

R15の本質は単なるReturn現象ではなく、`直前の小ダウターンの意識が再び働く構造的Action`。

**R19 separation**
R15とR19は別Rule。R15は`小ダウ構造 + 局面 + ライン方向 + 意識復活という構造的意味`を持つ。R19はTL Break後に価格が旧TL側へ戻る観測現象。`R15 = R19` とせず、`R15 is a subtype of R19` とも固定しない。

**Primary Stage**: `Trigger`

**Secondary**: `Phase`

**Source**: C01 p.19.

**Detector status**: `SMALL_AWARENESS_REVIVAL_DETECTION_TBD`.

**Detector must not invent**: recross requirement, touch-only rule, zone-entry rule, pips tolerance, candle count, reaction-count threshold.

**Status**: `CONFIRMED_RULE / DETECTION_TBD`

**User judgment**: `OK`

### R16 | 意識の復活（大）

**Confirmed formal definition**
一度Breakされた大ダウラインに対し、再びメイントレンド方向へ戻るActionを「意識の復活（大）」の候補として捉える。小ダウの上げ・下げが一巡した後に、次の小ダウサイクルの起点となる動きを見る。

R16の本質は`大ダウ側のメイントレンド意識の復活`。

`大ダウラインへタッチした = 意識の復活（大）` とはしない。`大ダウラインへ戻った = 即Entry` ともしない。

**Primary Stage**: `Trigger`

**Secondary**: `Phase / Environment`

**Source**: C01 p.20.

**Detector status**: `SMALL_DOW_CYCLE_DETECTION_TBD` plus line-return detection TBD.

**Status**: `CONFIRMED_RULE / DETECTION_TBD`

**User judgment**: `OK`

### R17 | 中間TL・カウンターTL

**Current baseline text**
- 中間TL：ターンを跨いだ高値・安値で引き、終点は最安値・最高値の一つ前を選ぶことがある
- カウンターTL：大ダウの主トレンドと逆方向の小・中ダウTL
- 大ダウ方向と調整方向を混同しない

**Source-grounded draft interpretation**
C01 p.21 defines an intermediate TL across turns and describes endpoint selection around the point before the large-Dow extreme; C03 p.13 defines counter TL as small/middle-Dow TL drawn opposite the large-Dow trend direction and distinguishes small vs middle by same-turn vs turn-spanning structure.

**Primary Stage proposal**: `Environment`

**Secondary**: `Observation / Setup`

**Image review**: `REQUIRED`.

**Open issues**
- exact endpoint selection and exceptions;
- whether `中間TL` and C03 `中ダウカウンターTL` need a formal relationship map;
- selection remains source/image dependent; no generic TA completion.

**User judgment**: `未確認`

### R18 | ラインブレイク後は地図を更新

**Current baseline text**
ブレイク直後にEntryだけを考えず、次の安値・高値がどこで形成されるか、新しい2点でTLを引き直せるかを確認する。上昇TLなら新終点も始点より高く、下降TLなら新終点も始点より低い必要がある。引き直したTL・CHで直近フィールドを再定義する。

**Source-grounded draft interpretation**
S05 directly prioritizes remapping after a line break: find the next high/low, determine whether a new TL can be drawn under the existing rising/falling-point geometry, redraw TL/CH, and re-grasp the currently recognized Field.

**Primary Stage proposal**: `Environment`

**Secondary**: `Observation`

**Image review**: `REQUIRED` because endpoint selection/remapping is visual.

**Open issues**
- exact high/low candidate selection is still governed by prior unresolved detector issues;
- relationship to R06/R07/R08 line-selection TBDs;
- no Entry rule should be added here.

**User judgment**: `未確認`

### R19 | リターンムーブ

**Confirmed formal definition**
Return Moveとは、トレンドラインをBreakした後、価格が旧トレンドライン側へ戻る動きとして観測される現象をいう。発生しやすい傾向として認識するが、Return Moveそれ自体を売買方向、Entry、小ダウBR成立、意識の復活成立、トレンド転換/継続確定等の判断根拠にはしない。

**Responsibility**
R19は`判断材料`ではなく`観測現象`。Primary Stageは`Observation`。

Return Moveが観測された場合、その後にR14小ダウBR、R15意識の復活（小）、その他の小ダウActionが形成されないかを見るための`OBSERVATION_CUE / SEARCH_CUE`として利用できる。これは`SIGNAL / TRIGGER / CONFIRMATION`ではない。

**No effect on TL / mapping**
R19単独でTL選択、引き直し、延長、削除、Zone変更、Field変更、Phase変更を行わない。ラインBreak後の高安確認、TL/CH更新、Field再定義はR18の責務であり、`R19 -> TL update`依存を作らない。

**Relation to R14/R15**
- R14内のReturnは小ダウBR Trigger構造の一部であり、R19の一般観測現象と自動同一視しない。
- R19が先に観測されてもR14/R15成立を意味しない。`R19 observed -> small-Dow structure watch -> R14/R15 independent check ->成立/不成立`。

**Primary Stage**: `Observation`

**Secondary**: `Downstream search context only`

**Source**: S06 / S03. Source describes tendency and possible market-participant behavior; user review constrains R19 responsibility to observation/cue and does not promote it to a trade signal.

**Detector status**: `RETURN_MOVE_DETECTION_TBD`.

**Detector must not invent**: exact-line touch, zone-entry threshold, pips tolerance, wick/body rule, candle count, elapsed time.

**Status**: `CONFIRMED_RULE / RETURN_DETECTION_TBD`

**User judgment**: `OK / 単なる現象として扱う`

### R20 | TL BRとCH BRの意味

**Current baseline text**
- TL BR：従来トレンドの参加者が撤退し、反対勢力が出やすい。トレンド転換候補
- CH BR：従来方向の参加者が有利になり、同方向へ加速しやすい。トレンド続伸候補
- CHは利確目標として意識されることが多く、到達だけで反対Entryを決めない

**Source-grounded draft interpretation**
S06 directly contrasts TL break as weakening the prior trend and making the opposite force more likely, versus CH break as favoring continuation/acceleration in the same direction. It also describes CH as commonly used as a profit target and warns conceptually that opposite-side participants have not necessarily exited merely because CH is reached.

**Primary Stage proposal**: `Trigger`

**Secondary**: `Environment`

**Image review**: `RECOMMENDED`.

**Open issues**
- `転換候補` and `続伸候補` must remain candidate interpretations, not guaranteed outcomes;
- exact BR detector remains separate;
- the baseline phrase about not deciding opposite Entry at CH arrival should be reviewed for responsibility placement rather than silently promoted.

**User judgment**: `未確認`

## 5. Review order after NS2-B1

Still unresolved:
1. `R11-R13` — Phase definitions and transition criteria.
2. `R17-R18 / R20` — intermediate/counter lines, remapping, TL/CH BR meaning.

R19 is already confirmed separately as an Observation/Cue and must not be reabsorbed into Trigger logic without a new user-approved change.

## 6. Prohibitions after NS2-B1

This document does not:
- alter R01-R10 semantics;
- confirm R11-R13, R17-R18, or R20;
- process R21+ or start NS2-C;
- create detector thresholds;
- fix D1/H4/H1/M15 mappings;
- create generic-TA replacements;
- add Entry/SL/TP/sizing/execution logic;
- create new Observation IDs;
- promote NS1 Observations to FIXED;
- treat R19 as Trigger, signal, confirmation, trade-direction evidence, confidence score, or TL-update condition;
- modify TC or `trade-plan-a`.
