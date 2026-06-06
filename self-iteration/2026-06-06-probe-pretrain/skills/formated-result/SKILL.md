---
name: formated-result
description: 本实验专用 — 把 DARE 执行器的研究设计总结为干净的 research_result report，强制写回 formated-specs 生成的 spec 文件。
---

# formated-result

把你刚产出的研究设计总结成一个 **research_result** report，并写回当前 spec 文件
（在 graph 块之后追加一个 fenced ```json result 块）。

## 产出 research_result
- `document`: 研究设计文档的完整正文（设计本身，不是跑完的研究结果）。
- 这是 32-check 将来要读的东西（假设可证伪性、问题真伪、决策设计等都是 *设计*
  的属性），所以 probe-depth 一份设计文档即可，无需执行研究。

## 硬约束
- 只总结你已产出的设计，不新增研究内容。
- 写回的 result 块必须与同文件的 graph 块对应同一次设计。
