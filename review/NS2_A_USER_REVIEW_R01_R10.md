# NS2-A User Review R01-R10

Status: **R01-R05 CONFIRMED / R06 CONFIRMED_BASIC + VISUAL_SELECTION_TBD / R07-R09 CONFIRMED_RULE + selection TBD / R10 CONFIRMED**

このファイルはNS2-Aのユーザー確認記録です。R01-R03はNS2-A1、R04-R06はNS2-A2、R07-R10はNS2-A3でユーザー確認結果を反映しています。R11以降は未処理です。

## 1. 一覧レビュー

| Rule | 簡単に言うと | 主Source | Primary Stage | 主な未解決 | Status | ユーザー判定 |
|---|---|---|---|---|---|---|
| R01 | 高値・安値の読み取りを全分析の土台にする。 | S01 / C01 | Environment | significant high/low detector | CONFIRMED | OK |
| R02 | 高値・安値がともに切上げ=上昇、ともに切下げ=下降。それ以外はどちらでもない。 | S01 | Environment | high/low selection | CONFIRMED | OK / 修正反映済み |
| R03 | N字形成後、上昇側は最安値、下降側は最高値をターン起点として遡及確定する。 | C01 / S01 + user clarification | Environment | N_PATTERN_DETECTION_TBD / Swing関係 | CONFIRMED_RULE / DETECTION_TBD | OK / 修正反映済み |
| R04 | 大・中・小ダウは構造尺度と分析目的で使い分け、時間足へ固定しない。 | C01 / C02 + user clarification | Environment | DOW_SCALE_DETECTION_TBD | CONFIRMED_RULE / DOW_SCALE_DETECTION_TBD | OK / 修正反映済み |
| R05 | ラインは買い手・売り手の意識とFieldを視覚化する目的で選ぶ。 | S03 | Environment | line candidate selection | CONFIRMED | OK |
| R06 | HL/TL/CHの基本形を固定する。 | S03 / S06 + A2画像 | Observation | VISUAL_SELECTION_TBD | CONFIRMED_BASIC / VISUAL_SELECTION_TBD | 基本OK / 画像確認済み |
| R07 | 大ダウラインは広い構造の外側、広範囲Fieldと際を見る。 | C01 + user clarification | Environment | LARGE_DOW_LINE_SELECTION_TBD | CONFIRMED_RULE / LINE_SELECTION_TBD | OK / LINE_SELECTION_TBD |
| R08 | 小ダウラインは一局面内の細かな構造、近い対称関係・クラスターを捉える。 | C01 + user clarification | Setup | SMALL_DOW_LINE_SELECTION_TBD | CONFIRMED_RULE / LINE_SELECTION_TBD | OK / Entry削除 / Selection TBD |
| R09 | TLはゾーンとして扱い、基本形と2つの応用形がある。反応履歴は信頼度補強。 | S04 + user clarification | Observation | TL_ZONE_APPLICATION_SELECTION_TBD | CONFIRMED_RULE / APPLICATION_SELECTION_TBD | OK / β独自制御削除 / 反応履歴追加 |
| R10 | Field=戦場の面、Action=そこで起きる変化。Area分けし内部はより細かな構造で見る。 | C02 + user clarification | Environment | FIELD_REPRESENTATION_TBD | CONFIRMED | OK / Area・細部引継ぎ追加 |

---

## R01｜高値・安値が土台

【正式定義】トレンド判断、ライン選択、トレードプランは、高値・安値の読み取りを土台にする。  
【Stage】 Environment  
【Status】 CONFIRMED  
【未解決】 significant high/lowの厳密なDetector。  
【ユーザー判定】 OK

---

## R02｜トレンドの定義

【正式定義】  
- 上昇トレンド：高値と安値がともに切り上がって推移する。  
- 下降トレンド：高値と安値がともに切り下がって推移する。  
- それ以外：上昇トレンドでも下降トレンドでもない。

`NOT_UP_OR_DOWN` は第三のトレンド種類ではなく否定状態。レンジ等へ自動分類しない。  
【Stage】 Environment  
【Status】 CONFIRMED  
【ユーザー判定】 OK / 修正反映済み

---

## R03｜ターンの区切り

【正式定義】  
- 上昇側：N字が1つ形成された後、その区間の最安値をターン起点として遡って確定する。  
- 下降側：N字が1つ形成された後、その区間の最高値をターン起点として遡って確定する。

候補極値の出現時点では確定せず、N字形成後に `candidate -> confirmed turn origin` とする。  
【Stage】 Environment  
【Status】 CONFIRMED_RULE / DETECTION_TBD  
【未解決】 `N_PATTERN_DETECTION_TBD`、NO103 Swingとの関係=`RELATIONSHIP_TBD`。  
【ユーザー判定】 OK / 修正反映済み

---

## R04｜大・中・小ダウを目的で分ける

【正式定義】大・中・小ダウは、値動きの構造尺度と分析目的によって使い分ける。  
- 大ダウ：広範囲のフィールドと際を捉える。  
- 中ダウ：大ダウ内の途中の構造・フィールドを捉える。  
- 小ダウ：局面内の細かな構造とアクションを捉える。  
- 特定時間足へ固定しない。

Entryは定義から除外。BRも小ダウそのものの定義にしない。  
【Stage】 Environment  
【Status】 CONFIRMED_RULE / DOW_SCALE_DETECTION_TBD  
【ユーザー判定】 OK / 修正反映済み

---

## R05｜ラインは目的で選ぶ

【正式定義】ラインは、買い手・売り手の意識と現在のフィールドを視覚化する目的で選ぶ。  
【Stage】 Environment  
【Status】 CONFIRMED  
【未解決】 複数候補からの実装上の選択基準。  
【ユーザー判定】 OK

---

## R06｜基本ライン

【正式定義】  
- HL：価格が反転している高値・安値に水平に引く。  
- 上昇TL：切り上げた2点の安値で引く。  
- 下降TL：切り下げた2点の高値で引く。  
- CH：TLと平行にし、上昇CHは直近高値側、下降CHは直近安値側へ合わせる。

【Stage】 Observation / Secondary: Environment  
【Status】 CONFIRMED_BASIC / VISUAL_SELECTION_TBD  
【Observation依存】 NO201, NO202, NO203  
【画像確認】 基本形は確認済み。複数候補選択は画像のみでは一意化しない。  
【ユーザー判定】 基本OK / 画像確認済み・選択規則TBD

---

## R07｜大ダウのライン

【正式定義】  
大ダウラインは、広いトレンド構造の外側を捉え、広範囲のフィールドと際を認識するために使用する。

- 大ダウTL：選択時点で一度も抜かれていないラインを基本とする。始点は絶対的な最安値・最高値とは限らない。  
- 大ダウHL：一つの大きなターン中の最安値・最高値に置く。  
- 際への接近：価格が大ダウの際へ接近した場合は、反応・反転の可能性を重要警戒する。

【簡単に言うと】 大きな戦場の外枠と際を見るライン。接近時は反応を警戒するが、反転を保証しない。  
【主Source】 C01 `短期集中コース 1回目.pdf`  
【Stage】 Primary: Environment / Secondary: Observation, Phase  
【Observation依存】 NO201, NO202。Dow scale detectorは別途TBD。  
【未解決】 `LARGE_DOW_LINE_SELECTION_TBD`。複数の有効候補からの機械選択は未確定。  
【不採用】 最外側なら必ず採用、最古/最新、接触回数最大、最緩角度、ATR、値幅、足数等の未出典選択規則。  
【ユーザー判定】 OK / LINE_SELECTION_TBD  
【Status】 CONFIRMED_RULE / LINE_SELECTION_TBD

---

## R08｜小ダウのライン

【正式定義】  
小ダウラインは、一つの局面内の細かな構造を捉えるために使用する。近い対称関係や値動きのクラスターに着目して選ぶ。小ダウBRを確認するために使用する場合が多い。大ダウ・中ダウが担う広いフィールド認識の代用にはしない。

【簡単に言うと】 局面内部の近い構造を見るライン。BRには使うがEntryそのものは定義しない。  
【主Source】 C01 `短期集中コース 1回目.pdf`  
【Stage】 Primary: Setup / Secondary: Environment, Observation  
【Observation依存】 NO201, NO202, NO203との関係あり得る。  
【未解決】 `SMALL_DOW_LINE_SELECTION_TBD`。「近い」の距離、クラスター本数、反応回数等は未定義。  
【ユーザー承認差分】 Entry表現を正式定義から削除。BRは用途であり小ダウラインの定義そのものではない。  
【ユーザー判定】 OK / Entry削除 / Selection TBD  
【Status】 CONFIRMED_RULE / LINE_SELECTION_TBD

---

## R09｜トレンドラインゾーン

【正式定義】  
トレンドラインは一本の線だけでなくゾーンとして扱う。

- 基本形：始点ローソク足のヒゲから実体までをゾーンとする。  
- 応用形1：チャネルライン側のゾーンから逆輸入する方法がある。  
- 応用形2：上昇TLは一段上、下降TLは一段下のローソク足実体まで広げる方法がある。

過去または途中で価格反応が確認できる場合、そのライン／ゾーンが市場で意識されている可能性を補強する材料とし、信頼度を高める要素として扱う。反応履歴は必須条件でも正解保証でもない。

【主Source】 S04 `07 トレンドラインゾーンの取り方.txt`  
【Stage】 Primary: Observation / Secondary: Environment  
【Observation依存】 NO202。TL Zoneは将来のObservation候補だが新IDは作らない。  
【ユーザー承認差分】 β版の「基本形優先・応用は反応履歴と理由がある場合だけ」という独自制御文を正式定義から削除。反応履歴は `confidence reinforcement` として追加。  
【未解決】 `TL_ZONE_APPLICATION_SELECTION_TBD`。どの状況で応用形を選ぶか、反応回数・pips幅・スコア等は未定義。  
【ユーザー判定】 OK / β独自制御削除 / 反応履歴追加 / Selection TBD  
【Status】 CONFIRMED_RULE / APPLICATION_SELECTION_TBD

---

## R10｜フィールドとアクションを分ける

【正式定義】  
- Field：際から際までの戦場を「面」として捉える。大・中・小ダウの構造に応じ、ラインや際によって相場を複数のField / Areaとして捉える。  
- Action：そのFieldや際で発生する値動き、および買い手・売り手の力関係の変化を捉える。  
- Field内部：ラインや際の付近ではActionや反応を確認し、ライン間の内部値動きは必要に応じてより細かな構造で確認する。

【簡単に言うと】 Fieldは「どこが戦場か」、Actionは「そこで何が変わったか」。  
【主Source】 C02 `短期集中コース 2回目.pdf` + user clarification  
【Stage】 Primary: Environment / Secondary: Setup, Trigger  
【時間足】 必ず下位足へ落とすとはしない。Dow Scaleと時間足を固定マッピングしない。  
【未解決】 `FIELD_REPRESENTATION_TBD`。独立ObservationかEnvironment出力かは後続Governance。  
【責務境界】 BR成立、Return成立、Entry、SL、TP、発注は後続。  
【ユーザー判定】 OK / エリア分け・細部構造への引継ぎ追加  
【Status】 CONFIRMED

---

## 2. NS1 / Observationへの影響

- R06-R08はNO201/NO202/NO203との関係を持つが、本工程ではこれらをFIXEDへ昇格しない。
- R09のTL Zone、R10のField/Actionについて新Observation IDは追加しない。
- NS1 Observation status変更はOBSERVATION_GOVERNANCEに従う別工程とする。

## 3. Stop condition

R01-R10のユーザーレビュー結果は上記状態で固定。R07/R08のline selection、R09のapplication selection、R10のField representationは実装上TBDとして分離する。R11以降およびNS2-Bには進まない。
