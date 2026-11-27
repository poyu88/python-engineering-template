# Migration Matrix

Source: `https://github.com/poyu88/trading_report`  
Source Commit SHA: `0c0a65d2adc0362ccccf54cf7050750b702d3607`  
Target: `python-engineering-template`  
Class: A Direct／B Generalize／C Template／D Exclude／E New／F Obsolete

| Source Path | Class | Target Path | Required Changes | Acceptance |
|---|---|---|---|---|
| `docs/DEVELOPMENT_WORKFLOW.md` | B | `docs/DEVELOPMENT_WORKFLOW.md` | 去交易耦合；通用 UAT；引用 Integrity | 權限未放寬 |
| `docs/CODING_STANDARDS.md` | B | `docs/CODING_STANDARDS.md` | 綠地強制 D/ANN；Mypy 分層；branch cov | 與 pyproject／CI 一致 |
| `docs/test/TDD.md` | B | `docs/test/TDD.md` | 去契約矩陣／絕對路徑 | 無業務 FIFO |
| `docs/test/TDD_STATUS.md` | C | `docs/test/TDD_STATUS.md` | 空白＋本階段真實紀錄 | 無來源 PASS 史 |
| `docs/prd/PRD.md` | C | `docs/prd/PRD.md` | 空白範本 | 無交易規則 |
| `docs/spec/SPEC.md` | C | `docs/spec/SPEC.md` | 空白範本 | 無 FIFO 契約 |
| `docs/audit/CODING_STANDARDS_ALIGNMENT.md` | C | `docs/audit/STANDARDS_ALIGNMENT.md` | 權威表；不移植過時 §E | 無「Ruff 未進 CI」 |
| `.cursor/rules/commit-rule.mdc` | A | 同 | 措辭澄清 | 五類別 |
| `.cursor/rules/py-env.mdc` | A | 同 | 註明 3.11 驗證基準 | 3.11 |
| `.cursor/rules/tdd-rule.mdc` | B | 同 | 正式／敏感資料用語 | 禁虛構 RED |
| `.cursor/rules/dev-workflow-rule.mdc` | B | 同 | 去 FIFO／trading.db | 權限同等或更嚴 |
| `.cursor/rules/backend-rule.mdc` | B | `.cursor/rules/python-rule.mdc` | `src/`；成熟工具指令（無自訂 gate） | uv 強制 |
| `.cursor/BUGBOT.md` | A/B | 同 | 加 Integrity 指針 | 非權威 |
| `.cursor/hooks.json` | A | 同 | 配線保留 | 兩 hook |
| `hooks/check_sensitive_*.py` | **B** | 同 | 路徑正規化／目錄／fail-open 揭露 | CR-PLAN-01 |
| `.github/workflows/pytest.yml` | B | 同 | lint／format／mypy／pytest jobs | contents:read |
| `pyproject.toml` | B/C | 同 | 重生；無業務 deps | uv sync --locked |
| `uv.lock` | D→重生 | 同 | 依新依賴生成 | 與 pyproject 一致 |
| `.python-version` | A | 同 | 3.11 | 一致 |
| `.gitignore` | B | 同 | 通用化 | 無強制券商附件規則 |
| `backend/**` 等業務 | D | — | 排除 | Exclusion 掃描 |
| — | E | `AGENTS.md` | 入口＋核心禁令 | CR-PLAN-07 |
| — | E | `docs/AGENT_INTEGRITY.md` | 五態＋anti-gaming | CR-PLAN-05 |
| — | E→**DEFERRED** | （已移出）`scripts/quality_gate.py` | Phase 3 FAIL；REMOVED FROM RELEASE SCOPE | F-01～F-04；私人備份 Evidence ID：`EV-P3-BACKUP` |
| — | E | `tests/test_sensitive_hooks.py` 等 | 負向證明 | CR-PLAN-01/05 |
| — | E | `docs/audit/MIGRATION_MATRIX.md` | 本檔 | CR-PLAN-06 |
| ALIGNMENT 過時 Ruff-CI | F | 不移植 | 現行含 Ruff | 文件一致 |
