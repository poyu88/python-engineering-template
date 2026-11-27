# SPEC — 技術規格（專案填寫範本）

> 空白範本。新專案在此填寫技術契約。不得從 trading_report 複製 FIFO／報表欄位／券商解析契約。

## 1. 架構概要

（待填）

## 2. 技術棧與環境

- Python **3.11**（與 `.python-version`／CI 對齊；其他版本未驗證不得宣稱相容）
- 套件管理：uv；權威：`pyproject.toml`／`uv.lock`
- 品質檢查：逐項 `ruff`／`ruff format --check`／`mypy`／`pytest`（見 README；無自訂 gate）

## 3. 目錄結構

見倉庫根目錄實際布局（`src/`、`tests/`、`hooks/`、`scripts/`、`docs/`）。

## 4. 介面與資料契約

（待填：API／CLI／schema／錯誤碼）

## 5. 安全與資料保護

- 正式／敏感資料與測試資料隔離
- 密鑰不得入庫
- Cursor 敏感 Hooks 為**輔助**，非完整安全邊界（見 AGENT_INTEGRITY）

## 6. 測試隔離

- 自動化測試使用 `tmp_path`／合成資料
- 不得讀寫正式生產路徑

## 7. 驗證矩陣

| ID | 規格 | 期望 | 自動化 |
|---|---|---|---|
| （待填） | | | |

## 8. 品質流程引用

技術 Done ≠ 流程完成。須依 [`DEVELOPMENT_WORKFLOW.md`](../DEVELOPMENT_WORKFLOW.md) 完成 CI／CR／UAT（適用時）與授權 Merge。
