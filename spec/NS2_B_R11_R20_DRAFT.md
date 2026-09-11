# NS2-B R11-R20 Review / Confirmation Record

Status: **NS2-B RULE SEMANTICS COMPLETE — DETECTOR / SELECTION TBDs REMAIN**

Repository: `toootakeooot-bit/tradeplan-engine-noda`

Branch: `feature/noda-v1`

NS2-B start HEAD: `b92dac35b625f81f86c71bdab2265f15c49b1ef7`

NS2-B1 start HEAD: `00532261164dca16232c2357a2801ae6b97cd501`

NS2-B2 start HEAD: `1e46eabd19207ce583aa93fe334b77df58a60986`

Scope: **R11-R20 only**. R01-R10 remain confirmed in NS2-A1/A2/A3. R21+ and NS2-C are out of scope.

## 1. Review control

NS2-B follows `spec/NS2_REVIEW_PROTOCOL.md`:

`AI draft -> 日本語レビュー -> user OK/修正/保留 -> required source/image/original verification -> final整理 -> audit -> CONFIRMED or unresolved`

R14-R16 and R19 were confirmed in NS2-B1. R11-R13, R17-R18 and R20 are confirmed in NS2-B2 at rule-semantics level. Detector / selection details explicitly listed as TBD remain unresolved by design and do not invalidate the semantic confirmation.

## 2. Summary matrix

| Rule | Name | Primary Stage | Secondary Stage | Main dependency / unresolved | Image/source review | Status |
|---|---|---|---|---|---|---|
| R11 | 3つの局面 | Phase | Environment | `PHASE_DETECTION_TBD` | REQUIRED completed: S02 text + C01/C03 phase-context visuals | `CONFIRMED_RULE / PHASE_DETECTION_TBD` |
| R12 | 先行期を狙う前提 | Phase | Setup | `EDGE_PROXIMITY_TBD` | REQUIRED completed: S07 text + C01 edge/small-Dow visual context | `CONFIRMED_RULE / EDGE_PROXIMITY_TBD` |
| R13 | 本格局面の確認 | Phase | Setup | `MAIN_PHASE_MA_ROLE_TBD`; detector TBD | REQUIRED completed: C03 pp.5-10 | `CONFIRMED_CORE / MA_ROLE_TBD / DETECTION_TBD` |
| R14 | 小ダウBR | Trigger | Phase / Setup | `SMALL_DOW_BR_DETECTION_TBD` | REQUIRED completed in NS2-B1 | `CONFIRMED_RULE / DETECTION_TBD` |
| R15 | 意識の復活（小） | Trigger | Phase | `SMALL_AWARENESS_REVIVAL_DETECTION_TBD` | REQUIRED completed in NS2-B1 | `CONFIRMED_RULE / DETECTION_TBD` |
| R16 | 意識の復活（大） | Trigger | Phase / Environment | `SMALL_DOW_CYCLE_DETECTION_TBD`; line return TBD | REQUIRED completed in NS2-B1 | `CONFIRMED_RULE / DETECTION_TBD` |
| R17 | 中間TL / 中ダウカウンターTL | Environment | Observation / Setup | `LINE_SELECTION_TBD`; Break detector TBD | REQUIRED completed: C01 p.21 + C03 p.13 | `CONFIRMED_RULE / LINE_SELECTION_TBD` |
| R18 | ラインBreak後の構造更新 | Environment | Observation | `HIGH_LOW_DETECTION_TBD`; `LINE_SELECTION_TBD` | S05 original text verified; visual endpoint-selection remains deliberately unresolved | `CONFIRMED_RULE / HIGH_LOW_DETECTION_TBD / LINE_SELECTION_TBD` |
| R19 | Return Move | Observation | Downstream search context only | `RETURN_MOVE_DETECTION_TBD` | RECOMMENDED completed in NS2-B1 | `CONFIRMED_RULE / RETURN_DETECTION_TBD` |
| R20 | TL / CHの性質とBRの意味 | Environment | Observation / Trigger | `BR_DETECTION_TBD` | S06 text/original explanation verified | `CONFIRMED_RULE / BR_DETECTION_TBD` |

## 3. Source locator baseline

External baseline remains `02_野田式判断ルール台帳.md` β0.3-A限定運用版. This file records user-approved differences; it does not silently overwrite the external ledger.

| Rule | Primary source | Verified source / visual locator |
|---|---|---|
| R11 | S02 | `05 トレンドの3つの局面.txt`; C01/C03 practical phase context |
| R12 | S07 / C01 | S07 points 1-3; C01 edge and small-Dow BR visual context |
| R13 | C03 | C03 pp.5-10: structural break, MA group, formation, finer-structure examples |
| R14 | C01 / S07 | C01 p.18; S07 point 3 |
| R15 | C01 | C01 p.19 |
| R16 | C01 | C01 p.20 |
| R17 | C01 / C03 | C01 p.21 intermediate TL; C03 p.13 counter TL |
| R18 | S05 | `08 ラインをブレイクした時の対処法.txt`: post-break high/low, redraw, TL/CH and Field remap |
| R19 | S06 / S03 | S06 Return Move section; responsibility constrained by NS2-B1 user review |
| R20 | S06 | `10 ラインの引き方例.txt`: TL vs CH purpose; TL BR vs CH BR explanation |

## 4. R11 | 3つの局面

### Confirmed formal definition

トレンドは `先行期 / 本格局面 / 最終局面` の3局面として捉える。

- `先行期`: トレンドが形成され始める初期局面。
- `本格局面`: トレンドの力が強く進行する主要局面。
- `最終局面`: トレンド自体は継続しているが、値動きが軟化していく終盤局面。

野田式ではこの3局面の考え方を、大きい構造・小さい構造の両方に適用する。

### Clarification / guard

S02では本格局面を強いトレンドとして説明する一方、保ち合いを含めて本格局面中と判断する場合も明示している。したがって `本格局面 = 常に急角度` とは機械化しない。

`局面名称だけでEntryしない` はR11の局面定義そのものではなく、downstream Entry責務との operational guard として扱う。

固定時間足対応（例 `大ダウ=D1`, `小ダウ=H1`）は作らない。

**Primary Stage**: `Phase`

**Secondary**: `Environment`

**Detector status**: `PHASE_DETECTION_TBD`

**Unresolved**:
- OHLCによる局面境界の検出;
- Phase開始/終了の確定方法;
- 大小局面の重なり表現;
- nested Phase data representation.

**Status**: `CONFIRMED_RULE / PHASE_DETECTION_TBD`

**User judgment**: `OK / NS2-B2 instruction`

## 5. R12 | 先行期を狙う前提

### Confirmed formal definition

先行期を捉えるときは、まず広い構造の `際` を探す。その際付近で、現在の最終局面から次の先行期へ切り替わる小さな構造・Actionを確認する。

構造順序:

`広い構造の際 -> 現在の最終局面 -> 細かな構造 / Action -> 次の先行期候補`

教材の週足→日足等は実例であり、固定時間足Ruleにはしない。正式表現は `広い構造 / より細かな構造` とする。

S07の `際で勝負すると損切りしやすくなる` は、際を狙う合理性の説明として保持するが、R12でSL位置・SL計算を作らない。

**Primary Stage**: `Phase`

**Secondary**: `Setup`

**Relation**: R07 edge / R08 small-Dow line / R10 Field-Action / R14 small-Dow BR.

**Detector status**: `EDGE_PROXIMITY_TBD`

**Unresolved**:
- 際付近の距離;
- pips幅;
- Zoneとの関係;
- 接触/接近の境界;
- candle/time condition.

**Status**: `CONFIRMED_RULE / EDGE_PROXIMITY_TBD`

**User judgment**: `OK / NS2-B2 instruction`

## 6. R13 | 本格局面の確認

### Confirmed structural core

大ダウの際へ到達した後、本格局面入りを確認する際は、最後の押し安値または戻し高値のBreakを重要な構造確認として見る。

C03 p.5 visually and textually shows the large-Dow edge context and the last push-low / return-high Break as a central structural check.

### MA role

C03 shows:
- 中期MA群 `21 / 40 / 62 EMA`;
- 長期MA `200 SMA`.

Source explicitly says the middle-term MA conditions are added when judging whether the market is entering the main phase. This establishes relevance, but NS2-B2 does **not** decide the exact mandatory level.

`MAIN_PHASE_MA_ROLE_TBD`

No rule is created that all 21/40/62 must align, 200SMA must align, or MA cross confirms Phase.

### Formation

C03 says formation can make the situation easier to enter/read. Formation is treated as `reinforcement / easier-to-read context`, not a mandatory main-phase gate.

### Finer-structure check

C03 H4/H1 examples are retained as examples only. Formal wording: `必要に応じて、より細かな構造でActionを確認する`.

**Primary Stage**: `Phase`

**Secondary**: `Setup`

**Detector status**: `DETECTION_TBD`

**MA role**: `MAIN_PHASE_MA_ROLE_TBD`

**Status**: `CONFIRMED_CORE / MA_ROLE_TBD / DETECTION_TBD`

**User judgment**: `OK / NS2-B2 instruction`

## 7. R14 | 小ダウBR — NS2-B1 regression-protected

大ダウの際へ到達した後、最終局面内の小ダウTLまたはHLを用いてBreakとReturnを確認し、次の先行期へ切り替わるActionを捉える。

`大ダウの際 -> 最終局面 -> 小ダウTL/HL -> Break -> Return -> 次の先行期候補`

**Primary Stage**: `Trigger`

**Secondary**: `Phase / Setup`

**Detector**: `SMALL_DOW_BR_DETECTION_TBD`

**Status**: `CONFIRMED_RULE / DETECTION_TBD`

No semantic change in NS2-B2.

## 8. R15 | 意識の復活（小） — NS2-B1 regression-protected

本格局面または最終局面内で、反対トレンド方向へ引いた小ダウラインが一度Breakされた後、再びそのライン側へ戻るActionを、直前の小ダウターンの意識が復活する候補として捉える。

R15はR19 Return Moveとは別Ruleであり、単なるReturn現象ではない。

**Primary Stage**: `Trigger`

**Secondary**: `Phase`

**Detector**: `SMALL_AWARENESS_REVIVAL_DETECTION_TBD`

**Status**: `CONFIRMED_RULE / DETECTION_TBD`

No semantic change in NS2-B2.

## 9. R16 | 意識の復活（大） — NS2-B1 regression-protected

一度Breakされた大ダウラインに対し、再びメイントレンド方向へ戻るActionを意識の復活（大）の候補として捉える。小ダウの上げ・下げが一巡した後に、次の小ダウサイクルの起点となる動きを見る。

**Primary Stage**: `Trigger`

**Secondary**: `Phase / Environment`

**Detector**: `SMALL_DOW_CYCLE_DETECTION_TBD`; line-return detector TBD.

**Status**: `CONFIRMED_RULE / DETECTION_TBD`

No semantic change in NS2-B2.

## 10. R17 | 中間TL / 中ダウカウンターTL

NS2-B2 user clarification fixes these as **separate concepts**. They are not synonyms, aliases, or a fixed parent/child relation.

### R17-A 中間TL

**Source core**: C01 p.21 defines an intermediate TL drawn across turns and shows endpoint selection around the point before the large-Dow extreme; it also notes that start/end may be drawn at non-absolute extremes.

**User-approved clarification**:
- 長期・中期的な視点で、過去の値動きから引いてくるTL;
- 小ダウまたはより細かな構造でBRを確認するための基準ライン;
- 過去から継続して意識されている構造を利用するため、局所的な短期ラインより信頼性を高めたラインとして扱う;
- 短期から中期まで比較的広く使える;
- 特に先行期や相場変化の予兆を捉えたい場面で使いやすい.

`信頼性が高い` は定性的な `confidence characteristic` とし、点数・接触回数・pips・ATR・ML評価に変換しない。

### R17-B 中ダウカウンターTL

**Source core**: C03 p.13 defines counter TL as small/middle-Dow TL drawn opposite the large-Dow trend direction and explicitly shows middle-Dow counter TL spanning turns.

**User-approved clarification**:
- 小ダウ構造の中でターンを跨ぐ;
- 大きなトレンド方向に対して逆方向;
- 主に目先の値動きを確認する局所的・短期的用途;
- 小ダウまたはより細かな構造でBRを見るための基準ライン;
- 特に本格局面で利用しやすい.

### Relation

共通点は `小ダウ / 細かな構造でBRを見る基準`。役割は似るが、対象構造・利用期間・局面用途が異なる。

`中間TL = 中ダウカウンターTL` は禁止。

**Primary Stage**: `Environment`

**Secondary**: `Observation / Setup`

**Selection status**: `LINE_SELECTION_TBD`

**Unresolved**:
- 中間TLの正確な始点/終点選択;
- 遡及期間;
- confidenceの定量化は行わない;
- 中ダウカウンターTL候補優先順位;
- Break detector.

**Status**: `CONFIRMED_RULE / LINE_SELECTION_TBD`

**User judgment**: `OK / USER APPROVED CLARIFICATION`

## 11. R18 | ラインBreak後の構造更新

### Confirmed formal definition

ラインBreak後はEntry判断より先に、新たに形成される高値・安値を確認する。その高値・安値を使ってTLを引き直し、TL/CHおよび現在のFieldを再把握する。

### Source-grounded geometry

S05 directly states that after a line Break, the next high/low formation is checked and the new high/low is used as a new endpoint candidate to redraw TL. For an up TL, the new endpoint must remain above the start; for a down TL, the new endpoint must remain below the start. The redrawn TL/CH is then used to re-grasp the current Field.

`必ず新しい2点を選び直す` とはしない。Source example includes existing start + new endpoint.

### User-approved structural-priority clarification

Break後に形成された新しい高値・安値は、当該TL更新の文脈では `外側に形成された新しい構造点` として無視できず、それ以前の対応する高値・安値より構造上の優先度が上がる。

`Break -> new outer high/low -> higher structural priority -> TL/CH update -> Field remap`

This is recorded as user-approved clarification, not silently attributed to S05 wording.

### R19 separation

R19 Return Move is not an R18 update condition. `R19 -> TL redraw` dependency is prohibited.

**Primary Stage**: `Environment`

**Secondary**: `Observation`

**Detector status**: `HIGH_LOW_DETECTION_TBD`

**Selection status**: `LINE_SELECTION_TBD`

**Unresolved**:
- OHLC high/low confirmation;
- multiple high/low candidate selection;
- exact redraw timing;
- CH reset candidate selection.

**Status**: `CONFIRMED_RULE / HIGH_LOW_DETECTION_TBD / LINE_SELECTION_TBD`

**User judgment**: `OK / USER APPROVED CLARIFICATION`

## 12. R19 | Return Move — NS2-B1 regression-protected

Return MoveはTLをBreakした後、価格が旧TL側へ戻る観測現象。売買判断・Trigger・Entry・BR成立・意識の復活成立・TL更新の根拠にはしない。

R14/R15等の小ダウActionを後続で探索するための `OBSERVATION_CUE / SEARCH_CUE` に限る。

**Primary Stage**: `Observation`

**Secondary**: `Downstream search context only`

**Detector**: `RETURN_MOVE_DETECTION_TBD`

**Status**: `CONFIRMED_RULE / RETURN_DETECTION_TBD`

No semantic change in NS2-B2.

## 13. R20 | TL / CHの性質とBRの意味

R20 is confirmed as a structural-context rule, not a standalone Entry Trigger.

### R20-A TL property

**Source core**: S06 states that TL is commonly used as a new-entry reference.

**User-approved clarification**:
- TLは新規建て・参加判断の基準として意識されやすい;
- 参加者が具体的な価格水準を目標に参加判断を行うため、意識水準が比較的明確になりやすい;
- Zoneは比較的狭くなりやすい;
- この意味でラインの意味・力はCHより相対的に強い.

`強い` は数値スコアではなく、参加判断が比較的明確な水準へ集中しやすいという定性的性質。

### R20-A TL BR

S06 states that TL Break is associated with prior-trend participants beginning to withdraw, prior trend force weakening, and opposite force appearing more easily; it calls this a trend-change Action.

NS2-B2 retains this as `候補 / 構造解釈` only. `TL BR = trend reversal confirmed` is prohibited.

### R20-B CH property

**Source core**: S06 states that CH is commonly used as a profit-taking target.

**User-approved clarification**:
- CHは既存参加者の利確・撤退側の基準として意識されやすい;
- 撤退はCH到達前 / 到達時 / Break時 / Break後 / Return後など複数のタイミングがあり得る;
- 行動地点の自由度が高いためTLより意識が一点に集中しにくい;
- この意味でCHのラインとしての力はTLより相対的に弱い.

`弱い` は数値スコアではなく、利確・撤退判断が分散しやすいという定性的性質。

### R20-B CH BR

S06 states that CH Break favors existing same-direction participants and can invite new same-direction entries, describing continuation/acceleration Action. NS2-B2 retains this as candidate structural interpretation only.

`CH BR = continuation confirmed` is prohibited. TL BR and CH BR are not treated as equal-strength Entry Triggers.

### Responsibility

R20 reads line properties and structural meaning of Break. It does **not** independently establish:
- Entry;
- buy/sell decision confirmation;
- Phase confirmation;
- trend-reversal confirmation;
- trend-continuation confirmation.

**Primary Stage**: `Environment`

**Secondary**: `Observation / Trigger`

**Detector status**: `BR_DETECTION_TBD`

**Status**: `CONFIRMED_RULE / BR_DETECTION_TBD`

**User judgment**: `OK / USER APPROVED CLARIFICATION`

## 14. Required visual / source review result

### R11
S02 text directly verifies the three phases, application to both large/small trends, and that consolidation can still be inside the main phase. C01/C03 practical course visuals were checked only to confirm scale/phase context; no detector threshold was inferred.

### R12
S07 directly verifies `際 -> 最終局面 -> small-Dow line/action` and the rationale that edge trading facilitates stop placement. C01 edge / BR visuals support the location/scale relationship. Weekly/daily examples are not fixed mappings.

### R13
C03 pp.5-10 visual review completed:
- p.5: large-Dow edge + last push-low/return-high Break;
- p.6: 21/40/62 EMA and 200SMA context;
- p.7: formation as easier-to-enter/read context;
- pp.9-10: finer-structure examples.
No MA or timeframe threshold was invented.

### R17
C01 p.21 and C03 p.13 visual review completed. They verify that the source-defined intermediate TL and middle-Dow counter TL are not visually identical concepts. User-approved role differences are explicitly kept separate from source text.

### R18
S05 original text gives explicit post-Break geometry, endpoint replacement conditions and TL/CH/Field remapping. The registered source file contains no embedded static chart image; therefore no image-derived endpoint-selection rule is created. Exact high/low and line selection remain TBD. This disposition satisfies the review gate without pretending a missing visual establishes additional logic.

### R20
S06 original text directly states TL as new-entry reference and CH as profit-target reference, and separately describes TL-BR trend-change Action vs CH-BR continuation/acceleration Action. User-approved TL/CH strength interpretation is recorded as clarification, not silently attributed to S06.

## 15. NS2-B unresolved detector / selection list

- R11 `PHASE_DETECTION_TBD`
- R12 `EDGE_PROXIMITY_TBD`
- R13 `MAIN_PHASE_MA_ROLE_TBD`
- R13 structural detection TBD
- R14 `SMALL_DOW_BR_DETECTION_TBD`
- R15 `SMALL_AWARENESS_REVIVAL_DETECTION_TBD`
- R16 `SMALL_DOW_CYCLE_DETECTION_TBD`
- R16 line-return detector TBD
- R17 `LINE_SELECTION_TBD`
- R17 Break detector TBD
- R18 `HIGH_LOW_DETECTION_TBD`
- R18 `LINE_SELECTION_TBD`
- R19 `RETURN_MOVE_DETECTION_TBD`
- R20 `BR_DETECTION_TBD`

These TBDs are implementation/detection gaps and do not mean the reviewed rule semantics are unconfirmed.

## 16. Scope protection

NS2-B2 does not:
- alter R01-R10 semantics;
- alter R14-R16 or R19 semantics;
- process R21+;
- start NS2-C;
- create a new Observation ID;
- promote NO201/NO202/NO203 to FIXED;
- create generic-TA detector logic;
- fix D1/H4/H1/M15 mappings;
- add Entry/SL/TP/Lot/Position Size/execution implementation;
- modify TC or `trade-plan-a`.

## 17. NS2-B completion state

All R11-R20 rule semantics have passed their user-review/confirmation gate, with unresolved detector/selection items explicitly preserved.

**NS2-B: COMPLETE at rule-semantics level.**

Work stops before R21 / NS2-C.
