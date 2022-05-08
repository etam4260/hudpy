from distutils.log import warn
from typing import Union
import hudinputcheck
import itertools
import urllib3
import pandas as pd
import json
import huddownloadbar

def hud_fmr_state_metroareas(state: Union[int, str, list: int, list: str, tuple: Union[int, str]],
                             year: Union[int, str, list: int, list: str, tuple: Union[int, str]],
                             key: str):
    """
    #' @name hud_fmr_state_metroareas
    #' @title hud_fmr_state_metroareas
    #' @description This function queries for a state and returns the
    #'   FMR calculation
    #'   at a metroarea resolution for all metroareas in this state.
    #' @param state The state to query for.
    #' @param year Gets the year that this data was recorded.
    #'   Can specify multiple years. Default is the
    #'   previous year.
    #' @param key The API key for this user. You must go to HUD and sign up
    #'   for an account and request for an API key.
    #' @keywords Fair Markets Rent API
    #' @returns A data frame with fair markets rent for metro areas in states.
    """  
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


def hud_fmr_state_counties(state: Union[int, str, list: int, list: str, tuple: Union[int, str]],
                           year: Union[int, str, list: int, list: str, tuple: Union[int, str]],
                           key: str):
    """
    #' @name hud_fmr_state_counties
    #' @title hud_fmr_state_counties
    #' @description This function queries for a state and returns the
    #'   FMR calculation
    #'   at a county resolution for all counties in this state.
    #' @param state The state to query for.
    #' @param year Gets the year that this data was recorded.
    #'   Can specify multiple years. Default is the
    #'   previous year.
    #' @param key The API key for this user. You must go to HUD and sign up
    #'   for an account and request for an API key.
    #' @keywords Fair Markets Rent API
    #' @returns A data frame with fair markets rent for counties in states.
    """
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

def hud_fmr_county_zip(county: Union[int, str, list: int, list: str, tuple: Union[int, str]],
                       year: Union[int, str, list: int, list: str, tuple: Union[int, str]],
                       key: str):
    """
    #' @name hud_fmr_county_zip
    #' @title hud_fmr_county_zip
    #' @description This function queries for a county and returns FMR calculation.
    #'    If the county is not
    #'    a small area, it will return only single
    #'    measurement for that county. If the county is considered a small area,
    #'    it will return data at a zip code level.
    #' @param county A county to query for.
    #' @param year Gets the year that this data was recorded.
    #'   Can specify multiple years. Default is the
    #'   previous year.
    #' @param key The API key for this user. You must go to HUD and sign up
    #'   for an account and request for an API key.
    #' @keywords Fair Markets Rent API
    #' @returns A data frame with fair markets rent for zip codes in counties.
    """

def hud_fmr_metroarea_zip(metroarea: Union[str, list: str, tuple: str],
                          year: Union[str, list: str, tuple: str],
                          key: str):
    """
    #' @name hud_fmr_metroarea_zip
    #' @title hud_fmr_metroarea_zip
    #' @description This function queries for a metroarea and returns
    #'    FMR calculation. If the metroarea is not
    #'    a small area, it will return only single
    #'    measurement for that metroarea. If the metrarea is considered a
    #'    small area, it will return data at a zip code level.
    #' @param metroarea A metroarea to query for.
    #' @param year Gets the year that this data was recorded.
    #'   Can specify multiple years. Default is the
    #'   previous year.
    #' @param key The API key for this user. You must go to HUD and sign up
    #'   for an account and request for an API key.
    #' @keywords Fair Markets Rent API
    #' @returns A data frame with fair markets rent for zip codes in metro areas.
    """