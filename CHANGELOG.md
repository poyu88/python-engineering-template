# Changelog

## 1.1.0-template — 2026-11-27／28（已 Merge；尚未 Tag／正式發布）

### 合併與 CI 結案（Stage C.6）

- PR [#1](https://github.com/poyu88/python-engineering-template/pull/1) 已 MERGED；Merge Commit `a86ba5d369b00fcb800a824e0975572864ee7e65`。
- 治理 Commit（PR head）`d71f302d17b2fae344084e8e859eb7422f4d5690`：PR CI run `46028699714` SUCCESS。
- master push CI run `46030784881` SUCCESS（驗證 Merge Commit `a86ba5d…`；**不得**套用至尚未建立的新 Commit）。
- VP-001 Remote CI → **PASS**；VP-002-D／VP-003 仍 **PENDING**。
- 文件規範版本維持 `1.1.0-template`；預定未來 Git Tag 為 **`v1.1.0`**（待 Owner 授權；指向結案合併後且該 SHA CI 通過之 Commit）。**尚未**打 Tag／正式發布。

### 治理內容（原候選說明，保留）

- 工程驗收狀態統一為四態：`PASS`｜`FAIL`｜`PENDING`｜`N/A`（見 `docs/AGENT_INTEGRITY.md`）。
- 新增 `docs/VERIFICATION_PENDING.md`：持久化待驗證事項與重驗條件。
- `DEVELOPMENT_WORKFLOW`：風險導向 Isolated Verification；權威表納入待驗證文件。
- Evidence Manifest：`checks[].status` 改四態說明；`overall` **DEPRECATED**（欄位保留；外部相容 VP-002-D 仍 PENDING）。
- 區分工具採用 `NOT_ADOPTED` 與驗收 `N/A`；禁止新建 Overall PASS 聚合器。
- 對齊 `AGENTS.md`、README、`.cursor/rules/dev-workflow-rule.mdc`、UAT 範本、KNOWN_LIMITATIONS 對照說明。
- **不**變更 CI／Lockfile／hooks 程式／品質門檻；Tag 仍待 Owner 授權。

## 1.0.0-template — 2026-11-27（Backup Consolidation）

- 新增 [`docs/BACKUP_AND_ARTIFACT_POLICY.md`](docs/BACKUP_AND_ARTIFACT_POLICY.md)；`AGENTS.md`／Workflow 精簡引用。
- 統一永久備份根與暫存根（本機路徑僅私人 INDEX）；禁止自建其他永久備份根。

## 1.0.0-template — 2026-11-27（Release Hygiene）

- Phase 3.1 Independent Re-review：**PASS WITH NOTES**（原 Phase 3 **FAIL** 未覆寫）。
- 發布衛生：移除正式母版私人絕對路徑與歷史執行 Log；證據改 Evidence ID／私人稽核歸檔。
- ENG-006 Future Acceptance 文案收斂；Hooks 維持 L3（Cursor runtime NOT_RUN）。
- README 新增「新專案初始化」：不得繼承母版 PASS 作自身驗收。

## 1.0.0-template — 2026-11-27（Scope Reduction）

- Phase 3 Independent CR：**FAIL**（報告保留，不改寫）。
- Owner Scope Reduction：移出自訂 Quality Gate／gate_models／專用測試至 private backup。
- 正式驗收改為成熟工具逐項執行；新增 `ENGINEERING_BACKLOG.md`、`KNOWN_LIMITATIONS.md`。
- F-06：澄清說明性 fixed-True 測試 ≠ mutation framework。
- F-09：hooks.json 使用 `uv run --locked`（CLI 契約證據歸私人稽核）。
- 不放寬 Ruff／Mypy／pytest／cov／權限／Commit 規則。

## 1.0.0-template — 2026-11-27（Phase 2 初建，歷史）

- 自 trading_report（SHA `0c0a65d2adc0362ccccf54cf7050750b702d3607`）提取工程治理制度。
- 曾引入自訂 quality_gate（後經 CR FAIL 移出發布範圍）。
