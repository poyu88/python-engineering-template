# Agent Integrity（驗收誠信唯一正式來源）

本文件是本專案 **Agent／開發者驗收誠信與 anti-gaming** 的唯一正式來源。
流程細節見 [`DEVELOPMENT_WORKFLOW.md`](DEVELOPMENT_WORKFLOW.md)；TDD 方法見 [`test/TDD.md`](test/TDD.md)。
本檔不取代 Code Review 的 `PASS`／`PASS WITH NOTES`／`FAIL` 三態結論。

來源制度參考：trading_report SHA `0c0a65d2adc0362ccccf54cf7050750b702d3607`。  
Phase 3 Independent CR：**FAIL**（保留；自訂 Quality Gate 已移出發布範圍，見 Backlog）。

---

## 0. 強制分層：文件 ≠ 自動化已完成

| 層級 | 意義 | 本版例子 |
|---|---|---|
| **POLICY** | 文件要求；靠 Agent 指令與 Independent CR | TDD 紀律、禁虛構證據、禁弱化斷言 |
| **ENFORCED (tool)** | 成熟工具強制；各工具自身 exit code | Ruff、format、Mypy、pytest＋branch cov、CI Jobs |
| **ADVISORY (L3)** | 輔助警示；非正式唯一依據 | Cursor 敏感 Hooks |
| **DEFERRED** | 未自動化／未成熟；僅 Backlog | 自訂 Quality Gate、通用 anti-gaming、mutation framework |

**禁止**將政策文件存在視為自動化機制已完成。  
**禁止**為讓 CR PASS 而製造替代假驗證、降低成熟工具門檻或刪除有價值測試。  
**禁止**為完成 TODO 強行實作 DEFERRED 項（須 Owner 授權）。

---

## 1. Anti-overengineering 永久原則

優先採用成熟、可驗證的既有工具及參考實作。

當需求、資料、測試契約或參考案例不足時，應明確記錄限制並列入 [`ENGINEERING_BACKLOG.md`](ENGINEERING_BACKLOG.md)。

不得為滿足規格完整性而強行實作不成熟的驗證機制。

不得進行缺乏實際需求的過度抽象化、過度工程化及形式化驗收。

不得為完成 TODO 而製造假性 PASS。

未經 Owner 授權，不得擅自啟動 DEFERRED 項目。

---

## 2. 驗證項目狀態（記錄用；非自訂聚合器）

記錄個別檢查結果時可使用：

`PASS`｜`FAIL`｜`NOT_RUN`｜`BLOCKED`｜`NOT_APPLICABLE`

本版**不**提供自訂 Overall PASS 程式。正式本機驗收＝下列成熟工具**逐項**成功：

```powershell
uv sync --locked --dev
uv run --locked ruff check .
uv run --locked ruff format --check .
uv run --locked mypy
uv run --locked pytest
```

任一必要工具非零 exit、未執行或結果不明確 → 不得宣稱本機驗收成功。  
`NOT_APPLICABLE` 必須有明確理由，且不得用來排除仍屬必要的成熟工具檢查。

> 此處是驗證項目狀態，不是 CR 結論三態。

---

## 3. 禁止的規避行為（Anti-gaming）

禁止：

1. 以固定 `True`／空實作取代實際驗證契約。
2. 以表面條件（僅檔案存在、空成功）冒充內容正確性（除非契約本身即為該條件）。
3. 偽造 PASS、測試／CI／UAT 結果或 TDD 歷史。
4. 用 Mock／Stub 隱藏必要負向案例。
5. 刪除、`skip`、`xfail` 或弱化必要測試換綠燈。
6. 擅自降低 Coverage、型別、Lint、format 門檻。
7. 全域 ignore、過寬 ignores、無理由 `noqa`／`type: ignore`。
8. 捕捉例外後回傳成功。
9. 改 CI 選取範圍或驗收函式逃避 CR。
10. 將未驗證項目標記完成。
11. 重新引入有缺陷的自訂 Overall PASS 聚合器而不經 Owner 授權與獨立驗證。

違規：CR **FAIL**、阻擋 Merge、RCA、補回歸、重新獨立 CR。實作 Agent 不得自行解除阻擋。

---

## 4. 輔助檢查 vs 正式驗收

| 類型 | 例子 | 語意 |
|---|---|---|
| 正式必要（L1） | Ruff、format、Mypy、pytest＋branch cov | 各工具 exit code；失敗／未跑 → 不得成功 |
| 輔助（L3） | Cursor sensitive hooks（可 fail-open） | **不是**完整安全邊界；偵測失敗 ≠ 安全 PASS |

---

## 5. 已知未自動化項目

見 [`KNOWN_LIMITATIONS.md`](KNOWN_LIMITATIONS.md) 與 [`ENGINEERING_BACKLOG.md`](ENGINEERING_BACKLOG.md)。  
Anti-gaming 目前主要依靠：**本文件（POLICY）＋成熟工具（ENFORCED）＋Independent CR**。
