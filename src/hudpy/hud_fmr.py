from __future__ import annotations
from distutils.log import warn
from typing import Union

import os
import itertools
import urllib3
import pandas as pd
import json

from datetime import date
from datetime import timedelta

from hudpy import hud_download_bar
from hudpy import hud_internet_online
from hudpy import hud_input_check
from hudpy import hud_pkg_env

def hud_fmr_state_metroareas(state: Union[int, str, list[int], list[str], tuple[int], tuple[str]],
                             year: Union[int, str, list[int], list[str], tuple[int], tuple[str]] = (date.today() -   timedelta(days = 365)).strftime("%Y"),
                             key: str = None) -> pd.DataFrame:
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

    >>> hud_fmr_state_metroareas(state = "VA", year = 2021)

    >>> hud_fmr_state_metroareas(state = "Alabama", year = 2021)
 
    >>> hud_fmr_state_metroareas(state = "24", year = 2021)
    """  
    
    if hud_pkg_env.pkg_env["internet_on"] == False: 
        if not hud_internet_online.internet_on():
            raise ConnectionError("You currently do not have internet access.")
        else:
            hud_pkg_env.pkg_env["internet_on"] == True
            
    if(key == None and os.getenv("HUD_KEY") != None):
        key = os.getenv("HUD_KEY")
        
    args = hud_input_check.fmr_il_input_check_cleansing(state, year, key)
    query = args[0]
    year = args[1]
    key = args[2]
    querytype = args[3]

    error_urls = list()

    # Create all combinations of query and year...
    all_queries = list(itertools.product(query, year))

    # Make query calls for all queries.
    result = pd.DataFrame()

    if hud_pkg_env.pkg_env["pool_manager"] == None: hud_pkg_env.pkg_env["pool_manager"] = urllib3.PoolManager()
    
    for i in range(len(all_queries)):
        urls = "https://www.huduser.gov/hudapi/public/fmr/" + \
               "statedata/" + \
               all_queries[i][0] + \
               "?year=" + \
               all_queries[i][1]

        headers = {"Authorization": "Bearer " + key, "User-Agent": "https://github.com/etam4260/hudpy"}
        call = hud_pkg_env.pkg_env["pool_manager"].request("GET", urls, headers = headers)
                               
        cont = json.loads(call.data.decode('utf-8'))

        if "error" in pd.json_normalize(cont).columns:
            error_urls.append(urls)
        else:
            cont = pd.json_normalize(cont["data"]["metroareas"]) 
        
            cont["year"] = [all_queries[i][1] for j in range(0, cont.shape[0])]
            result = pd.concat([result, cont])
                
        hud_download_bar.download_bar(done = i + 1, total = len(all_queries), current = urls, error = len(error_urls))


    # Just print a newline
    print()

    if len(error_urls) != 0:
        # Print all error urls
        # Construct warning message... 
        warn("Could not find data for queries: \n\n" +
             "\n".join(map(lambda x: "*" + x, error_urls)) +
             "\n\nIt is possible that your key maybe invalid or " +
             "there isn't any data for these parameters, " +
             "If you think this is wrong please " +
             "report it at https://github.com/etam4260/hudpy/issues.")

    return(result.reset_index())


def hud_fmr_state_counties(state: Union[int, str, list[int], list[str], tuple[int], tuple[str]],
                           year: Union[int, str, list[int], list[str], tuple[int], tuple[str]] = (date.today() - timedelta(days = 365)).strftime("%Y"),
                           key: str = None) -> pd.DataFrame:
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

    >>> hud_fmr_state_counties(state = "VA", year = 2021)

    >>> hud_fmr_state_counties(state = "Alabama", year = 2021)
 
    >>> hud_fmr_state_counties(state = "24", year = 2021)
    """

    if hud_pkg_env.pkg_env["internet_on"] == False: 
        if not hud_internet_online.internet_on():
            raise ConnectionError("You currently do not have internet access.")
        else:
            hud_pkg_env.pkg_env["internet_on"] == True
            
    if key == None and os.getenv("HUD_KEY") != None:
        key = os.getenv("HUD_KEY")
        
    args = hud_input_check.fmr_il_input_check_cleansing(state, year, key)
    query = args[0]
    year = args[1]
    key = args[2]
    querytype = args[3]
    
    error_urls = list()

    # Create all combinations of query and year...
    all_queries = list(itertools.product(query, year))

    # Make query calls for all queries.
    result = pd.DataFrame()
    
    if hud_pkg_env.pkg_env["pool_manager"] == None: hud_pkg_env.pkg_env["pool_manager"] = urllib3.PoolManager()
  
    for i in range(len(all_queries)):
        urls = "https://www.huduser.gov/hudapi/public/fmr/" + \
               "statedata/" + \
               all_queries[i][0] + \
               "?year=" + \
               all_queries[i][1]

        headers = {"Authorization": "Bearer " + key, "User-Agent": "https://github.com/etam4260/hudpy"}
        call = hud_pkg_env.pkg_env["pool_manager"].request("GET", urls, headers = headers)
                            
        cont = json.loads(call.data.decode('utf-8'))
        
        if "error" in pd.json_normalize(cont).columns:
            error_urls.append(urls)
        else:
            cont = pd.json_normalize(cont["data"]["counties"]) 
        
            cont["year"] = [all_queries[i][1] for j in range(0, cont.shape[0])]
            result = pd.concat([result, cont])

        hud_download_bar.download_bar(done = i + 1, total = len(all_queries), current = urls, error = len(error_urls))


    # Just print a newline
    print()

    if len(error_urls) != 0:
        # Print all error urls
        # Construct warning message... 
        warn("Could not find data for queries: \n\n" +
             "\n".join(map(lambda x: "*" + x, error_urls)) +
             "\n\nIt is possible that your key maybe invalid or " +
             "there isn't any data for these parameters, " +
             "If you think this is wrong please " +
             "report it at https://github.com/etam4260/hudpy/issues.")


    return(result.reset_index())


def hud_fmr_county_zip(county: Union[int, str, list[int], list[str], tuple[int], tuple[str]],
                       year: Union[int, str, list[int], list[str], tuple[int], tuple[str]] = (date.today() - timedelta(days = 365)).strftime("%Y"),
                       key: str = None) -> pd.DataFrame:
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

    >>> hud_fmr_county_zip(county = "5100199999", year = 2021)
 
    >>> hud_fmr_county_zip(county = "5100199999", year = "2021")
 
    >>> hud_fmr_county_zip(county = 5151099999, year = 2021)
    """

    if hud_pkg_env.pkg_env["internet_on"] == False: 
        if not hud_internet_online.internet_on():
            raise ConnectionError("You currently do not have internet access.")
        else:
            hud_pkg_env.pkg_env["internet_on"] == True
            
    if(key == None and os.getenv("HUD_KEY") != None):
        key = os.getenv("HUD_KEY")
        
    args = hud_input_check.fmr_il_input_check_cleansing(county, year, key)
    query = args[0]
    year = args[1]
    key = args[2]
    querytype = args[3]

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
 
    if hud_pkg_env.pkg_env["pool_manager"] == None: hud_pkg_env.pkg_env["pool_manager"] = urllib3.PoolManager()
    
    for i in range(len(urls)):
        url = urls[i]

        headers = {"Authorization": "Bearer " + key, "User-Agent": "https://github.com/etam4260/hudpy"}
        call = hud_pkg_env.pkg_env["pool_manager"].request("GET", url, headers = headers)
                         
        cont = json.loads(call.data.decode('utf-8'))    
    
   
        if "error" in pd.json_normalize(cont).columns:
            error_urls.append(urls)
        else:
            
            content = pd.json_normalize(cont["data"]) 
        
            # The structure of data depends on small area.
            if int(content["smallarea_status"]) == 0:
                
                content.insert(0, "zip", [None])
                
                content.rename(columns={"basicdata.year": "year",
                                        "basicdata.Efficiency": "Efficiency",
                                        "basicdata.One-Bedroom": "One-Bedroom",
                                        "basicdata.Two-Bedroom": "Two-Bedroom",
                                        "basicdata.Three-Bedroom": "Three-Bedroom",
                                        "basicdata.Four-Bedroom": "Four-Bedroom"
                                       }, inplace = True)
                
                content["county"] = [all_queries[i][1] for j in range(0, content.shape[0])]
                
                result = pd.concat([result, content])
             
                
            elif int(content["smallarea_status"]) == 1:
                
                basicdata = pd.json_normalize(cont["data"]["basicdata"]) 
                content = pd.concat([content] * basicdata.shape[0], ignore_index=True)
                content.drop('basicdata', axis=1, inplace=True)
                
                
                merged = pd.concat([content, basicdata], axis = 1)
                zip = merged["zip_code"] 
                merged.drop("zip_code", axis=1, inplace=True)
                merged.insert(0, "zip", zip)
                
                year = merged["year"] 
                merged.drop("year", axis=1, inplace=True)
                merged["year"] = year
                merged["county"] = [all_queries[i][1] for j in range(0, merged.shape[0])]
                
                # drop zip and move it
                result = pd.concat([result, merged])

        hud_download_bar.download_bar(done = i + 1, total = len(all_queries), current = url, error = len(error_urls))

    if len(error_urls) != 0:
        # Print all error urls
        # Construct warning message...
        
        warn("Could not find data for queries: \n\n" +
             "\n".join(map(lambda x: "*" + x, error_urls)) +
             "\n\nIt is possible that your key maybe invalid or " +
             "there isn't any data for these parameters, " +
             "If you think this is wrong please " +
             "report it at https://github.com/etam4260/hudpy/issues.") 
            
            
    return(result.reset_index())



def hud_fmr_metroarea_zip(metroarea: Union[str, list[str], tuple[str]],
                          year: Union[int, str, list[int], list[str], tuple[int], tuple[str]] = (date.today() - timedelta(days = 365)).strftime("%Y"),
                          key: str = None) -> pd.DataFrame:
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

    >>> hud_fmr_metroarea_zip(metroarea = "METRO47900M47900", year = 2018)
 
    >>> hud_fmr_metroarea_zip(metroarea = "METRO29180N22001", year = 2019)
 
    >>> hud_fmr_metroarea_zip(metroarea = "METRO10380M10380", year = 2020)
    """

    if hud_pkg_env.pkg_env["internet_on"] == False: 
        if not hud_internet_online.internet_on():
            raise ConnectionError("You currently do not have internet access.")
        else:
            hud_pkg_env.pkg_env["internet_on"] == True
          
        
    if(key == None and os.getenv("HUD_KEY") != None):
        key = os.getenv("HUD_KEY")

    args = hud_input_check.fmr_il_input_check_cleansing(metroarea, year, key)
    query = args[0]
    year = args[1]
    key = args[2]
    querytype = args[3]

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
        
    if hud_pkg_env.pkg_env["pool_manager"] == None: hud_pkg_env.pkg_env["pool_manager"] = urllib3.PoolManager()
    
    for i in range(len(urls)):
        url = urls[i]

        headers = {"Authorization": "Bearer " + key, "User-Agent": "https://github.com/etam4260/hudpy"}
        call = hud_pkg_env.pkg_env["pool_manager"].request("GET", url, headers = headers)

        cont = json.loads(call.data.decode('utf-8'))  
        
        if "error" in pd.json_normalize(cont).columns:
            error_urls.append(urls)
        else:
            
            content = pd.json_normalize(cont["data"]) 
    
            # The structure of data depends on small area.
            if int(content["smallarea_status"]) == 0:
                content.insert(0, "zip", [None])
                
                content.rename(columns={"basicdata.year": "year",
                                        "basicdata.Efficiency": "Efficiency",
                                        "basicdata.One-Bedroom": "One-Bedroom",
                                        "basicdata.Two-Bedroom": "Two-Bedroom",
                                        "basicdata.Three-Bedroom": "Three-Bedroom",
                                        "basicdata.Four-Bedroom": "Four-Bedroom"
                                       }, inplace = True)
                
                content["metroarea"] = [all_queries[i][1] for j in range(0, content.shape[0])]
                
                result = pd.concat([result, content])
                
            elif int(content["smallarea_status"]) == 1:
                basicdata = pd.json_normalize(cont["data"]["basicdata"]) 
                content = pd.concat([content] * basicdata.shape[0], ignore_index=True)
                content.drop('basicdata', axis=1, inplace=True)
                
                
                merged = pd.concat([content, basicdata], axis = 1)
                zip = merged["zip_code"] 
                merged.drop("zip_code", axis=1, inplace=True)
                merged.insert(0, "zip", zip)
                
                year = merged["year"] 
                merged.drop("year", axis=1, inplace=True)
                merged["year"] = year
                merged["metroarea"] = [all_queries[i][1] for j in range(0, merged.shape[0])]
                
                # drop zip and move it
                result = pd.concat([result, merged])
    
        hud_download_bar.download_bar(done = i + 1, total = len(all_queries), current = url, error = len(error_urls))

    if len(error_urls) != 0:
        # Print all error urls
        # Construct warning message...
        
        warn("Could not find data for queries: \n\n" +
             "\n".join(map(lambda x: "*" + x, error_urls)) +
             "\n\nIt is possible that your key maybe invalid or " +
             "there isn't any data for these parameters, " +
             "If you think this is wrong please " +
             "report it at https://github.com/etam4260/hudpy/issues.")
            
    return(result.reset_index())