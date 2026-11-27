# Changelog

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
