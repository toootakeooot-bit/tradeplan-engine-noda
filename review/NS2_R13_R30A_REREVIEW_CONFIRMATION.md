# NS2 R13 / R30-A Re-review Confirmation

Status: **USER RE-REVIEW COMPLETE**

Repository: `toootakeooot-bit/tradeplan-engine-noda`

Branch: `feature/noda-v1`

Start HEAD: `7d2135ed32985af2f8ee6616483f6e9a9a246009`

## 1. Review reason

R13 and R30-A were reopened before NS2 closeout because the previous records left MA's semantic role as `MAIN_PHASE_MA_ROLE_TBD` and did not fully reflect the user's confirmed NODA usage.

The re-review also clarified how Fibonacci Expansion and CH / Field scale changes relate to main-phase recognition.

## 2. User judgment

### R13

User judgment: **OK / 修正内容を確定**

Accepted points:
- 本格局面は単一条件ではなく複数の確認方法を重ねて信頼性を上げる;
- 大ダウの際 -> 最後の押し安値 / 戻し高値Break is one structural confirmation path;
- MA direction is a formal main-phase confirmation path;
- Fibonacci / Field scale is an additional confirmation path;
- CH Break, not a Fibonacci percentage alone, is the structural cue for possible movement into a wider Field;
- `200% / 261.8%` do not automatically force a timeframe / scale switch;
- detailed Formation recognition remains owned by R28 / R29.

### R30-A

User judgment: **OK / 修正内容を確定**

Accepted points:
- MA is used for main-phase judgment in current NODA Core;
- middle-term MA group = `21 / 40 / 62 EMA`;
- long-term MA = `200 SMA`;
- bullish main-phase judgment uses both groups upward; bearish uses both downward;
- MA is not used as a decision element for early phase / final phase in the current user-approved operating definition;
- exact MA period values are reference values and are not treated as the semantic essence of the rule;
- no additional MA role is created elsewhere.

## 3. Source-confirmed evidence

Primary Source: C03 `短期集中コース 3回目.pdf`.

Verified:
- p.4 main-phase workflow;
- p.5 large-Dow edge + last push-low / return-high Break;
- p.6 middle-term MA group and long-term MA in main-phase judgment;
- p.7 Formation context;
- pp.16-17 Fibonacci Expansion continuation levels and small-Dow / large-Dow scale usage.

Source confirms:
- use of MA in main-phase judgment;
- 21 / 40 / 62 EMA and 200 SMA;
- middle-term MA direction as small-Dow direction context;
- long-term MA direction as large-Dow direction context;
- all-up / all-down directional examples for main phase;
- Fibonacci Expansion as a trend-continuation level tool with 100 / 161.8 / 200 / 261.8 reference levels.

## 4. User-approved clarification boundary

The following are intentionally recorded as `USER_APPROVED_CLARIFICATION`, not as teacher-source wording:
- main-phase confirmation should combine multiple methods to increase confidence;
- current NODA Core does not use MA as a judgment element in early / final phase;
- MA period values are not treated as semantically strict / essential;
- `100%～161.8%` is used as a practical current-Field main-phase volume reference;
- CH Break is the structural cue to question the current Field scale and re-observe the wider Dow / higher timeframe.

These clarifications do not authorize an invented machine detector.

## 5. Detector state

Still unresolved:
- `PHASE_DETECTION_TBD`;
- `MA_DIRECTION_DETECTION_TBD`;
- `FIELD_TRANSITION_DETECTION_TBD`.

No pips, candle count, fixed slope, MA order, MA cross, perfect order, ATR, ML, or score rule has been added.

## 6. Supersession

For current NS2 interpretation, `spec/NS2_R13_R30A_REREVIEW.md` supersedes only the R13 / R30-A semantic portions of earlier NS2-B / NS2-C review records.

Historical files remain valid as audit history but are not the latest semantic authority for R13 / R30-A.

## 7. Result

- R13: `CONFIRMED_RULE / PHASE_DETECTION_TBD / MA_DIRECTION_DETECTION_TBD / FIELD_TRANSITION_DETECTION_TBD`
- R30-A: `CONFIRMED_CORE / MA_DIRECTION_DETECTION_TBD`
- R30-B: unchanged `OUT_OF_NODA_CORE / FUTURE_VALIDATION_CANDIDATE`

R13 and R30-A are ready for NS2 closeout disposition at rule-semantics level.
