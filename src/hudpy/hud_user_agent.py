import os

def hud_set_user_agent(user_agent:str):
    """
    Set a user agent when querying the HUD User APIs.
   
    Parameters
    ----------
    user_agent : A character vector with the user agent.
    in_wkdir : set the key in the user's .RProfile in this directory.
        Is defaulted to false.
    in_home : set the key in the user's HOME directory.
        Is defaulted to false.

    See Also
    --------
    * hud_get_user_agent()
    * hud_set_user_agent()

    Examples
    --------

    >>> hud_set_user_agent("im-the-user")

    """
    if not isinstance(user_agent, str):
        raise ValueError("Key should be a string.")

    os.environ["HUD_USER_AGENT"] = user_agent


def hud_get_user_agent():
    """        
    Get the most recent user agent set.
   
    See Also
    --------
    hud_get_user_agent()
    hud_set_user_agent()

    Examples
    --------

    >>> hud_get_user_agent()

    Returns
    -------
    A character vector with the user agent used for querying HUD User
    APIs.
    
    """  
        
    return(os.getenv("HUD_USER_AGENT"))
