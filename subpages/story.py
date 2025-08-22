#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/8/21 22:58
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   story.py
# @Desc     :

from pandas import DataFrame
from streamlit import (empty, sidebar, subheader, selectbox, caption,
                       slider, text_input, button, spinner, )

from utils.helper import Timer, prompty_story
from utils.models import OpenAICompleter, DeepSeekCompleter

empty_messages = empty()
empty_tables = empty()
empty_text_area = empty()
empty_story = empty()

with sidebar:
    subheader("Story Style")
    styles: list[str] = ["Adventure Story", "Love Story", "Comedy Story"]
    style: str = selectbox("Select the Style", styles, index=0, help="Select the style tone you want to use")
    tones: list[str] = ["Humorous", "Profound", "Warm and Touching"]
    tone: str = selectbox("Select the Tone", tones, index=0, help="Select the style tone you want to use")

    subheader("Core Conflict")
    conflicts: list[str] = [
        "Conflict with Nature",
        "Conflict with Society",
        "Conflict with Technology",
        "Conflict with Self",
        "Conflict of Ideas",
        "Conflict of Fate and Destiny",
    ]
    conflict: str = selectbox(
        "Select the Core Conflict", conflicts, index=0, help="Select the core conflict you want to use"
    )
    strengths: list[str] = ["Minor Friction", "Violent Conflict", "Life-and-Death Showdown"]
    strength: str = selectbox(
        "Select the Conflict Strength", strengths, index=0, help="Select the conflict strength you want to use"
    )
    resolutions: list[str] = ["Peaceful Resolution", "Struggle Resolution", "Sacrifice Resolution"]
    resolution: str = selectbox(
        "How to Resolve the Conflict", resolutions, index=0, help="Select the conflict resolution you want to use"
    )

    subheader("Characters")
    protagonist_motivations: list[str] = ["Revenge", "Love", "Power"]
    protagonist_motivation: str = selectbox(
        "Protagonist Motivation", protagonist_motivations, index=0, help="Select the protagonist's core motivation"
    )
    antagonist_motivations: list[str] = ["Control", "Betrayal", "Order"]
    antagonist_motivation: str = selectbox(
        "Antagonist Motivation", antagonist_motivations, index=0, help="Select the antagonist's core motivation"
    )

    relations: list[str] = ["Lover", "Stranger", "Rival"]
    relation: str = selectbox(
        "Relation to Protagonist", relations, index=0, help="Select the relation between antagonist and protagonist"
    )

    subheader("Structure")
    structures: list[str] = ["Three-Act Structure", "Five-Act Structure"]
    structure: str = selectbox("Story Structure", structures, index=0, help="Select the story structure")
    pacing_options: list[str] = ["Slow", "Moderate", "Fast"]
    pacing: str = selectbox("Story Pacing", pacing_options, index=0, help="Select the pacing of the story")

    subheader("Presentation Format")
    lengths: list[str] = ["500 words", "1000 words", "1500 words"]
    length: str = selectbox("Script Length", lengths, index=0, help="选择剧本的长度 / Select the script length")

    dialogue_ratios: list[str] = ["Low (20-30%)", "Medium (40-60%)", "High (70-80%)"]
    dialogue_ratio: str = selectbox(
        "Dialogue ratio", dialogue_ratios, index=0, help="Select the ratio between dialogue and narration"
    )

    languages: list[str] = ["English", "Chinese", "French", "Russian"]
    language: str = selectbox(
        "Select a Language", languages, index=1,
        help="Choose a language for data analysis. The model will respond in the selected language."
    )

    story_config = {
        "story_style": {"category": style, "tone": tone},
        "conflict": {"conflict": conflict, "strength": strength, "resolution": resolution},
        "characters": {
            "protagonist_motivation": protagonist_motivation,
            "antagonist_motivation": antagonist_motivation,
            "relation_to_protagonist": relation
        },
        "structure": {"structure": structure, "pacing": pacing},
        "format": {"length": length, "dialogue_ratio": dialogue_ratio}
    }
    rows = []
    for section, values in story_config.items():
        for key, value in values.items():
            rows.append({"section": section, "variables": key, "selection": value})
    df = DataFrame(rows)
    empty_tables.data_editor(df, height=460, hide_index=True, disabled=True)

    models: list[str] = ["OpenAI", "DeepSeek"]
    model: str = selectbox(
        "Select a Large Language Model", ["Select a model"] + models, index=0,
        help="Choose a large language model to be used for data analysis."
    )
    if model != "Select a model":
        caption(f"The model you selected is **{model}**.")

        match model:
            case "OpenAI":
                subheader("OpenAI Parameters")
                temperature: float = slider(
                    "Temperature", min_value=0.0, max_value=2.0, value=1.0, step=0.1, disabled=True,
                    help="Controls the randomness of the model's output. Lower values make it more deterministic.",
                )
                Top_p: float = slider(
                    "Top-p", min_value=0.0, max_value=1.0, value=1.0, step=0.1, disabled=True,
                    help="Controls the diversity of the model's output by sampling from the top p% of the probability distribution.",
                )
                model: str = selectbox(
                    "OpenAi Model", ["gpt-3.5-turbo", "gpt-4.1-mini", "gpt-5"], index=1, disabled=False,
                    help="Select the OpenAI model to use.",
                )
                match model:
                    case "gpt-3.5-turbo":
                        caption(r"Cost — Input: **\$0.50**, Output: **\$1.50** / 1M tokens")
                    case "gpt-4.1-mini":
                        caption(r"Cost — Input: **\$0.40**, Output: **\$1.60** / 1M tokens")
                    case "gpt-5":
                        caption(r"Cost — Input: **\$1.25**, Output: **\$10.00** / 1M tokens")
                    case _:
                        caption("No cost information available for this model.")
                api_key: str = text_input(
                    "OpenAI API Key",
                    max_chars=164, type="password",
                    help="OpenAI API key for authentication",
                )
                caption(f"The length of API key you entered is {len(api_key)} characters.")
                if not api_key:
                    empty_messages.error("Please enter your OpenAI API key.")
                elif api_key and not api_key.startswith("sk-"):
                    empty_messages.error("Please enter a **VALID** OpenAI API key.")
                elif api_key and api_key.startswith("sk-") and len(api_key) != 164:
                    empty_messages.warning("The length of OpenAI API key should be 164 characters.")
                elif api_key and api_key.startswith("sk-") and len(api_key) == 164:
                    empty_messages.success(
                        "The OpenAI API key is valid. Please enter a story theme or a story description."
                    )

                    story_theme: str = empty_text_area.text_area(
                        "Story Theme or Story Description", max_chars=100,
                        placeholder="Please enter a story theme or a story description within 100 characters.",
                        help="Please enter a story theme or a story description",
                    )
                    if story_theme != "":
                        empty_messages.info("You can click the button to generate a new story script.")

                        if button(
                                "Generate a New Story Script", type="primary", use_container_width=True,
                                help="Click to generate a new story script using the selected model and parameters."
                        ):
                            with Timer("Generate a New Story Script") as timer:
                                with spinner("Generating Story Script"):
                                    role: str = (
                                        "You are a professional, creative, and attractive scriptwriter. "
                                        "You are skilled in creating engaging and structured scripts. "
                                    )
                                    prompt: str = prompty_story(role, story_config, language)
                                    opener = OpenAICompleter(api_key=api_key, temperature=temperature, top_p=Top_p)
                                    response: str = opener.client(content=role, prompt=prompt, model=model)
                                    empty_story.markdown(response)
                            empty_messages.success(timer)
            case "DeepSeek":
                subheader("DeepSeek Parameters")
                temperature: float = slider(
                    "Temperature", min_value=0.0, max_value=1.0, value=1.0, step=0.1, disabled=True,
                    help="Controls the randomness of the model's output. Lower values make it more deterministic.",
                )
                model: str = selectbox(
                    "DeepSeek Model", ["deepseek-chat"], index=0, disabled=True,
                    help="Select the DeepSeek model to use.",
                )
                api_key: str = text_input(
                    "DeepSeek API Key",
                    max_chars=35, type="password",
                    help="DeepSeek API key for authentication",
                )
                caption(f"The length of API key you entered is {len(api_key)} characters.")
                if not api_key:
                    empty_messages.error("Please enter your DeepSeek API key.")
                elif api_key and not api_key.startswith("sk-"):
                    empty_messages.error("Please enter a **VALID** DeepSeek API key.")
                elif api_key and api_key.startswith("sk-") and len(api_key) != 35:
                    empty_messages.warning("The length of DeepSeek API key should be 164 characters.")
                elif api_key and api_key.startswith("sk-") and len(api_key) == 35:
                    empty_messages.success(
                        "The DeepSeek API key is valid. Please enter a story theme or a story description"
                    )

                    story_theme: str = empty_text_area.text_area(
                        "Story Theme or Story Description", max_chars=100,
                        placeholder="Please enter a story theme or a story description within 100 characters.",
                        help="Please enter a story theme or a story description",
                    )
                    if story_theme != "":
                        empty_messages.info("You can click the button to generate a new story script.")

                        if button(
                                "Generate a New Story Script", type="primary", use_container_width=True,
                                help="Click to generate a new story script using the selected model and parameters."
                        ):
                            with Timer("Generate a New Story Script") as timer:
                                with spinner("Generating Story Script"):
                                    role: str = (
                                        "You are a professional, creative, and attractive scriptwriter. "
                                        "You are skilled in creating engaging and structured scripts. "
                                    )
                                    prompt: str = prompty_story(role, story_config, language)
                                    seeker = DeepSeekCompleter(api_key=api_key, temperature=temperature)
                                    response: str = seeker.client(content=role, prompt=prompt, model=model)
                                    empty_story.markdown(response)
                            empty_messages.success(timer)
            case _:
                empty_messages.error(f"Model {model} is not supported yet. Please choose another model.")
    else:
        empty_messages.warning("Please select a model to generate a story!")
