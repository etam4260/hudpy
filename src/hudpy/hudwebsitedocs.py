import os
import platform


def hudpy_website(website:str = ["github-pages","github"]):
    """
    #' @name hudpy_website
    #' @title hudpy_website
    #' @description Quickly get documentation 
    #    for the hudpy package by opening up
    #'   the websites associated with it. 
    #    Currently supports Linux, Darwin 
    #    and Windows OS.
    #' @param website An array of websites.
    #'   1) "github-pages"
    #'   2) "github"
    """

    github_pages = "https://etam4260.github.io/hudr/"
    github = "https://github.com/etam4260/hudr"

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