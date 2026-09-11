# NS2 R13 / R30-A Re-review — Superseding Definition

Status: **CONFIRMED AT RULE-SEMANTICS LEVEL — DETECTOR DETAILS REMAIN TBD**

Repository: `toootakeooot-bit/tradeplan-engine-noda`

Branch: `feature/noda-v1`

Start HEAD: `7d2135ed32985af2f8ee6616483f6e9a9a246009`

## 1. Purpose and precedence

This record captures the user re-review of R13 and R30-A and **supersedes only the R13 / R30-A semantic portions** of the earlier NS2-B / NS2-C review records.

Historical review and audit files remain unchanged for traceability.

Controlling boundaries remain:
- `docs/SOURCE_POLICY.md`;
- `spec/NS2_REVIEW_PROTOCOL.md`;
- NS0 responsibility boundaries;
- NS1 Observation Governance.

No detector, Entry, SL, TP, sizing, execution, TC logic, or generic-TA logic is implemented here.

## 2. Evidence classification

The following labels are used deliberately.

- `SOURCE_CONFIRMED`: directly supported by registered teacher Source.
- `USER_APPROVED_CLARIFICATION`: user-approved operating interpretation / scope clarification that is not promoted to teacher wording.
- `TBD`: exact machine-detection or representation remains unresolved.

Primary Source for both R13 and R30-A is C03 `短期集中コース 3回目.pdf`.

Verified C03 locations:
- p.4: main-phase workflow, including environment recognition and middle-term MA group;
- p.5: large-Dow edge + last push-low / return-high Break;
- p.6: 21 / 40 / 62 EMA, 200 SMA, and use in main-phase judgment;
- p.7: Formation in the main-phase workflow;
- pp.16-17: Fibonacci Expansion for trend-continuation levels using small-Dow / large-Dow N-wave scale.

## 3. R13 | 本格局面の確認

### 3.1 Core principle

`USER_APPROVED_CLARIFICATION`

本格局面は単一条件だけで確定させるのではなく、複数の確認方法を重ね、整合するほど判断の信頼性を高める。

R13 is therefore a **main-phase confirmation rule with multiple evidence paths**, not a single mandatory detector.

### 3.2 Method A — price-structure confirmation

`SOURCE_CONFIRMED`

大ダウの際へ到達した後、最後の押し安値または戻し高値のBreakを確認し、先行期を過ぎて本格局面へ移行した候補として捉える。

C03 p.5 directly supports this structural sequence.

Exact OHLC / candle / distance criteria remain `PHASE_DETECTION_TBD`.

### 3.3 Method B — MA-direction confirmation

`SOURCE_CONFIRMED`

本格局面かどうかの判断にMA条件を加える。

- 中期MA群: `21 / 40 / 62 EMA`;
- 長期MA: `200 SMA`;
- 中期MA群は小ダウ方向感を見る;
- 長期MAは大ダウ方向感を見る.

買い方向では中期MA群と長期MAがともに上向き、売り方向ではともに下向きであることを、本格局面判断の確認根拠として使用する。

C03 p.4 / p.6 supports all-up / all-down middle-term MA direction and the small-Dow / large-Dow directional-role distinction.

Exact mechanical definition of `上向き / 下向き` remains `MA_DIRECTION_DETECTION_TBD`.

The following are **not** added:
- MA perfect order / mandatory ordering;
- MA cross rule;
- numeric slope threshold;
- distance / divergence threshold;
- score.

### 3.4 Method C — Fibonacci / Field scale confirmation

#### Source-confirmed core

`SOURCE_CONFIRMED`

Fibonacci Expansion is used to observe trend-continuation levels.

- when measuring from a small-Dow N-wave, that wave ratio is treated as the 100% reference;
- for swing / larger-Dow analysis, the large-Dow N-wave ratio is the more appropriate scale;
- C03 shows continuation reference levels including `100% / 161.8% / 200% / 261.8%`.

#### User-approved field interpretation

`USER_APPROVED_CLARIFICATION`

- 現在観測しているField内では、基準波動100%に対する `100%～161.8%` 程度の続伸を、本格局面の値幅・ボリューム確認の一つとして使う;
- Fieldの切替は `200%到達` 等のFibonacci比率だけで機械的に決めない;
- 現在観測中のFieldのCHをBreakした場合、現在の尺度を超えて次の広いFieldへ移行した可能性を考え、上位のDow構造 / 上位足で再観測する;
- `200% / 261.8%` 等は、広いFieldへ移行した後も含む続伸水準として観測でき、これらの比率単独では上位足移行を確定しない.

The visual relationship was user-reviewed against C03 pp.16-17. Because chart geometry alone may not create an unstated universal detector, exact CH-Break / field-transition detection remains `FIELD_TRANSITION_DETECTION_TBD`.

### 3.5 Formation boundary

C03 p.7 shows Formation as part of the practical main-phase workflow and says Formation can make the situation easier to enter / read.

However, R13 does not own detailed Formation recognition or continuation / reversal classification.

- R28 owns Reversal Formation Setup semantics;
- R29 owns Continuation Formation Setup semantics.

Formation is therefore **not duplicated as an R13 mandatory gate**. R13 may reference R28 / R29 as downstream / adjacent evidence where relevant.

### 3.6 R13 final responsibility

R13 answers:

> `現在の値動きを本格局面と判断する根拠は何か`

using multiple source-backed / user-approved evidence paths while leaving exact detectors unresolved.

**Primary Stage**: `Phase`

**Secondary**: `Environment / Setup context`

**Status**:

`CONFIRMED_RULE / PHASE_DETECTION_TBD / MA_DIRECTION_DETECTION_TBD / FIELD_TRANSITION_DETECTION_TBD`

## 4. R30-A | MAの位置付け

### 4.1 Core use

`SOURCE_CONFIRMED`

野田式Coreにおいて、MAは本格局面判断に使用する。

C03 directly supports:
- main-phase judgment using the middle-term MA group;
- `21 / 40 / 62 EMA` as the middle-term group;
- `200 SMA` as the long-term MA;
- middle-term MA direction as small-Dow directional context;
- long-term MA direction as large-Dow directional context.

### 4.2 Directional agreement

`SOURCE_CONFIRMED`

- bullish main-phase confirmation: middle-term MA group and long-term MA are both upward;
- bearish main-phase confirmation: middle-term MA group and long-term MA are both downward.

The exact mechanical slope detector remains `MA_DIRECTION_DETECTION_TBD`.

### 4.3 Scope restriction

`USER_APPROVED_CLARIFICATION`

For the current NODA Core operating definition:
- MA is used as a **main-phase judgment element**;
- MA is **not used as a judgment element for the early phase or final phase**;
- MA is not given additional unrelated responsibilities elsewhere in NODA Core.

This is recorded as a user-approved scope restriction. C03 confirms main-phase use but does not by itself prove a universal teacher statement that MA is never observed outside that phase.

### 4.4 Parameter treatment

`USER_APPROVED_CLARIFICATION`

`21 / 40 / 62 EMA` and `200 SMA` are the current reference parameters, but the exact day-count values are not treated as the essential semantic core of the rule.

This clarification does **not** authorize automatic parameter optimization, alternate-MA search, scoring, or detector tuning.

### 4.5 Prohibitions

R30-A does not create:
- MA perfect order / mandatory ordering;
- MA cross Entry / Trigger;
- numeric slope threshold;
- MA divergence threshold;
- score;
- standalone Entry / SL / TP logic.

### 4.6 R13 / R30-A boundary

R13 owns:

> `本格局面をどの根拠で確認するか`

R30-A owns:

> `MAを野田式Coreのどこで、何のために使うか`

R30-A therefore defines MA scope / placement; R13 defines its concrete use within main-phase confirmation.

**RuleType**: `NODA_STRATEGY_CORE_AUXILIARY`

**Owner**: `Phase`

**Primary Stage**: `2-2 Phase`

**Secondary**: `2-1 Environment context only`

**Status**:

`CONFIRMED_CORE / MA_DIRECTION_DETECTION_TBD`

R30-B remains unchanged:

`OUT_OF_NODA_CORE / FUTURE_VALIDATION_CANDIDATE`

## 5. Superseded points

The following prior statements are superseded for current NS2 interpretation:

- R13: `MAIN_PHASE_MA_ROLE_TBD` as if MA's semantic role itself were still unknown;
- R13: treating Formation as the main unresolved R13 reinforcement responsibility;
- R30-A: placing MA broadly as an Environment-first auxiliary without the user-approved main-phase-only scope restriction;
- R30-A: retaining `MAIN_PHASE_MA_ROLE_TBD` after the role has been user-reviewed.

The detector remains TBD; the **semantic role no longer does**.

## 6. No implementation in NS2

This re-review does not implement:
- Phase detection;
- MA-direction detection;
- Field-transition detection;
- Fibonacci detector logic;
- Formation detection;
- Entry / SL / TP / sizing / execution.

Those remain downstream responsibilities.
