from __future__ import annotations
from typing import Union

import os
import platform

from hudpy import hud_internet_online

def hudpy_website(website: Union[int, str, list[int], list[str], tuple[int], tuple[str]] = ["github-pages", "github"]):
    
    """
    Function to quickly open the associated website documentation for the hudpy package.

    Parameters
    ----------

    website : The websites to open in default browser.

    Examples
    --------
    >>> rhud_website("github-pages")

    >>> rhud_website("github")

    >>> rhud_website()
    """ 

    if(not hud_internet_online.internet_on()): raise ConnectionError("You currently do not have internet access.")

    github_pages = "https://etam4260.github.io/hudpy/"
    github = "https://github.com/etam4260/hudpy"

    if platform.system() == "Linux":
        if "github-pages" in website:
            os.system("open" + " " + github_pages) 
        if "github" in website:
            os.system("open" + " " + github)
    elif platform.system() == "Darwin":
        if "github-pages" in website:
            os.system("open" + " " + github_pages) 
        if "github" in website:
            os.system("open" + " " + github) 
    elif platform.system() == "Windows":
        if "github-pages" in website:
            os.system("start" + " " + github_pages)
        if "github" in website: 
            os.system("start" + " " + github)
