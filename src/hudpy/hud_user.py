from __future__ import annotations
from typing import Union
from distutils.log import warn

import os
from datetime import date
import pandas as pd
import itertools
import json
import urllib3

from datetime import date
from datetime import timedelta
from hudpy import hud_internet_online
from hudpy import hud_input_check
from hudpy.hud_fmr import *
from hudpy.hud_cw import *
from hudpy import hud_pkg_env
from hudpy import hud_download_bar
from hudpy import hud_do_query_calls


def hud_cw(type: Union[str, int],
           query: Union[int, str, list[int], list[str], tuple[int], tuple[str]] = None,
           year: Union[int, str, list[int], list[str], tuple[int], tuple[str]] = (date.today() -   timedelta(days = 365)).strftime("%Y"),
           quarter: Union[int, str, list[int], list[str], tuple[int], tuple[str]] = 1,
           minimal: bool = False,
           key: str = None) -> pd.DataFrame:
    """
    Omni-function to query the Crosswalks API provided by US
    Department of Housing and Urban Development. This follows closely 
    to the design of API provided by HUD. 

    Parameters
    ----------
    type : Must be a number between 1 and 12 depending on the Crosswalk
        type. You can also supply the string name.
        1) zip-tract
        2) zip-county
        3) zip-cbsa
        4) zip-cbsadiv (Available 4th Quarter 2017 onwards)
        5) zip-cd
        6) tract-zip
        7) county-zip
        8) cbsa-zip
        9) cbsadiv-zip (Available 4th Quarter 2017 onwards)
        10) cd-zip
        11) zip-countysub (Available 2nd Quarter 2018 onwards)
        12) countysub-zip (Available 2nd Quarter 2018 onwards)

    query :   
         Depending on the type specified, the input for query changes:
         
         5 digit USPS ZIP code of the data to retrieve.
         E.g. 22031 for type 1 to 5 and 11 .
         
         or
         
         11 digit unique 2000 or 2010 Census tract GEOID consisting of
         state FIPS + county FIPS + tract code. Eg: 51059461700  for type 6
         
         or
         
         5 digit unique 2000 or 2010 Census county GEOID consisting of
         state FIPS + county FIPS. Eg: 51600 for type 7
         
         or
         
         5 digit CBSA code for Micropolitan and Metropolitan Areas
         Eg: 10380 for type 8
         
         or
         
         5-digit CBSA Division code which only applies to Metropolitan Areas.
         Eg: 35614 for type 9
         
         or
         
         4-digit GEOID for the Congressional District which consists of
         state FIPS + Congressional District code. Eg: 7200 for type 10
         
         or
         
         10-digit GEOID for the County sub Eg: 4606720300 for type 12

    year : Gets the year(s) that this data was recorded. Can specify multiple
        years. Default is the previous year.
    
    quarter : Gets the quarter(s) of the year(s) that this data was recorded.
        Defaults to the first quarter of the year(s).

    minimal : Return just the crosswalked geoids if true. Otherwise, return
        all fields. This does not remove duplicates.

    key : The API key for this user. You must go to HUD and sign up for an
        account and request for an API key.

    See Also
    --------
    
    * crosswalk()
    * hud_cw_zip_tract()
    * hud_cw_zip_county()
    * hud_cw_zip_cbsa()
    * hud_cw_zip_cbsadiv()
    * hud_cw_zip_countysub()
    * hud_cw_zip_cd()
    * hud_cw_tract_zip()
    * hud_cw_county_zip()
    * hud_cw_cbsa_zip()
    * hud_cw_cbsadiv_zip()
    * hud_cw_cd_zip()
    * hud_cw_countysub_zip()
    * hud_cw()

    Returns
    -------

    A dataframe mapping the geoid(s) query to their corresponding crosswalked geoid(s), including 
    data on their intersecting residential, business, other, and total address percentage. 
    For more details on these measurements, visit https://www.huduser.gov/portal/dataset/uspszip-api.html

    Examples
    --------

    >>> hud_cw(type = 1, zip = "35213", year = "2010", quarter = "1")
    
    >>> hud_cw(type = 1, zip = "35213", year = "2010", quarter = "1",
        minimal = True)



    >>> hud_cw(type = "2", query = "35213", year = ["2016", "2020"],
       quarter = c("2"))

    >>> hud_cw(type = "2", query = "35213", year = ["2016", "2020"],
       quarter = c("2"), minimal = True)



    >>> hud_cw(type = 3, query = 35213, year = ["2012", "2011"],
       quarter = "3")

    >>> hud_cw(type = 3, query = 35213, year = ["2012", "2011"],
       quarter = "3", minimal = True)



    >>> hud_cw(type = 4, query = "22031", year = ["2017", "2019"],
       quarter = "4")
       
    >>> hud_cw(type = 4, query = "22031", year = ["2017", "2019"],
       quarter = "4")



    >>> hud_cw(type = "5", query = "35213", year = [2011, "2012"],
       quarter = ["1", "2"])

    >>> hud_cw(type = "5", query = "35213", year = [2011, "2012"],
       quarter = ["1", "2"])



    >>> hud_cw(type = 6, query = "48201223100", year = ["2017", "2010"],
       quarter = ["1", "2", "3"])

    >>> hud_cw(type = 6, query = "48201223100", year = ["2017", "2010"],
       quarter = ["1", "2", "3"])



    >>> hud_cw(type = 7, query = "22031", year = ["2010", "2011"],
       quarter = ["1", "2", "3"])

    >>> hud_cw(type = 7, query = "22031", year = ["2010", "2011"],
       quarter = ["1", "2", "3"])



    >>> hud_cw(type = 8, query = "10140", year = ["2010", "2011"],
       quarter = ["1", "2"])

    >>> hud_cw(type = 8, query = "10140", year = ["2010", "2011"],
       quarter = ["1", "2"])



    >>> hud_cw(type = 9, query = "10380", year = ["2017"],
       quarter = ["1", "2", "3"])

    >>> hud_cw(type = 9, query = "10380", year = ["2017"],
       quarter = ["1", "2", "3"])



    >>> hud_cw(type = 10, query = "2202", year = ["2010", "2011"],
       quarter = ["4", "3"])

    >>> hud_cw(type = 10, query = "2202", year = ["2010", "2011"],
       quarter = ["4", "3"])



    >>> hud_cw(type = 11, query = "35213", year = ["2019", "2020"],
       quarter = ["2", "3"])
       
    >>> hud_cw(type = 11, query = "35213", year = ["2019", "2020"],
       quarter = ["2", "3"])



    >>> hud_cw(type = 12, query = "4606720300 ", year = ["2019", "2019", "2019"],
       quarter = ["4", "4"])
    >>> hud_cw(type = 12, query = "4606720300 ", year = ["2019", "2019", "2019"],
       quarter = ["4", "4"])

    """
    
    # Call the appropriate decomposed function depending on type specified
    if type == 1 or type == "1" or type == "zip-tract" :
        return(hud_cw_zip_tract(zip = query, year = year, quarter = quarter, minimal = minimal, key = key))
    
    elif type == 2 or type == "2" or type == "zip-county":
        return(hud_cw_zip_county(zip = query, year = year, quarter = quarter, minimal = minimal, key = key))
    
    elif type == 3 or type == "3" or type == "zip-cbsa":
        return(hud_cw_zip_cbsa(zip = query, year = year, quarter = quarter, minimal = minimal, key = key))
    
    elif type == 4 or type == "4" or type == "zip-cbsadiv":
        return(hud_cw_zip_cbsadiv(zip = query, year = year, quarter = quarter, minimal = minimal, key = key))
    
    elif type == 5 or type == "5" or type == "zip-cd":
        return(hud_cw_zip_cd(zip = query, year = year, quarter = quarter, minimal = minimal, key = key))
    
    elif type == 6 or type == "6" or type == "tract-zip":    
        return(hud_cw_tract_zip(tract = query, year = year, quarter = quarter, minimal = minimal, key = key))
        
    elif type == 7 or type == "7" or type == "county-zip":
        return(hud_cw_county_zip(county = query, year = year, quarter = quarter, minimal = minimal, key = key))
        
    elif type == 8 or type == "8" or type == "cbsa-zip":
        return(hud_cw_cbsa_zip(cbsa = query, year = year, quarter = quarter, minimal = minimal, key = key))
        
    elif type == 9 or type == "9" or type == "cbsadiv-zip":
        return(hud_cw_cbsadiv_zip(cbsadiv = query, year = year, quarter = quarter, minimal = minimal, key = key))
    elif type == 10 or type == "10" or type == "cd-zip":
        return(hud_cw_cd_zip(cd = query, year = year, quarter = quarter, minimal = minimal, key = key))
        
    elif type == 11 or type == "11" or type == "zip-countysub": 
        return(hud_cw_zip_countysub(zip = query, year = year, quarter = quarter, minimal = minimal, key = key))     
    elif type == 12 or type == "12" or type == "countysub-zip":
        return(hud_cw_countysub_zip(countysub = query, year = year, quarter = quarter, minimal = minimal, key = key))
    else:
        raise ValueError("\nPlease check if the type argument is valid.")
    
    

def hud_fmr(query: Union[int, str, list[int], list[str], tuple[int], tuple[str]] = None,
            year: Union[int, str, list[int], list[str], tuple[int], tuple[str]] = (date.today() -   timedelta(days = 365)).strftime("%Y"),
            key: str = None) -> pd.DataFrame:
    """
    Function to query the Fair Markets Rent API provided by US
    Department of Housing and Urban Development. This function encapsulated
    the functionalities of. If querying for a state, data will be returned 
    with measurements for metroareas and counties within the state(s). Querying 
    for county(s) or metroarea(s) will return data at a zipcode level if 
    area is a 'small area.' Otherwise, measurement be described at the county
    or metroareas resolution.

    * hud_fmr_state_metroareas()
    * hud_fmr_state_counties()
    * hud_fmr_county_zip()
    * hud_fmr_metroarea_zip()

    Parameters
    ----------

    query : Can provide either a 5 digit FIPS code + 99999 at end,
         state (abbreviation, fip, fullname), or CBSA code.

    year : Gets the year(s) that this data was recorded. Can specify multiple
        year(s). Default is the previous year.

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

    This returns a dataframe with fair markets rent measurements based on the resolution of query.
    For more details about these measurements, go to https://www.huduser.gov/portal/dataset/fmr-api.html

    Examples
    --------

    >>> hud_fmr("VA", year = 2021)

    >>> hud_fmr("5100199999", year = 2021)

    >>> hud_fmr("METRO47900M47900", year = 2018)
    """

    if key == None and os.getenv("HUD_KEY") != None:
        key = os.getenv("HUD_KEY")
        
    args = hud_input_check.fmr_il_input_check_cleansing(query, year, key)

    query = args[0]
    year = args[1]
    key = args[2]
    querytype = args[3]

    # If state query, will provide data at metro and county level
    # Call helper functions...
    if (querytype == ["state"]):
        # Merge county level data with metroarea data.
        return({"counties": hud_fmr_state_counties(query, year, key),
                    "metroareas": hud_fmr_state_metroareas(query, year, key)})
    elif querytype == ["cbsa"]:
        # Returns zip level data.
        return(hud_fmr_metroarea_zip(query, year, key))
    elif querytype == ["county"]:
        # Returns zip level data.
        return(hud_fmr_county_zip(query, year, key))
    

    
    
def hud_il(query: Union[int, str, list[int], list[str], tuple[int], tuple[str]] = None,
           year: Union[int, str, list[int], list[str], tuple[int], tuple[str]] = (date.today() -   timedelta(days = 365)).strftime("%Y"),
           key: str = None) -> pd.DataFrame:
    """
    Function to query the Income Limits API provided by US
    Department of Housing and Urban Development. Measurements are provided at 
    the same resolution as the query.

    Parameters
    ----------

    query : Can provide either a 5 digit FIPS code + 99999 at end,
         state (abbreviation, fip, fullname), or CBSA code.

    year : Gets the year(s) that this data was recorded. Can specify multiple
        year(s). Default is the previous year.

    key : The API key for this user. You must go to HUD and sign up for an
        account and request for an API key.

    Returns
    -------

    This returns a dataframe with income limits measurements based on the resolution of query.
    For more details about these measurements, go to https://www.huduser.gov/portal/dataset/fmr-api.html
    
    Examples
    --------

    >>> hud_il("VA", year = 2021)

    >>> hud_il("5100199999", year = 2021)

    >>> hud_il("METRO47900M47900", year = 2018)
    
    """
    
    if hud_pkg_env.pkg_env["internet_on"] == False: 
        if not hud_internet_online.internet_on():
            raise ConnectionError("You currently do not have internet access.")
        else:
            hud_pkg_env.pkg_env["internet_on"] == True
            
    if key == None and os.getenv("HUD_KEY") != None:
        key = os.getenv("HUD_KEY")
    
    args = hud_input_check.fmr_il_input_check_cleansing(query, year, key)
    
    query = args[0]
    year = args[1]
    key = args[2]
    querytype = args[3]

    error_urls = list()

    all_queries = list(itertools.product(query, year))
    
    # Make query calls for all queries.
    result = pd.DataFrame()

    if hud_pkg_env.pkg_env["pool_manager"] == None: hud_pkg_env.pkg_env["pool_manager"] = urllib3.PoolManager()
    
    for i in range(len(all_queries)):
        url_piece = "statedata/" if querytype == ["state"] else "data/"
        
        urls = "https://www.huduser.gov/hudapi/public/il/" + \
               url_piece + \
               all_queries[i][0] + \
               "?year=" + \
               all_queries[i][1]

        headers = {"Authorization": "Bearer " + key, "User-Agent": "https://github.com/etam4260/hudpy"}
        call = hud_pkg_env.pkg_env["pool_manager"].request("GET", urls, headers = headers)
                               
        cont = json.loads(call.data.decode('utf-8'))
        
        if cont == "State Level data is not available for this input" or "error" in pd.json_normalize(cont).columns:
            error_urls.append(urls)
        else:
            
            if querytype == ["state"]:
                data = pd.json_normalize(cont["data"])
                
                ver_low = pd.json_normalize(cont["data"]["very_low"])
                ext_low = pd.json_normalize(cont["data"]["extremely_low"])
                low = pd.json_normalize(cont["data"]["low"])
                
                res = pd.concat([data, ver_low, ext_low, low], axis = 1)
                
                res.rename(columns = {"statecode": "query"}, inplace = True)
                
            elif querytype == ["county"]:
                res =  pd.json_normalize(cont["data"])
                res.insert(1, "query", all_queries[i][0])
            elif querytype == ["cbsa"]:
                res =  pd.json_normalize(cont["data"])
                res.insert(1, "query", all_queries[i][0])
                
            result = pd.concat([result, res])
        
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
    

def hud_chas(type: Union[str, int],
             state_id: Union[int, str, list[int], list[str], tuple[int], tuple[str]] = None,
             entity_id: Union[int, str, list[int], list[str], tuple[int], tuple[str]] = None,
             year: Union[int, str, list[int], list[str], tuple[int], tuple[str]] = "2014-2018",
             key: str = None) -> pd.DataFrame:
    """
    Function to query Comprehensive Housing and Affordability (CHAS) API provided
    by the US Department of Housing and Urban Development. This returns CHAS measurements
    based on the geoids queried for. This follows closely to how HUD designed their API. For more 
    intuitive querying check the other functions [See Also] below.

    Parameters
    ----------
    type: Queries the data based off:
         1 - Nation
         2 - State
         3 - County
         4 - MCD
         5 - Place

    state_id: The state(s) to query for CHAS. Can be provided as the full name, fip code or
        abbreviation. If no state_id or entity_id is provided, then will query for the nation.
        For types 2,3,4,5, you must provide a stateId.

    entity_id: If None, then will query for state level data described in state_id. Can also supply county
        fip, place code, or minor civil division code. For types 3,4,5, you must provide a fips code.

    year : Gets the year(s) that this data was recorded. Defaults to 2014-2018.
         There are specific year ranges that are only accepted.
         * 2014-2018
         * 2013-2017
         * 2012-2016
         * 2011-2015
         * 2010-2014
         * 2009-2013
         * 2008-2012
         * 2007-2011
         * 2006-2010

    key : The API key for this user. You must go to HUD and sign up for an
        account and request for an API key.

    See Also
    --------
    
    * hud_chas()
    * hud_chas_nation()
    * hud_chas_state()
    * hud_chas_county()
    * hud_chas_place()
    * hud_chas_mcd()

    Returns
    -------
    This returns a dataframe with CHAS data for the specified query. 
    For more details about these measurements, go to
    https://www.huduser.gov/portal/dataset/chas-api.html

    Examples
    --------
    >>> hud_chas(1)

    >>> hud_chas("2", state_id = "56")

    >>> hud_chas("3", "51", "199")

    >>> hud_chas("4", "51", 94087)

    >>> hud_chas("5", "51", 48996)

    """

    if hud_pkg_env.pkg_env["internet_on"] == False: 
        if not hud_internet_online.internet_on():
            raise ConnectionError("You currently do not have internet access.")
        else:
            hud_pkg_env.pkg_env["internet_on"] == True

    if key == None and os.getenv("HUD_KEY") != None:
        key = os.getenv("HUD_KEY")

    if type == "nation":
        type = 1
    elif type == "state":
        type = 2
    elif type == "county":
        type = 3
    elif type == "mcd":
        type = 4
    elif type == "place":
        type = 5
    elif type == "city":
        type = 5

    if not isinstance(type, (int, str)) :
        raise ValueError("\ntype should be int or str")
    
    if state_id != None and not isinstance(state_id, (int, str, list)):
        raise ValueError("\nstate_id should be int, str, or list or tuple of ints and strings.")
    
    if entity_id != None and not isinstance(entity_id, (int, str, list)):
        raise ValueError("\nentity_id should be int, str, or list or tuple of ints and strings.")

    if not isinstance(year, (int, str, list)) :
        raise ValueError("\nYear should be int, str, or list or tuple of ints and strings.")
    
    if key == None:
        raise ValueError("\nIt looks like the HUD_KEY was not set: use hud_set_key().")
        
    if not isinstance(key, str):
        raise ValueError("\nKey should be a string")

    year = [str(year)] if isinstance(year, str) or isinstance(year, int) else list(map(lambda x: str(x), year))

    if isinstance(state_id, str) or isinstance(state_id, int):
        state_id = [str(state_id)] 
        entity_id = [str(entity_id)]
        
    year = list(set(map(lambda x: str.strip(x), year)))
    
    possible_years = ["2014-2018", "2013-2017",
                      "2012-2016", "2011-2015",
                      "2010-2014", "2009-2013",
                      "2008-2012", "2007-2011",
                      "2006-2010"]

    for i in range(0, len(year)):
        if year[i] not in possible_years:
            raise ValueError("\nOne of the years does not fall into the values " +
                             "expected")
    
    if str(type) != "1":
        state_id  = list(set(map(lambda x: str.strip(x), state_id )))
        entity_id = list(set(map(lambda x: str.strip(x), entity_id)))

    if int(type) < 1 or int(type) > 5:
        raise ValueError("\nThe type input is not in the range of 1-5")


    if str(type) == "1": 
        all_queries = list(itertools.product(["https://www.huduser.gov/hudapi/public/chas?type=1"], 
                                             ["&year="], year))
        
        urls = []
        for i in range(len(all_queries)):
            urls.append(
                all_queries[i][0] + 
                all_queries[i][1] +
                all_queries[i][2] 
            )


    elif str(type) == "2": 
        if state_id == None: raise ValueError("You need to specify a stateId for this type.")
           

        all_queries = list(itertools.product(["https://www.huduser.gov/hudapi/public/chas?type=2&stateId="], 
                                            state_id, ["&year="], year))
        
        urls = []
        for i in range(len(all_queries)):
            urls.append(
                all_queries[i][0] + 
                all_queries[i][1] +
                all_queries[i][2] +
                all_queries[i][3]
            )
  
    elif str(type) == "3" or str(type) == "4" or str(type) == "5": 
        if state_id == None or entity_id == None: 
            raise ValueError("You need to specify a stateId and entityId for this type.")

        if len(state_id) != len(entity_id):
            raise ValueError("\nYou need to make sure stateId and entityId are " + \
                             "of same length and correspond to each other by index.")
    
        all_queries = list(itertools.product(["https://www.huduser.gov/hudapi/public/chas?type="], [str(type)],
                                              ["&stateId="], state_id, ["&year="], year))
        
        urls = []
        for i in range(0, len(all_queries)):
            urls.append(
                all_queries[i][0] + 
                all_queries[i][1] +
                all_queries[i][2] +
                all_queries[i][3] +
                "&entityId=" +
                entity_id[i % len(entity_id)]+
                all_queries[i][4] +
                all_queries[i][5] 
            )


    return(hud_do_query_calls.chas_do_query_calls(urls, key = key))
