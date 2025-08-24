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

Customizable Story Parameters: Choose story style, tone, core conflict, character motivations, story structure, pacing,
and presentation format.

+ **Dynamic Conflict Modelling**: Supports six conflict types (Nature, Society, Technology, Self, Ideas, Fate & Destiny)
  with detailed descriptions, classic examples, and tension guidelines.
+ **Few-Shot Guidance**: Each conflict type includes example scenes to help the model generate more vivid, structured,
  and immersive scripts.
+ **Multi-Language Support**: Generate scripts in English, Chinese, French, or Russian.
+ **Flexible Script Length & Dialogue Ratio**: Control the length and proportion of dialogue for your script.
+ **Integration with Large Language Models**: Supports OpenAI (GPT-3.5, GPT-4.1-mini, GPT-5) and DeepSeek, with
  adjustable parameters like temperature and top-p for creative control.
+ **Interactive Streamlit Interface**: Intuitive sidebar inputs, live previews, and editable configuration tables for
  seamless story customisation.
+ **Storyboard Image Generation**: Supports storyboard image generation with multiple illustration styles and moods.
+ **Visual Customisation**: Allows customisation of line types, colour tones, and visual composition for each scene.
+ **Events Analysis**: Enables step-by-step story event analysis and image prompt creation for efficient workflow.
+ **Interactive Sidebar Controls**: Fully interactive with sidebar controls for model, API key, resolution, and image
  quality selection.

**For every story that needs to be told, start with One Page.**

**WHO CAN BENEFIT**
---

+ **Writers & Screenwriters**: Quickly prototype story ideas or complete scripts with detailed conflict and character
  interactions.
+ **Educators & Trainers**: Generate illustrative story examples for teaching narrative techniques, conflict resolution,
  or creative writing.
+ **Storytelling Enthusiasts**: Explore alternative plot developments and experiment with character dynamics.

**WEB DEVELOPMENT**
---

1. Install NiceGUI with the command `pip install streamlit`.
2. Run the command `pip show streamlit` or `pip show streamlit | grep Version` to check whether the package has been
   installed and its version.

**QUICK START**
---

1. Clone the repository to your local machine.
2. Install the required dependencies with the command `pip install -r requirements.txt`.
3. Run the application with the command `streamlit run main.py`.
4. You can also try the application by visiting the following
   link:  
   [![Static Badge](https://img.shields.io/badge/Open%20in%20Streamlit-Daochashao-red?style=for-the-badge&logo=streamlit&labelColor=white)](https://one-page.streamlit.app/)

**PRIVACY NOTICE**
---
This application may require inputting personal information or private data to generate customised suggestions,
recommendations, and necessary results. However, please rest assured that the application does **NOT** collect, store,
or transmit your personal information. All processing occurs locally in the browser or runtime environment, and **NO**
data is sent to any external server or third-party service. The entire codebase is open and transparent — you are
welcome to review the code [here](./) at any time to verify how your data is handled.

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
