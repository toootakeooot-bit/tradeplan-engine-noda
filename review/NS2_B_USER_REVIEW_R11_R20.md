# NS2-B User Review R11-R20

Status: **COMPLETE AT RULE-SEMANTICS LEVEL — DETECTOR / SELECTION TBDs REMAIN**

Repository: `toootakeooot-bit/tradeplan-engine-noda`

Branch: `feature/noda-v1`

NS2-B start HEAD: `b92dac35b625f81f86c71bdab2265f15c49b1ef7`

NS2-B1 start HEAD: `00532261164dca16232c2357a2801ae6b97cd501`

NS2-B2 start HEAD: `1e46eabd19207ce583aa93fe334b77df58a60986`

R01-R10 remain confirmed under NS2-A1/A2/A3. R14-R16 and R19 remain confirmed under NS2-B1. NS2-B2 confirms R11-R13, R17-R18 and R20 at rule-semantics level.

## 1. Review summary

| Rule | Plain meaning | Primary Stage | Main unresolved | User judgment |
|---|---|---|---|---|
| R11 | トレンドを先行期・本格局面・最終局面の3段階で捉え、大小構造へ適用 | Phase | `PHASE_DETECTION_TBD` | OK |
| R12 | 広い構造の際を探し、最終局面から次の先行期へ移る細かなActionを見る | Phase | `EDGE_PROXIMITY_TBD` | OK |
| R13 | 大ダウの際後、最後の押し安値/戻し高値Breakを本格局面の主要構造確認に使う | Phase | `MAIN_PHASE_MA_ROLE_TBD`; detector TBD | OK / Core confirmed |
| R14 | 際→最終局面→小ダウTL/HL→Break+Return→次の先行期候補 | Trigger | `SMALL_DOW_BR_DETECTION_TBD` | OK / NS2-B1 |
| R15 | 小ダウの直前ターンの意識復活を構造的Actionとして捉える | Trigger | `SMALL_AWARENESS_REVIVAL_DETECTION_TBD` | OK / NS2-B1 |
| R16 | 大ダウ側のメイントレンド意識復活と次サイクル起点を見る | Trigger | `SMALL_DOW_CYCLE_DETECTION_TBD` | OK / NS2-B1 |
| R17 | 中間TLと中ダウカウンターTLを別概念として使い分ける | Environment | `LINE_SELECTION_TBD` | OK / User clarification reflected |
| R18 | Break後の新高安を使いTL/CH/Fieldを更新する | Environment | `HIGH_LOW_DETECTION_TBD`; `LINE_SELECTION_TBD` | OK / User clarification reflected |
| R19 | Return Moveは単なる観測現象/探索Cue | Observation | `RETURN_MOVE_DETECTION_TBD` | OK / NS2-B1 |
| R20 | TL/CHの参加者目的の違いとBRの構造的意味を読む | Environment | `BR_DETECTION_TBD` | OK / User clarification reflected |

---

## R11｜3つの局面

【正式定義】
トレンドは `先行期 / 本格局面 / 最終局面` の3局面として捉える。

- 先行期：トレンドが形成され始める初期局面。
- 本格局面：トレンドの力が強く進行する主要局面。
- 最終局面：トレンド自体は継続しているが、値動きが軟化していく終盤局面。
- 大きい構造・小さい構造の両方へ3局面の考え方を適用する。

【注意】
`本格局面 = 常に急角度` ではない。S02は保ち合いを含めて本格局面中と判断する場合も説明している。

`局面名称だけでEntryしない` はR11の定義本体ではなく downstream Entry boundary / operational guard。

固定時間足対応は作らない。

【主Source】 S02 `05 トレンドの3つの局面.txt`
【補助Source】 C01 / C03
【Primary Stage】 Phase
【Secondary】 Environment
【画像/原典確認】 完了。S02 text + C01/C03 phase context。閾値は推論していない。
【Detector】 `PHASE_DETECTION_TBD`
【Status】 `CONFIRMED_RULE / PHASE_DETECTION_TBD`
【ユーザー判定】 OK

---

## R12｜先行期を狙う前提

【正式定義】
先行期を捉えるときは、まず広い構造の `際` を探す。その際付近で、現在の最終局面から次の先行期へ切り替わる小さな構造・Actionを確認する。

`広い構造の際 -> 現在の最終局面 -> 細かな構造 / Action -> 次の先行期候補`

週足→日足等は実例であり固定Ruleにしない。

【SL説明】
S07の `際で勝負すると損切りしやすくなる` は際を狙う合理性として保持するが、R12ではSL計算・SL位置を作らない。

【主Source】 S07 `16 《練習》先行期を狙ったエントリー.txt`
【補助Source】 C01
【Primary Stage】 Phase
【Secondary】 Setup
【画像/原典確認】 完了。S07 text + C01 edge/small-Dow visual context。
【Detector】 `EDGE_PROXIMITY_TBD`
【Status】 `CONFIRMED_RULE / EDGE_PROXIMITY_TBD`
【ユーザー判定】 OK

---

## R13｜本格局面の確認

【正式Core】
大ダウの際へ到達した後、本格局面入りを確認する際は、最後の押し安値または戻し高値のBreakを重要な構造確認として見る。

【MA】
C03では21/40/62 EMAと200SMAが本格局面判断に関係することは確認できる。しかし必須度は固定しない。

`MAIN_PHASE_MA_ROLE_TBD`

【Formation】
`形成してくると入りやすくなる` というSource表現に合わせ、Formationは reinforcement / easier-to-read context とし、本格局面成立の必須Gateにはしない。

【細かな構造】
必要に応じて、より細かな構造でActionを確認する。H4/H1は実例であり固定マッピングにしない。

【主Source】 C03 `短期集中コース 3回目.pdf`
【Primary Stage】 Phase
【Secondary】 Setup
【画像確認】 完了。p.5構造Break、p.6 MA、p.7 Formation、p.9-10 finer structure。
【Status】 `CONFIRMED_CORE / MA_ROLE_TBD / DETECTION_TBD`
【ユーザー判定】 OK / Core confirmed

---

## R14｜小ダウBR

NS2-B1定義を維持。変更なし。

【Primary Stage】 Trigger
【Secondary】 Phase / Setup
【Detector】 `SMALL_DOW_BR_DETECTION_TBD`
【Status】 `CONFIRMED_RULE / DETECTION_TBD`
【ユーザー判定】 OK

---

## R15｜意識の復活（小）

NS2-B1定義を維持。R19とは別Rule。変更なし。

【Primary Stage】 Trigger
【Secondary】 Phase
【Detector】 `SMALL_AWARENESS_REVIVAL_DETECTION_TBD`
【Status】 `CONFIRMED_RULE / DETECTION_TBD`
【ユーザー判定】 OK

---

## R16｜意識の復活（大）

NS2-B1定義を維持。変更なし。

【Primary Stage】 Trigger
【Secondary】 Phase / Environment
【Detector】 `SMALL_DOW_CYCLE_DETECTION_TBD`; line-return detector TBD
【Status】 `CONFIRMED_RULE / DETECTION_TBD`
【ユーザー判定】 OK

---

## R17｜中間TL / 中ダウカウンターTL

【重要】
`中間TL` と `中ダウカウンターTL` は別概念。同義語・別名・完全な上下関係にはしない。

### 中間TL

【Source core】
C01 p.21：ターンを跨いだ安値・高値で引く。終点に大ダウ極値の一つ前を使う形が示され、始点/終点が絶対極値以外の場合もある。

【User approved clarification】
- 長期・中期的な視点で過去から引く;
- 小ダウ/細かな構造でBRを見る基準ライン;
- 局所短期ラインより信頼性を高めたラインとして扱う;
- 短期から中期まで比較的広く利用;
- 先行期・予兆把握で使いやすい.

信頼性は定性的性質であり数値化しない。

### 中ダウカウンターTL

【Source core】
C03 p.13：大ダウ方向と逆方向に引くカウンターTL。中ダウはターンを跨いだ状態で引く。

【User approved clarification】
- 小ダウ構造内でターンを跨ぐ;
- 大きなトレンド方向に対して逆方向;
- 局所的・目先中心;
- 小ダウ/細かな構造でBRを見る基準ライン;
- 本格局面で使いやすい.

【共通点と差】
両者とも小ダウ/細部BRを見る基準として役割は似るが、対象構造・利用期間・局面用途が異なる。

【Primary Stage】 Environment
【Secondary】 Observation / Setup
【画像確認】 完了。C01 p.21 / C03 p.13。
【Selection】 `LINE_SELECTION_TBD`
【Status】 `CONFIRMED_RULE / LINE_SELECTION_TBD`
【ユーザー判定】 OK / USER APPROVED CLARIFICATION

---

## R18｜ラインBreak後の構造更新

【正式定義】
ラインBreak後はEntry判断より先に、新たに形成される高値・安値を確認する。その高値・安値を使ってTLを引き直し、TL/CHおよび現在のFieldを再把握する。

【Source core】
S05は、Break後の次の高安、新終点候補、上昇TL/下降TLの基本幾何、TL/CHによるField再把握を直接説明する。`必ず新しい2点を選び直す` とはしない。

【User approved clarification】
Break後に形成された外側の新高安は無視できず、当該TL更新文脈では以前の対応高安より構造優先度が上がる。

`Break -> new outer high/low -> higher structural priority -> TL/CH update -> Field remap`

【R19との分離】
Return MoveはTL更新条件ではない。`R19 -> TL redraw` は禁止。

【Primary Stage】 Environment
【Secondary】 Observation
【Source/original review】 S05原典textを確認。登録Sourceに静止画がないため、画像由来の候補選択Ruleは作らず、選択/DetectorをTBD保持。
【Detector】 `HIGH_LOW_DETECTION_TBD`
【Selection】 `LINE_SELECTION_TBD`
【Status】 `CONFIRMED_RULE / HIGH_LOW_DETECTION_TBD / LINE_SELECTION_TBD`
【ユーザー判定】 OK / USER APPROVED CLARIFICATION

---

## R19｜Return Move

NS2-B1定義を維持。単なる観測現象 / Search Cue。変更なし。

【Primary Stage】 Observation
【Secondary】 Downstream search context only
【Detector】 `RETURN_MOVE_DETECTION_TBD`
【Status】 `CONFIRMED_RULE / RETURN_DETECTION_TBD`
【ユーザー判定】 OK / 単なる現象として扱う

---

## R20｜TL / CHの性質とBRの意味

### TL

【Source core】
S06：TLは新規Entry目安として使う参加者が多い。

【User approved clarification】
- 新規建て・参加判断の基準として意識されやすい;
- 水準が比較的明確になりやすい;
- Zoneは比較的狭くなりやすい;
- CHより相対的にラインの意味・力が強い.

`強い` は点数ではなく、参加判断が明確な水準へ集中しやすいという定性的性質。

### TL BR

S06の転換Action説明は候補/構造解釈として保持する。`TL BR = 転換確定` にはしない。

### CH

【Source core】
S06：CHは利確目標として使う参加者が多い。

【User approved clarification】
- 利確・撤退側の基準;
- 到達前/到達時/Break時/Break後/Return後など撤退判断に自由度がある;
- 意識が一点へ集中しにくい;
- TLより相対的にラインの力が弱い.

`弱い` は点数ではなく、利確/撤退判断が分散しやすいという定性的性質。

### CH BR

S06の続伸/加速Action説明は候補/構造解釈として保持する。`CH BR = 続伸確定` にはしない。

R20自体は単独Entry Triggerではない。

【Primary Stage】 Environment
【Secondary】 Observation / Trigger
【Detector】 `BR_DETECTION_TBD`
【Status】 `CONFIRMED_RULE / BR_DETECTION_TBD`
【ユーザー判定】 OK / USER APPROVED CLARIFICATION

## 2. Final NS2-B review state

R11-R20のRule semanticsはユーザーレビュー完了。

残るのはDetector / Selection / representation等の明示TBDのみ。

`NS2-B: COMPLETE at rule-semantics level`

R21以降およびNS2-Cは未着手のまま停止する。
