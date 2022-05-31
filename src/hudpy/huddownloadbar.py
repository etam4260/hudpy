import math
from typing import Union
import re

def download_bar(done : int = None,
                 total : int = None,
                 percentage : float = None,
                 current : Union[str, int] = None,
                 error: int = None
                 ):
    """
    Function to output a download bar to the terminal. If done and total are inputted, it will
    calculate the percentage. The percentage is used to calculate the size of the current
    download bar.

    Parameters
    ----------

    done : The number of items completed.

    total : The total number of items needed to be processed.

    percentage : The percentage completed. 

    current : The current working item.

    error : The number of url queries that have errored out.

    Examples
    --------

    >>> download_bar(done = 10, total = 20, current = "https::url@hg.edu", error = 2)

    """
    done_perc = done/total
    remain_perc = (total-done)/total

    # Create the number of bars to appear on the screen
    done_bars = "=" * round(done_perc * 50)
    remain_bars = "-" *  round(remain_perc * 50)

    url = re.search(r"https://www.huduser.gov/hudapi/public/(.*)", current).group(1)

    
    if (round(remain_perc * 50) - round(remain_perc * 50)) == 0.5:
        remain_bar = "-" * math.floor(remain_perc * 50)
    
    # Create the entire loading bar
    loading = "Downloading\t" + "[" + str(done_bars) + str(remain_bars) + "]\t" + \
                str(round(done_perc * 100, 0)) + "%\t" + str(done) + \
                 "/" + str(total) + "\t" + str(error) + "\t" + str(url)

    # Print to the same line over and over again in the terminal. 
    print("\r" + str(loading), end = "")