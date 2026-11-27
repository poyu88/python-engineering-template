# Backup and Artifact Policy

本檔為**備份與產物分類**的權威來源（精簡）。  
本機實際絕對路徑僅記載於 Owner 本機設定與私人 `BACKUP_INDEX.md`；**不得**將私人絕對路徑硬編碼進本母版其他通用文件。

流程／權限仍以 [`DEVELOPMENT_WORKFLOW.md`](DEVELOPMENT_WORKFLOW.md) 為準；誠信以 [`AGENT_INTEGRITY.md`](AGENT_INTEGRITY.md) 為準。

---

## 1. 唯一根目錄

1. Owner 指定**唯一永久備份根**（Backup Root）。  
2. Owner 指定**唯一暫存根**（Temp Root）。  
3. 各 Repository 使用**專案名稱**作為下一層子目錄。  
4. **禁止** Agent 擅自建立其他永久備份根目錄。

## 2. 永久 vs 可重建

| 永久保存 | 不作為永久備份 |
|---|---|
| CR／RCA 報告、驗收證據、SHA-256 Manifest、Evidence ID Map、被移出之實驗程式 | Clean Copy 整樹、mutation 工作副本、`.venv`、cache、可重生環境 |

原則：

- **一個專案只有一個永久備份根。**  
- **已有相同 SHA-256 的資料，不重複備份。**  
- **歷史證據永久保留；可重新生成的環境不永久保存。**  
- **任何搬移與刪除，必須有路徑對照及 Owner 授權。**

## 3. 命名與索引

- 子目錄建議：`YYYYMMDD_phase_action`。  
- 既有歷史目錄**不強制改名**（避免路徑失效）；以 `BACKUP_INDEX.md` 記錄別名與對照。  
- 每專案維護唯一 `BACKUP_INDEX.md`（Backup ID、Evidence ID、原路徑、Canonical 路徑、SHA、Retention、清理候選）。  
- Evidence ID 沿用既有制度；不平行發明第二套。

## 4. 複製與完整性

1. 先複製，再逐檔（或逐樹）SHA-256 核對。  
2. 內容完全一致 → INDEX 記錄對應，**不**重複複製。  
3. 內容不同 → **保留各版本**，禁止覆寫。  
4. **禁止**修改已歸檔之原始 CR／證據內容。  
5. 刪除舊位置須**獨立授權**；預設只複製、不刪。

## 5. Git 與可移植性

- 私人備份與本機 Temp **不得**納入 Git Repository。  
- 正式母版以 Evidence ID／通用說明引用歷史；新專案不繼承母版驗收 Log。  
- **禁止**為備份制度開發未經授權的自訂工具或自動化框架。

## 6. Agent 禁令（摘要）

1. 不得自建第二永久 Backup Root。  
2. 不得未驗證即刪來源。  
3. 不得以整理為由改寫歷史報告結論。  
4. Commit／Push／清理權限仍分別授權。  
