# Python Engineering Template — 品質開發流程（主文件）

本文件是本專案 **端到端品質開發流程** 的唯一正式來源。
產品／技術契約與測試方法分別以 PRD／SPEC／TDD 為準；誠信以 [`AGENT_INTEGRITY.md`](AGENT_INTEGRITY.md) 為準。技術債見 [`ENGINEERING_BACKLOG.md`](ENGINEERING_BACKLOG.md)。

制度繼承自 trading_report SHA `0c0a65d2adc0362ccccf54cf7050750b702d3607`，已去除交易業務耦合。  
Phase 3 Independent CR：**FAIL**（自訂 Quality Gate 已移出 v1.0 發布範圍；原報告不改寫）。

| 文件 | 職責 |
|---|---|
| `docs/DEVELOPMENT_WORKFLOW.md`（本檔） | PRD→TDD→Commit→Push→PR→CI→Review→UAT→Merge |
| `docs/CODING_STANDARDS.md` | Python 風格、Docstring、Type Hints、Ruff／Mypy／Coverage |
| `docs/AGENT_INTEGRITY.md` | 驗收誠信、anti-gaming、反過度工程 |
| `docs/ENGINEERING_BACKLOG.md` | DEFERRED／EXPERIMENTAL 技術債 |
| `docs/KNOWN_LIMITATIONS.md` | 已知限制 |
| `docs/BACKUP_AND_ARTIFACT_POLICY.md` | 永久備份／暫存產物分類與 INDEX |
| `docs/prd/PRD.md` | 產品需求（專案填寫） |
| `docs/spec/SPEC.md` | 技術規格（專案填寫） |
| `docs/test/TDD.md` | TDD 方法 |
| `docs/test/TDD_STATUS.md` | **實際**測試結果 |
| `AGENTS.md` | 跨 Agent 入口 |
| `.github/workflows/pytest.yml` | GitHub Actions CI |
| `.cursor/rules/*.mdc` | Agent 精簡規則 |

若本檔與 Cursor Rule 衝突，以本檔為準並回報不一致處。

---

## 1. 核心流程

```text
PRD / SPEC
    → TDD（RED → GREEN → REFACTOR → REGRESSION）
    → Git Commit
    → Git Push
    → Pull Request
    → GitHub Actions CI
    → Code Review
    → UAT
    → Merge
```

- **本機 pytest 通過 ≠ GitHub CI Success ≠ 人工 UAT 通過**。
- 本機正式驗收＝成熟工具**逐項**通過（各記 exit code），**無**自訂 Overall PASS 聚合器。

---

## 2. 各階段要求

### 2.1 PRD / SPEC

增量修改；未決決策不得由 Agent 自行假定。

### 2.2 TDD

見 [`docs/test/TDD.md`](test/TDD.md)。不得虛構歷史；不得用正式／敏感生產資料做自動化測試。

### 2.3–2.5 Git Commit / Push / PR

- Commit：`add|fix|restruct|test|doc`＋繁中（`commit-rule.mdc`）。
- Agent 僅在明確授權時 Commit；不得自行 Push／PR／Merge。
- **禁止 Force Push（無例外）**。
- 不得擅自使用個人 Token 或擴大寫入權限。

### 2.6 GitHub Actions CI

以 [`.github/workflows/pytest.yml`](../.github/workflows/pytest.yml) 為準。

| 項目 | 內容 |
|---|---|
| 權限 | `contents: read` |
| Jobs | lint（ruff＋format）、mypy、pytest＋coverage（以 YAML 為準） |
| Python | **3.11** |

未實際跑過的遠端 CI 標 **NOT_RUN**。CI ≠ UAT ≠ CR。

### 2.7 Code Review

結論：`PASS`／`PASS WITH NOTES`／`FAIL`。  
Finding 欄位：Finding ID、Severity、File、Line、Evidence、Violated Rule、Risk、Required Fix、Verification Method。  
Reviewer 未授權不得改碼或 Merge。

### 2.8 UAT

pytest 全綠不能取代 UAT。隔離：`output/uat_<主題>/`、`data/uat/<主題>/`；禁止寫正式資料路徑。

### 2.9 Merge

規格＋TDD／本機成熟工具＋CI＋CR＋UAT（適用時）＋**使用者明確授權**。合併後核對 SHA／PR／master／CI。

---

## 3. Agent 權限邊界（強制）

| 動作 | 預設 | 例外 |
|---|---|---|
| 讀取規格／程式／測試 | 允許 | — |
| 修改程式／測試 | 任務授權範圍內 | 不得放寬門檻或契約 |
| 本機 Commit | **禁止** | 使用者明確要求 |
| Push | **禁止** | 使用者明確要求（仍不得 Force） |
| Force Push／改寫遠端歷史 | **禁止** | **無例外** |
| PR／Merge | **禁止** | 使用者明確要求 |
| 個人 Token／擴大寫入 | **禁止** | 無例外 |
| 啟動 DEFERRED Backlog | **禁止** | Owner 明確授權 |
| 讀寫正式／敏感生產資料 | **禁止** | 使用者明確本機驗收指示 |

---

## 4. 三種「通過」的定義

| 名稱 | 意義 | 不代表 |
|---|---|---|
| 本機成熟工具通過 | 上列 ruff／format／mypy／pytest 各 exit 0 | 不代表 CI；不代表 UAT |
| GitHub CI Success | YAML 必要 Job 皆過 | 不代表 UAT；不代表可自動 Merge |
| 人工 UAT | 使用者驗收並留證據 | 不因工具全綠自動成立 |

---

## 5. 本機最小檢查表

1. [ ] 已讀 PRD／SPEC／TDD／Integrity／Backlog（若相關）
2. [ ] RED／GREEN／REFACTOR（適用時）真實紀錄
3. [ ] `uv run --locked ruff check .` exit 0
4. [ ] `uv run --locked ruff format --check .` exit 0
5. [ ] `uv run --locked mypy` exit 0
6. [ ] `uv run --locked pytest` exit 0
7. [ ] `TDD_STATUS.md` 已更新真實結果
8. [ ] 使用者授權後才 Commit／Push／PR／Merge

---

## 6. 文件維護

權威不雙重維護。表格與 YAML 衝突時以 YAML 為準並修正本檔。Class C 證據不覆寫史實，僅追加後補。
