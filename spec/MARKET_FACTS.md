# NS1 Market Facts

Status: **NS1 baseline**

Repository: `toootakeooot-bit/tradeplan-engine-noda`

Branch: `feature/noda-v1`

## 1. Purpose

This document fixes the L0 **Common Market Facts** layer used as supplied market information before NODA-specific interpretation.

NS1 does not define trading logic, NODA environment logic, a common executable schema, or a detector implementation. The objective is to separate objective supplied records from NODA-derived interpretation.

## 2. Boundary rule

A Market Fact is a value or record supplied by the prepared market input without requiring NODA strategy interpretation.

A Market Fact is **not** promoted into a NODA Observation merely because a similar trading term exists.

Mandatory distinction:

- raw candle `High` / `Low` = Market Fact;
- deciding that a raw high / low is a NODA-significant high / low = NODA Observation;
- raw candle series = Market Fact;
- deciding that a pattern of candles forms a NODA Swing = NODA Observation.

## 3. L0 minimum set

| ID | Name | Status | Definition at NS1 | Source / authority | Determinism | Open issue |
|---|---|---|---|---|---|---|
| MF001 | OHLC | FIXED | Supplied candle Open, High, Low, Close values. No NODA significance is implied. | NS0 responsibility baseline / supplied market record semantics | Deterministic as supplied | None at conceptual level |
| MF002 | Timestamp | FIXED | Supplied timestamp associated with a market record or candle. | NS0 responsibility baseline | Deterministic as supplied | Exact timezone/normalization belongs to future input contract |
| MF003 | Symbol | FIXED | Supplied instrument identifier. | NS0 responsibility baseline | Deterministic as supplied | Broker alias normalization belongs to future input contract |
| MF004 | Timeframe | FIXED | Supplied timeframe identifier associated with market data. | NS0 responsibility baseline | Deterministic as supplied | Canonical encoding belongs to future input contract |
| MF005 | Current Price | PROVISIONAL | A supplied current-price field, without NS1 deciding whether it is Bid, Ask, Last, Mid, or another quote semantic. | NS0 candidate fact | Deterministic only after input contract fixes quote semantics | NS1-OI-007 |
| MF006 | Raw Candle Series | PROVISIONAL | Supplied ordered candle records containing raw market values. NS1 does not fix closed/open candle policy, ordering, completeness, or missing-data handling. | NS0 candidate fact | Deterministic only after input contract conventions are fixed | NS1-OI-008 |

## 4. OHLC semantics

`MF001` defines the conceptual raw OHLC record only.

NS1 does not define:

- candle aggregation rules;
- broker timezone;
- spread treatment;
- Bid/Ask construction;
- whether the current forming candle is included;
- gap filling;
- missing-bar repair;
- resampling;
- synthetic candles.

Those items belong to the future prepared-market-input contract and must not be silently inferred here.

## 5. What is not L0

The following are not declared Market Facts by NS1:

- NODA-significant High / Low;
- Swing;
- HL / TL / CH;
- 大ダウ / 小ダウ;
- Trend;
- Field;
- 際;
- Phase;
- BR;
- Formation;
- Break / Return;
- support/resistance conversion;
- Entry / SL / TP / Wait / Invalidation judgments.

These require NODA interpretation or later strategy stages.

## 6. Source policy

`docs/SOURCE_POLICY.md` remains controlling.

No generic technical-analysis convention, TradingCursor behavior, AI inference, or performance optimization may redefine an L0 item into a NODA strategy concept.

## 7. Reproducibility requirement

For FIXED L0 concepts, identical supplied records must preserve identical values.

For PROVISIONAL L0 concepts, reproducibility is conditional on the future input contract fixing the unresolved transport/quote semantics.

NS1 specifies this requirement only; no parser, normalizer, adapter, or execution code is introduced.

## 8. Change rule

New L0 facts may be added later only through `spec/OBSERVATION_GOVERNANCE.md`.

Adding a fact must not renumber existing IDs. Changing the meaning of an existing fact requires explicit audited change classification and cannot be disguised as an ADD.
