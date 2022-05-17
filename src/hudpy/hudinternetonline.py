import urllib3

def internet_on() -> bool:
    try:
        urllib3.urlopen('http://216.58.192.142', timeout=1)
        return True
    except urllib3.URLError as err: 
        return False