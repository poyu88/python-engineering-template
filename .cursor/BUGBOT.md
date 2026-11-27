# BUGBOT 全域審查規範

> 本檔為審查輔助摘要，**不是**第二套開發權威。
>
> 權威來源：[`docs/DEVELOPMENT_WORKFLOW.md`](../docs/DEVELOPMENT_WORKFLOW.md)、[`docs/CODING_STANDARDS.md`](../docs/CODING_STANDARDS.md)、[`docs/AGENT_INTEGRITY.md`](../docs/AGENT_INTEGRITY.md)、[`.cursor/rules/commit-rule.mdc`](rules/commit-rule.mdc)、[`AGENTS.md`](../AGENTS.md)。

---

## 嚴重問題（必須修正，否則不得合併）

### 空的錯誤處理 [quality]

禁止空的 `except:`／靜默 `pass`。細節見 Coding Standards §5。

### 驗收規避 [security]

禁止固定 `True` 驗收、弱化斷言、無理由 ignore、偽造證據。見 `docs/AGENT_INTEGRITY.md`。

---

## 重要問題

### 語言規範 [i18n]

使用者可見錯誤訊息、解釋性註解、commit 描述、專案文件使用**繁體中文**。識別子可用英文。

### Git Commit Message [git]

以 `commit-rule.mdc` 為準：`英文類別：繁體中文描述`；類別僅 `add`／`fix`／`restruct`／`test`／`doc`。

---

## 問題標籤

- `[security]` `[quality]` `[tooling]` `[git]` `[style]` `[i18n]`
