import urllib3

def internet_on() -> bool:
    """
    Pings the Google servers and determines whether a response was returned. If data is returned
    then user has access to internet.

    Returns
    -------

    Returns True if user has internet access, false if not.

    Examples
    --------
    >>> internet_on()
    """
    try:
        urllib3.urlopen('http://216.58.192.142', timeout=1)
        return True
    except urllib3.URLError as err: 
        return False