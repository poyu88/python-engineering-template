# TDD 規範（唯一正式來源）

繼承自 trading_report SHA `0c0a65d2adc0362ccccf54cf7050750b702d3607` 之方法論。

| 文件 | 職責 |
|---|---|
| `docs/test/TDD.md`（本檔） | TDD 政策 |
| `docs/DEVELOPMENT_WORKFLOW.md` | 端到端流程 |
| `docs/AGENT_INTEGRITY.md` | 誠信 |
| `.cursor/rules/tdd-rule.mdc` | Agent 強制入口 |
| `docs/test/TDD_STATUS.md` | 實際證據 |

---

## 1. 核心原則

**RED → GREEN → REFACTOR → REGRESSION**

不得虛構歷史；不得削弱斷言換綠燈。特徵化／回歸 ≠ 當次 TDD。

---

## 2. 階段定義

- **RED**：失敗須來自預期行為未滿足（非環境／import 錯）。
- **GREEN**：最小實作；不弱化斷言。
- **REFACTOR**：不改行為。
- **REGRESSION**：完整成熟工具檢查並更新 `TDD_STATUS.md`。

---

## 3. 安全與隔離

`tmp_path`／合成資料；禁正式／敏感生產資料；缺私有測資 ≠ PASS。

---

## 4. 執行方式（PowerShell，專案根目錄）

```powershell
uv sync --locked --dev
uv run --locked pytest tests/test_hello.py -q -x --tb=short
uv run --locked ruff check .
uv run --locked ruff format --check .
uv run --locked mypy
uv run --locked pytest -q
```

---

## 5. 母版示範

- `src/app/hello.py`、`demo_validate.py`
- `tests/test_hello.py`、`test_demo_validate.py`（含**說明性** fixed-True 對照，非 mutation framework）
- `hooks/`＋`tests/test_sensitive_hooks.py`（L3 輔助）

自訂 Quality Gate 已移出 v1.0（見 ENGINEERING_BACKLOG）。

---

## 6. 狀態紀錄

更新 `TDD_STATUS.md`：真實指令、通過／失敗數、Commit 或 `NOT_COMMITTED`。禁止虛構通過。

---

## 7. 與流程

本機 REGRESSION ≠ CI ≠ UAT。
