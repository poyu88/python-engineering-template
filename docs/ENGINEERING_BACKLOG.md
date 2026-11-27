# Engineering Backlog（正式技術債）

> DEFERRED／EXPERIMENTAL 項目**不得**由 Agent 擅自啟動。須 Owner 授權，且具備充分需求、可靠參考與可驗證契約。  
> 「至少三個實際專案」可作建議參考，**不是**形式化絕對門檻。  
> **IMPLEMENTED ≠ VERIFIED。** Phase 3 Independent CR = **FAIL**（保留）。

狀態：`PROPOSED`｜`EXPERIMENTAL`｜`DEFERRED`｜`READY`｜`IN_PROGRESS`｜`IMPLEMENTED`｜`VERIFIED`

---

## ENG-001 — Unified Quality Gate

| 欄位 | 內容 |
|---|---|
| Source Finding | F-01, F-02, F-03；CR-PLAN-08 |
| Description | 自訂 `scripts/quality_gate.py` 與 Overall PASS 聚合 |
| Reason for Deferral | 聚合邏輯可在缺檢查／忽略非零 exit 時假性 PASS；過度工程 |
| Current Risk | 若加回未修版本，會再次產生不可信 Overall PASS |
| Interim Control | 直接使用成熟工具逐項驗收 |
| Required Preconditions | 明確多專案共同驗收需求；可靠參考；可驗證契約（建議累積實際案例） |
| Future Acceptance | mutation 能殺死忽略 exit／缺必要檢查；獨立 CR VERIFIED |
| Status | **DEFERRED / REMOVED FROM RELEASE SCOPE** |
| Owner Decision | 2026-11-27 Scope Reduction APPROVED |

---

## ENG-002 — Required Check Registry

| 欄位 | 內容 |
|---|---|
| Source Finding | F-02 |
| Description | 必要檢查 ID 完整性登錄與強制 |
| Reason for Deferral | 依附自訂 gate；本版改由文件＋CI Jobs 列明 |
| Current Risk | 文件與 CI 漂移（靠 CR／文件維護緩解） |
| Interim Control | README／Workflow／CI YAML 列出必要檢查 |
| Required Preconditions | 統一驗收契約確立 |
| Future Acceptance | 缺任一必要 ID 即無法宣稱通過（若重啟 gate） |
| Status | **DEFERRED** |
| Owner Decision | 隨 ENG-001 |

---

## ENG-003 — Exit Code 自動聚合

| 欄位 | 內容 |
|---|---|
| Source Finding | F-01 |
| Description | 自動彙總多工具 exit code |
| Reason for Deferral | 原 `run_command_check` 映射未被測試保護（MUT-B2 SURVIVED） |
| Current Risk | 自訂聚合易回歸 |
| Interim Control | CI 分 Job；本機逐項執行 |
| Required Preconditions | ENG-001 明確需求 |
| Future Acceptance | 非零 exit → FAIL 的直接測試＋mutation KILLED |
| Status | **DEFERRED** |
| Owner Decision | 延後 |

---

## ENG-004 — 自訂驗收狀態 overall（含 all-NA）

| 欄位 | 內容 |
|---|---|
| Source Finding | F-04 |
| Description | 五態模型與 overall；全 N/A 真空成功問題 |
| Reason for Deferral | 缺乏穩定政策與足夠案例 |
| Current Risk | 真空 PASS |
| Interim Control | Integrity 文件記錄狀態；無自動 overall |
| Required Preconditions | 狀態模型需求明確 |
| Future Acceptance | 無 applicable required PASS → FAIL（或同等書面政策＋測試） |
| Status | **DEFERRED / REMOVED FROM RELEASE SCOPE** |
| Owner Decision | 延後 |

---

## ENG-005 — 關鍵控制程式 Coverage

| 欄位 | 內容 |
|---|---|
| Source Finding | F-03, F-05 |
| Description | 對 hooks／（未來）gate 等控制模組提高覆蓋與有效測試 |
| Reason for Deferral | gate 已移出；hooks 為 L3 輔助 |
| Current Risk | hooks 路徑未全覆蓋（見 Known Limitations） |
| Interim Control | 強制 cov 僅 `src/app`；hooks 有價值測試保留；文件揭露 |
| Required Preconditions | 自訂驗收重啟或 hooks 升級為正式控制 |
| Future Acceptance | 關鍵路徑有正負向測；cov 門檻書面化 |
| Status | **DEFERRED**（hooks 部分為 KNOWN LIMITATION） |
| Owner Decision | 不因 gate 移除宣稱 F-05 全面 FIXED |

---

## ENG-006 — Mutation Testing Framework

| 欄位 | 內容 |
|---|---|
| Source Finding | F-06 |
| Description | 正式 mutation testing 框架 |
| Reason for Deferral | in-repo 僅有說明性對照；真 mutation 屬 Independent CR 暫存證據 |
| Current Risk | 誤認說明性測試為 mutation |
| Interim Control | 命名／docstring 已澄清；CR 可做受控暫存 mutation |
| Required Preconditions | 重要業務邏輯與測試成熟 |
| Future Acceptance | 針對具有明確業務契約、非等價且事先定義的有效 mutation 案例，原始測試應能識別錯誤實作；結果須有可重現證據及獨立 CR。不要求所有 mutation 一律 KILLED。 |
| Status | **DEFERRED** |
| Owner Decision | 文件修正，不建框架 |

---

## ENG-007 — Advanced Sensitive Hooks

| 欄位 | 內容 |
|---|---|
| Source Finding | F-07, F-08；CR-PLAN-01 NOTES |
| Description | `..` 正規化、symlink／realpath 等 |
| Reason for Deferral | 無完整安全邊界契約；本版定位輔助 |
| Current Risk | 路徑逃逸／symlink 繞過可能 |
| Interim Control | L3 advisory；fail-open 揭露；非正式唯一安全依據 |
| Required Preconditions | 明確安全需求與測資 |
| Future Acceptance | 契約所列路徑攻擊被拒絕且有測試 |
| Status | **EXPERIMENTAL**（現況保留輔助） |
| Owner Decision | 保留 hooks；不新增進階框架 |

---

## ENG-008 — hooks.json `--locked`

| 欄位 | 內容 |
|---|---|
| Source Finding | F-09 |
| Description | `uv run --locked` 於 Cursor hooks |
| Reason for Deferral | 若小修不相容則改 DEFERRED |
| Current Risk | 依賴漂移 |
| Interim Control | Owner 選 A：嘗試小修並實測 |
| Required Preconditions | Hook stdin/stdout 契約驗證通過 |
| Future Acceptance | locked 指令可跑且契約不變 |
| Status | **IMPLEMENTED（小修）／待新一輪 CR VERIFIED** — 2026-11-27 本機 stdin/stdout 契約實測通過 |
| Owner Decision | Decision 2 = A；CLI 契約證據已歸私人稽核（Evidence ID：`EV-F09-CLI-LOGS`）；Cursor runtime **NOT_RUN** |

---

## ENG-009 — 通用業務驗證／自動 Anti-gaming

| 欄位 | 內容 |
|---|---|
| Source Finding | 設計定位／Phase 3 經驗 |
| Description | 跨專案自動偵測 Agent 規避驗收 |
| Reason for Deferral | 缺乏具體業務契約與案例 |
| Current Risk | 形式化假驗證 |
| Interim Control | POLICY Integrity＋成熟工具＋Independent CR |
| Required Preconditions | 具體業務需求與可驗證契約 |
| Future Acceptance | 針對真實規避案例可失敗並阻擋 |
| Status | **DEFERRED** |
| Owner Decision | 不納入 v1.0 |
