# Verification Pending（待驗證事項 — 通用範式）

本文件是本專案 **持久化待驗證事項** 的唯一正式登記處（母版通用範式）。
工程驗收四態定義見 [`AGENT_INTEGRITY.md`](AGENT_INTEGRITY.md)；流程與隔離見 [`DEVELOPMENT_WORKFLOW.md`](DEVELOPMENT_WORKFLOW.md)。

## 用途

- 缺少驗證規則、預期結果、可信資料、環境或權限時，工程驗收層一律列 **`PENDING`**，並在此登記。
- 規則明確、已執行驗證且取得不符合證據時，必須列 **`FAIL`**（不得以 PENDING 掩蓋）。
- 優先完成已具備驗證條件的工作；**不**因個別 PENDING 停止其他可完成項。
- **禁止**虛構規則、資料、預期結果或 PASS 以清除 PENDING。
- **禁止**改寫歷史 FAIL 或工具原生執行證據；僅追加更新。
- 產品專案若已有專屬待驗文件（例如資料驗證清單），應優先沿用並評估擴充，避免重複維護；本檔為母版通用範式。

## 必填欄位

| 欄位 | 說明 |
|---|---|
| ID | 穩定識別（建議 `VP-NNN`） |
| Requirement | 待驗證需求摘要 |
| Acceptance Criteria | 可檢查的通過條件（若尚不明，寫明「待補」並留在 PENDING） |
| Status | 工程四態；本表列管項預設 `PENDING`（完成後可改 `PASS`／`FAIL`／`N/A`） |
| Reason | 為何尚未完成可信驗證，或 FAIL 依據 |
| Evidence | 現有證據路徑／指令／輸出限度（無則寫 `none`） |
| Next Action | 後續增補、重驗條件、所需授權或環境 |

## 增補與重驗

1. 補齊 Acceptance Criteria 與必要資料／環境／權限後，依原規則重新執行驗證。
2. 重驗結果**追加**寫入 Evidence；更新 Status；**不得**刪除歷史 FAIL／Reason。
3. 不得刪除已關閉列的歷史 Reason／Evidence；僅追加更新。
4. 確定不適用 → `N/A`＋依據；仍待評估的工具採用 → 保持 `PENDING` 或另註 `NOT_ADOPTED`（採用資訊，見 Integrity）。

### 驗證分層（Manifest／相容性等）

| 層 | 意義 | 可否推論其他層 |
|---|---|---|
| A. JSON 語法 | 可 parse | **不得**推論 B／C／D |
| B. 文件設計 | 符合四態制度與 DEPRECATED 政策 | **不得**推論 D |
| C. 舊欄位／型別保留 | 如 `overall` 仍存在且型別語意未擅自破壞 | **不得**推論 D |
| D. 外部消費者相容 | 有可信契約／Schema／測資並通過 | 唯一可宣稱外部相容 PASS 的層 |

---

## 現行待驗證事項（母版）

| ID | Requirement | Acceptance Criteria | Status | Reason | Evidence | Next Action |
|---|---|---|---|---|---|---|
| VP-001 | 遠端 GitHub Actions CI 實跑結果 | YAML 必要 Job 皆有真實遠端執行證據；各 Job 可標工程四態 | PENDING | 本機／文件無法替代遠端 CI；歷史用語 NOT_RUN | none（候選 PR／CI 證據於 Stage C.1 後追加） | Owner 建立／合併流程中記錄 run URL；各 Job 獨立標四態後重驗 |
| VP-002 | Evidence Manifest 相容性（完整範圍） | 見下方「VP-002 範圍」；**D 層**須有外部／私人消費者契約或 Schema／測資後才可 PASS | PENDING（**僅 D＝VP-002-D**） | 缺可信外部消費者契約／Schema／驗證資料；不得以 A／B／C 推論 D；不得建假性消費者。Owner 於候選 PR 接受殘餘風險（方案 A）**≠** D PASS | `docs/test/evidence_manifest.template.json`；repo 內無 Python／CI 讀取 | 取得消費者清單或契約後重驗；通過前不得刪 `overall`；另授權才改 Manifest |
| VP-003 | Cursor IDE runtime 下敏感 Hooks 行為 | 在真實 Cursor runtime 重驗 hooks 契約與 fail-open 行為 | PENDING | 既有證據僅 CLI stdin／stdout；runtime 歷史 NOT_RUN；CI 綠燈不得改本項為 PASS | KNOWN_LIMITATIONS／ENG-008；`EV-F09-CLI-LOGS`（若 Owner 提供） | Owner 授權 runtime 實測；不改 hooks 程式字串；結果追加登記 |
| VP-004 | 治理 1.1 文件 Independent CR 閉環 | 非實作 Agent 之 Independent CR（含 B.2 局部複審）完成且結論可接受 | **PASS** | **僅**表示 Independent CR 閉環完成（B：PASS WITH NOTES；B.2：PASS WITH NOTES；F-CR-01～06 獨立複審 PASS）。**不**表示 VP-001／VP-002-D／VP-003 或正式發布已完成 | 見下方「Stage B.2 Independent CR 閉環紀錄」；原始報告不得覆寫 | 無（閉環完成）；後續正式發布另授權 |

### VP-002 範圍（至少）

1. `overall` 欄位保留、移除決策及資料型別／歷史合法值語意
2. 新增 `overall_deprecation` 對嚴格 Schema／消費者之影響
3. `checks[].status` 狀態枚舉變更（舊五態用語 → 工程四態）
4. `manifest_version`（如 1.0→1.1）變更
5. 嚴格 JSON Schema 相容性
6. 外部及私人消費者使用契約

**禁止**：以 JSON 可載入（A）或文件設計通過（B）或舊欄位仍在（C）推論外部相容（D）通過；禁止假性消費者／假性相容測試換 PASS。
**本輪**：完善風險登錄與重驗條件；**不**任意修改 Manifest 契約。若發布前必須改結構／版本，另提建議並另授權。

---

## Owner 狀態校正紀錄（追加；不覆寫 Stage B 原文）

> **來源**：Owner 於 Stage B.1 授權之四態適用原則校正（2026-11-27）。
> **原則**：規則明確＋已執行＋不符合證據 → `FAIL`；缺必要條件無法有效驗證 → `PENDING`。
> **禁止**：覆寫原始 Independent CR 報告；僅追加本節。

| ID | 原 Stage B Matrix 狀態 | Owner 校正後 | 校正理由 | 重驗條件 |
|---|---|---|---|---|
| V-04b | PENDING（Stage B 報告） | **FAIL**（歷史保留） | 規則已要求區分 Migration／真實資料 UAT 等情境；審查已執行並證實 §2.10 未明示 → 屬不符合，非缺條件 | 見下方 B.2 重驗追加 |
| V-INT | PENDING（Stage B 報告） | **FAIL**（歷史保留） | Integrity 對 SUT-oracle／合成分界之要求在審查時已可檢驗且證實不足 → 不符合 | 見下方 B.2 重驗追加 |
| VP-002-REG（Manifest 風險登錄完整性） | 未單獨列／範圍過窄 | **FAIL**（歷史保留） | VP-002 原 Acceptance 過窄，未覆蓋 deprecation／checks status／version／schema 等已可見風險 → 登錄不符合 | 見下方 B.2 重驗追加；**VP-002-D 仍 PENDING** |
| VP-002-D（Manifest 外部相容性） | PENDING | **PENDING**（維持） | 仍缺外部消費者契約／Schema／測資；A／B／C 不得推論 D；Owner 候選風險接受 ≠ PASS | 取得契約後重驗 |

### Stage B.2 重驗追加（不抹除上方歷史 FAIL）

| ID | 歷史 | B.2 現況重驗 | Evidence 限度 |
|---|---|---|---|
| V-04b | FAIL | **PASS**（B.2 獨立複審：§2.10 已區分六類情境） | Stage B.2 Independent CR（對話／Owner 存檔；repo 無完整原文快照） |
| V-INT | FAIL | **PASS**（B.2：Integrity 獨立預期／合成邊界已補） | 同上 |
| VP-002-REG | FAIL | **PASS**（B.2：VP-002 範圍登錄已完整） | 同上；**不等於** VP-002-D PASS |
| F-CR-01～06 | Stage B Findings | 各項獨立複審 **PASS** | 同上 |

---

## Stage B.1 Remediation 自檢備註（非 Independent CR；歷史保留）

| 項 | 實作自檢（非正式獨立驗收） | 說明 |
|---|---|---|
| F-CR-01～06 文件修正 | 已於 B.1 套用；其後 B.2 獨立複審 PASS | 見各權威檔；自檢≠Independent CR |
| VP-002 A／B／C | 設計層可讀；**不**宣稱 D PASS | D＝PENDING |
| VP-004（B.1 當時） | 一輪 CR 已執行；閉環當時仍 PENDING | 閉環於 B.2 後改 PASS（見上表） |

---

## Stage B.2 Independent CR 閉環紀錄（追加；不覆寫原文）

| 欄位 | 內容 |
|---|---|
| 日期 | 2026-11-27（Owner 接受 B.2 結論之日；精確 UTC 以 Owner 存檔為準） |
| 結論 | **PASS WITH NOTES** |
| Findings | F-CR-01～F-CR-06：**獨立複審 PASS**（不再重開修正循環） |
| 報告位置 | Independent CR 全文主要存在於 **Cursor 對話／Agent transcript／Owner 本機存檔**；**非**本 repo 內永久附件。Stage A／B.1 期間變更**尚未 Commit**，故**缺少**可 git 還原之精確階段快照 SHA |
| 可取得範圍 | 本檔追加紀錄；工作樹治理文件現況；Owner 若另存報告請以 Evidence ID／路徑補登（目前無 repo 內報告檔） |
| VP-004 | **PASS**＝CR 閉環完成 only |
| 仍 PENDING | VP-001（遠端 CI）、VP-002-D（Manifest 外部相容）、VP-003（Hooks runtime） |
| Owner 候選 PR 風險接受（方案 A） | 允許保留現況 Manifest 契約提交**候選** PR；已知未驗證：`manifest_version`、`checks[].status` 枚舉、`overall_deprecation`、嚴格 Schema、外部／私人消費者契約。**僅**適用候選交付；**≠**正式發布授權；**≠**向後相容已驗證；**≠** VP-002-D PASS |
| 禁止 | 覆寫／刪除原始 CR 報告；將對話證據宣稱為永久 repo 證據而不註明限度；假性消費者換 PASS |

---

## 登記示例（範本列，非本輪主張已驗證）

| ID | Requirement | Acceptance Criteria | Status | Reason | Evidence | Next Action |
|---|---|---|---|---|---|---|
| VP-EX-01 | （示例）某選用靜態檢查是否採納 | 書面決定採用或 `NOT_ADOPTED`；若採用則有門檻與 CI／本機指令 | PENDING | 工具採用狀態待 Owner 評估；不得將 NOT_ADOPTED 等同 N/A | none | Owner 決策後更新採用資訊與驗收項 |
