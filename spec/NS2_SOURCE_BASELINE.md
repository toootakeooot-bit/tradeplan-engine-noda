# NS2 Source Baseline

Status: **NS2-0 baseline**

Repository: `toootakeooot-bit/tradeplan-engine-noda`

Branch: `feature/noda-v1`

NS1 baseline HEAD: `0d23aec3b324f27acca6d8595ddbf883bd64fb15`

## 1. Purpose

NS2-0 fixes the source and review basis used by NS2-A and later rule-inventory work. It does not redefine, renumber, add, delete, split, merge, or implement R01-R37.

## 2. Current Rule Ledger

The current comparison baseline for R01-R37 is:

`02_野田式判断ルール台帳.md`

For NS2, the existing Rule ID, current rule text, and source labels in this ledger are preserved as the starting record. If later review finds a problem, record a difference candidate first; do not silently overwrite the baseline text.

## 3. Source Registry

The source registry is:

`01_資料優先順位・登録台帳.md`

Its Source IDs, source classes, evidence ranking, and use restrictions remain controlling. NS2-0 does not create a competing source hierarchy.

## 4. Primary source set

### Short Intensive Core

| Source ID | Registered role |
|---|---|
| C01 | 先行期、大・小ダウ、際、BR、意識の復活、中間TL |
| C02 | トレードプラン、SL、TP、RR、資金管理、フィールドとアクション |
| C03 | 本格局面、MA、フォーメーション、カウンターTL |
| C04 | 反転・継続フォーメーションと目標値 |

### Silver foundation rule material

| Source ID | Registered role |
|---|---|
| S01 | 高値・安値、上昇・下降トレンド、ターン |
| S02 | 先行期・本格局面・最終局面 |
| S03 | HL・TL・CH、サポート・レジスタンス、BR |
| S04 | トレンドラインゾーン |
| S05 | ラインブレイク後の高値・安値、ライン引き直し |
| S06 | リターンムーブ、TL BRとCH BR |
| S07 | 際、最終局面、小ダウTL、先行期Entry |

The primary NS2 source set is therefore `C01-C04 + S01-S07`.

S08-S12 are operating/learning materials and are not automatically promoted to primary trading-rule evidence. Personal cases, other-student cases, validation records, old control versions, and unregistered material remain restricted by the Source Registry.

## 5. Evidence priority

NS2 inherits the registered priority exactly:

`A0 -> A1 -> A2 -> B1 -> B2 -> C1 -> D1`

- A0: completed teacher-answer transcript with context/segment identifiable.
- A1: explicit Core PDF / Silver foundation text.
- A2: teacher screen annotation; drawing existence is evidence, intent is not inferred beyond support.
- B1/B2/C1/D1 retain the meanings defined in the Source Registry.

No NS2 work may reorder this priority for convenience.

## 6. Source conflict rule

If sources conflict, do not merge, average, vote, or choose by convenience. Record `SOURCE CONFLICT` containing:

- affected Rule ID;
- Source A and locator;
- Source B and locator;
- exact difference;
- whether priority resolves the conflict;
- why a decision is or is not possible;
- additional evidence needed;
- review status.

If text and a visual example appear inconsistent, use `IMAGE/TEXT CONFLICT` or an OPEN ISSUE until the authoritative context resolves it.

## 7. Media roles

### Text / transcript
Used to establish explicit rule meaning and source wording.

### Image / teacher annotation
Used to verify where an already sourced concept appears on a chart: high/low selection, turns, scale, HL/TL/CH placement, line endpoints, zone extent, field position, BR state, and similar visual relationships.

Images alone do not create general rules.

### Audio / video
Teacher statements may become evidence only when the statement, time/segment, and context are traceable. An AI impression of a video is not a teacher statement.

### Cases / historical AI outputs
Used only as application examples, boundary examples, counterexample candidates, or investigation leads. A single case cannot establish a general NODA rule.

## 8. Rule text freeze during NS2-0

NS2-0 makes no final Stage classification and no observation-definition confirmation. It does not implement high/low detection, Dow, line detection, Phase, Setup, Trigger, Entry, SL, or TP logic.

R01-R37 remain unchanged in meaning and numbering during NS2-0.

## 9. Relation to NS0 / NS1

`docs/SOURCE_POLICY.md`, `spec/RESPONSIBILITY.md`, and NS1 Market Facts / Observation governance remain controlling. In particular:

- raw Market Facts remain separate from NODA interpretation;
- TBD/PROVISIONAL states are preserved rather than guessed;
- TC logic and generic TA are not substitute source evidence;
- `trade-plan-a` and the TC Engine are outside NS2-0 modification scope.
