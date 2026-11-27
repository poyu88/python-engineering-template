## Summary

<!-- 做了什麼、為什麼 -->

## 變更範圍

<!-- 模組／檔案 -->

## 測試證據（逐項成熟工具）

- [ ] `uv run --locked ruff check .`（exit code：）
- [ ] `uv run --locked ruff format --check .`（exit code：）
- [ ] `uv run --locked mypy`（exit code：）
- [ ] `uv run --locked pytest`（exit code／passed／failed／skipped：）

## 風險

<!-- 契約、資料、相容性 -->

## UAT 待驗收

<!-- 適用時列出；不適用請寫 NOT_APPLICABLE 理由 -->

## 檢查

- [ ] 未包含正式資料／Secrets
- [ ] 未放寬品質門檻
- [ ] 未擅自啟動 DEFERRED Backlog
- [ ] Agent 未自行 Merge
