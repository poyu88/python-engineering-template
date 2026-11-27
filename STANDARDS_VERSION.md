# Standards Version

| 欄位 | 值 |
|---|---|
| Template name | Python Engineering Governance Template |
| Version（文件規範） | `1.1.0-template`（文件內版本字串；**不**因日後打 Tag 而改此欄） |
| Positioning | **v1.1 Engineering Standards Template** — 四態驗收／待驗證登記／風險導向隔離 |
| Merge status | **已合併**至 `master`：PR [#1](https://github.com/poyu88/python-engineering-template/pull/1)；Merge Commit `a86ba5d369b00fcb800a824e0975572864ee7e65` |
| Historical CI evidence | PR CI run `46028699714`（`headSha`=`d71f302d…`）SUCCESS；master push CI run `46030784881`（`headSha`=`a86ba5d…`）SUCCESS。詳見 `docs/VERIFICATION_PENDING.md` Stage C.6。**僅**證明該等 SHA；不得套用至尚未建立的結案／Tag Commit |
| Independent CR | Stage B／B.2 = **PASS WITH NOTES**（F-CR-01～06 複審 PASS；VP-004 **PASS**） |
| Tag／Release（當前） | **尚未**建立；既有 tag 僅 `v1.0.0`。Owner 預定未來 Tag 名為 **`v1.1.0`**（延續 `v1.0.0` 命名），指向「結案 PR 合併且該 SHA 之 master CI 通過」後的正式 Commit；**本輪不建 Tag** |
| Still PENDING | VP-002-D（Manifest 外部相容）；VP-003（Hooks Cursor runtime） |
| Historical | 原 Phase 3 Independent CR = **FAIL**（保留，不覆寫） |
| Source repository | `https://github.com/poyu88/trading_report` |
| Source commit SHA | `0c0a65d2adc0362ccccf54cf7050750b702d3607` |
| Python baseline | **3.11** |
| Prior release | `1.0.0-template`（tag `v1.0.0`） |

見 [`CHANGELOG.md`](CHANGELOG.md)、[`docs/VERIFICATION_PENDING.md`](docs/VERIFICATION_PENDING.md)、[`docs/ENGINEERING_BACKLOG.md`](docs/ENGINEERING_BACKLOG.md)、[`docs/KNOWN_LIMITATIONS.md`](docs/KNOWN_LIMITATIONS.md)。
