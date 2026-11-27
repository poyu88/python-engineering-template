# AGENTS.md — 所有 Agent 的共同入口

本檔是跨 Agent 的**精簡入口**，不是第二套完整規範。細節以各唯一權威來源為準。

## 開發前必讀

依任務至少閱讀：

| 需求 | 權威文件 |
|---|---|
| 流程／權限／CR／UAT／Merge／隔離 | [`docs/DEVELOPMENT_WORKFLOW.md`](docs/DEVELOPMENT_WORKFLOW.md) |
| 風格／Docstring／Ruff／Mypy | [`docs/CODING_STANDARDS.md`](docs/CODING_STANDARDS.md) |
| TDD 方法 | [`docs/test/TDD.md`](docs/test/TDD.md) |
| 驗收誠信／四態／anti-gaming | [`docs/AGENT_INTEGRITY.md`](docs/AGENT_INTEGRITY.md) |
| 待驗證登記 | [`docs/VERIFICATION_PENDING.md`](docs/VERIFICATION_PENDING.md) |
| 技術債／成熟度 | [`docs/ENGINEERING_BACKLOG.md`](docs/ENGINEERING_BACKLOG.md)、[`docs/KNOWN_LIMITATIONS.md`](docs/KNOWN_LIMITATIONS.md) |
| 備份／產物分類 | [`docs/BACKUP_AND_ARTIFACT_POLICY.md`](docs/BACKUP_AND_ARTIFACT_POLICY.md) |
| 產品需求 | [`docs/prd/PRD.md`](docs/prd/PRD.md) |
| 技術契約 | [`docs/spec/SPEC.md`](docs/spec/SPEC.md) |
| 工具與依賴 | `pyproject.toml`／`uv.lock` |
| CI 實際行為 | [`.github/workflows/pytest.yml`](.github/workflows/pytest.yml) |
| 規範版本 | [`STANDARDS_VERSION.md`](STANDARDS_VERSION.md) |

Cursor Rules（`.cursor/rules/*.mdc`）與 [`BUGBOT.md`](.cursor/BUGBOT.md) 僅為精簡指針。

## 核心禁止事項（強制）

1. **禁止**虛構測試結果、RED／GREEN 歷史、CI／UAT／驗收證據，或虛構驗證規則／預期結果／PASS。
2. **禁止**弱化測試斷言、刪除／skip／xfail 必要驗證，或擅自降低 Coverage／型別／Lint 門檻。
3. **禁止**未經 Owner 明確授權執行 Commit、Push、建立／合併 PR、Merge、Tag。
4. **禁止** Force Push 或改寫遠端 Git 歷史（**無例外**；Agent 永不執行）。
5. **禁止**在規範衝突時自行選擇較寬鬆的規則；必須回報並以較嚴格／權威文件為準；衝突未決時工程驗收標 `PENDING`。
6. **禁止**使用無理由的 `Any`、全域 `ignore_missing_imports`、無理由 `type: ignore`／`noqa`、Coverage 排除或 `continue-on-error` 逃避驗收。
7. **禁止**為滿足規格完整性而強行實作缺乏需求／契約／案例的驗證機制，或製造假性 PASS。
8. **禁止**未經 Owner 授權擅自啟動 `ENGINEERING_BACKLOG` 中的 DEFERRED 項目。
9. **禁止**擅自建立其他永久備份根；永久／暫存根由 Owner 指定，細節見 [`docs/BACKUP_AND_ARTIFACT_POLICY.md`](docs/BACKUP_AND_ARTIFACT_POLICY.md)。
10. **禁止**以自我檢查冒充 Independent CR；禁止新建 Overall PASS 聚合器；禁止盲目全庫替換狀態字串。
11. 開發前必須閱讀與本次變更相關的權威文件；不得假定未記載的政策。
12. 缺規則／資料／環境／權限時標 `PENDING` 並登記 [`docs/VERIFICATION_PENDING.md`](docs/VERIFICATION_PENDING.md)；不停止其他可完成工作。

## 衝突處理

| 衝突類型 | 以誰為準 |
|---|---|
| Rule vs Workflow | `docs/DEVELOPMENT_WORKFLOW.md` |
| Rule vs Coding Standards | `docs/CODING_STANDARDS.md` |
| Rule vs TDD.md | `docs/test/TDD.md` |
| 文件表格 vs CI YAML | `.github/workflows/pytest.yml` |
| 依賴清單 | `pyproject.toml`／`uv.lock` |
| 誠信／工程驗收四態 | `docs/AGENT_INTEGRITY.md` |
| 待驗證事項 | `docs/VERIFICATION_PENDING.md` |

發現不一致：回報衝突，工程驗收層標 **`PENDING`**，不得靜默採寬鬆解釋。

## 工程驗收四態（摘要）

僅：`PASS`｜`FAIL`｜`PENDING`｜`N/A`。細節與映射見 Integrity。
工具採用 `NOT_ADOPTED` **不是**四態之一，不得直接等同 `N/A`。

## Executable Quality Controls（L1 ENFORCED）

本機與 CI 共用同一組**成熟工具**必要檢查（各自獨立執行與記錄 exit code；**無**自訂 Overall PASS 聚合器）：

```powershell
uv sync --locked --dev
uv run --locked ruff check .
uv run --locked ruff format --check .
uv run --locked mypy
uv run --locked pytest
```

- Ruff lint／format
- Mypy（`src/`、`hooks/`、`tests/support/`）
- pytest
- Branch Coverage（`src/app`，門檻 80%）

Cursor 敏感 Hooks 為 **L3 輔助警示**，非正式安全驗收唯一依據；其原生 `detection_status` 字串不得當工程四態替換。
