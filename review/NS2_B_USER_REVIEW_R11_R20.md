# NS2-B User Review R11-R20

Status: **USER REVIEW REQUIRED**

Repository: `toootakeooot-bit/tradeplan-engine-noda`

Branch: `feature/noda-v1`

NS2-B start HEAD: `b92dac35b625f81f86c71bdab2265f15c49b1ef7`

R01-R10 remain confirmed under NS2-A1/A2/A3. R11-R20 are not confirmed yet.

## 1. Review summary

| Rule | Plain meaning | Main source | Primary Stage proposal | Image review | Main unresolved point | User judgment |
|---|---|---|---|---|---|---|
| R11 | トレンドを先行期・本格局面・最終局面の3段階で見る | S02 / C01 / C03 | Phase | REQUIRED | 局面境界Detector、ネストした局面 | 未確認 |
| R12 | 大きい構造の際を探し、その付近で次の先行期への動きを待つ | S07 / C01 | Phase | REQUIRED | `際付近` の境界、SL説明の責務 | 未確認 |
| R13 | 大ダウの際から本格局面入りを、最後の押し安値/戻し高値や補助情報で確認する | C03 | Phase | REQUIRED | MA/Formationの必須度、時間足例の扱い | 未確認 |
| R14 | 最終局面の小ダウTL/HLのBRとReturnで次の先行期を捉える | C01 / S07 | Trigger | REQUIRED | Break/Return Detector | 未確認 |
| R15 | 小ダウラインを抜けて戻る動きで直前ターンの意識復活を見る | C01 | Trigger | REQUIRED | Break/Return、R03/R19との境界 | 未確認 |
| R16 | 一度抜けた大ダウラインへ戻り、メイントレンド復帰候補を見る | C01 | Trigger | REQUIRED | 小ダウ1サイクルの定義 | 未確認 |
| R17 | ターンを跨ぐ中間TLと、大ダウ逆方向のカウンターTLを区別する | C01 / C03 | Environment | REQUIRED | 中間TL終点選択、概念関係 | 未確認 |
| R18 | ラインBR後は次の高安と新TL/CHでFieldを更新する | S05 | Environment | REQUIRED | 新終点の候補選択 | 未確認 |
| R19 | TL BR後は旧TLへのReturnが起きやすく、逆側の力が出る候補 | S06 / S03 | Trigger | RECOMMENDED | 接触/Return許容範囲 | 未確認 |
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

【正式定義案】
最終局面内で、トレンド方向に引いた小ダウTL、または最後の押し安値・戻し高値に置いたHLをBR対象として使う。大ダウの際へ到達後、そのBreakとReturnを確認して次の先行期候補を捉える。

【主Source】 C01 p.18 / S07
【Primary Stage候補】 Trigger
【Secondary】 Phase / Setup
【画像確認】 REQUIRED
【不明点】 Break / Return Detector
【ユーザー判定】 未確認

---

## R15｜意識の復活（小）

【正式定義案】
本格局面または最終局面内で反対トレンド方向へ引いた小ダウラインが一度抜けた後、再びそのラインへ戻るActionを、直前の小ダウターンの意識が復活する候補として捉える。

【主Source】 C01 p.19
【Primary Stage候補】 Trigger
【Secondary】 Phase
【画像確認】 REQUIRED
【不明点】 Break / Return Detector、R03 Turn・R19 Return Moveとの境界
【ユーザー判定】 未確認

---

## R16｜意識の復活（大）

【正式定義案】
一度抜けた大ダウラインへ戻り、メイントレンドへ復帰する候補を捉える。小ダウの上げ・下げを一巡した後、次サイクルの起点を見る。

【主Source】 C01 p.20
【Primary Stage候補】 Trigger
【Secondary】 Phase / Environment
【画像確認】 REQUIRED
【不明点】 小ダウ1サイクルのDetector、ラインReturn Detector
【ユーザー判定】 未確認

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

【正式定義案】
- 上昇TLを下へBreakした後は、旧上昇TL方向へ戻るReturn Moveが発生しやすく、その付近で新規の売り目線が出やすい候補とする。
- 下降TLを上へBreakした後は、旧下降TL方向へ戻るReturn Moveが発生しやすく、その付近で新規の買い目線が出やすい候補とする。

必ず起きるとは扱わない。

【主Source】 S06 `10 ラインの引き方例.txt`
【補助Source】 S03
【Primary Stage候補】 Trigger
【Secondary】 Setup
【画像確認】 RECOMMENDED
【不明点】 Return接触許容範囲、line/zoneとの関係
【ユーザー判定】 未確認

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

## 2. Recommended first user-review batch

Start with `R11-R13` because R14-R20 depend on Phase / edge context.

Suggested response format:

`R11 OK / 修正 / 保留`
`R12 OK / 修正 / 保留`
`R13 OK / 修正 / 保留`

Add any meaning corrections in plain Japanese. No R11-R20 rule becomes CONFIRMED until the user review gate and required visual/source verification are complete.
