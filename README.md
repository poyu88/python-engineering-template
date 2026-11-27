# Python Engineering Governance Template

可重用的 Python 工程治理母版（**1.1.0-template 候選**：成熟規範＋成熟工具＋四態驗收；非交易系統。尚未正式發布／無新 Tag）。

| 項目 | 值 |
|---|---|
| Version | 見 [`STANDARDS_VERSION.md`](STANDARDS_VERSION.md)（候選 `1.1.0-template`） |
| Source | `https://github.com/poyu88/trading_report` |
| Source SHA | `0c0a65d2adc0362ccccf54cf7050750b702d3607` |
| Python | **3.11**（已驗證基準） |

## 環境

```powershell
uv sync --locked --dev
```

## 正式品質檢查（逐項成熟工具；不聚合）

```powershell
uv run --locked ruff check .
uv run --locked ruff format --check .
uv run --locked mypy
uv run --locked pytest
```

每項檢查須獨立記錄 Command、Exit Code、輸出摘要與工程四態（`PASS`｜`FAIL`｜`PENDING`｜`N/A`）。
**本版不提供**自訂 Quality Gate／Overall PASS 聚合器（見 [`docs/ENGINEERING_BACKLOG.md`](docs/ENGINEERING_BACKLOG.md)）。
缺條件時標 `PENDING` 並登記 [`docs/VERIFICATION_PENDING.md`](docs/VERIFICATION_PENDING.md)。

## 文件地圖

| 文件 | 職責 |
|---|---|
| [`AGENTS.md`](AGENTS.md) | Agent 入口與核心禁令 |
| [`docs/DEVELOPMENT_WORKFLOW.md`](docs/DEVELOPMENT_WORKFLOW.md) | 流程／權限／CR／UAT／Merge／風險隔離 |
| [`docs/CODING_STANDARDS.md`](docs/CODING_STANDARDS.md) | 風格／Ruff／Mypy／Coverage |
| [`docs/AGENT_INTEGRITY.md`](docs/AGENT_INTEGRITY.md) | 驗收誠信／四態 |
| [`docs/VERIFICATION_PENDING.md`](docs/VERIFICATION_PENDING.md) | 待驗證事項 |
| [`docs/ENGINEERING_BACKLOG.md`](docs/ENGINEERING_BACKLOG.md) | 延後／實驗性技術債 |
| [`docs/KNOWN_LIMITATIONS.md`](docs/KNOWN_LIMITATIONS.md) | 已知限制 |
| [`docs/test/TDD.md`](docs/test/TDD.md) | TDD 方法 |
| [`docs/audit/`](docs/audit/) | 移植矩陣與驗收紀錄 |

## 新專案初始化（從本 Template 建立時）

1. 保留本母版來源與版本資訊（見上表／[`STANDARDS_VERSION.md`](STANDARDS_VERSION.md)）。
2. **重新**撰寫本專案自己的 [`docs/prd/PRD.md`](docs/prd/PRD.md) 與 [`docs/spec/SPEC.md`](docs/spec/SPEC.md)；不得沿用空白範本當作已完成需求。
3. **重新**建立本專案的 `TDD_STATUS`、Independent CR／UAT 與驗收證據；**不得**將母版的 PASS／PASS WITH NOTES 當作本專案已驗收。
4. 執行 `uv sync --locked --dev` 後再跑成熟工具檢查。
5. [`docs/ENGINEERING_BACKLOG.md`](docs/ENGINEERING_BACKLOG.md) 中的 DEFERRED／EXPERIMENTAL 項目，須取得 Owner 授權後才可啟動。
6. Cursor 敏感 Hooks 為 **L3 輔助**；若不需要，可由 Owner 停用 `.cursor/hooks.json`。使用前須先完成 `uv sync`；**不得**視為完整安全邊界。
7. 沿用或擴充待驗證登記（母版範式：`VERIFICATION_PENDING.md`）；產品專屬清單優先既有文件。

## 原則

- 本機 pytest ≠ GitHub CI ≠ 人工 UAT
- Commit／Push／PR／Merge／Tag 分別授權；禁止 Force Push
- 工程驗收四態：`PASS`｜`FAIL`｜`PENDING`｜`N/A`；工具採用 `NOT_ADOPTED` ≠ `N/A`
- Cursor 敏感 Hooks 為 **L3 輔助**，非正式安全邊界唯一機制
- Coverage ≠ 功能正確；不得以假性 PASS 掩蓋未完成工作
- 遠端 CI 未執行時工程層標 `PENDING`（歷史用語 NOT_RUN 可保留），不得標 PASS
- 獨立驗收環境依風險選擇（見 Workflow §2.10）；Worktree／Clone ≠ OS 沙箱
- 新專案繼承工程**規範與工具**，不繼承上一專案的驗收成功紀錄
