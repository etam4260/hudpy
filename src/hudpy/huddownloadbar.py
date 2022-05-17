import math
from typing import Union

def download_bar(done:int = None, total:int = None, percentage:float = None, current: Union[str, int] = None):
    """
    #' @name download_bar
    #' @title download_bar
    #' @description A simple loading bar for the number of queries completed:
    #'   prints the loading bar to the R console.
    #' @param done The number of operations done.
    #' @param total The number of total operations needed.
    #' @param current The current item being worked on.
    #' @param percentage Can supply a percentage instead of done and total.
    """

    done_perc = done/total
    remain_perc = (total-done)/total

    # Create the number of bars to appear on the screen
    done_bars = "=" * round(done_perc * 50)
    remain_bars = "-" *  round(remain_perc * 50)

    if (round(remain_perc * 50) - round(remain_perc * 50)) == 0.5:
        remain_bar = "-" * math.floor(remain_perc * 50)
    
    # Create the entire loading bar
    loading = "Downloading\t" + "[" + done_bars + remain_bars + "]\t" + \
                round(done_perc * 100, 0), "%\t" + done + "/" + total

    # Print to the same line over and over again in the terminal. 
    print("\r" + loading, end = "")