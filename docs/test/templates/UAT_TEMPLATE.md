# UAT Template

| 欄位 | 內容 |
|---|---|
| 主題 | |
| 日期 | |
| 執行者 | |
| 相關 PR／分支 | |
| 規格依據 | PRD／SPEC 章節 |

## 隔離路徑

| 類型 | 路徑 |
|---|---|
| 產出 | `output/uat_<主題>/` |
| 資料副本 | `data/uat/<主題>/` |
| 正式資料 | **未寫入**（確認） |

隔離程度依風險選擇（見 `docs/DEVELOPMENT_WORKFLOW.md` §2.10）：日常 TDD 不強制 Clone；正式／敏感／真實資料 UAT／Migration 須適當隔離。Worktree／Clone ≠ OS 沙箱。

## 檢查清單（工程驗收四態）

個別**工程驗收項目**結果僅使用：`PASS`｜`FAIL`｜`PENDING`｜`N/A`（定義見 `docs/AGENT_INTEGRITY.md`）。
缺規則／資料／環境／權限 → `PENDING`；規則明確且已驗證不符合 → `FAIL`。
並登記 `docs/VERIFICATION_PENDING.md`（若適用）。

| ID | 項目 | 結果 (PASS/FAIL/PENDING/N/A) | 證據 |
|---|---|---|---|
| U1 | | | |
| U2 | | | |

## 結論（UAT 業務裁決空間）

- **工程項目四態**與 **UAT 整體業務裁決**分開：
  - 工程項目：上表四態。
  - UAT 整體裁決：依**各專案既定契約**決定狀態集合與通過條件（**不**強制所有專案使用同一組裁決狀態）。
- UAT 整體裁決 **不得**當成通用工程 Overall PASS 聚合器。
- UAT 整體裁決 **不得**掩蓋未完成的工程驗證項目（有必要項為 `PENDING`／`FAIL` 時，不得宣稱全部驗收完成）。
- 示例裁決欄（可依專案契約調整，非強制枚舉）：`PASS`／`FAIL`／`PENDING`
- 備註：
