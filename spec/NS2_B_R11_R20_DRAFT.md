# NS2-B R11-R20 Draft

Status: **DRAFT / USER REVIEW REQUIRED**

Repository: `toootakeooot-bit/tradeplan-engine-noda`

Branch: `feature/noda-v1`

NS2-B start HEAD: `b92dac35b625f81f86c71bdab2265f15c49b1ef7`

Scope: **R11-R20 only**. R01-R10 remain as confirmed in NS2-A1/A2/A3. R21+ are out of scope. This file does not modify the external Rule Ledger.

## 1. Review control

NS2-B follows `spec/NS2_REVIEW_PROTOCOL.md`:

`AI draft -> Japanese user review -> OK/修正/保留 -> required source/image verification -> final整理 -> audit -> CONFIRMED or unresolved`

No R11-R20 item is `CONFIRMED` in this draft.

## 2. Summary matrix

| Rule | Name | Primary Stage proposal | Secondary Stage proposal | Main dependency / relation | Image review | AI confidence | Status |
|---|---|---|---|---|---|---|---|
| R11 | 3つの局面 | Phase | Environment | R02/R04/R07/R10; Phase representation TBD | REQUIRED | HIGH semantics / MEDIUM detector | REVIEW_REQUIRED |
| R12 | 先行期を狙う前提 | Phase | Setup | R07 edge, R08 small-Dow line, R10 Field/Action | REQUIRED | HIGH semantics | REVIEW_REQUIRED |
| R13 | 本格局面の確認 | Phase | Setup | NO101/NO102; large-Dow edge; MA/formation auxiliary handling | REQUIRED | MEDIUM | REVIEW_REQUIRED |
| R14 | 小ダウBR | Trigger | Phase / Setup | R07/R08; NO201/NO202; return relation | REQUIRED | HIGH semantics / MEDIUM trigger boundary | REVIEW_REQUIRED |
| R15 | 意識の復活（小） | Trigger | Phase | small-Dow line; Turn relation | REQUIRED | HIGH | REVIEW_REQUIRED |
| R16 | 意識の復活（大） | Trigger | Phase / Environment | large-Dow line; small-Dow cycle relation | REQUIRED | HIGH | REVIEW_REQUIRED |
| R17 | 中間TL・カウンターTL | Environment | Observation / Setup | NO202; Dow scale; Turn | REQUIRED | HIGH semantics / MEDIUM selection | REVIEW_REQUIRED |
| R18 | ラインブレイク後は地図を更新 | Environment | Observation | NO101/NO102/NO202/NO203; Field remap | REQUIRED | HIGH | REVIEW_REQUIRED |
| R19 | リターンムーブ | Trigger | Setup | NO202; support/resistance-role shift | RECOMMENDED | HIGH | REVIEW_REQUIRED |
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
| R19 | S03, S06 | S06 `10 ラインの引き方例.txt`: `ラインのブレイク後は【リターンムーブ】が発生しやすい` section. S03 provides support/resistance and line-break context. |
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

**Current baseline text**
- TL：最終局面内でトレンド方向に引いた小ダウTL
- HL：最終局面内の最後の押し安値・戻し高値
- 大ダウの際へ到達後、ブレイクとリターンを確認して先行期を狙う

**Source-grounded draft interpretation**
C01 p.18 explicitly defines small-Dow BR line types in the final phase and links them to targeting the early phase after reaching the large-Dow edge. S07 reinforces the break-return sequence for a final-phase small-Dow TL.

**Primary Stage proposal**: `Trigger`

**Secondary**: `Phase / Setup`

**Image review**: `REQUIRED`.

**Open issues**
- exact break definition;
- exact return definition;
- distinction between TL BR and HL BR in automation;
- do not create candle-close/pips thresholds without source.

**User judgment**: `未確認`

### R15 | 意識の復活（小）

**Current baseline text**
本格局面または最終局面内で、反対トレンド方向へ引いた小ダウラインが一度抜けた後、再びラインへ戻るアクション。直前の小ダウターンの意識が復活した候補として扱う。

**Source-grounded draft interpretation**
C01 p.19 directly describes a small-Dow line drawn opposite the trend direction in the main/final phase, a break, then a return to the line, interpreted as revival of the immediately preceding turn awareness and used to target the early phase.

**Primary Stage proposal**: `Trigger`

**Secondary**: `Phase`

**Image review**: `REQUIRED`.

**Open issues**
- exact break/return detector;
- exact relationship to R03 Turn and R19 Return Move;
- whether `候補` wording should remain explicit.

**User judgment**: `未確認`

### R16 | 意識の復活（大）

**Current baseline text**
一度抜けた大ダウラインへ戻り、メイントレンドへ復帰する候補。小ダウの上げ・下げを一巡した後、次サイクルの起点を探す。

**Source-grounded draft interpretation**
C01 p.20 directly describes returning to a once-broken large-Dow line, targeting a return to the main trend, after one small-Dow up/down cycle and while looking for the next-cycle origin.

**Primary Stage proposal**: `Trigger`

**Secondary**: `Phase / Environment`

**Image review**: `REQUIRED`.

**Open issues**
- exact definition of one completed small-Dow cycle;
- exact line-return detector;
- relationship to R03 Turn and R19 Return Move.

**User judgment**: `未確認`

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

**Current baseline text**
- 上昇TLを下抜けた後：戻りで旧上昇TLへ接触する場面に売り圧力が出る候補
- 下降TLを上抜けた後：戻りで旧下降TLへ接触する場面に買い圧力が出る候補
- 発生しやすい傾向であり、必ず起きるとは扱わない

**Source-grounded draft interpretation**
S06 explicitly states return moves are likely after line breaks: after breaking an up TL downward, price often rises back toward the former TL and new selling can appear; the reverse applies to a broken down TL.

**Primary Stage proposal**: `Trigger`

**Secondary**: `Setup`

**Image review**: `RECOMMENDED`.

**Open issues**
- exact contact/return tolerance;
- whether return must touch the exact line or zone;
- do not invent pips/candle thresholds.

**User judgment**: `未確認`

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

## 5. Review order

Recommended user-review batches:

1. `R11-R13` — Phase definitions and transition criteria.
2. `R14-R16` — BR and awareness-revival triggers.
3. `R17-R20` — intermediate/counter lines, remapping, return move, TL/CH BR meaning.

R11-R13 should be reviewed first because R14-R20 depend on Phase / edge context.

## 6. Prohibitions for NS2-B draft

This draft does not:
- confirm any R11-R20 rule;
- alter R01-R10 semantics;
- create detector thresholds;
- fix D1/H4/H1/M15 mappings;
- create generic-TA replacements;
- add Entry/SL/TP/sizing/execution logic;
- create new Observation IDs;
- promote NS1 Observations to FIXED;
- modify TC or `trade-plan-a`;
- process R21+.
