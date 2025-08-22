#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/8/21 22:47
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   layout.py
# @Desc     :   

from streamlit import set_page_config, Page, navigation


def page_config() -> None:
    """ Set the window
    :return: None
    """
    set_page_config(
        page_title="AI Customer Support",
        page_icon=":material/script:",
        layout="wide",
        initial_sidebar_state="expanded",
    )


def pages_setter() -> None:
    """ Set the subpages on the sidebar
    :return: None
    """
    pages: dict = {
        "page": [
            "subpages/home.py",
            "subpages/story.py",
            "subpages/storyboard.py",
            "subpages/about.py",
        ],
        "title": [
            "Home",
            "Story Script Generator",
            "Storyboard Generator",
            "About",
        ],
        "icon": [
            ":material/home:",
            ":material/auto_stories:",
            ":material/photo_library:",
            ":material/info:",
        ],
    }

    structure: dict = {
        "Introduction": [
            Page(page=pages["page"][0], title=pages["title"][0], icon=pages["icon"][0]),
        ],
        "Core Functions": [
            Page(page=pages["page"][1], title=pages["title"][1], icon=pages["icon"][1]),
            Page(page=pages["page"][2], title=pages["title"][2], icon=pages["icon"][2]),
        ],
        "Information": [
            Page(page=pages["page"][3], title=pages["title"][3], icon=pages["icon"][3]),
        ],
    }
    pg = navigation(structure, position="sidebar", expanded=True)
    pg.run()
