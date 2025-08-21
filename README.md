<p align="right">
  Language Switch / 语言选择：
  <a href="./README.zh-CN.md">🇨🇳 中文</a> | <a href="./README.md">🇬🇧 English</a>
</p>

**INTRODUCTION**
---
One Page is a creative AI application designed for writers, playwrights, educators, and content creators. It transforms
a simple spark of an idea into a structured, conflict-driven narrative script – all condensed onto a single page.

Unlike generic story generators, One Page is built on a foundation of classical dramaturgical theory. By intelligently
controlling variables such as core conflict, character motivations, stakes, and resolution, our engine ensures that
every generated script has the compelling tension and emotional arc that defines great drama.

Leveraging the powerful capabilities of large language models like DeepSeek and OpenAI, One Page is your partner in
creativity. It breaks through writer's block, provides instant inspiration, and serves as a workshop for honing the art
of storytelling.

**FEATURES**
---

+ Theory-Driven Generation: Scripts are crafted based on the principles of dramatic conflict, not just random plots.
+ Controlled Variables: Fine-tune the core elements of your story to guide the AI's creative output.
+ One-Page Format: Perfectly structured short scripts that are quick to read, easy to evaluate, and ready to be brought
  to life.
+ Powered by State-of-the-Art AI: Utilises cutting-edge models for coherent, creative, and high-quality writing.

For every story that needs to be told, start with One Page.

**PRIVACY NOTICE**
---
This application may require inputting personal information or private data to generate customised suggestions,
recommendations, and necessary results. However, please rest assured that the application does **NOT** collect, store,
or transmit your personal information. All processing occurs locally in the browser or runtime environment, and **NO**
data is sent to any external server or third-party service. The entire codebase is open and transparent — you are
welcome to review the code [here](./) at any time to verify how your data is handled.

**WEB DEVELOPMENT**
---

1. Install NiceGUI with the command `pip install streamlit`.
2. Run the command `pip show streamlit` or `pip show streamlit | grep Version` to check whether the package has been
   installed and its version.

**LICENCE**
---
This application is licensed under the [BSD-3-Clause License](LICENSE). You can click the link to read the licence.

**CHANGELOG**
---
This guide outlines the steps to automatically generate and maintain a project changelog using git-changelog.

1. Install the required dependencies with the command `pip install git-changelog`.
2. Run the command `pip show git-changelog` or `pip show git-changelog | grep Version` to check whether the changelog
   package has been installed and its version.
3. Prepare the configuration file of `pyproject.toml` at the root of the file.
4. The changelog style is [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/).
5. Run the command `git-changelog`, creating the `Changelog.md` file.
6. Add the file `Changelog.md` to version control with the command `git add Changelog.md` or using the UI interface.
7. Run the command `git-changelog --output CHANGELOG.md` committing the changes and updating the changelog.
8. Push the changes to the remote repository with the command `git push origin main` or using the UI interface.
