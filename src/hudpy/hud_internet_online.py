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
    http = urllib3.PoolManager()
    r = http.request('GET', 'https://github.com')
    r.status
    
    if(r.status == 200):
        return True
    else:
        return False