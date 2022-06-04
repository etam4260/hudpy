import os

def hud_get_key() -> str:
    """
    Get the current HUD_KEY environment variable.

    Returns
    -------

    Returns a string containing the HUD_KEY environment variable.

    See Also
    --------
    * hud_set_key()

    Examples
    --------
    >>> hud_get_key()
    """
    
    return(os.getenv("HUD_KEY"))

def hud_set_key(key:str):
    """
    Function to set the HUD_KEY environment variable.

    Parameters
    ----------

    key : The key obtained at https://www.huduser.gov/hudapi/public/register?comingfrom=1.

    See Also
    --------
    * hud_get_key()

    Examples
    --------
    >>> hud_set_key("DWKQOD442OLKDF3")
    """
    if not isinstance(key, str):
        raise ValueError("Key should be a string.")

    os.environ["HUD_KEY"] = key