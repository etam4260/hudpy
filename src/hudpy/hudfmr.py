from distutils.log import warn
from sqlite3 import DatabaseError
from typing import Union, List, Tuple
import hudinputcheck
import itertools
import urllib3
import pandas as pd
import json
import huddownloadbar
import hudinternetonline

def hud_fmr_state_metroareas(state: Union[int, str, List[int], List[str], Tuple[int], Tuple[str]] = (date.today() -   timedelta(days = 365)).strftime("%Y"),
                             year: Union[int, str, List[int], List[str], Tuple[int], Tuple[str]] = 1,
                             key: str = os.getenv("HUD_KEY")) -> pd.DataFrame:
    """
    Function to query the Fair Markets Rent API provided by US
    Department of Housing and Urban Development. This returns metroarea
    FMR for state level queries.

    Parameters
    ----------

    state : The state to query for. Can be abbreviation, fip code, or
         full name.

    year : Gets the year that this data was recorded. Can specify multiple
        years. Default is the previous year.

    key : The API key for this user. You must go to HUD and sign up for an
        account and request for an API key.

    See Also
    --------
    
    * hud_fmr()
    * hud_fmr_state_metroareas()
    * hud_fmr_state_counties()
    * hud_fmr_county_zip()
    * hud_fmr_metroarea_zip()

    Returns
    -------

    This returns a dataframe with metroarea
    fair markets rent based on state level queries.

    Examples
    --------

    >>> hud_fmr_state_metroareas("VA", year = c(2021))

    >>> hud_fmr_state_metroareas("Alabama", year = c(2021))
 
    >>> hud_fmr_state_metroareas("24", year = c(2021)))
    """  
    
    if(not hudinternetonline.internet_on()): raise ConnectionError("You currently do not have internet access.")
    
    args = hudinputcheck.fmr_il_input_check_cleansing(state, year, key)
    query = args[1]
    year = args[2]
    key = args[3]

    error_urls = list()

    # Create all combinations of query and year...
    all_queries = list(itertools.product(query, year))

    # Make query calls for all queries.
    result = pd.DataFrame()

    for i in range(len(all_queries)):
        urls = "https://www.huduser.gov/hudapi/public/fmr/" + \
               "statedata/" + \
               all_queries[i, 1] + \
               "?year=" + \
               all_queries[i, 2]

        headers = {"Authorization": "Bearer " + key, "User-Agent": "https://github.com/etam4260/hudpy"}
        call = urllib3.http.request("GET", urls, headers = headers, timeout = 30)
                            
        cont = json.loads(call.data.decode('utf-8'))
        
        huddownloadbar.download_bar(i, len(all_queries))

        if "error" in cont.columns:
            error_urls.append(urls)
        else:
            result.append(cont["data"]["metroareas"])

   # Just print a newline
    print()

    if len(error_urls) != 0:
        # Print all error urls
        # Construct warning message... 
        warn_msg = "Could not find data for queries: \n\n" + \
                    "\n".join(error_urls) +  "\n" + \
                    "It is possible that your key is invalid or there isn't \
                    any data for these parameters. If you think this is wrong please \
                    report it at https://github.com/etam4260/hudpy/issues"    


        warn(warn_msg)

    return(result)


def hud_fmr_state_counties(state: Union[int, str, List[int], List[str], Tuple[int], Tuple[str]],
                           year: Union[int, str, List[int], List[str], Tuple[int], Tuple[str]] = (date.today() - timedelta(days = 365)).strftime("%Y"),
                           key: str = os.getenv("HUD_KEY")) -> pd.DataFrame:
    """
    Function to query the Fair Markets Rent API provided by US
    Department of Housing and Urban Development. This returns county
    FMR for state level queries.

    Parameters
    ----------

    state : The state to query for. Can be abbreviation, fip code, or
         full name.

    year : Gets the year that this data was recorded. Can specify multiple
        years. Default is the previous year.

    key : The API key for this user. You must go to HUD and sign up for an
        account and request for an API key.
        
    See Also
    --------
    
    * hud_fmr()
    * hud_fmr_state_metroareas()
    * hud_fmr_state_counties()
    * hud_fmr_county_zip()
    * hud_fmr_metroarea_zip()

    Returns
    -------

    This returns a dataframe with county
    fair markets rent based on state level queries.

    Examples
    --------

    >>> hud_fmr_state_counties("VA", year = c(2021))

    >>> hud_fmr_state_counties("Alabama", year = c(2021))
 
    >>> hud_fmr_state_counties("24", year = c(2021)))
    """

    if(not hudinternetonline.internet_on()): raise ConnectionError("You currently do not have internet access.")

    args = hudinputcheck.fmr_il_input_check_cleansing(state, year, key)
    query = args[1]
    year = args[2]
    key = args[3]

    error_urls = list()

    # Create all combinations of query and year...
    all_queries = list(itertools.product(query, year))

    # Make query calls for all queries.
    result = pd.DataFrame()

    for i in range(len(all_queries)):
        urls = "https://www.huduser.gov/hudapi/public/fmr/" + \
               "statedata/" + \
               all_queries[i, 1] + \
               "?year=" + \
               all_queries[i, 2]

        headers = {"Authorization": "Bearer " + key, "User-Agent": "https://github.com/etam4260/hudpy"}
        call = urllib3.http.request("GET", urls, headers = headers, timeout = 30)
                            
        cont = json.loads(call.data.decode('utf-8'))
        
        huddownloadbar.download_bar(i, len(all_queries))

        if "error" in cont.columns:
            error_urls.append(urls)
        else:
            result.append(cont["data"]["counties"])

   # Just print a newline
    print()

    if len(error_urls) != 0:
        # Print all error urls
        # Construct warning message... 
        warn_msg = "Could not find data for queries: \n\n" + \
                    "\n".join(error_urls) +  "\n" + \
                    "It is possible that your key is invalid or there isn't \
                    any data for these parameters. If you think this is wrong please \
                    report it at https://github.com/etam4260/hudpy/issues"    


        warn(warn_msg)

    return(result)

def hud_fmr_county_zip(county: Union[int, str, List[int], List[str], Tuple[int], Tuple[str]],
                       year: Union[int, str, List[int], List[str], Tuple[int], Tuple[str]] = (date.today() - timedelta(days = 365)).strftime("%Y"),
                       key: str = os.getenv("HUD_KEY")) -> pd.DataFrame:
    """
    Function to query the Fair Markets Rent API provided by US
    Department of Housing and Urban Development. This returns zip code
    FMR for county level queries.

    Parameters
    ----------

    county : Counties to query for. Must be provided as a 5 digit fips code.

    year : Gets the year that this data was recorded. Can specify multiple
        years. Default is the previous year.

    key : The API key for this user. You must go to HUD and sign up for an
        account and request for an API key.
        
    See Also
    --------
    
    * hud_fmr()
    * hud_fmr_state_metroareas()
    * hud_fmr_state_counties()
    * hud_fmr_county_zip()
    * hud_fmr_metroarea_zip()

    Returns
    -------

    This returns a dataframe with zip code level
    fair markets rent based on county queries.

    Examples
    --------

    >>> hud_fmr_county_zip("5100199999", year = c(2021))
 
    >>> hud_fmr_county_zip("5100199999", year = c("2021"))
 
    >>> hud_fmr_county_zip(5151099999, year = c(2021))
    """

    if(not hudinternetonline.internet_on()): raise ConnectionError("You currently do not have internet access.")

    args = hudinputcheck.fmr_il_input_check_cleansing(county, year, key)
    query = args[1]
    year = args[2]
    key = args[3]

    error_urls = list()

    all_queries = list(itertools.product(["https://www.huduser.gov/hudapi/public/fmr/data/"], query, ["?year="], year))
    
    # Make query calls for all queries.
    result = pd.DataFrame()
    
    urls = []
    for i in range(0, len(all_queries)):
        urls.append(
            all_queries[i][0] + 
            all_queries[i][1] +
            all_queries[i][2] +
            all_queries[i][3]
        )

    for i in range(len(urls)):
        url = urls[i]

        headers = {"Authorization": "Bearer " + key, "User-Agent": "https://github.com/etam4260/hudpy"}
        call = urllib3.http.request("GET", url, headers = headers, timeout = 30)

        cont = json.loads(call.data.decode('utf-8'))    
        cont = pd.json_normalize(cont) 

        huddownloadbar.download_bar(i, len(urls))

        if "error" in cont.columns:
            error_urls.append(urls)
        else:
            result.append(cont["data"]["counties"])


def hud_fmr_metroarea_zip(metroarea: Union[str, List[str], Tuple[str]],
                          year: Union[int, str, List[int], List[str], Tuple[int], Tuple[str]] = (date.today() - timedelta(days = 365)).strftime("%Y"),
                          key: str = os.getenv("HUD_KEY")) -> pd.DataFrame:
    """
    Function to query the Fair Markets Rent API provided by US
    Department of Housing and Urban Development. This returns zip code
    FMR for metroarea level queries.

    Parameters
    ----------

    metroarea : Metroareas to query for.

    year : Gets the year that this data was recorded. Can specify multiple
        years. Default is the previous year.

    key : The API key for this user. You must go to HUD and sign up for an
        account and request for an API key.
        
    See Also
    --------
    
    * hud_fmr()
    * hud_fmr_state_metroareas()
    * hud_fmr_state_counties()
    * hud_fmr_county_zip()
    * hud_fmr_metroarea_zip()

    Returns
    -------

    This returns a dataframe with zip code level
    fair markets rent based on metroarea queries.

    Examples
    --------

    >>> hud_fmr_metroarea_zip("METRO47900M47900", year = c(2018))
 
    >>> hud_fmr_metroarea_zip("METRO29180N22001", year = c(2019))
 
    >>> hud_fmr_metroarea_zip("METRO10380M10380", year = c(2020))
    """

    if(not hudinternetonline.internet_on()): raise ConnectionError("You currently do not have internet access.")


    args = hudinputcheck.fmr_il_input_check_cleansing(metroarea, year, key)
    query = args[1]
    year = args[2]
    key = args[3]

    error_urls = list()

    all_queries = list(itertools.product(["https://www.huduser.gov/hudapi/public/fmr/data/"], query, ["?year="], year))
    
    # Make query calls for all queries.
    result = pd.DataFrame()
    
    urls = []
    for i in range(0, len(all_queries)):
        urls.append(
            all_queries[i][0] + 
            all_queries[i][1] +
            all_queries[i][2] +
            all_queries[i][3]
        )

    for i in range(len(urls)):
        url = urls[i]

        headers = {"Authorization": "Bearer " + key, "User-Agent": "https://github.com/etam4260/hudpy"}
        call = urllib3.http.request("GET", url, headers = headers, timeout = 30)

        cont = json.loads(call.data.decode('utf-8'))    
        cont = pd.json_normalize(cont) 

        huddownloadbar.download_bar(i, len(urls))

        if "error" in cont.columns:
            error_urls.append(urls)
        else:
            result.append(cont["data"]["counties"])