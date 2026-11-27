# Agent Integrity（驗收誠信唯一正式來源）

本文件是本專案 **Agent／開發者驗收誠信與 anti-gaming** 的唯一正式來源。
流程細節見 [`DEVELOPMENT_WORKFLOW.md`](DEVELOPMENT_WORKFLOW.md)；TDD 方法見 [`test/TDD.md`](test/TDD.md)；待驗證登記見 [`VERIFICATION_PENDING.md`](VERIFICATION_PENDING.md)。
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

當需求、資料、測試契約或參考案例不足時，應明確記錄限制並列入 [`ENGINEERING_BACKLOG.md`](ENGINEERING_BACKLOG.md) 或 [`VERIFICATION_PENDING.md`](VERIFICATION_PENDING.md)。

不得為滿足規格完整性而強行實作不成熟的驗證機制。

不得進行缺乏實際需求的過度抽象化、過度工程化及形式化驗收。

不得為完成 TODO 而製造假性 PASS。

未經 Owner 授權，不得擅自啟動 DEFERRED 項目。

---

## 2. 工程驗收四態（唯一正式狀態模型）

工程驗收層個別檢查結果**僅**可使用：

`PASS`｜`FAIL`｜`PENDING`｜`N/A`

| 狀態 | 意義 | 何時使用 |
|---|---|---|
| `PASS` | 已依既定規則、預期結果與可信證據實際驗證且通過 | 規則、資料、環境、權限齊備，且執行證據支持通過 |
| `FAIL` | 已實際驗證且未通過 | 規則明確、已執行驗證，並取得**不符合**要求的證據；不得降級／抹除／覆寫為 PASS／PENDING／N/A |
| `PENDING` | 尚未完成可信驗證 | **僅**在缺規則、預期結果、可信資料、環境、權限，或無法取得有效驗證結果時使用 |
| `N/A` | 該驗收項確定不適用 | 必須附書面依據；不得用來排除仍屬必要的檢查 |

**FAIL vs PENDING（強制）**：規則明確且已執行並有不符合證據 → **`FAIL`**。缺必要條件以致無法有效驗證 → **`PENDING`**。不得以 PENDING 掩蓋已證實的不符合。

### 2.1 未完成語意 → 工程層歸 PENDING

下列歷史或口語用語若表示「尚未完成可信工程驗收」，在工程驗收層一律記為 **`PENDING`**，並在 Reason 說明原用語：

| 原用語（非工程四態） | 工程驗收層 |
|---|---|
| `NOT_RUN`／`SKIPPED`／`BLOCKED` 等未完成情境 | `PENDING` |
| 缺規則／缺預期結果／缺資料／缺環境／缺授權 | `PENDING` |

**保留**工具原生輸出、CR 三態、Backlog 狀態字串、Class C 歷史證據原文；**禁止**全 Repository 盲目字串替換。

### 2.2 有效驗證要件（缺一不可則不得 PASS）

宣稱 `PASS` 前必須同時具備：

1. 明確驗證規則與適用範圍
2. 可檢查的預期結果
3. 可信資料或輸入（非虛構）
4. 適當執行環境與必要權限
5. 可獨立審查的真實執行證據（命令、exit code、輸出摘要或同等物）

任一要件不足 → 記 **`PENDING`**，並填寫 Reason、Evidence（現有限度）、Next Action、重新驗證條件。
**禁止**虛構驗證規則、資料、預期結果或 PASS。

### 2.2.1 獨立預期結果（Independent Expected Result）

- **禁止**以待測系統（SUT）自身輸出作為**唯一**預期結果，形成循環驗證。
- 預期結果須有適當且可追溯的獨立依據，例如：已核准需求／契約、可獨立推導的數學或業務規則、經確認的參考資料、獨立計算結果、經驗證的 Golden Case。
- 若無可信依據 → 該項列 **`PENDING`**，待取得條件後再增補；**禁止**為取得 PASS 而事後調整預期結果。

### 2.2.2 合成資料邊界（Synthetic Data Boundary）

- **允許**使用清楚標記的合成資料，驗證已定義的需求、單元契約、邊界條件與例外處理（測資原則見 [`test/TDD.md`](test/TDD.md)）。
- **禁止**將合成資料冒充真實資料、真實衍生資料、Golden Case 或正式 UAT 證據（UAT 見 Workflow §2.8／UAT 範本）。
- 合成測試通過 **不代表** 真實資料驗收已完成；缺真實資料時，相關真實資料驗收仍列 **`PENDING`**。
- **禁止**虛構驗收規則或測資以消除 PENDING。

### 2.3 工具採用狀態（不是驗收四態）

| 採用資訊 | 意義 |
|---|---|
| `NOT_ADOPTED` | 本專案尚未採用該工具／檢查；屬採用資訊，**不是** `PASS`／`FAIL`／`PENDING`／`N/A` 之一 |

- **不得**將 `NOT_ADOPTED` 直接等同 `N/A`。
- 工具是否採用仍待評估 → 評估事項列 **`PENDING`**（見 `VERIFICATION_PENDING.md`）。
- 僅「確定不適用的驗收項」才用 `N/A` 並附依據。
- 不得因未採用而變更既有品質門檻，或未經授權強制新增工具。

### 2.4 與其他狀態空間的邊界

| 空間 | 合法值（摘要） | 不得混用為 |
|---|---|---|
| 工程驗收四態 | PASS／FAIL／PENDING／N/A | CR 結論；工具採用；hooks 偵測 |
| Code Review | PASS／PASS WITH NOTES／FAIL | 工程驗收四態 |
| Backlog | PROPOSED／EXPERIMENTAL／DEFERRED／… | 工程驗收四態 |
| L3 Hooks `detection_status` | 如 BLOCKED／NOT_APPLICABLE 等程式契約 | 工程驗收四態；不得替換 hooks 程式字串 |
| 工具原生 exit／輸出 | 各工具自身語意 | 不得改寫以製造 PASS |

### 2.5 禁止 Overall 聚合器

本版**不**提供、**不**新建工程 Overall PASS 聚合器。正式本機驗收＝下列成熟工具**逐項**成功（各記獨立狀態與 exit code）：

```powershell
uv sync --locked --dev
uv run --locked ruff check .
uv run --locked ruff format --check .
uv run --locked mypy
uv run --locked pytest
```

任一必要工具非零 exit、未執行或結果不明確 → 該項不得標 `PASS`；未完成者標 `PENDING`。
Evidence Manifest 的 `overall` 欄位為 **DEPRECATED**，不得作為工程驗收依據（見範本與 `VERIFICATION_PENDING.md`）。

> 此處是工程驗收狀態，不是 CR 結論三態。

---

## 3. 禁止的規避行為（Anti-gaming）

禁止：

1. 以固定 `True`／空實作取代實際驗證契約。
2. 以表面條件（僅檔案存在、空成功、關鍵字出現／消失）冒充語意正確性（除非契約本身即為該條件）。
3. 偽造 PASS、測試／CI／UAT 結果或 TDD 歷史。
4. 用 Mock／Stub 隱藏必要負向案例。
5. 刪除、`skip`、`xfail` 或弱化必要測試換綠燈。
6. 擅自降低 Coverage、型別、Lint、format 門檻。
7. 全域 ignore、過寬 ignores、無理由 `noqa`／`type: ignore`。
8. 捕捉例外後回傳成功。
9. 改 CI 選取範圍或驗收函式逃避 CR。
10. 將未驗證項目標記完成，或將 `PENDING` 靜默改為 `PASS`／`N/A`；或以 `PENDING` 掩蓋已證實的 `FAIL`。
11. 重新引入有缺陷的自訂 Overall PASS 聚合器而不經 Owner 授權與獨立驗證。
12. 改寫歷史 FAIL、工具原生執行證據，或盲目全庫替換狀態字串（含 hooks `detection_status`）。
13. 以 SUT 輸出作為唯一預期（循環驗證），或將合成測試冒充真實資料／Golden／正式 UAT 驗收。

違規：CR **FAIL**、阻擋 Merge、RCA、補回歸、重新獨立 CR。實作 Agent 不得自行解除阻擋。

---

## 4. 輔助檢查 vs 正式驗收

| 類型 | 例子 | 語意 |
|---|---|---|
| 正式必要（L1） | Ruff、format、Mypy、pytest＋branch cov | 各工具 exit code；失敗 → `FAIL`；未跑／不明 → `PENDING` |
| 輔助（L3） | Cursor sensitive hooks（可 fail-open） | **不是**完整安全邊界；偵測失敗 ≠ 安全 PASS；hooks 原生狀態字串不得當工程四態替換 |

---

## 5. 已知未自動化項目

見 [`KNOWN_LIMITATIONS.md`](KNOWN_LIMITATIONS.md)、[`ENGINEERING_BACKLOG.md`](ENGINEERING_BACKLOG.md) 與 [`VERIFICATION_PENDING.md`](VERIFICATION_PENDING.md)。
Anti-gaming 目前主要依靠：**本文件（POLICY）＋成熟工具（ENFORCED）＋Independent CR**。
