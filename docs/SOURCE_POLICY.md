# NODA Source Policy

Status: **NS0 source-policy baseline**

Repository: `toootakeooot-bit/tradeplan-engine-noda`

## 1. Purpose

This policy governs how NODA-specific rules are sourced, classified, changed, and audited.

The primary objective is to preserve fidelity to authoritative NODA teaching material while preventing AI inference, TC logic, or generic technical-analysis conventions from silently becoming NODA rules.

## 2. Authoritative source principle

Future NODA rule definitions must be grounded in material explicitly attributable to the teacher / authoritative NODA source set.

Authoritative evidence takes precedence over:

- AI-generated interpretation;
- generic technical-analysis definitions;
- TC / TradingCursor behavior;
- convenience assumptions made for implementation;
- backtest-driven rule invention.

If authoritative evidence is absent or ambiguous, the rule must remain unresolved rather than being completed by inference.

## 3. Traceability requirement

Every future formal NODA rule should be traceable to its source.

At minimum, future rule records should be able to carry:

- rule ID;
- rule name;
- source reference;
- source excerpt location or equivalent locator;
- interpretation status;
- responsible stage such as Environment / Phase / Setup / Trigger / Entry / SL / TP / Wait-Invalidation;
- unresolved notes when applicable.

NS0 does not create or rewrite the R01–R37 ledger. This requirement governs later NS work.

## 4. Prohibited rule creation

The following are prohibited unless later supported by authoritative NODA evidence and explicitly approved through the rule-change process:

- adding a new trading rule because it seems technically reasonable;
- filling a missing NODA definition with common market-analysis practice;
- converting TC behavior into a NODA rule;
- using RSI, BB, MACD, or other generic indicators to complete a missing NODA rule merely because they are available;
- inferring a mandatory threshold, candle count, price distance, or timeframe that the source does not state;
- converting an example into a universal rule without evidence that it is universal;
- optimizing a rule solely to improve historical performance.

## 5. TC separation policy

TC / TradingCursor may be used as a separate engine or future comparison target, but its internal strategy logic is not source evidence for NODA.

Therefore:

- TC output must not be treated as teacher evidence;
- TC concepts must not fill NODA `TBD` fields;
- NODA concepts must not be injected into TC to force agreement;
- future `compare` mode must preserve independent results;
- disagreement between TC and NODA must be recorded as a difference, not automatically reconciled.

## 6. Generic technical-analysis separation

Generic technical-analysis knowledge may be useful as background explanation, but it must not become a formal NODA rule unless the authoritative NODA source explicitly adopts it.

Where a familiar term such as high/low, trend, break, return, support, resistance, formation, or swing appears, the implementation must use the NODA-specific meaning when that meaning is defined.

Do not assume that a generic textbook definition is equivalent to the NODA definition.

## 7. Market fact vs interpretation policy

Raw supplied market records and NODA interpretation must remain separate.

Examples of raw facts:

- OHLC values;
- timestamp;
- symbol;
- timeframe;
- current price;
- candle-series records.

Examples of NODA interpretation candidates:

- significant high / low selection;
- swing recognition;
- HL / TL / CH;
- 大ダウ / 小ダウ;
- Field;
- 際;
- Phase;
- BR;
- formation;
- Break / Return;
- support/resistance conversion.

A raw candle High/Low must never be silently promoted into a NODA-significant high/low without an explicit NODA rule.

## 8. Uncertainty states

When a source is incomplete, contradictory, missing, or not yet reviewed, later work must use an explicit unresolved state rather than inventing certainty.

Permitted specification labels include:

- `TBD` — definition or ownership not yet fixed;
- `PROVISIONAL` — temporary structure subject to source confirmation;
- `UNKNOWN` — runtime or case-level judgment cannot be resolved from available rule evidence.

Exact runtime semantics may be refined in later NS work, but the principle of preserving uncertainty is fixed by NS0.

## 9. Rule-change discipline

Future changes to NODA rules should distinguish at least:

1. source correction — fixing transcription or source-reference error;
2. classification correction — moving a rule to the correct stage without altering meaning;
3. clarification — expressing the same sourced rule more precisely;
4. rule addition — adding newly confirmed teacher guidance;
5. rule deletion / retirement — removing a rule only with evidence and audit trail;
6. implementation correction — code changed to match an already-fixed rule, without changing the rule itself.

Performance improvement alone is not sufficient justification for changing a NODA rule.

## 10. R01–R37 handling principle

R01–R37 are treated as existing governed rule assets.

NS0 does not:

- rewrite them;
- renumber them;
- merge them;
- split them;
- delete them;
- add new semantics;
- remap them definitively.

Later NS work may classify them into the NODA internal stages only after source verification and with traceability preserved.

## 11. Audit requirement

Later NS milestones that alter rule definitions, mappings, or implementation must be auditable for:

- source traceability;
- no silent TC logic import;
- no generic-TA substitution;
- no unsupported new rule;
- no meaning drift from authoritative material;
- explicit treatment of unresolved items.

## 12. NS0 freeze

During NS0, the source policy itself is being established. No strategy logic is implemented and no R01–R37 meaning is changed.

Any uncertainty discovered during NS0 is carried forward as an `OPEN ISSUE` rather than resolved by inference.
