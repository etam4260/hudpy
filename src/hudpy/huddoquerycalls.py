from __future__ import annotations
from typing import Union

import urllib3
import pandas as pd

import json
from distutils.log import warn

from hudpy import huddownloadbar
from hudpy import hudpkgenv

def chas_do_query_calls(urls: Union[str, list[str]], key: str) -> pd.DataFrame:
    """
    Helper function to query Comprehensive Housing and Affordability (CHAS) API from 
    the US Department of Housing and Urban Development for 
    all hud_chas() family of functions. 

    Parameters
    ----------
    urls: The urls to query for.

    key : The API key for this user. You must go to HUD and sign up for an
        account and request for an API key.

    Returns
    -------
    This concatenates the response bodies from all urls call as a dataframe.

    """

    error_urls = list()
    res = pd.DataFrame()

    all_measurements = list("geoname", "sumlevel", "year",
                            "A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8", "A9",
                            "A10", "A11", "A12", "A13", "A14", "A15", "A16", "A17",
                            "A18",
                            "B1", "B2", "B3", "B4", "B5", "B6", "B7",
                            "B8", "B9",
                            "C1", "C2", "C3", "C4", "C5", "C6",
                            "D1", "D2", "D3",
                            "D4", "D5", "D6", "D7", "D8", "D9", "D10", "D11", "D12",
                            "E1", "E2", "E3", "E5", "E6", "E7", "E9", "E10", "E11",
                            "E13", "E14", "E15", "E17", "E18", "E19", "E21", "E22",
                            "E23",
                            "F1", "F2", "F3", "F5", "F6", "F7", "F9", "F10", "F11",
                            "F13", "F14", "F15", "F17", "F18", "F19", "F21", "F22",
                            "F23",
                            "G1", "G2", "G3", "G5", "G6", "G7", "G9", "G10", "G11",
                            "G13", "G14", "G15", "G17", "G18", "G19",
                            "H1", "H2", "H4", "H5", "H7", "H8", "H10", "H11", "H13",
                            "H14", "H16",
                            "I1", "I2", "I4", "I5", "I7", "I8", "I10", "I11",
                            "I13", "I14", "I16",
                            "J1", "J2", "J4", "J5", "J7", "J8", "J10",
                            "J11", "J13", "J14", "J16")

    if hudpkgenv.pkg_env["pool_manager"] == None: hudpkgenv.pkg_env["pool_manager"] = urllib3.PoolManager()
    
    for i in range(len(urls)):

        url = urls[i]
        
        headers = {"Authorization": "Bearer " + key, "User-Agent": "https://github.com/etam4260/hudpy"}
        
        call = hudpkgenv.pkg_env["pool_manager"].request("GET", url, headers = headers)

        cont = json.loads(call.data.decode('utf-8'))    
        cont = pd.json_normalize(cont) 

        huddownloadbar.download_bar(i + 1, len(urls))

        if "error" in cont.columns or len(cont) == 0:
            # Need to output a single error message instead of a bunch when
            # something bad occurs. Append to list of errored urls.
            error_urls.append(url)
        else:
            not_measured = all_measurements[all_measurements not in cont[1].columns]
            # Check this CHAS data does not have data defined for
            # all expected fields. If so fill them in with NA's.

            if len(not_measured) >= 1:
                extra_mes = pd.repeat(None, len(not_measured))
                extra_mes.names = not_measured

                res = pd.concat([res, cont])
            else:
                res = pd.concat([res, cont])
            
    print("\n")

    # Spit out error messages to user after all
    # queries are done.
    if (len(error_urls) != 0):
        # Spit out error messages to user after all
        # queries are done.

        warn("Could not find data for queries: \n\n" +
             " ".join(map(lambda x: "*" + x, error_urls)) +
             "\n\nIt is possible that your key maybe invalid or " +
             "there isn't any data for these parameters, " +
             "If you think this is wrong please " +
             "report it at https://github.com/etam4260/rhud/issues.")

    return(res)


def cw_do_query_calls(urls, query, year, quarter, primary_geoid,
                            secondary_geoid, key) -> pd.DataFrame:
    """
    Helper function to query Crosswalk(cw) API from 
    the US Department of Housing and Urban Development for 
    all hud_cw() family of functions. 

    Parameters
    ----------
    urls : The urls to query for.

    query : The geoids to query for.

    year : The years to query for.

    quarter : The quarters in the year to query for

    primary_geoid : The first geoid part of a function call. For example,
        hud_cw_zip_tract() has zip as first GEOID and tract as second GEOID.

    secondary_geoid : The second geoid part of a function call.

    key : The API key for this user. You must go to HUD and sign up for an
        account and request for an API key.

    Returns
    -------
    This concatenates the response bodies from all urls call as a dataframe.

    """

    error_urls = list()
    res = pd.DataFrame()
  
    if hudpkgenv.pkg_env["pool_manager"] == None: hudpkgenv.pkg_env["pool_manager"] = urllib3.PoolManager()
    
    for i in range(len(urls)):

        url = urls[i]

        headers = {"Authorization": "Bearer " + key, "User-Agent": "https://github.com/etam4260/hudpy"}
        call = hudpkgenv.pkg_env["pool_manager"].request("GET", url, headers = headers)
    
        cont = json.loads(call.data.decode('utf-8'))    
        cont = pd.json_normalize(cont["data"]["results"]) 
        
        huddownloadbar.download_bar(i + 1, len(urls))
        
        if "error" in cont.columns or len(cont) == 0:
            # Need to output a single error message instead of a bunch when
            # something bad occurs. Append to list of errored urls.
            error_urls.append(url)
        else:
    
            cont.rename(columns = {'geoid': secondary_geoid}, inplace = True)
            cont["query"] = [query[i] for j in range(0, cont.shape[0])]
            cont["year"] = [year[i] for j in range(0, cont.shape[0])]
            cont["quarter"] = [quarter[i] for j in range(0, cont.shape[0])]
            
            res = pd.concat([res, cont])
    
            
    print("\n")
    
    # Spit out error messages to user after all
    # queries are done.
    if (len(error_urls) != 0):
        # Spit out error messages to user after all
        # queries are done.

        warn("Could not find data for queries: \n\n" +
             " ".join(map(lambda x: "*" + x, error_urls)) +
             "\n\nIt is possible that your key maybe invalid or " +
             "there isn't any data for these parameters, " +
             "If you think this is wrong please " +
             "report it at https://github.com/etam4260/rhud/issues.")

    return(res)


def misc_do_query_calls(urls: Union[str, list[str]], key: str) -> pd.DataFrame:
    """
    Helper function to query misc APIs from 
    the US Department of Housing and Urban Development for 
    all hudmisc.py family of functions. 

    Parameters
    ----------
    urls: The urls to query for.

    key : The API key for this user. You must go to HUD and sign up for an
        account and request for an API key.

    Returns
    -------
    This concatenates the response bodies from all urls call as a dataframe.
    """    

    error_urls = list()
    res = pd.DataFrame()


    if hudpkgenv.pkg_env["pool_manager"] == None: hudpkgenv.pkg_env["pool_manager"] = urllib3.PoolManager()
    
    for i in range(len(urls)):

        url = urls[i]

        headers = {"Authorization": "Bearer " + key, "User-Agent": "https://github.com/etam4260/hudpy"}
        call = hudpkgenv.pkg_env["pool_manager"].request("GET", url, headers = headers)

        cont = json.loads(call.data.decode('utf-8'))    
        cont = pd.json_normalize(cont) 

        huddownloadbar.download_bar(i + 1, len(urls))

        if "error" in cont.columns or len(cont) == 0:
            # Need to output a single error message instead of a bunch when
            # something bad occurs. Append to list of errored urls.
            error_urls.append(url)
        else:
           
            res = pd.concat([res, cont])
   
            
    print("\n")

    # Spit out error messages to user after all
    # queries are done.
    if (len(error_urls) != 0):
        # Spit out error messages to user after all
        # queries are done.

        warn("Could not find data for queries: \n\n" +
             " ".join(map(lambda x: "*" + x, error_urls)) +
             "\n\nIt is possible that your key maybe invalid or " +
             "there isn't any data for these parameters, " +
             "If you think this is wrong please " +
             "report it at https://github.com/etam4260/rhud/issues.")

    return(res)