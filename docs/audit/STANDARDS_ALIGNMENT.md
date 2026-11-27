# Standards Alignment

## 權威關係

| 主題 | 權威 |
|---|---|
| 流程／權限 | `docs/DEVELOPMENT_WORKFLOW.md` |
| 風格／工具政策 | `docs/CODING_STANDARDS.md` |
| 誠信 | `docs/AGENT_INTEGRITY.md` |
| TDD | `docs/test/TDD.md` |
| 技術債 | `docs/ENGINEERING_BACKLOG.md` |
| 已知限制 | `docs/KNOWN_LIMITATIONS.md` |
| 依賴／Ruff／Mypy／cov | `pyproject.toml`／`uv.lock` |
| CI | `.github/workflows/pytest.yml` |
| Agent 入口 | `AGENTS.md` |

來源：trading_report SHA `0c0a65d2adc0362ccccf54cf7050750b702d3607`。

## 成熟度 L1–L4

| Level | 名稱 | 本版內容 |
|---|---|---|
| L1 ENFORCED | 成熟工具 | Ruff lint／format、Mypy、pytest、branch cov；CI Jobs（遠端 NOT_RUN） |
| L2 POLICY | 文件＋CR | TDD、PRD／SPEC、Commit、Integrity、UAT／CR／RCA、權限 |
| L3 EXPERIMENTAL | 輔助 | Sensitive hooks（advisory） |
| L4 DEFERRED | 延後 | 自訂 Quality Gate、狀態聚合、自動 anti-gaming、mutation framework |

## Phase 3

Independent CR = **FAIL**。自訂 gate 缺陷（F-01～F-04）採 **DEFERRED／REMOVED FROM RELEASE SCOPE**，不是 FIXED。
