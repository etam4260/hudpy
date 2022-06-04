from __future__ import annotations
from typing import Union

import urllib3
import pandas as pd

import json
from distutils.log import warn

from hudpy import hud_download_bar
from hudpy import hud_pkg_env

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

    if hud_pkg_env.pkg_env["pool_manager"] == None: hud_pkg_env.pkg_env["pool_manager"] = urllib3.PoolManager()
    
    for i in range(len(urls)):

        url = urls[i]
        
        headers = {"Authorization": "Bearer " + key, "User-Agent": "https://github.com/etam4260/hudpy"}
        
        call = hud_pkg_env.pkg_env["pool_manager"].request("GET", url, headers = headers)

        cont = json.loads(call.data.decode('utf-8'))    
    
        if "error" in pd.json_normalize(cont).columns:
            # Need to output a single error message instead of a bunch when
            # something bad occurs. Append to list of errored urls.
            error_urls.append(url)
        else:
            
            cont = pd.json_normalize(cont[0]) 
                
            res = pd.concat([res, cont])
        
        hud_download_bar.download_bar(done = i + 1, total = len(urls), current = url, error = len(error_urls))

    print("\n")

    # Spit out error messages to user after all
    # queries are done.
    if (len(error_urls) != 0):
        # Spit out error messages to user after all
        # queries are done.

        warn("Could not find data for queries: \n\n" +
             "\n".join(map(lambda x: "*" + x, error_urls)) +
             "\n\nIt is possible that your key maybe invalid or " +
             "there isn't any data for these parameters, " +
             "If you think this is wrong please " +
             "report it at https://github.com/etam4260/hudpy/issues.")


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
  
    if hud_pkg_env.pkg_env["pool_manager"] == None: hud_pkg_env.pkg_env["pool_manager"] = urllib3.PoolManager()
    
    for i in range(len(urls)):

        url = urls[i]

        headers = {"Authorization": "Bearer " + key, "User-Agent": "https://github.com/etam4260/hudpy"}
        call = hud_pkg_env.pkg_env["pool_manager"].request("GET", url, headers = headers)
    
        cont = json.loads(call.data.decode('utf-8'))    

        if "error" in pd.json_normalize(cont).columns:
            
            # Need to output a single error message instead of a bunch when
            # something bad occurs. Append to list of errored urls.
            error_urls.append(url)
        else:
            cont = pd.json_normalize(cont["data"]["results"]) 
        
            cont.rename(columns = {'geoid': secondary_geoid}, inplace = True)
            cont[primary_geoid] = [query[i] for j in range(0, cont.shape[0])]
            cont["year"] = [year[i] for j in range(0, cont.shape[0])]
            cont["quarter"] = [quarter[i] for j in range(0, cont.shape[0])]
            
            res = pd.concat([res, cont])
        
        hud_download_bar.download_bar(done = i + 1, total = len(urls), current = url, error = len(error_urls))

            
    print("\n")
    
    # Spit out error messages to user after all
    # queries are done.
    if (len(error_urls) != 0):
        
        # Spit out error messages to user after all
        # queries are done.
        warn("Could not find data for queries: \n\n" +
             "\n".join(map(lambda x: "*" + x, error_urls)) +
             "\n\nIt is possible that your key maybe invalid or " +
             "there isn't any data for these parameters, " +
             "If you think this is wrong please " +
             "report it at https://github.com/etam4260/hudpy/issues.")


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


    if hud_pkg_env.pkg_env["pool_manager"] == None: hud_pkg_env.pkg_env["pool_manager"] = urllib3.PoolManager()
    
    for i in range(len(urls)):

        url = urls[i]

        headers = {"Authorization": "Bearer " + key, "User-Agent": "https://github.com/etam4260/hudpy"}
        call = hud_pkg_env.pkg_env["pool_manager"].request("GET", url, headers = headers)

        cont = json.loads(call.data.decode('utf-8'))    
        cont = pd.json_normalize(cont) 

        if "error" in pd.json_normalize(cont).columns:
            # Need to output a single error message instead of a bunch when
            # something bad occurs. Append to list of errored urls.
            error_urls.append(url)
        else:
           
            res = pd.concat([res, cont])
        
        hud_download_bar.download_bar(done = i + 1, total = len(urls), current = url, error = len(error_urls))

            
    print("\n")

    # Spit out error messages to user after all
    # queries are done.
    if (len(error_urls) != 0):
        # Spit out error messages to user after all
        # queries are done.

        warn("Could not find data for queries: \n\n" +
             "\n".join(map(lambda x: "*" + x, error_urls)) +
             "\n\nIt is possible that your key maybe invalid or " +
             "there isn't any data for these parameters, " +
             "If you think this is wrong please " +
             "report it at https://github.com/etam4260/hudpy/issues.")

    return(res)