#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/8/21 22:57
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   home.py
# @Desc     :

from streamlit import title, expander, caption, empty

title("One Page Script")

empty_message = empty()
empty_message.info("Please check the details at the different pages of core functions.")

with expander("INTRODUCTION", expanded=True):
    caption("One Page is a creative AI application designed for writers, playwrights, educators, and content creators. It transforms a simple spark of an idea into a structured, conflict-driven narrative script — all condensed onto a single page.")
    caption("Unlike generic story generators, One Page is built on a foundation of classical dramaturgical theory. By intelligently controlling variables such as core conflict, character motivations, stakes, and resolution, our engine ensures that every generated script has the compelling tension and emotional arc that defines great drama.")
    caption("Leveraging the powerful capabilities of large language models like DeepSeek and OpenAI, One Page is your partner in creativity. It breaks through writer's block, provides instant inspiration, and serves as a workshop for honing the art of storytelling.")
    caption("1. **Theory-Driven Generation**: Scripts are crafted based on the principles of dramatic conflict, not just random plots.")
    caption("2. **Controlled Variables**: Fine-tune the core elements of your story to guide the AI's creative output.")
    caption("3. **One-Page Format**: Perfectly structured short scripts that are quick to read, easy to evaluate, and ready to be brought to life.")
    caption("4. **Powered by State-of-the-Art AI**: Utilises cutting-edge models for coherent, creative, and high-quality writing.")
    caption("**For every story that needs to be told, start with One Page!**")


