# TEMPLATE_ACCEPTANCE

> 本檔為**母版治理與歷史決策摘要**。  
> 母版的驗收結論**不得**作為從本 Template 建立之新專案的驗收證據。  
> 完整原始 Log／私人路徑／Phase 3.1 執行證據見私人稽核歸檔（Evidence ID）。

| 欄位 | 值 |
|---|---|
| Source Repository | `https://github.com/poyu88/trading_report` |
| Source Commit SHA | `0c0a65d2adc0362ccccf54cf7050750b702d3607` |
| Template Version | `1.0.0-template`（Standards Template） |
| Git Commit | `NOT_COMMITTED` |
| Remote CI | **NOT_RUN** |

---

## A. Phase 2 Self-check（歷史）

| 欄位 | 值 |
|---|---|
| 日期 | 2026-11-27 |
| 角色 | Developer Self-check |
| Quality Gate（當時） | OVERALL PASS |
| 其後 | Phase 3 Independent CR = **FAIL**；gate 已移出 |

原 Phase 3 Independent CR 報告：**FAIL**（永久保留，不得覆寫）。  
Evidence ID：`EV-P3-CR-FAIL`。

---

## B. Scope Reduction Self-check（歷史）

| 欄位 | 值 |
|---|---|
| 日期 | 2026-11-27 |
| 角色 | Developer Self-check（**不是** Independent CR PASS） |
| 原 Phase 3 CR | **FAIL**（保留） |
| Owner Decision | Scope Reduction APPROVED |

### B.1 備份與 SHA-256

| 項目 | 結果 |
|---|---|
| 正式備份（私人） | Evidence ID：`EV-P3-BACKUP` |
| 移出檔對照 | Evidence ID：`EV-P3-SHA-VERIFY` — 原檔為**逐列**雜湊核對皆為 `True`（**無** `ALL_MATCH=True` 頁尾字面）；Phase 3.1 Reviewer 獨立重算全部吻合 |
| 原 CR 工作區 | Evidence ID：`EV-P3-CR-FAIL`（未刪除） |
| 扁平備份命名 | `tests/support/gate_models.py` ↔ 備份 `support_gate_models.py`（Evidence ID：`EV-P3-FLAT-GATE-MODELS`；Owner 接受） |

### B.2 移出檔案

- `scripts/quality_gate.py`
- `scripts/gate_models.py`
- `scripts/__init__.py`（整個 `scripts/` 已移除）
- `tests/test_quality_gate.py`
- `tests/test_quality_gates_negative.py`
- `tests/support/gate_models.py`

無 stub／固定 True 取代。

### B.3 測試數量

| 時點 | passed | 說明 |
|---|---|---|
| Scope Reduction 前 | 39 | 含 gate 專用測 |
| 之後 | **26** | 移除 13 個 gate 專屬測試；保留功能測仍在 |

移除理由：專屬於已移出實驗功能，非弱化保留功能。

### B.4 成熟工具實測（Self-check）

當時五項成熟工具皆 exit 0（26 passed；`src/app` branch cov 100%）。  
原始執行 Log 已移出正式母版，私人歸檔 Evidence ID：`EV-SR-SELFCHECK-LOGS`。

**未**重建自訂 Overall PASS 聚合器。

### B.5 F-09（Self-check）

`hooks.json` 使用 `uv run --locked python hooks/...`。  
CLI stdin／stdout 契約當時實測通過；原始 Log Evidence ID：`EV-F09-CLI-LOGS`。  
**不**將原 Phase 3 改為 PASS。

### B.6 Clean Copy（Self-check）

私人環境 Clean Copy 當時通過（sync／import／pytest 26 passed；無 `scripts/quality_gate.py`）。  
細節見私人備份（`EV-P3-BACKUP` 相關）。

### B.7 Findings Disposition（摘要）

| Finding | Disposition |
|---|---|
| F-01～F-04 | **DEFERRED / REMOVED FROM RELEASE SCOPE**（非 FIXED） |
| F-05 | Gate 部分隨移出；**hooks 未完成驗證仍為 KNOWN LIMITATION／DEFERRED**（非全面 FIXED） |
| F-06 | 文義／測試命名已澄清 |
| F-07～F-08 | Backlog／Known Limitations |
| F-09 | 小修＋CLI 契約實測；Cursor runtime **NOT_RUN** |

### B.8 結論（歷史）

本機 Scope Reduction self-check：成熟工具全 PASS。  
當時**不得**自稱 Independent CR PASS。

---

## C. Phase 3.1 Independent Re-review

| 欄位 | 值 |
|---|---|
| 日期 | 2026-11-27 |
| 角色 | Independent Reviewer |
| Verdict | **PASS WITH NOTES** |
| 阻擋級 Findings | **0** |
| 原 Phase 3 CR | 仍為 **FAIL**（未覆寫） |
| Evidence ID | `EV-P31-CR`、`EV-P31-MANIFEST`、`EV-P31-TOOLS` |

Owner 接受 PASS WITH NOTES，並授權 Release Hygiene（不新增功能、不啟動 DEFERRED）。

---

## D. Release Hygiene（本輪）

| 欄位 | 值 |
|---|---|
| 日期 | 2026-11-27 |
| 角色 | Developer（僅授權衛生整理） |
| 私人歸檔 | Evidence ID map：見私人 `20261127_phase31_release_hygiene/EVIDENCE_ID_MAP.md` |
| 整理前本檔備份 | Evidence ID：`EV-RH-PRE-TA` |

### D.1 Notes Disposition（N-01～N-07）

| ID | Disposition |
|---|---|
| N-01 | 本檔改 Evidence ID／通用說明；移除私人絕對路徑 |
| N-02 | `_scope_reduction_verify`／`_f09_hook_verify` 移出正式母版至私人歸檔 |
| N-03 | Hooks 維持 L3；Cursor runtime NOT_RUN；接受限制 |
| N-04 | ENG-006 Future Acceptance 文案修正（不啟動框架） |
| N-05 | 清理可重生 Cache／coverage 產物 |
| N-06 | 接受扁平備份命名；保留路徑對照 |
| N-07 | 修正 ALL_MATCH 文義；以逐列 True＋獨立重算為準 |

### D.2 Hooks（N-03）

- 定位：**L3 EXPERIMENTAL／ADVISORY**
- CLI stdin／stdout 契約：已於 Phase 3.1 獨立驗證
- Cursor IDE runtime：**NOT_RUN**（不得冒充整合通過）
- 新專案須先 `uv sync --locked --dev` 再依賴 Hooks
- 不得作為完整安全邊界；不需要時可由 Owner 停用 `.cursor/hooks.json`
- **不**新增自動啟用／環境偵測／安全驗收框架

---

## E. 給新專案的聲明

從本 Template 建立的新專案：

1. 必須重新撰寫自身 PRD／SPEC／驗收證據。  
2. **不得**將本檔或母版 PASS WITH NOTES 當作該專案已驗收。  
3. 須建立自身 `TDD_STATUS` 與 Independent CR／UAT 紀錄。  
4. DEFERRED 項目須 Owner 授權後才可啟動。
