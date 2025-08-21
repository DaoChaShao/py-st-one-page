#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/8/21 23:31
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   helper.py
# @Desc     :   

from json import dumps
from time import perf_counter


class Timer(object):
    """ timing code blocks using a context manager """

    def __init__(self, description: str = None, precision: int = 5):
        """ Initialise the Timer class
        :param description: the description of a timer
        :param precision: the number of decimal places to round the elapsed time
        """
        self._description: str = description
        self._precision: int = precision
        self._start: float = 0.0
        self._end: float = 0.0
        self._elapsed: float = 0.0

    def __enter__(self):
        """ Start the timer """
        self._start = perf_counter()
        print()
        print("-" * 50)
        print(f"{self._description} has been started.")
        return self

    def __exit__(self, *args):
        """ Stop the timer and calculate the elapsed time """
        self._end = perf_counter()
        self._elapsed = self._end - self._start

    def __repr__(self):
        """ Return a string representation of the timer """
        if self._elapsed != 0.0:
            print("-" * 50)
            return f"{self._description} took {self._elapsed:.{self._precision}f} seconds."
        return f"{self._description} has NOT been started."


def prompty_generator(role: str, story_config: dict, language: str = "Chinese") -> str:
    """ Generate a prompt for LLM to create a one-page script based on the user-selected story configuration.
    :param role: str: The role of the LLM (e.g., "Professional Scriptwriter")
    :param story_config: dict: The user-selected story configuration (style, conflict, characters, structure, format)
    :param language: str: The language in which the LLM should respond ("Chinese" or "English")
    :return: str: The generated prompt for the LLM
    """
    # Define the conflict details, including specific presentation methods, values, classic cases, and conflict tensions.
    conflict_details = {
        "Conflict with Nature": {
            "description": "Opposition between natural forces and human will",
            "value": "Show human resilience and survival instinct",
            "examples": ["Titanic – shipwreck scene", "The Day After Tomorrow – climate disaster impact on society"],
            "tension": "Collision between natural laws and human desires"
        },
        "Conflict with Society": {
            "description": "Individual vs societal norms, rules or public opinion",
            "value": "Reveal moral dilemmas under social pressure",
            "examples": ["The Hunger Games", "V for Vendetta"],
            "tension": "Personal desire against societal rules"
        },
        "Conflict with Technology": {
            "description": "Human vs technology or AI",
            "value": "Explore ethics of technology and limits of human control",
            "examples": ["The Matrix", "Westworld"],
            "tension": "Technological advancement vs human authority"
        },
        "Conflict with Self": {
            "description": "Internal psychological struggle or moral dilemma",
            "value": "Show inner conflict and character growth",
            "examples": ["Good Will Hunting", "Black Swan"],
            "tension": "Personal desire vs rational principle"
        },
        "Conflict of Ideas": {
            "description": "Clash between different beliefs, values, or philosophies",
            "value": "Reveal intellectual conflict and its social/relationship impact",
            "examples": ["12 Angry Men", "Source Code"],
            "tension": "Ideological clashes driving actions and emotions"
        },
        "Conflict of Fate and Destiny": {
            "description": "Struggle against destiny or uncontrollable forces",
            "value": "Show heroism and sense of fate",
            "examples": ["Hamlet", "Schindler's List"],
            "tension": "Personal effort vs predetermined fate"
        }
    }

    # Few-shot examples for all conflict types
    few_shots = {
        "Conflict with Nature": "On a stormy island, young explorer Erin clutches a rope, battling the furious waves. Every splash challenges her courage, testing both skill and instinct.",
        "Conflict with Society": "In a dystopian city, rebel Alex confronts the oppressive regime. Each decision risks exposure, forcing him to navigate both fear and strategy.",
        "Conflict with Technology": "As the AI overrides the city's systems, engineer Maya races against time. Her actions intertwine with the machine's logic, testing human ingenuity.",
        "Conflict with Self": "Torn between ambition and loyalty, Daniel paces the room. His mind debates right and wrong, each thought a battle shaping his choices.",
        "Conflict of Ideas": "Two philosophers argue passionately over justice in court, each conviction challenging the other's worldview, driving tension and reflection.",
        "Conflict of Fate and Destiny": "Prophesied hero Leo faces trials beyond control. Each event pushes him closer to fate, yet he struggles to assert free will."
    }

    config_json = dumps(story_config, ensure_ascii=False, indent=2)

    instruction: str = (
        f"Your task is to generate a story script based on the following story configuration. "
        f"The script must strictly follow the user's choices of style, core conflict, character motivations, story structure, and presentation format. "
        f"Ensure the story is coherent, conflict-driven, and characters' motivations are clear. "
        f"Keep the story rich and complete, suitable for a script.\n\n"
        f"Requirements:\n"
        f"- Present the story in natural paragraphs; do not use 'Act 1/Act 2' or bullet points.\n"
        f"- Dialogue and narration should blend naturally"
        f"- Include concrete details: actions, scenes, sensory experiences, and character thoughts.\n"
        f"- Use the conflict type details for reference to depict dramatic tension:\n"
        f"{dumps(conflict_details, ensure_ascii=False, indent=2)}\n"
        f"- Few-shot examples for writing style based on conflict type:\n"
        f"{dumps(few_shots, ensure_ascii=False, indent=2)}\n"
        f"- Do not output word counts, dialogue ratio, summaries, or analysis.\n"
        f"- Output only the story text in {language}, preferably in Markdown format."
    )
    constraints: str = (
        f"Do not include greetings, sign-offs, or irrelevant content. "
        f"Focus solely on delivering a professional, creative, attractive and structured script. "
        f"Maintain narrative tension and clarity."
    )

    prompt: str = (
        f"{role}\n\n"
        f"The following is the story configuration provided by the user:\n\n"
        f"{config_json}\n\n"
        f"{instruction}\n\n"
        f"{constraints}"
    )
    return prompt
