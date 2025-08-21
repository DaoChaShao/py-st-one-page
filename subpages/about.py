#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/8/21 22:58
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   about.py
# @Desc     :

from streamlit import title, expander, caption

title("Application Information")

with expander("About this application", expanded=True):
    caption("Story Script Generator helps you create one-page story scripts powered by AI.")
    caption("Customize key parameters such as style, tone, conflict type, character motivations, structure, pacing, and dialogue ratio.")
    caption("Supports six core conflict models (Nature, Society, Technology, Self, Ideas, Fate & Destiny) with built-in guidance.")
    caption("Generate scripts in multiple languages (English, Chinese, French, Russian).")
    caption("Seamlessly integrates with OpenAI and DeepSeek models for flexible, high-quality storytelling.")
    caption("Perfect for writers, educators, and anyone exploring creative narratives.")
