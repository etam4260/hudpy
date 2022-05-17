import os


def hud_get_key() -> str:
    """
    #' @name hud_get_key
    #' @title hud_get_key
    #' @description  Return most recent key set in
    #    the HUD_KEY environment variable.
    #'   If no key is set, return "".
    #' @returns Returns a string.
    """
    
    return(os.getenv("HUD_KEY"))

def hud_set_key(key:str):
    """
    #' @name hud_set_key
    #' @title hud_set_key
    #' @description A wrapper around Sys.getenv() 
    #'   to set HUD_KEY environment variable.
    #' @param key key obtained at
    #'   https://www.huduser.gov/hudapi/public/register?comingfrom=1
    """

    os.environ["HUD_KEY"] = key