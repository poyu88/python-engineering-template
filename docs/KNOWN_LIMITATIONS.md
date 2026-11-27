# Known Limitations

本檔記錄母版**已知限制**。不得將限制隱藏為已完成能力。

| 限制 | 說明 | 相關 |
|---|---|---|
| 無正式自訂 Quality Gate／Overall 聚合器 | **1.1.0-template 候選**仍**不**提供工程 Overall PASS 聚合器；正式驗收用成熟工具逐項執行。ENG-001～ENG-004 維持 **DEFERRED／REMOVED FROM RELEASE SCOPE**，不得重啟實作 | ENG-001～004；F-01～F-04 |
| 無通用業務驗證框架 | 僅有示範 `demo_validate`；各專案自建契約 | ENG-009 |
| 無完整自動 Anti-gaming | 主要靠 Integrity（POLICY）、成熟工具、Independent CR | ENG-009 |
| Coverage 範圍 | 強制 branch＋80% 僅針對 `src/app`；**不**覆蓋 hooks 全部執行路徑 | F-05；ENG-005 |
| Cursor Hooks | **L3 EXPERIMENTAL／ADVISORY**；可 fail-open；非正式安全唯一依據；不宣稱完整路徑／symlink 防護 | F-07, F-08；ENG-007 |
| Hooks 驗證範圍 | CLI stdin／stdout 契約已獨立驗證；**Cursor IDE runtime = NOT_RUN**；新專案須先 `uv sync`；不需要時可由 Owner 停用 hooks | F-09；ENG-008 |
| Hooks 驗證未完成部分 | `main`／部分邊界、symlink、realpath、`..` 正規化等仍不足 | F-05（hooks 部分）、F-07、F-08 — **非**因移出 gate 而 FIXED |
| Remote CI | 尚未對遠端 Actions 實跑 | 歷史用語 **NOT_RUN**；工程驗收層歸 **PENDING**（`VERIFICATION_PENDING` VP-001） |
| Python 版本 | 僅驗證 **3.11** | py-env |
| Mutation framework | 未安裝；in-repo 說明性測試 ≠ mutation | F-06；ENG-006 |
| Phase 3 CR | 結論 **FAIL**；報告與證據不得改寫為 PASS | Evidence ID：`EV-P3-CR-FAIL`（私人稽核） |
| 歷史執行 Log | 母版不附帶上一輪 Self-check／Hook 原始 Log；新專案不得繼承母版 PASS 作自身驗收 | Release Hygiene；`EV-SR-SELFCHECK-LOGS`／`EV-F09-CLI-LOGS` |
| Manifest `overall` | 欄位保留且 **DEPRECATED**；不得作工程驗收聚合 | VP-002；ENG-004 |

> **對照（1.1.0-template）**：上表「NOT_RUN」等為**歷史／證據用語**，予以保留不抹除。工程驗收層對未完成項使用 `PENDING`（見 `AGENT_INTEGRITY.md`）。Hooks 列中的 Cursor runtime **NOT_RUN** 同此對照（VP-003）。既有 **FAIL** 不得改寫。

## 成熟度分級（摘要）

| Level | 名稱 | 本版 |
|---|---|---|
| L1 | ENFORCED | Ruff／format／Mypy／pytest／cov；CI YAML（遠端執行仍為歷史 NOT_RUN／工程 PENDING） |
| L2 | POLICY | TDD、PRD／SPEC、Commit、Integrity 四態、Pending 登記、UAT／CR、權限、風險隔離 |
| L3 | EXPERIMENTAL | Sensitive hooks（輔助；原生 detection_status 非工程四態） |
| L4 | DEFERRED | 自訂 gate、狀態聚合、自動 anti-gaming、mutation framework |
