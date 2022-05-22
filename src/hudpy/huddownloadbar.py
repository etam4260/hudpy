import math
from typing import Union

def download_bar(done : int = None, total : int = None, percentage : float = None, current : Union[str, int] = None):
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

    Examples
    --------

    >>> download_bar(10, 20)

    """
    done_perc = done/total
    remain_perc = (total-done)/total

    # Create the number of bars to appear on the screen
    done_bars = "=" * round(done_perc * 50)
    remain_bars = "-" *  round(remain_perc * 50)

    if (round(remain_perc * 50) - round(remain_perc * 50)) == 0.5:
        remain_bar = "-" * math.floor(remain_perc * 50)
    
    # Create the entire loading bar
    loading = "Downloading\t" + "[" + str(done_bars) + str(remain_bars) + "]\t" + \
                str(round(done_perc * 100, 0)) + "%\t" + str(done) + "/" + str(total)

    # Print to the same line over and over again in the terminal. 
    print("\r" + str(loading), end = "")