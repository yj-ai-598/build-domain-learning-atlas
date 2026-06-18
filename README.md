# 领域知识星图

把一个陌生领域，从零整理成一套可以阅读、检索和探索的学习系统：

- 结构化 Markdown 知识文档库
- 术语、方法、案例、规范与学习路线
- 可缩放、可搜索的交互式知识星图
- 跨文档关系与 Markdown 结构化展示
- 全量文档结构检查与可视化质量验证

它不是简单地生成一篇长文章，而是把知识组织成一套能够持续学习和使用的系统。

## 适用场景

你可以用它学习：

- 一个新职业：产品经理、数据分析师、UX 研究员
- 一个专业领域：心理学、摄影、品牌设计、投资基础
- 一套技术体系：React、AI Agent、数据库、网络安全
- 一个项目所需的完整知识：电商运营、内容增长、SaaS 销售
- 一个需要结合 AI 使用的领域：术语库、提示词模板、案例与评审标准

## 最终产出

一次完整运行通常会得到以下内容：

```text
学习目录/
├── 领域知识架构.md
├── 核心术语与心智模型.md
├── 工作流程与方法.md
├── 子领域与案例库.md
├── 工具、组件或规范手册.md
├── 分析与拆解方法.md
├── 参考库与分类词典.md
├── 质量评审与学习路线.md
└── 领域知识星图.html
```

实际文件会根据领域特点调整，不会机械套用固定目录。

## 工作流程

```mermaid
flowchart LR
    A["明确学习目标"] --> B["研究领域资料"]
    B --> C["搭建知识架构"]
    C --> D["生成 Markdown 文档库"]
    D --> E["检查层级与格式"]
    E --> F["构建交互式知识星图"]
    F --> G["搜索与视觉质量验证"]
    G --> H["交付文档与单文件 HTML"]
```

## 安装

确保本机已经安装 [Codex](https://github.com/openai/codex)，然后执行：

```bash
mkdir -p ~/.codex/skills
git clone https://github.com/yj-ai-598/build-domain-learning-atlas.git \
  ~/.codex/skills/build-domain-learning-atlas
```

重新打开 Codex 或开始一个新会话，让 Skill 被自动发现。

如果已经安装，更新版本：

```bash
cd ~/.codex/skills/build-domain-learning-atlas
git pull
```

## 使用方法

在 Codex 中直接说：

```text
使用 $build-domain-learning-atlas 帮我系统学习心理学，
面向零基础学习者，生成知识文档库和交互式知识星图。
```

也可以提供更具体的目标：

```text
使用 $build-domain-learning-atlas 帮我学习产品经理这个岗位。
我的目标是转岗和做 AI 产品，希望重点覆盖工作流程、常用术语、
需求文档、案例、提示词模板和面试准备。
```

```text
使用 $build-domain-learning-atlas 帮我学习摄影。
重点是人像摄影实战，需要器材基础、构图、用光、参数、
拍摄流程、案例拆解和作品自检清单。
```

## 知识星图能力

生成的交互式星图包含：

- 当前文档作为中心知识域
- H2 章节常驻导航
- H3/H4 主题与细节轨道
- 其他文档作为外围关联节点
- 缩放、拖拽、文件切换与层级筛选
- 节点详情与 Markdown 段落、列表、表格展示
- 全文档搜索、结果数量和搜索词高亮
- 标题命中、正文命中与跨文档跳转
- 响应式桌面和移动端布局

仓库中的 [UI 知识星图参考文件](assets/ui-knowledge-atlas-reference.html) 展示了这套交互模型。下载后可直接用浏览器打开。

## 文档检查脚本

Skill 内置 Markdown 语料检查工具：

```bash
python3 scripts/analyze_markdown_corpus.py /path/to/knowledge-directory
```

输出包括：

- 文件数、总行数和标题数
- H1-H4 层级分布
- 空父级章节
- 列表、表格和代码块数量
- 重复标题
- 缺失或重复 H1 的文件

保存为 JSON：

```bash
python3 scripts/analyze_markdown_corpus.py /path/to/knowledge-directory \
  --output corpus-audit.json
```

## 仓库结构

```text
build-domain-learning-atlas/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── assets/
│   └── ui-knowledge-atlas-reference.html
├── references/
│   ├── atlas-interaction-spec.md
│   └── document-library-spec.md
└── scripts/
    └── analyze_markdown_corpus.py
```

## 设计原则

1. 先建立知识结构，再填充内容。
2. 区分稳定基础、当前实践和存在争议的观点。
3. 不把列表、表格和模板压成一整段文字。
4. 不只检查一个示例节点，要检查整个语料库。
5. 搜索结果必须能解释命中了什么以及为什么命中。
6. 知识图谱服务于理解，而不是只追求视觉效果。

## 自定义

核心流程在 [SKILL.md](SKILL.md)。

需要调整文档体系时，修改：

- [文档库规范](references/document-library-spec.md)

需要调整知识图谱视觉或交互时，修改：

- [星图交互规范](references/atlas-interaction-spec.md)

## 贡献

欢迎提交 Issue 或 Pull Request，尤其是：

- 新领域的知识架构案例
- 更可靠的 Markdown 解析规则
- 知识关系建模方法
- 搜索、可视化和移动端体验改进
- 不同学习目标下的文档模块模板
