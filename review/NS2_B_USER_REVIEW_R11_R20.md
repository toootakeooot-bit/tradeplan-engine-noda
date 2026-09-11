# NS2-B User Review R11-R20

Status: **PARTIAL CONFIRMATION — R14-R16 / R19 CONFIRMED; R11-R13 / R17-R18 / R20 USER REVIEW REQUIRED**

Repository: `toootakeooot-bit/tradeplan-engine-noda`

Branch: `feature/noda-v1`

NS2-B start HEAD: `b92dac35b625f81f86c71bdab2265f15c49b1ef7`

NS2-B1 start HEAD: `00532261164dca16232c2357a2801ae6b97cd501`

R01-R10 remain confirmed under NS2-A1/A2/A3. In NS2-B1, R14-R16 and R19 are user-confirmed at rule-semantics level. R11-R13, R17-R18 and R20 remain unconfirmed.

## 1. Review summary

| Rule | Plain meaning | Main source | Primary Stage | Image review | Main unresolved point | User judgment |
|---|---|---|---|---|---|---|
| R11 | トレンドを先行期・本格局面・最終局面の3段階で見る | S02 / C01 / C03 | Phase | REQUIRED | 局面境界Detector、ネストした局面 | 未確認 |
| R12 | 大きい構造の際を探し、その付近で次の先行期への動きを待つ | S07 / C01 | Phase | REQUIRED | `際付近` の境界、SL説明の責務 | 未確認 |
| R13 | 大ダウの際から本格局面入りを、最後の押し安値/戻し高値や補助情報で確認する | C03 | Phase | REQUIRED | MA/Formationの必須度、時間足例の扱い | 未確認 |
| R14 | 大ダウの際→最終局面→小ダウTL/HLのBreak+Returnで次の先行期候補を捉える | C01 / S07 | Trigger | REQUIRED | `SMALL_DOW_BR_DETECTION_TBD` | OK |
| R15 | 小ダウの反対方向ラインをBreak後に戻るActionを、直前ターンの意識復活候補として捉える | C01 | Trigger | REQUIRED | `SMALL_AWARENESS_REVIVAL_DETECTION_TBD` | OK |
| R16 | 大ダウラインBreak後、メイントレンド方向へ戻るActionと次の小ダウサイクル起点を見る | C01 | Trigger | REQUIRED | `SMALL_DOW_CYCLE_DETECTION_TBD` | OK |
| R17 | ターンを跨ぐ中間TLと、大ダウ逆方向のカウンターTLを区別する | C01 / C03 | Environment | REQUIRED | 中間TL終点選択、概念関係 | 未確認 |
| R18 | ラインBR後は次の高安と新TL/CHでFieldを更新する | S05 | Environment | REQUIRED | 新終点の候補選択 | 未確認 |
| R19 | TL Break後に旧TL側へ戻る現象。売買判断ではなく、その後の小ダウAction探索の手掛かり | S06 / S03 | Observation | RECOMMENDED | `RETURN_MOVE_DETECTION_TBD` | OK / 単なる現象として扱う |
| R20 | TL BRは転換候補、CH BRは続伸・加速候補 | S06 | Trigger | RECOMMENDED | BR Detector、候補と確定の区別 | 未確認 |

---

## R11｜3つの局面

【現行台帳】
- 先行期：先行参加者が仕込み、一般参加者はまだ悲観的な時期
- 本格局面：角度と勢いが強い主要トレンドの進行期
- 最終局面：一般参加者が遅れて入り、トレンドは続くが値動きが軟化する時期
- 野田式では大小のトレンドにも適用する

【正式定義案】
トレンドは、`先行期 / 本格局面 / 最終局面` の3局面として捉える。

- 先行期：先行参加者が仕込み、一般参加者はまだ悲観的な時期。
- 本格局面：トレンドの力が強く進行する主要局面。
- 最終局面：トレンド自体は継続しているが、一般参加者が遅れて参加し、値動きが軟化していく局面。
- 野田式では、大きく見たトレンド・小さく見たトレンドの両方に3局面の考え方を適用する。

【簡単に言うと】
1本のトレンドを「始まり・本番・終盤」の3段階で読む。大きい波でも小さい波でも同じ考え方を使う。

【AI理解】
S02は、本格局面中に保ち合いを含む場合もあると説明しているため、`本格局面 = 常に急角度` と機械化しない方がよい。角度・勢いは典型的特徴であり、局面Detectorは別途必要。

【主Source】 S02 `05 トレンドの3つの局面.txt`
【補助Source】 C01 / C03
【Evidence】 A1
【Primary Stage候補】 Phase
【Secondary】 Environment
【画像確認】 REQUIRED
【不明点】 局面境界Detector、複数構造尺度で局面が重なる場合の表現
【AI confidence】 HIGH semantics / MEDIUM detector
【ユーザー判定】 未確認

---

## R12｜先行期を狙う前提

【現行台帳】
先行期は「際で勝負する」発想。上位の大ダウライン・ゾーン等の際を見つけ、その付近で最終局面から次の先行期へ移る小ダウActionを待つ。際から離れたEntryはSLが遠くなり、損切りが増えやすい。

【正式定義案】
先行期を捉えるときは、まず広い構造の`際`を探す。その際付近で、現在の最終局面から次の先行期へ切り替わる小さな構造・Actionを確認する。

【簡単に言うと】
相場の真ん中ではなく、まず「端・境界」を探し、その近くで次の流れが始まる動きを待つ。

【AI理解】
S07の週足→日足は実例であり、固定時間足Ruleにはしない。`際で勝負すると損切りしやすい` という説明はSourceにあるが、R12本体にどこまで含めるかはレビュー対象。

【主Source】 S07 `16 《練習》先行期を狙ったエントリー.txt`
【補助Source】 C01
【Evidence】 A1
【Primary Stage候補】 Phase
【Secondary】 Setup
【関係】 R07 / R08 / R10 / R14
【画像確認】 REQUIRED
【不明点】 際付近の境界、SL説明の責務位置
【AI confidence】 HIGH
【ユーザー判定】 未確認

---

## R13｜本格局面の確認

【現行台帳】
大ダウの際へ到達後、反対側の最後の押し安値または戻し高値のブレイクを確認する。中期MA群（21・40・62EMA）、200SMA、フォーメーションを補助にし、必要なら4時間足・1時間足へ下げて波形を確認する。

【正式定義案】
大ダウの際へ到達した後、本格局面入りを確認する際は、最後の押し安値または戻し高値のブレイクを重要な構造確認として見る。C03で示される中期MA群・長期MA・フォーメーションは、本格局面判断を補助する情報として扱う候補とする。

【簡単に言うと】
際から本当に本格トレンドへ進み始めたかを、高安の重要ポイントのBreakを中心に確認し、MAや形も補助に見る。

【AI理解】
C03は21/40/62EMAを`（本）かどうかの判断に条件も加える`と説明する一方、Formationは`形成してくると入りやすくなる`という表現。よって、MAとFormationを同じ必須度で扱うのは未確定。H4/H1も実例であって固定要件とは限らない。

【主Source】 C03 `短期集中コース 3回目.pdf`
【Evidence】 A1
【Primary Stage候補】 Phase
【Secondary】 Setup
【画像確認】 REQUIRED
【不明点】 最後の押し安値/戻し高値Breakの必須度、MAの必須度、Formationの役割、時間足固定の可否
【AI confidence】 MEDIUM
【ユーザー判定】 未確認

---

## R14｜小ダウBR

【正式定義】
大ダウの際へ到達した後、最終局面内の小ダウラインを用いてBreakとReturnを確認し、次の先行期へ切り替わるActionを捉える。

対象ライン：
- TL：最終局面内で現在のトレンド方向に引いた小ダウTL。
- HL：最終局面内の最後の押し安値・戻し高値に置いた小ダウHL。

構造順序：
`大ダウの際 -> 最終局面 -> 小ダウTL / HL -> Break -> Return -> 次の先行期候補`

【責務境界】
R14はTrigger構造まで。Entry価格、注文方法、SL、TP、Lot、Position Size、発注は扱わない。

【主Source】 C01 p.18
【補助Source】 S07
【Primary Stage】 Trigger
【Secondary】 Phase / Setup
【画像確認】 REQUIRED
【Detector】 `SMALL_DOW_BR_DETECTION_TBD`
【未確定】 Breakのpips/終値/ヒゲ条件、Return距離・本数・時間条件
【Status】 `CONFIRMED_RULE / DETECTION_TBD`
【ユーザー判定】 OK

---

## R15｜意識の復活（小）

【正式定義】
本格局面または最終局面内で、反対トレンド方向へ引いた小ダウラインが一度Breakされた後、再びそのライン側へ戻るActionを、直前の小ダウターンの意識が復活する候補として捉える。

【本質】
単なるReturn現象ではなく、`直前の小ダウターンの意識が再び働く構造的Action`。

【R19との分離】
R15とR19は別Rule。R15は`小ダウ構造 + 局面 + ライン方向 + 意識復活という構造的意味`を持つ。R19はTL Break後に価格が旧TL側へ戻る観測現象。`R15 = R19` とせず、R15をR19の下位Ruleとも定義しない。

【主Source】 C01 p.19
【Primary Stage】 Trigger
【Secondary】 Phase
【画像確認】 REQUIRED
【Detector】 `SMALL_AWARENESS_REVIVAL_DETECTION_TBD`
【未確定】 完全再クロス/接触/Zone進入、pips距離、本数、反応回数
【Status】 `CONFIRMED_RULE / DETECTION_TBD`
【ユーザー判定】 OK

---

## R16｜意識の復活（大）

【正式定義】
一度Breakされた大ダウラインに対し、再びメイントレンド方向へ戻るActionを「意識の復活（大）」の候補として捉える。小ダウの上げ・下げが一巡した後に、次の小ダウサイクルの起点となる動きを見る。

【本質】
`大ダウ側のメイントレンド意識の復活`。

【注意】
`大ダウラインへタッチした = 意識の復活（大）` ではない。`大ダウラインへ戻った = 即Entry` でもない。

【主Source】 C01 p.20
【Primary Stage】 Trigger
【Secondary】 Phase / Environment
【画像確認】 REQUIRED
【Detector】 `SMALL_DOW_CYCLE_DETECTION_TBD`、line-return detector TBD
【Status】 `CONFIRMED_RULE / DETECTION_TBD`
【ユーザー判定】 OK

---

## R17｜中間TL・カウンターTL

【正式定義案】
- 中間TL：ターンを跨いだ高値・安値で引くTL。終点として大ダウ極値の一つ前を選ぶ例がある。
- カウンターTL：大ダウの主トレンド方向と逆方向に引く小ダウ・中ダウTL。

大ダウ方向と調整方向を混同しない。

【主Source】 C01 p.21 / C03 p.13
【Primary Stage候補】 Environment
【Secondary】 Observation / Setup
【画像確認】 REQUIRED
【不明点】 中間TL終点選択、`中間TL`と`中ダウカウンターTL`の関係
【ユーザー判定】 未確認

---

## R18｜ラインブレイク後は地図を更新

【正式定義案】
ラインBreak後は、Entry判断より先に次の高値・安値がどこで形成されるかを確認し、新しい2点でTLを引き直せるかを確認する。引き直したTL/CHによって直近Fieldを再把握する。

上昇TLは新終点が始点より高く、下降TLは新終点が始点より低いという基本幾何を維持する。

【主Source】 S05 `08 ラインをブレイクした時の対処法.txt`
【Primary Stage候補】 Environment
【Secondary】 Observation
【画像確認】 REQUIRED
【不明点】 新終点候補の選択、既存LINE_SELECTION_TBDとの接続
【ユーザー判定】 未確認

---

## R19｜リターンムーブ

【正式定義】
Return Moveとは、トレンドラインをBreakした後、価格が旧トレンドライン側へ戻る動きとして観測される現象をいう。

発生しやすい傾向として認識するが、Return Moveそれ自体を売買方向、Entry、小ダウBR成立、意識の復活成立、トレンド転換・継続確定等の判断根拠にはしない。

【役割】
`判断材料`ではなく`観測現象`。その後にR14小ダウBR、R15意識の復活（小）、その他の小ダウActionが形成されないかを見るための`OBSERVATION_CUE / SEARCH_CUE`として利用できる。

これは`SIGNAL / TRIGGER / CONFIRMATION`ではない。

【TL / mappingへの影響】
R19単独でTL選択、引き直し、延長、削除、Zone変更、Field変更、Phase変更を行わない。ラインBreak後の高安確認、TL/CH更新、Field再定義はR18の責務。

【R14/R15との関係】
- R14内のReturnは小ダウBR Trigger構造の一部。R19と自動同一視しない。
- R19観測後にR14/R15を探索してよいが、R19単独でR14/R15成立とはしない。
- 処理イメージ：`R19 observed -> small-Dow structure watch -> R14/R15 independent check -> 成立 / 不成立`。

【主Source】 S06 `10 ラインの引き方例.txt`
【補助Source】 S03
【Primary Stage】 Observation
【Secondary】 Downstream search context only
【画像確認】 RECOMMENDED
【Detector】 `RETURN_MOVE_DETECTION_TBD`
【未確定】 exact-line touch / Zone進入、pips距離、ヒゲ/実体、本数、経過時間
【Status】 `CONFIRMED_RULE / RETURN_DETECTION_TBD`
【ユーザー判定】 OK / 単なる現象として扱う

---

## R20｜TL BRとCH BRの意味

【正式定義案】
- TL BR：従来トレンド側の力が弱まり、反対勢力が出現しやすくなるため、トレンド転換候補として捉える。
- CH BR：従来トレンド方向の勢力が有利になり、同方向へ続伸・加速しやすくなる候補として捉える。

いずれも`候補`であり結果保証ではない。

【主Source】 S06 `10 ラインの引き方例.txt`
【Primary Stage候補】 Trigger
【Secondary】 Environment
【画像確認】 RECOMMENDED
【不明点】 BR Detector、CH到達時の反対Entryに関する文の責務位置
【ユーザー判定】 未確認

## 2. Remaining user-review batches

未確定ブロック：

- `R11-R13`
- `R17-R18 / R20`

R19はNS2-B1で先行確定したが、今後R17-R20全体の整合確認時に参照してよい。ただし新しいユーザー承認なしにTriggerへ戻したり、R14/R15と統合してはならない。
