import os
import platform
import hudinternetonline
from typing import Union

def hudpy_website(website: Union[str, int, list: int, list: str, tuple: Union[int, str]] = ["github-pages", "github"]):
    """
    #' @name hudpy_website
    #' @title hudpy_website
    #' @description Quickly get documentation 
    #    for the hudpy package by opening up
    #'   the websites associated with it. 
    #    Currently supports Linux, Darwin 
    #    and Windows OS.
    #' @param website A list of websites.
    #'   1) "github-pages"
    #'   2) "github"
    """ 

    if(not hudinternetonline.internet_on()): raise ConnectionError("You currently do not have internet access.")

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
