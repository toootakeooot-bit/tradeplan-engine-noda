# NS2-A User Review R01-R10

Status: **R01-R03 CONFIRMED / R04-R10 USER REVIEW REQUIRED**

このファイルはNS2-Aのユーザー確認記録です。R01-R03はNS2-A1でユーザー確認結果を反映済みです。R04-R10は引き続き `未確認` であり、`CONFIRMED` ではありません。

## 1. 一覧レビュー

| Rule | 簡単に言うと | 主Source | Stage | Observation依存 | 画像確認 | 不明点 | ユーザー判定 |
|---|---|---|---|---|---|---|---|
| R01 | まず高値・安値を読む。そこが全分析の土台。 | S01 / C01 | Environment (CONFIRMED) | NO101/NO102 | OPTIONAL | 重要高安の厳密な検出規則 | OK |
| R02 | 高値と安値が両方切り上がれば上昇、両方切り下がれば下降。それ以外は上昇でも下降でもない。 | S01 | Environment (CONFIRMED) | NO101/NO102 | OPTIONAL | 重要高安の厳密な選択アルゴリズム | OK / 修正反映済み |
| R03 | N字が1つ形成された後、上昇側はその区間の最安値、下降側は最高値をターン起点として遡って確定する。 | C01 / S01 + user-confirmed clarification | Environment (CONFIRMED) | NO101/NO102、NO103はRELATIONSHIP_TBD | Rule定義は確認済み / Detector検証は後続 | N_PATTERN_DETECTION_TBD、Swingとの関係 | OK / 修正反映済み |
| R04 | 大・中・小ダウは見る目的・波の尺度を分ける。 | C01 / C02 | Environment | 新Observation候補あり | REQUIRED | 尺度境界、時間足との関係 | 未確認 |
| R05 | ラインは未来予測のためでなく、買い手・売り手と戦場を可視化するために選ぶ。 | S03 | Environment | TBD | OPTIONAL | 実装上の選択基準 | 未確認 |
| R06 | HL/TL/CHには基本の引き方がある。 | S03 / S06 | Observation | NO201/NO202/NO203 | REQUIRED | 複数候補時の選択優先 | 未確認 |
| R07 | 大ダウラインは広いフィールドと際を見るための線。 | C01 | Environment | NO201/NO202 + 尺度TBD | REQUIRED | TL始点の具体選択 | 未確認 |
| R08 | 小ダウラインは局面内のBRやEntryアクションを見るための線。 | C01 | Setup | NO201/NO202/NO203 + 尺度TBD | REQUIRED | 大/中との境界 | 未確認 |
| R09 | TLは線一本でなくゾーンとして扱い、基本形と応用形がある。 | S04 | Observation | NO202 + TL Zone候補 | REQUIRED | β版制御文と教材表現の関係 | 未確認 |
| R10 | フィールドは戦場の面、アクションはそこで起きる変化。 | C02 | Environment | TBD | RECOMMENDED | FieldをObservation化するか | 未確認 |

---

## R01｜高値・安値が土台

【正式定義】  
トレンド判断、ライン選択、トレードプランは、高値・安値の読み取りを土台にする。

【簡単に言うと】  
まず高値と安値を見る。そこが野田式分析の出発点。

【AIはこう理解している】  
野田式の環境認識を開始する前提ルール。高値・安値そのものの厳密な選び方は別途定義が必要。

【主Source】 S01 `04 トレンドの判断方法.txt`  
【補助Source】 C01 `短期集中コース 1回目.pdf`  
【Stage】 Primary: Environment (CONFIRMED)  
【Observation依存】 NO101, NO102  
【画像確認】 Rule Definitionの確定には不要。将来の検出・回帰例では使用可能。  
【不明点】 どのRaw High/Lowを「読むべき高値・安値」と採用するかの厳密なDetector。  
【Source Conflict】 なし  
【ユーザー判定】 OK

【ユーザー承認済み差分】  
現行基準Rule Ledgerの「インジケーターを先に見て方向を決めない」は今回の正式定義から除外する。補助ルール、注記、OPEN ISSUE等としても残さない。変更理由=`USER_REVIEW_APPROVED_CLARIFICATION`。

---

## R02｜トレンドの定義

【正式定義】  
- 上昇トレンド：高値と安値がともに切り上がって推移する。  
- 下降トレンド：高値と安値がともに切り下がって推移する。  
- それ以外：上昇トレンドでも下降トレンドでもない。

`NOT_UP_OR_DOWN` は新しいトレンド種類ではなく、上昇・下降のどちらの条件にも該当しない否定状態としてのみ扱う。

【簡単に言うと】  
高値・安値が両方上なら上昇、両方下なら下降。それ以外を勝手にレンジや横ばいへ分類しない。

【AIはこう理解している】  
トレンド定義は上昇・下降の2種類。判定出力は必要に応じ `UPTREND / DOWNTREND / NOT_UP_OR_DOWN` の3状態を表現できる。

【主Source】 S01 `04 トレンドの判断方法.txt`  
【補助Source】 なし  
【Stage】 Primary: Environment (CONFIRMED)  
【Observation依存】 NO101, NO102  
【画像確認】 Rule Definitionの確定には不要。将来の回帰テスト例として使用可能。  
【不明点】 NO101/NO102の厳密な選択アルゴリズム。  
【Source Conflict】 なし  
【ユーザー判定】 OK / 修正反映済み

【ユーザー承認済み差分】  
現行基準Rule Ledgerの「方向未確定、レンジ、またはターン変化候補」という自動分類は採用しない。変更理由=`USER_REVIEW_APPROVED_CLARIFICATION`。

---

## R03｜ターンの区切り

【正式定義】  
- 上昇側：N字が1つ形成された後に、そのN字を形成する区間の最安値が確定し、その最安値をターンの起点として遡って確定する。  
- 下降側：N字が1つ形成された後に、そのN字を形成する区間の最高値が確定し、その最高値をターンの起点として遡って確定する。

ターン起点は高値・安値候補が出現した瞬間に即時確定するのではなく、N字形成後に `candidate` から `confirmed turn origin` へ遡及確定する。

【簡単に言うと】  
N字が1つできてから、そのN字の始まりとなる極値を後からターン起点として確定する。上昇側は最安値、下降側は最高値。

【AIはこう理解している】  
後続の大中小ダウ、ライン、局面が利用するEnvironmentの構造認識ルール。Ruleの意味は確認済みだが、OHLCからN字完成を機械判定するDetectorはまだ定義しない。

【主Source】 C01 / S01（ターン概念・大小ターンの文脈）  
【ユーザー確認】 N字形成後の遡及起点確定を `USER_REVIEW_APPROVED_CLARIFICATION` として反映。既存SourceがこのN字文言を直接記載しているとは扱わない。  
【Stage】 Primary: Environment (CONFIRMED)  
【Observation依存】 NO101, NO102。NO103 Swingとの関係は `RELATIONSHIP_TBD`。  
【画像確認】 Rule DefinitionはCONFIRMED。Visual Detector verificationは後続工程。  
【不明点】 `N_PATTERN_DETECTION_TBD`。SwingとTurnの関係。  
【Source Conflict】 なし  
【ユーザー判定】 OK / 修正反映済み

【不採用】  
左ターンの最後の戻り高値/押し安値抜け条件、および38%戻し条件は今回の体系へ一切登録しない。

---

## R04｜大・中・小ダウを目的で分ける

【正式定義】  
大ダウは広範囲のフィールドと際、中ダウは大ダウトレンド中の途中フィールド、小ダウは局面内のアクション・BR・Entry候補を捉えるために使い分ける。

【簡単に言うと】  
大は全体、小は実際のアクション、中はその途中を見る。細かく見ただけでは大ダウ分析の代わりにならない。

【AIはこう理解している】  
波を単なる時間足で分けるのではなく、分析目的と構造スケールで使い分けるEnvironmentルール。

【主Source】 C01 / C02  
【Stage候補】 Primary: Environment / Secondary: Phase / Setup  
【Observation依存】 既存IDでは確定せず。Turn/Dow scaleをObservation候補として記録。  
【画像確認】 REQUIRED  
【不明点】 大・中・小の具体的な境界、時間足との対応。  
【Source Conflict】 なし  
【ユーザー判定】 未確認

---

## R05｜ラインは「引けた」ではなく「目的で選ぶ」

【正式定義】  
ラインの第一目的は、買い手と売り手の意識と現在のフィールドを視覚化すること。無目的にラインを増やさず、意図して選択する。

【簡単に言うと】  
引ける線を全部引くのではなく、今の戦場を理解するために必要な線を選ぶ。

【AIはこう理解している】  
ライン検出の幾何学ルールではなく、Environmentでラインを選ぶ目的・優先思想を規定するルール。

【主Source】 S03 `06 ラインの種類、引き方.txt`  
【Stage候補】 Primary: Environment / Secondary: Observation  
【Observation依存】 TBD  
【画像確認】 OPTIONAL  
【不明点】 自動化時に「選ぶ」をどう規則化するかは未定義。  
【Source Conflict】 なし  
【ユーザー判定】 未確認

---

## R06｜基本ライン

【正式定義】  
HLは価格が反転している高値・安値に水平に引く。上昇TLは切り上げた2点の安値、下降TLは切り下げた2点の高値で引く。CHはTLと平行で、上昇時は直近高値、下降時は直近安値に合わせる。

【簡単に言うと】  
HL/TL/CHには基本の置き方がある。特にTLは高値2点・安値2点を逆にしない。

【AIはこう理解している】  
NS1のNO201/NO202/NO203を正式化する主要Source候補。

【主Source】 S03  
【補助Source】 S06（ファイル確認済み、詳細LocatorはTBD）  
【Stage候補】 Primary: Observation / Secondary: Environment  
【Observation依存】 NO201, NO202, NO203  
【画像確認】 REQUIRED  
【不明点】 複数の候補点がある場合の選択優先順位。  
【Source Conflict】 なし  
【ユーザー判定】 未確認

---

## R07｜大ダウのライン

【正式定義】  
大ダウTLは選択時点で一度も抜かれていない線を基本とし、始点が絶対的な最安値・最高値とは限らない。大ダウHLは一つの大きなターン中の最安値・最高値。用途は広範囲のフィールドと際を捉えること。

【簡単に言うと】  
大ダウラインは大きな戦場と際を見るための線。細かいEntry線とは役割が違う。

【AIはこう理解している】  
Environmentで上位の戦場を定義する重要ルール。

【主Source】 C01 p.16付近  
【Stage候補】 Primary: Environment / Secondary: Observation / Phase  
【Observation依存】 NO201, NO202。大ダウ尺度はTBD。  
【画像確認】 REQUIRED  
【不明点】 最安値・最高値以外を始点にできる具体的条件。  
【Source Conflict】 なし  
【ユーザー判定】 未確認

---

## R08｜小ダウのライン

【正式定義】  
小ダウラインは一つの局面内で引き、近い対称関係や値動きのクラスターに着目する。主用途は小ダウBRやEntryアクションで、全体フィールドの代用にはしない。

【簡単に言うと】  
小ダウラインは大局を見る線ではなく、局面内のBRやEntry候補を見るための近距離の線。

【AIはこう理解している】  
Environmentで認識した構造からSetup候補へ橋渡しするライン。

【主Source】 C01 p.17付近  
【Stage候補】 Primary: Setup / Secondary: Environment / Observation  
【Observation依存】 NO201/NO202/NO203。小ダウ尺度はTBD。  
【画像確認】 REQUIRED  
【不明点】 大ダウ・中ダウとの境界と、クラスター選択の具体性。  
【Source Conflict】 なし  
【ユーザー判定】 未確認

---

## R09｜トレンドラインゾーン

【正式定義】  
S04では、基本形を始点ローソク足のヒゲから実体までとし、CH側ゾーンからの逆輸入、上昇TLでは一段上・下降TLでは一段下のローソク足実体までという応用系も説明している。

【簡単に言うと】  
TLは一本の価格線としてだけでなく幅のあるゾーンとして見る。最初は始点のヒゲ～実体が基本。

【AIはこう理解している】  
TLそのもの(NO202)に付随する空間的な観測表現。将来TL Zoneを別Observationにするか検討が必要。

【主Source】 S04 `07 トレンドラインゾーンの取り方.txt`  
【Stage候補】 Primary: Observation / Secondary: Environment  
【Observation依存】 NO202 + TL Zone候補  
【画像確認】 REQUIRED  
【不明点】 現行台帳の「β版通常判断は基本形優先」という運用文と、教材の練習推奨表現の関係。  
【Source Conflict】 なし（ただし運用表現の整理は必要）  
【ユーザー判定】 未確認

---

## R10｜フィールドとアクションを分ける

【正式定義】  
フィールドは戦場の際から際までの面を捉える視点、アクションは買いと売りの力関係の変化やフィールドの抜き差しを捉える視点として分ける。

【簡単に言うと】  
フィールドは「どこが戦場か」、アクションは「そこで何が変わったか」。

【AIはこう理解している】  
Environmentの面の認識と、その後のSetup/Triggerとなる変化を混同しないための境界ルール。

【主Source】 C02 p.14付近  
【Stage候補】 Primary: Environment / Secondary: Setup / Trigger  
【Observation依存】 TBD  
【画像確認】 RECOMMENDED  
【不明点】 FieldをObservation層にするか、Environment出力として持つか。  
【Source Conflict】 なし  
【ユーザー判定】 未確認

---

## 2. レビュー推奨順

R01-R03はNS2-A1で確認済み。次はユーザー指示後に `R04-R06`、その後 `R07-R10` の順で確認する。R04/R06/R07/R08/R09は画像確認を行うまで最終確定しない。