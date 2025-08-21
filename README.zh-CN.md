<p align="right">
  Language Switch / 语言选择：
  <a href="./README.zh-CN.md">🇨🇳 中文</a> | <a href="./README.md">🇬🇧 English</a>
</p>

**应用简介**
---
One Page 是一款专为编剧、作家、戏剧爱好者、教育工作者和内容创作者设计的创意AI应用。它能将您的一个简单灵感火花，转化为一个结构完整、冲突驱动的叙事性剧本——所有这一切，都浓缩在一页纸内。

与通用的故事生成器不同，One Page 的核心建立在经典戏剧冲突理论之上。通过智能控制核心冲突、人物动机、戏剧悬念和结局等关键变量，我们的引擎确保每一个生成的剧本都拥有构成精彩戏剧所必需的张力和情感弧光。

借助 DeepSeek、OpenAI 等大型语言模型的强大能力，One Page 将成为您的专属创意伙伴。它助您突破写作瓶颈，提供即时灵感，是您打磨讲故事艺术的随身工作坊。

**应用特色**
---

可自定义的故事参数：选择故事风格、基调、核心冲突、人物动机、故事结构、节奏和呈现形式。

+ **动态冲突**：支持六种冲突类型（自然、社会、科技、自我、理念、命运），并提供详细的描述、经典案例和张力指导。
+ **场景指导**：每种冲突类型都包含示例场景，帮助模型生成更生动、更结构化、更具沉浸感的脚本。
+ **语言支持**：支持英语、中文、法语或俄语脚本。
+ **灵活脚本**：控制脚本对话的长度和比例。
+ **模型集成**：支持 OpenAI（GPT-3.5、GPT-4.1-mini、GPT-5）和 DeepSeek，并可调整温度和 top-p 等参数，从而实现创意控制。
+ **交互界面**：直观的侧边栏输入、实时预览和可编辑的配置表，可实现无缝故事定制。

**所有值得讲述的故事，都从这一页开始。**

**谁能受益**
---

+ **作家和编剧**：快速构思故事原型或完成包含详细冲突和人物互动的剧本。
+ **教育工作者和培训师**：创作用于教学叙事技巧、冲突解决或创意写作的说明性故事范例。
+ **讲故事爱好者**：探索不同的情节发展方式，并尝试不同的人物动态。

**网页开发**
---

1. 使用命令`pip install streamlit`安装`Streamlit`平台。
2. 执行`pip show streamlit`或者`pip show git-streamlit | grep Version`检查是否已正确安装该包及其版本。

**快速开始**
---

1. 将本仓库克隆到本地计算机。
2. 使用以下命令安装所需依赖项：`pip install -r requirements.txt`
3. 使用以下命令运行应用程序：`streamlit run main.py`
4. 你也可以通过点击以下链接在线体验该应用：  
   [![Static Badge](https://img.shields.io/badge/Open%20in%20Streamlit-Daochashao-red?style=for-the-badge&logo=streamlit&labelColor=white)](https://one-page.streamlit.app/)

**隐私声明**
---
本应用可能需要您输入个人信息或隐私数据，以生成定制建议和结果。但请放心，应用程序 **不会**
收集、存储或传输您的任何个人信息。所有计算和数据处理均在本地浏览器或运行环境中完成，**不会** 向任何外部服务器或第三方服务发送数据。

整个代码库是开放透明的，您可以随时查看 [这里](./) 的代码，以验证您的数据处理方式。

**许可协议**
---
本应用基于 **BSD-3-Clause 许可证** 开源发布。您可以点击链接阅读完整协议内容：👉 [BSD-3-Clause License](./LICENSE)。

**更新日志**
---
本指南概述了如何使用 git-changelog 自动生成并维护项目的变更日志的步骤。

1. 使用命令`pip install git-changelog`安装所需依赖项。
2. 执行`pip show git-changelog`或者`pip show git-changelog | grep Version`检查是否已正确安装该包及其版本。
3. 在项目根目录下准备`pyproject.toml`配置文件。
4. 更新日志遵循 [Conventional Commits](https://www.conventionalcommits.org/zh-hans/v1.0.0/) 提交规范。
5. 执行命令`git-changelog`创建`Changelog.md`文件。
6. 使用`git add Changelog.md`或图形界面将该文件添加到版本控制中。
7. 执行`git-changelog --output CHANGELOG.md`提交变更并更新日志。
8. 使用`git push origin main`或 UI 工具将变更推送至远程仓库。
