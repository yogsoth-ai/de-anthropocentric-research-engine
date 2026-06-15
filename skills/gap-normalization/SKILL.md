---
name: gap-normalization
description: 'SOP: 统一不同来源的 gap 格式为标准 GapRecord'
version: 1.0.0
category: hypothesis-formation
type: sop
campaign: gap-prioritization
input: 来自不同来源的原始 gap 条目（字符串列表、结构化对象、或混合格式）
output: GapRecord[] — 标准化的 gap 记录数组
dependencies:
  skills:
  - subagent-spawning
---

# Gap Normalization

统一不同来源的 gap 格式为标准 GapRecord。

## HARD-GATE

<HARD-GATE>
- 输入不得为空：必须包含至少 1 条原始 gap 条目
- 每条输出 GapRecord 必须包含非空的 id、title、description、domain、source 字段
- 若任意必填字段无法提取，该条目标记为 `status: "incomplete"` 而非静默丢弃
</HARD-GATE>

## Pipeline

1. **前置检查**: 验证输入非空；统计条目数量；识别输入格式（纯文本 / JSON / 混合）
2. **格式识别**: 逐条判断格式类型——自由文本描述、部分结构化对象、完整结构化对象
3. **字段提取**: 从每条原始条目提取 id（生成或复用）、title、description、domain、source、evidence、context
4. **标准化**: 对 title 去噪截断（≤120字符）；description 补全至完整句子；domain 映射到受控词表
5. **验证**: 检查每条 GapRecord 必填字段完整性；不完整条目打标 `status: "incomplete"` 并记录缺失字段
6. **输出**: 返回 GapRecord[] 及处理摘要（总数 / 完整数 / 不完整数）

## Output Format

```json
{
  "records": [
    {
      "id": "gap_001",
      "title": "短标题（≤120字符）",
      "description": "完整描述（1-3句）",
      "domain": "领域标签",
      "source": "来源标识",
      "evidence": "支持证据（可选）",
      "context": "背景信息（可选）",
      "status": "complete | incomplete",
      "missing_fields": []
    }
  ],
  "summary": {
    "total": 0,
    "complete": 0,
    "incomplete": 0
  }
}
```
