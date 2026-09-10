# NODA TradePlan Engine Responsibility

Status: **NS0 responsibility baseline**

Repository: `toootakeooot-bit/tradeplan-engine-noda`

Branch: `feature/noda-v1`

## 1. Formal name

The formal name of this component is:

**NODA TradePlan Engine**

NODA TradePlan Engine is an independent strategy-decision engine. It owns strategy-side interpretation and planning only. It does not own risk sizing, broker execution, position lifecycle management, scheduler behavior, or ticket tracking.

## 2. External responsibility boundary

To preserve future interchangeability with the TC TradePlan Engine, the external responsibility boundary is:

**Environment → Setup → Trigger → Entry → SL → TP → Wait / Invalidation**

The engine may return a valid no-entry / wait outcome.

The external contract is intentionally strategy-agnostic: TC and NODA may produce the same broad categories of decision output without sharing internal strategy logic.

## 3. NODA internal decision chain

NODA has one explicit internal stage not required of TC:

**Environment → Phase → Setup → Trigger → Entry → SL → TP → Wait / Invalidation**

`Phase` is a NODA-native internal responsibility. It may include, where supported by authoritative NODA sources in later work, concepts such as 先行局面・本格局面・最終局面・際.

`Phase` must not be imposed on TC, and TC output must not be normalized by injecting NODA Phase logic.

## 4. In scope

NODA TradePlan Engine is responsible for the following strategy-side categories.

### 4.1 Environment

- interpret supplied market data under NODA rules;
- derive NODA-specific market structure and context where supported by authoritative rules;
- hold future classifications such as 大ダウ / 小ダウ, trend, field, HL / TL / CH, or other NODA-native environment concepts.

### 4.2 Phase

- represent NODA-native phase classification;
- keep phase logic independent from TC;
- permit `UNKNOWN`, `PROVISIONAL`, or equivalent unresolved states when the governing rule is not yet fixed.

### 4.3 Setup

- determine whether a NODA setup candidate exists;
- represent future NODA-native concepts such as BR candidate, line, formation, trace/痕跡 where supported by authoritative sources.

### 4.4 Trigger

- represent the activation condition required before entry becomes valid;
- keep future NODA-native concepts such as Break, Return, and support/resistance conversion within NODA logic when formally sourced.

### 4.5 Entry

- determine strategy-side direction and entry condition / zone / level when supported;
- permit no-entry outcomes;
- stop at strategy planning and not perform actual order placement.

### 4.6 SL

- determine strategy-side stop location / condition / invalidation basis;
- not calculate lot or position size from the SL distance.

### 4.7 TP

- determine strategy-side take-profit candidate / condition / level;
- not perform broker-side close execution.

### 4.8 Wait / Invalidation

- explicitly represent wait / no-trade states;
- represent conditions that invalidate a current strategy plan;
- preserve unresolved states rather than inventing missing rules.

## 5. Market Facts vs NODA interpretation boundary

The distinction between supplied market facts and NODA interpretation is mandatory.

### 5.1 Common / Prepared Market Input side

The following are candidate supplied facts, subject to the later common input contract:

- OHLC candle values;
- timestamp;
- symbol;
- timeframe;
- current price;
- raw candle-series data.

These are observations or supplied market records. NS0 does not define the future common schema.

### 5.2 NODA interpretation side

The following are candidate NODA interpretations / derived strategy concepts and therefore belong inside NODA if and when authoritative rules support them:

- NODA-significant high / low recognition;
- swing recognition;
- HL / TL / CH;
- 大ダウ / 小ダウ;
- trend;
- field;
- 際;
- 先行局面 / 本格局面 / 最終局面;
- BR candidate;
- line;
- formation;
- 痕跡;
- Break / Return;
- support/resistance conversion;
- other NODA-native interpretations.

A candle's raw `High` / `Low` value is not the same responsibility as deciding that the price is a NODA-significant high / low.

Any item whose boundary or exact meaning is not yet confirmed must remain `PROVISIONAL` or `TBD`; NS0 must not settle it by inference.

## 6. Source-governed NODA logic

The repository may later contain and classify NODA-specific rules such as:

- R01–R37;
- 大ダウ / 小ダウ;
- HL / TL / CH;
- Field;
- 際;
- Phase;
- BR;
- formation;
- Break / Return;
- support/resistance conversion;
- Entry conditions;
- SL strategy conditions;
- TP strategy conditions;
- Wait / Invalidation.

NS0 does **not** add, delete, optimize, reinterpret, or implement any of these rules. Their meaning remains governed by authoritative source material and future NS work.

## 7. Explicit out-of-scope responsibilities

NODA TradePlan Engine must not perform or own:

- account balance management;
- monetary allowed-loss decision;
- risk-percent policy;
- lot calculation;
- position-size calculation;
- margin management;
- broker order creation or submission;
- order modification;
- close execution;
- open-position lifecycle management;
- ticket tracking;
- W8 responsibility;
- W9 responsibility;
- W10 Scheduler responsibility;
- MT4 operation;
- notification delivery.

Entry / SL / TP scope ends at strategy-side condition / price / level planning. Money sizing and execution are downstream responsibilities.

## 8. TC / NODA separation principle

TC and NODA are separate strategy engines.

They may later share:

- the same prepared market input conditions;
- a common external result contract / TradePlanState;
- common validation outside either strategy engine.

They must not share or blend internal strategy logic.

Specifically:

- no TC-native strategy rule may be imported into NODA merely to fill a gap;
- no NODA-native concept may be forced into TC;
- compare mode must compare independent outputs, not create a hybrid decision;
- differences between engine outputs are valid data and must not be auto-reconciled by strategy blending.

## 9. Future integration boundary

The intended future architecture is conceptual only in NS0:

```text
prepared market input
        ↓
Engine Adapter
        ├─ TC Engine
        └─ NODA Engine
        ↓
Common TradePlanState
        ↓
Validator / Risk / Sizing / Execution
```

Future selection modes may include:

- `engine = tc`
- `engine = noda`
- `engine = compare`

NS0 does not implement the Adapter, compare mode, or common schema.

## 10. Relationship to `trade-plan-a`

`toootakeooot-bit/trade-plan-a` is outside NS0 implementation scope.

NS0 must not modify:

- W8;
- W9;
- W10;
- W11;
- W12;
- existing production behavior;
- current W12 test conditions.

Future integration is documented conceptually only.

## 11. NS0 non-goals

NS0 does not:

- rewrite R01–R37;
- add or delete NODA rules;
- implement significant-high / low recognition;
- implement swing or Dow logic;
- implement Phase logic;
- implement BR logic;
- implement Entry / SL / TP algorithms;
- implement an Adapter;
- implement common schema;
- implement execution;
- modify the TC engine;
- modify `trade-plan-a`;
- evaluate or optimize trading performance.

## 12. Open issues carried forward

The following are intentionally unresolved and must be fixed in later NS work using authoritative source evidence:

1. exact formal definitions of NODA-significant high / low and swing recognition;
2. exact ownership and definitions of HL / TL / CH;
3. exact Environment / Phase boundary for 大ダウ / 小ダウ, Field, 際 and related concepts;
4. exact mapping of R01–R37 to the internal stages;
5. common prepared market input schema;
6. common TradePlanState / engine result schema;
7. exact semantics of `PROVISIONAL`, `TBD`, `UNKNOWN`, and future runtime states.

These open issues are not defects in NS0; resolving them here would exceed the responsibility-freeze scope.
