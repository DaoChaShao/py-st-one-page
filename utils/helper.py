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


def prompty_story(role: str, story_config: dict, language: str = "Chinese") -> str:
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

    motivation_details = {
        "Revenge": {
            "definition": "Driven by a desire to retaliate for a past wrong or harm.",
            "function": "Generates tension and forward momentum through emotional intensity.",
            "behavioral_cues": [
                "Recalling past injuries or injustices",
                "Using symbolic objects (photo, weapon, letter) to trigger action",
                "Obsessive pursuit of retaliation that clouds judgment"
            ],
            "examples": [
                "Hamlet secretly plotting against Claudius",
                "Kill Bill's Beatrix pursuing vengeance"
            ]
        },
        "Love": {
            "definition": "Motivated by deep attachment—romantic, familial, or platonic.",
            "function": "Adds emotional depth and softens or complicates conflicts.",
            "behavioral_cues": [
                "Making sacrifices for the loved one",
                "Balancing personal desire against duty or risk",
                "Tender moments amid chaos or tension"
            ],
            "examples": [
                "Romeo and Juliet risking everything for each other",
                "The Notebook showing enduring affection against obstacles"
            ]
        },
        "Power": {
            "definition": "Desire to achieve dominance, influence, or control over people, systems, or outcomes.",
            "function": "Shapes choices and conflicts, often creating moral dilemmas and tension with others.",
            "behavioral_cues": [
                "Strategic planning or manipulation of situations and people",
                "Testing boundaries of control while facing ethical dilemmas",
                "Moments of hesitation revealing internal conflict",
                "Decisions that reveal prioritisation of ambition over personal relationships"
            ],
            "examples": [
                "Macbeth plotting to seize the throne",
                "Frank Underwood manoeuvring politically to gain influence"
            ]
        }
    }

    structure_details = {
        "Three-Act Structure": {
            "definition": "A classic dramatic model dividing the story into three main parts.",
            "function": "Provides a clear beginning, middle, and end to ensure narrative coherence.",
            "pattern": {
                "Act 1 (Setup)": "Introduce world, characters, and initial conflict.",
                "Act 2 (Confrontation)": "Escalate the conflict, test characters, reveal stakes.",
                "Act 3 (Resolution)": "Reach climax and resolve the main conflict, showing consequences."
            },
            "examples": [
                "The Lion King (Disney, 1994): Simba’s exile (Act 1), growing up and facing Scar (Act 2), final battle and reclaiming the throne (Act 3).",
                "The Matrix (1999): Neo’s awakening (Act 1), training and resisting agents (Act 2), battle and becoming The One (Act 3)."
            ]
        },
        "Five-Act Structure": {
            "definition": "A more detailed narrative arc often used in classical dramas and long-form storytelling.",
            "function": "Allows deeper character development and gradual escalation of conflict.",
            "pattern": {
                "Act 1 (Exposition)": "Introduce setting, characters, and initial situation.",
                "Act 2 (Rising Action)": "Conflict begins and tension increases.",
                "Act 3 (Climax)": "The turning point of highest tension and drama.",
                "Act 4 (Falling Action)": "Consequences unfold, conflicts move toward resolution.",
                "Act 5 (Denouement)": "Final resolution, showing outcome and closure."
            },
            "examples": [
                "Hamlet (Shakespeare): Ghost’s revelation (Act 1), Hamlet’s hesitation (Act 2), play within a play (Act 3), downfall (Act 4), tragic resolution (Act 5).",
                "Breaking Bad (TV series as macro-structure): Walter White’s decision to cook meth (Act 1), escalation with cartels (Act 2), climax against Gus (Act 3), downfall (Act 4), resolution in final season (Act 5)."
            ]
        }
    }

    pacing_details = {
        "Slow": {
            "definition": "A reflective and detailed storytelling pace.",
            "function": "Allows deeper exploration of emotions, settings, and character psychology.",
            "techniques": [
                "Long descriptive passages",
                "Internal monologues",
                "Extended dialogue exchanges"
            ],
            "examples": [
                "The Remains of the Day (Kazuo Ishiguro)",
                "Call Me by Your Name (André Aciman)"
            ]
        },
        "Moderate": {
            "definition": "A balanced pace between action and reflection.",
            "function": "Keeps narrative engaging while still allowing depth of character and world-building.",
            "techniques": [
                "Alternating between scenes of action and quiet moments",
                "Balanced dialogue and narration",
                "Smooth transitions"
            ],
            "examples": [
                "The Lord of the Rings (J.R.R. Tolkien)",
                "The Hunger Games (Suzanne Collins)"
            ]
        },
        "Fast": {
            "definition": "A quick, action-driven pace with minimal reflection.",
            "function": "Creates excitement, urgency, and tension.",
            "techniques": [
                "Short, punchy sentences",
                "Frequent conflicts and plot twists",
                "Minimal description, focus on action"
            ],
            "examples": [
                "The Da Vinci Code (Dan Brown)",
                "Mad Max: Fury Road (Film)"
            ]
        }
    }

    dialogue_ratio_details = {
        "Low (20-30%)": {
            "definition": "Dialogue is used sparingly; narration dominates.",
            "function": "Best for introspection, world-building, or epic storytelling.",
            "techniques": [
                "Focus on narration and description",
                "Dialogue appears only at key dramatic moments"
            ],
            "examples": [
                "1984 (George Orwell)",
                "The Road (Cormac McCarthy)"
            ]
        },
        "Medium (40-60%)": {
            "definition": "Balanced use of dialogue and narration.",
            "function": "Maintains readability while showcasing character interaction.",
            "techniques": [
                "Dialogue alternates with descriptive passages",
                "Conversations advance plot while narration builds atmosphere"
            ],
            "examples": [
                "Harry Potter series (J.K. Rowling)",
                "To Kill a Mockingbird (Harper Lee)"
            ]
        },
        "High (70-80%)": {
            "definition": "Dialogue-heavy narrative, close to a screenplay style.",
            "function": "Best for dynamic character-driven stories, strong dramatic tension.",
            "techniques": [
                "Rapid exchanges between characters",
                "Narration is brief, mostly stage-setting"
            ],
            "examples": [
                "The Great Gatsby (dialogue-heavy parts)",
                "Most stage plays and screenplays (e.g., Tennessee Williams, Aaron Sorkin)"
            ]
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
        f"Your task is to generate a complete story script based on the following configuration. "
        f"The script must follow the user's selected style, conflict type, character motivations, "
        f"story structure, pacing, and dialogue ratio. "
        f"Ensure the story is coherent, conflict-driven, and characters’ motivations are reflected naturally through actions, choices, and inner thoughts. "
        f"Keep the story rich in detail and immersive, suitable for a dramatic script.\n\n"

        f"Writing Requirements:\n"
        f"- Present the story in flowing natural paragraphs (avoid 'Act 1/Act 2' or bullet points).\n"
        f"- Blend dialogue and narration organically; dialogue should reveal character motivations and escalate conflict.\n"
        f"- Each scene must have clear causal logic: choices or events lead naturally to the next.\n"
        f"- Use environment, events, or other characters to drive changes—avoid sudden unexplained shifts.\n"
        f"- Include vivid concrete details: actions, sensory impressions, atmosphere, and inner thoughts.\n"
        f"- Major decisions or turning points must include gradual psychological development and reflection.\n\n"

        f"Reference Materials:\n"
        f"1. Conflict details:\n{dumps(conflict_details, ensure_ascii=False, indent=2)}\n\n"
        f"2. Character motivation details:\n{dumps(motivation_details, ensure_ascii=False, indent=2)}\n\n"
        f"3. Story structure details:\n{dumps(structure_details, ensure_ascii=False, indent=2)}\n\n"
        f"4. Pacing details:\n{dumps(pacing_details, ensure_ascii=False, indent=2)}\n\n"
        f"5. Dialogue ratio details:\n{dumps(dialogue_ratio_details, ensure_ascii=False, indent=2)}\n\n"
        f"6. Few-shot examples by conflict type:\n{dumps(few_shots, ensure_ascii=False, indent=2)}\n\n"

        f"Additional Output Instructions:\n"
        f"- After finishing the story text, also generate a section called 'Safe Visual Description.\n"
        f"- The 'Safe Visual Description' must:\n"
        f"  * Focus only on cinematic and safe visual elements (characters’ appearance, environment, atmosphere).\n"
        f"  * Avoid mentioning blood, gore, hate, explicit violence, or disturbing concepts.\n"
        f"  * Replace emotional or dark concepts with visual metaphors (e.g., 'soft golden light breaking through mist' instead of 'deep despair').\n"
        f"  * Be formatted as a short paragraph suitable as an input to DALL·E image generation.\n"

        f"Output Rules:\n"
        f"- Do not include word counts, dialogue ratios, summaries, or meta-analysis.\n"
        f"- Output only the story text in {language}, preferably formatted in Markdown.\n"
        f"- Do not include greetings, sign-offs, or irrelevant content."
    )

    prompt: str = (
        f"{role}\n\n"
        f"The following is the story configuration provided by the user:\n\n"
        f"{config_json}\n\n"
        f"{instruction}"
    )
    return prompt


def prompt_events(story: str) -> str:
    """ Generate a prompt for LLM to create a list of 4-6 key events based on the user-selected story configuration.
    :param story: str: The story generated by the LLM
    :return: str: The generated prompt for the LLM
    """
    instruction: str = (
        f"Your task is to analyse the provided story and identify 4-6 key events that are crucial to the plot development. "
        f"These events should be significant turning points that drive the narrative forward and reveal important aspects of the characters and their motivations.\n\n"

        f"Writing Requirements:\n"
        f"- Each event should be described in a single, concise sentence.\n"
        f"- The events must be listed in chronological order as they occur in the story.\n"
        f"- Ensure that the events capture the essence of the story's conflict, character development, and major plot twists.\n\n"

        f"Output Rules:\n"
        f"- The output must be valid JSON only (no explanations, no comments).\n"
        f"- JSON should be an array of objects.\n"
        f"- Each object must contain:\n"
        f"  - id (e.g., event1, event2)\n"
        f"  - event (a one-sentence action description)\n"
        f"  - characters (array of characters involved)\n"
        f"  - location\n"
        f"  - visual (a detailed scene description suitable for image generation)\n\n"

        f"Example output format:\n"
        f"[\n"
        f"  {{\n"
        f"    \"id\": \"scene 1\",\n"
        f"    \"visual\": \"A dimly lit library with towering shelves, where a young boy pushes against a creaky wooden panel, revealing a hidden door.\"\n"
        f"    \"location\": \"library\",\n"
        f"    \"characters\": [\"boy\"],\n"
        f"    \"event\": \"The boy discovers a hidden door in the library.\",\n"
        f"  }},\n"
        f"  ...\n"
        f"]"
    )
    prompt: str = (
        f"The following is the story provided by the user:\n\n"
        f"{story}\n\n"
        f"{instruction}"
    )
    return prompt


def prompt_event(events: list[dict], style: str, line_type: str, colour_tone: str, mood: str) -> list[str]:
    prompts = []
    for event in events:
        characters = ", ".join(event['characters'])
        prompt = (
            f"Create a SINGLE cinematic illustration.\n\n"
            f"Scene description: {event['visual']}.\n"
            f"Key moment: {event['event']}.\n"
            f"Main characters: {characters}.\n"
            f"Location: {event['location']}.\n\n"
            f"Art Direction:\n"
            f"- Illustration Style: {style}\n"
            f"- Line Type: {line_type}\n"
            f"- Colour Tone: {colour_tone}\n"
            f"- Mood: {mood}\n\n"
            f"STRICT RULES:\n"
            f"- Generate ONLY ONE single illustration (not multiple, not collage, not panels).\n"
            f"- The output must look like a cinematic MOVIE STILL, not a storyboard or comic.\n"
            f"- DO NOT include any text, words, subtitles, speech bubbles, or symbols.\n"
            f"- Keep character appearances consistent across all scenes "
            f"(same ethnicity, same face, same clothing style).\n"
            f"- The image should be expressive, atmospheric, and cinematic.\n"
        )
        prompts.append(prompt)
    return prompts


def prompt_image(entered_text: str, style: str, line_type: str, colour_tone: str, mood: str) -> str:
    prompt: str = (
        f"{entered_text}\n\n"
        f"Art Direction:\n"
        f"- Illustration Style: {style}\n"
        f"- Line Type: {line_type}\n"
        f"- Colour Tone: {colour_tone}\n"
        f"- Mood: {mood}\n\n"
        f"Important rules:\n"
        f"- Only ONE illustration (not multiple, not collage).\n"
        f"- Do NOT include any text or words.\n"
        f"- Keep the scene cinematic and consistent.\n"
    )
    return prompt
