#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/8/22 13:27
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   storyboard.py
# @Desc     :

from json import loads
from streamlit import (empty, sidebar, subheader, selectbox, caption,
                       slider, text_input, button, session_state, write)

from utils.helper import prompt_events, prompt_event, prompt_image, Timer
from utils.models import OpenAIImageCompleter, OpenAITextCompleter

empty_messages = empty()
empty_areas_info = empty()
empty_areas = empty()
empty_image = empty()
empty_images = [empty() for _ in range(10)]
empty_events = empty()

if "story" not in session_state:
    session_state["story"] = ""
if "images" not in session_state:
    session_state["images"] = []

with sidebar:
    subheader("Design Controls")
    styles: list[str] = ["Children's Illustration", "Watercolour", "Manga", "Realistic", "Cartoon", "Pixel Art"]
    style: str = selectbox(
        "Select Illustration Style", styles, index=0,
        help="Choose an illustration style for your storyboard"
    )
    line_types: list[str] = ["Soft", "Clear", "Rough"]
    line_type: str = selectbox(
        "Select Line Type", line_types, index=0,
        help="Choose a line type for your storyboard"
    )
    colour_tones: list[str] = ["Dark", "Warm", "Cool", "High Contrast"]
    colour_tone: str = selectbox(
        "Select Colour Tone", colour_tones, index=0,
        help="Choose a colour tone for your storyboard"
    )
    moods: list[str] = ["Tense", "Sad", "Romantic", "Mysterious", "Heroic"]
    mood: str = selectbox(
        "Select Mood", moods, index=0,
        help="Choose a mood for your storyboard"
    )

    # subheader("Camera Controls")
    # angles: list[str] = ["Eye Level", "Top View", "Low Angle", "Side View"]
    # camera_angle: str = selectbox(
    #     "Select Camera Angle", angles, index=0,
    #     help="Choose a camera angle for your storyboard"
    # )
    # distances: list[str] = ["Close-up", "Medium Shot", "Wide Shot", "Extreme Close-up", "Over the Shoulder"]
    # camera_distance: str = selectbox(
    #     "Select Camera Distance", distances, index=0,
    #     help="Choose a camera distance for your storyboard"
    # )
    # compositions: list[str] = ["Rule of Thirds", "Golden Ratio", "Symmetrical", "Asymmetrical"]
    # composition: str = selectbox(
    #     "Select Composition", compositions, index=0,
    #     help="Choose a composition style for your storyboard"
    # )

    subheader("Models Settings")
    brands: list[str] = ["OpenAI", ]
    brand: str = selectbox(
        "Select Model Brand", brands, index=0, disabled=True,
        help="Choose a model brand for your storyboard generation"
    )
    models: list[str] = ["dall-e-3", "dall-e-2"]
    model: str = selectbox(
        "Select Model", models, index=0, disabled=True,
        help="Choose a model for your storyboard generation"
    )
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

        image_num: int = slider(
            "Stream Partial Images",
            min_value=0, max_value=3, value=0, disabled=True,
            help="If you set partial_images to 0, you will only receive the final image"
        )
        qualities: list[str] = ["standard", "hd"]
        image_quality: str = selectbox(
            "Image Quality", qualities, index=0,
            help="Choose an image quality for your storyboard"
        )
        resolution: list[str] = ["1024x1024", "1024x1792", "1792x1024"]
        image_resolution: str = selectbox(
            "Image Resolution", resolution, index=0,
            help="Choose an image resolution for your storyboard"
        )
        languages: list[str] = ["English", "Chinese", "French", "Russian"]
        language: str = selectbox(
            "Select a Language", languages, index=1,
            help="Choose a language for data analysis. The model will respond in the selected language."
        )

        filename: str = "storyboard"
        if session_state.story != "":
            empty_messages.info("Click the **Generate an Image** button to generate your storyboard image.")

            if session_state.images:
                for i, image_display in enumerate(session_state.images):
                    empty_images[i].image(session_state.images[i], use_container_width=True)
                    empty_messages.success("Image generated and loaded successfully!")
            else:
                # Storyboard image generation based on the entered prompt
                if button("Generate an Image", type="primary", use_container_width=True):
                    # Story segmentation
                    role: str = "You are a Professional Story Planner and Event Analyzer."
                    prompt: str = prompt_events(session_state.story)
                    opener: OpenAITextCompleter = OpenAITextCompleter(api_key)
                    events: str = opener.client(role, prompt)
                    # empty_events.write(loads(events))
                    prompts: list[str] = prompt_event(loads(events), style, line_type, colour_tone, mood)
                    # empty_events.write(prompts)

                    completer: OpenAIImageCompleter = OpenAIImageCompleter(api_key, model)
                    for i, prompt_image in enumerate(prompts):
                        completer.client(session_state.story, image_quality, image_resolution, f"{filename}-{i}")
                        image_path: str = f"{filename}-{i}.png"
                        if image_path not in session_state.images:
                            session_state.images.append(image_path)

                    for i, image_display in enumerate(session_state.images):
                        empty_images[i].image(session_state.images[i], use_container_width=True)
                        empty_messages.success("Image generated and loaded successfully!")
        else:
            entered_text: str = empty_areas.text_area(
                "Image Description", max_chars=3000,
                placeholder="Enter the description of the image you want to generate...",
                help="Enter an image description for your storyboard"
            )
            if entered_text == "":
                empty_messages.warning("Please enter the description of the image you want to generate.")
                empty_areas_info.info(
                    "Example: Draw a gorgeous image of a river made of white owl feathers, snaking its way through a serene winter landscape"
                )
                # entered_text: str = "Draw a gorgeous image of a river made of white owl feathers, snaking its way through a serene winter landscape"
                # entered_text: str = "A children's book drawing of a veterinarian using a stethoscope to listen to the heartbeat of a baby otter."
            else:
                empty_messages.info("Click the **Generate an Image** button to generate your storyboard image.")

                # Storyboard image generation based on the entered prompt
                if button("Generate an Image", type="primary", use_container_width=True):
                    prompt: str = prompt_image(entered_text, style, line_type, colour_tone, mood)

                    completer: OpenAIImageCompleter = OpenAIImageCompleter(api_key, model)
                    completer.client(prompt, image_quality, image_resolution, filename)
                    empty_image.image(f"{filename}.png", use_container_width=True)
                    empty_messages.success("Image generated and loaded successfully!")
