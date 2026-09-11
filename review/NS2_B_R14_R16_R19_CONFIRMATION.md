# NS2-B1 R14-R16 / R19 Confirmation

Repository: `toootakeooot-bit/tradeplan-engine-noda`

Branch: `feature/noda-v1`

Start HEAD: `00532261164dca16232c2357a2801ae6b97cd501`

Scope: **R14 / R15 / R16 / R19 user-reviewed confirmation only**.

R11-R13, R17-R18 and R20 remain `REVIEW_REQUIRED`. R21+ and NS2-C are out of scope.

## 1. Confirmation summary

| Rule | Confirmed role | Primary Stage | Secondary | Status | User judgment |
|---|---|---|---|---|---|
| R14 | Small-Dow BR Trigger | Trigger | Phase / Setup | `CONFIRMED_RULE / DETECTION_TBD` | OK |
| R15 | Small awareness revival structural Action | Trigger | Phase | `CONFIRMED_RULE / DETECTION_TBD` | OK |
| R16 | Large awareness revival / main-trend return Action | Trigger | Phase / Environment | `CONFIRMED_RULE / DETECTION_TBD` | OK |
| R19 | Return Move observation phenomenon / search cue | Observation | Downstream search context only | `CONFIRMED_RULE / RETURN_DETECTION_TBD` | OK / 単なる現象として扱う |

## 2. R14 confirmed definition

大ダウの際へ到達した後、最終局面内の小ダウラインを用いてBreakとReturnを確認し、次の先行期へ切り替わるActionを捉える。

対象ライン:
- TL: 最終局面内で現在のトレンド方向に引いた小ダウTL。
- HL: 最終局面内の最後の押し安値・戻し高値に置いた小ダウHL。

構造順序:

`大ダウの際 -> 最終局面 -> 小ダウTL / HL -> Break -> Return -> 次の先行期候補`

R14はTrigger構造までを扱う。Entry価格、注文方法、SL、TP、Lot、Position Size、発注は後続責務。

Detector: `SMALL_DOW_BR_DETECTION_TBD`.

以下は未定義:
- Break pips閾値;
- 終値確定条件;
- ヒゲ抜け条件;
- Return許容距離;
- Returnまでのローソク足本数;
- Break後の経過時間条件。

## 3. R15 confirmed definition

本格局面または最終局面内で、反対トレンド方向へ引いた小ダウラインが一度Breakされた後、再びそのライン側へ戻るActionを、直前の小ダウターンの意識が復活する候補として捉える。

本質は`単なるReturn現象`ではなく、`直前の小ダウターンの意識が再び働く構造的Action`。

Detector: `SMALL_AWARENESS_REVIVAL_DETECTION_TBD`.

以下は未定義:
- 完全再クロス必須か;
- 接触だけでよいか;
- Zone進入でよいか;
- pips許容距離;
- ローソク足本数;
- 反応回数。

## 4. R16 confirmed definition

一度Breakされた大ダウラインに対し、再びメイントレンド方向へ戻るActionを「意識の復活（大）」の候補として捉える。小ダウの上げ・下げが一巡した後に、次の小ダウサイクルの起点となる動きを見る。

本質は`大ダウ側のメイントレンド意識の復活`。

以下の単純化は禁止:
- `大ダウラインへタッチ = 意識の復活（大）`;
- `大ダウラインへ戻る = 即Entry`。

Detector: `SMALL_DOW_CYCLE_DETECTION_TBD`; line-return detection also remains TBD.

## 5. R19 confirmed definition

Return Moveとは、トレンドラインをBreakした後、価格が旧トレンドライン側へ戻る動きとして観測される現象をいう。

発生しやすい傾向として認識するが、Return Moveそれ自体を以下の判断根拠にはしない:
- 買い / 売り方向;
- Entry;
- 小ダウBR成立;
- 意識の復活成立;
- トレンド転換確定;
- トレンド継続確定;
- 信頼度 / score。

R19のPrimary Stageは`Observation`。`Trigger`ではない。

Return Move観測後、その後のR14、R15、その他の小ダウActionを探すための`OBSERVATION_CUE / SEARCH_CUE`として使うことはできる。これは`SIGNAL / TRIGGER / CONFIRMATION`ではない。

Detector: `RETURN_MOVE_DETECTION_TBD`.

## 6. R19 and TL / mapping boundary

R19単独では以下を変更しない:
- TL選択;
- TL引き直し;
- TL延長;
- TL削除;
- Zone;
- Field;
- Phase。

ラインBreak後に次の高値・安値を確認し、TL/CHを引き直し、Fieldを再定義する責務はR18側にある。

`R19 -> TL update` dependency is prohibited.

## 7. R19 versus R14

R14内の`Break + Return`は、小ダウBR Trigger構造の一部。

R19は、TL Break後に旧TL側へ戻る一般的な観測現象。

同じ`Return`語を含んでも、`R14 Return == R19 Return Move`と自動同一視しない。R19単独でR14成立とはしない。

## 8. R19 versus R15

R15は`小ダウ構造 + 局面 + ライン方向 + 意識復活という構造的意味`を持つTrigger Action。

R19は観測現象のみ。

したがって:
- `R15 != R19`;
- R15をR19の下位Ruleとは固定しない;
- `R19 observed -> R15成立`とはしない。

許される関係:

`R19 observed -> small-Dow structure watch -> R15 conditions independently checked -> 成立 / 不成立`

R14についても同様に独立確認する。

## 9. Source and visual verification

### R14
- Primary: C01 `短期集中コース 1回目.pdf`, p.18.
- Supplemental: S07 `16 《練習》先行期を狙ったエントリー.txt`.
- C01 p.18 visual reviewed: TL/HL small-Dow BR types, final-phase context, large-Dow edge context are visually consistent with the confirmed semantics.

### R15
- Primary: C01 p.19.
- C01 p.19 visual reviewed: main/final-phase opposite-direction small-Dow line, break then return Action, and `直前のターンの復活` wording are consistent with the confirmed semantics.

### R16
- Primary: C01 p.20.
- C01 p.20 visual reviewed: once-broken large-Dow line, return toward main trend, small-Dow up/down cycle and next-cycle origin are visually consistent with the confirmed semantics.

### R19
- Primary: S06 `10 ラインの引き方例.txt`.
- Supplemental: S03.
- Source text supports Return Move as a post-break phenomenon/tendency. The user-approved responsibility restriction is stronger than the source's participant-behavior commentary: R19 is not promoted to a trade signal.

No image-derived threshold or unstated teacher intent is added.

## 10. User-approved difference record

`USER APPROVED DIFFERENCE` / `USER_REVIEW_APPROVED_CLARIFICATION`:

- R14: confirmed as Trigger structure, with Entry/SL/TP/sizing/execution excluded.
- R15: confirmed as structural awareness-revival Action; explicitly separated from R19.
- R16: confirmed as large-Dow/main-trend awareness revival; simple line touch is insufficient.
- R19: reclassified from draft `Trigger` proposal to `Observation`; Return Move itself is not a decision input, signal, confirmation, score, or TL-update condition. It may act only as a search/observation cue for later independent R14/R15 checks.

The external `02_野田式判断ルール台帳.md` is not directly overwritten here.

## 11. Observation governance

No new Observation ID is added.

R19 is assigned management Stage `Observation`, but this does not create a new NS1 Observation ID or promote NO201/NO202/NO203 to `FIXED`.

Detector issues remain unresolved under the normal governance path.

## 12. Remaining review scope

Remain `REVIEW_REQUIRED`:
- R11;
- R12;
- R13;
- R17;
- R18;
- R20.

R21+ is not processed. NS2-C is not started.
