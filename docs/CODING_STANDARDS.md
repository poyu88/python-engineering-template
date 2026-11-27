# Coding Standards（Python 風格唯一正式來源）

本文件是本專案 **Python 程式碼風格與可維護性標準** 的唯一正式來源。

| 文件 | 職責 |
|---|---|
| `docs/CODING_STANDARDS.md`（本檔） | 風格、Docstring、Type Hints、Ruff／Mypy／Coverage |
| `docs/DEVELOPMENT_WORKFLOW.md` | 端到端流程 |
| `docs/AGENT_INTEGRITY.md` | 驗收誠信 |
| `pyproject.toml`／`uv.lock` | 工具設定唯一權威 |
| `.github/workflows/pytest.yml` | 實際 CI 行為 |

若本檔與 Cursor Rule 衝突，以本檔為準。

---

## 1. Python 基本規範

- **版本**：Python **3.11**（已驗證基準）。
- PEP 8／PEP 257；**Ruff** 檢查與格式。
- 行寬 100；原始碼在 `src/`；根目錄 `uv sync`／`uv run`。
- 依賴以 `pyproject.toml`／`uv.lock` 為準；禁 pip／poetry／conda／`requirements.txt`。
- 套件須可安裝並 `import app`。

---

## 2. Google Style Docstring

公開模組／類別／函式採 Google Style。  
工具：`convention = "google"`；Ruff 選定 `E,F,I,UP,B,ANN,D,SIM,RUF`。  
`tests/test_*.py`／`conftest.py` 可精準豁免 D／ANN（見 pyproject）。  
精確忽略：`RUF001`（繁中全形標點）。禁止無理由 noqa。

---

## 3. Type Hints 與 Mypy

| 目錄 | 要求 |
|---|---|
| `src/` | Strict |
| `hooks/` | Strict |
| `tests/support/` | Strict |
| 一般 `tests/` | 適度放寬 |

禁止無理由 `Any`、全域 `ignore_missing_imports`、無理由 `type: ignore`。  
（自訂 `scripts/quality_gate` 已移出 v1.0；Mypy 範圍不含已移除路徑。）

---

## 4–5. 領域計算／錯誤與日誌

不得盲目 `--fix` 改變領域計算結果；禁裸 except／靜默吞錯；日誌禁密鑰。

---

## 6. 測試

TDD 以 [`docs/test/TDD.md`](test/TDD.md) 為準。  
Coverage：**branch**＋`src/app` **80%** 門檻。Coverage ≠ 功能正確。  
說明性固定 True 對照測試 ≠ Mutation Testing 框架（見 F-06／Backlog）。

---

## 7. 本機與 CI 指令（正式）

| 場景 | 指令 |
|---|---|
| Lint | `uv run --locked ruff check .` |
| Format | `uv run --locked ruff format --check .` |
| Mypy | `uv run --locked mypy` |
| Pytest＋cov | `uv run --locked pytest` |

無自訂 Quality Gate 統一入口。CI 分 Job，門檻不得低於上表。

---

## 8. Code Review

結論格式見 Workflow。風格以本檔為準。
