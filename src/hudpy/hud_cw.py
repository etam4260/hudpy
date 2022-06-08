from __future__ import annotations
from typing import Union

from datetime import date, timedelta
import pandas as pd

import os
import itertools

from hudpy import hud_input_check
from hudpy import hud_internet_online
from hudpy import hud_do_query_calls

def hud_cw_zip_tract(zip: Union[int, str, list[int], list[str], tuple[int], tuple[str]],
                     year: Union[int, str, list[int], list[str], tuple[int], tuple[str]] = (date.today() - timedelta(days = 365)).strftime("%Y"),
                     quarter: Union[int, str, list[int], list[str], tuple[int], tuple[str]] = 1,
                     minimal: bool = False,
                     key: str = None) -> pd.DataFrame:
    """
    Function to query the Crosswalks API provided by US
    Department of Housing and Urban Development. This returns the crosswalk for
    zip to tract.

    Parameters
    ----------
    zip : 5 digit USPS ZIP code of the data to retrieve. E.g. 22031 for type
        functions 1 to 5 and 11 .

    year : Gets the year that this data was recorded. Can specify multiple
        years. Default is the previous year.
    
    quarter : Gets the quarter of the year that this data was recorded.
        Defaults to the first quarter of the year.

    minimal : Return just the crosswalked GEOIDs if true. Otherwise, return
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

    A dataframe mapping the zip code(s) to their corresponding crosswalked tract(s), including 
    data on their intersecting residential, business, other, and total address percentage.

    Examples
    --------

    >>> hud_cw_zip_tract(zip = "35213", year = "2010", quarter = "1")
    
    >>> hud_cw_zip_tract(zip = "35213", year = "2010", quarter = "1",
        minimal = True)

    """
    
    if(not hud_internet_online.internet_on()): raise ConnectionError("You currently do not have internet access.")
    
    if(key == None and os.getenv("HUD_KEY") != None):
        key = os.getenv("HUD_KEY")
        

    primary_geoid = "zip"
    secondary_geoid = "tract"

    args = hud_input_check.cw_input_check_cleansing(primary_geoid = primary_geoid,
                                                    secondary_geoid = secondary_geoid,
                                                    query = zip,
                                                    year = year,
                                                    quarter = quarter,
                                                    key = key)
    zip = args[0]
    year = args[1]
    quarter = args[2]
    key = args[3]

    if any(list(map(lambda x: len(x) != 5, zip))):
         raise ValueError("Zip inputs are not all of length 5")


    all_queries = list(itertools.product(zip, year, quarter))

    urls = []
    for i in range(len(all_queries)):
        urls.append(
            "https://www.huduser.gov/hudapi/public/usps?type=" +
            "1" +
            "&query=" +
            all_queries[i][0] +
            "&year=" +
            all_queries[i][1] +
            "&quarter=" +
            all_queries[i][2] 
        )
    

    if minimal == True:
        res = hud_do_query_calls.cw_do_query_calls(urls, [i[0] for i in all_queries],
                                [i[1] for i in all_queries], [i[2] for i in all_queries],
                                primary_geoid,
                                secondary_geoid,
                                key)
        if not res.empty:
            return(list(res.reset_index()["tract"]))
        else:
            return([])

    return(hud_do_query_calls.cw_do_query_calls(urls, [i[0] for i in all_queries],
                                [i[1] for i in all_queries], [i[2] for i in all_queries],
                                primary_geoid,
                                secondary_geoid,
                                key).reset_index())


def hud_cw_zip_county(zip: Union[int, str, list[int], list[str], tuple[int], tuple[str]],
                      year: Union[int, str, list[int], list[str], tuple[int], tuple[str]] = (date.today() - timedelta(days = 365)).strftime("%Y"),
                      quarter: Union[int, str, list[int], list[str], tuple[int], tuple[str]] = 1,
                      minimal: bool = False,
                      key: str = None) -> pd.DataFrame:
    """ 
    Function to query the Crosswalks API provided by US
    Department of Housing and Urban Development. This returns the crosswalk for
    zip to county.

    Parameters
    ----------
    zip : 5 digit USPS ZIP code of the data to retrieve. E.g. 22031 for type
        functions 1 to 5 and 11 .

    year : Gets the year that this data was recorded. Can specify multiple
        years. Default is the previous year.
    
    quarter : Gets the quarter of the year that this data was recorded.
        Defaults to the first quarter of the year.

    minimal : Return just the crosswalked GEOIDs if true. Otherwise, return
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

    A dataframe mapping the zip code(s) to their corresponding crosswalked county(s), including 
    data on their intersecting residential, business, other, and total address percentage.

    Examples
    --------

    >>> hud_cw_zip_county(zip = "35213", year = "2010", quarter = "1")
    
    >>> hud_cw_zip_county(zip = "35213", year = "2010", quarter = "1"),
        minimal = True)

    """

    if(not hud_internet_online.internet_on()): raise ConnectionError("You currently do not have internet access.")
    
    if(key == None and os.getenv("HUD_KEY") != None):
        key = os.getenv("HUD_KEY")
        
    primary_geoid = "zip"
    secondary_geoid = "county"

    
    args = hud_input_check.cw_input_check_cleansing(primary_geoid = primary_geoid,
                                                    secondary_geoid = secondary_geoid,
                                                    query = zip,
                                                    year = year,
                                                    quarter = quarter,
                                                    key = key)
    zip = args[0]
    year = args[1]
    quarter = args[2]
    key = args[3]


    if any(list(map(lambda x: len(x) != 5, zip))):
         raise ValueError("Zip inputs are not all of length 5")


    all_queries = list(itertools.product(zip, year, quarter))

    urls = []
    for i in range(len(all_queries)):
        urls.append(
            "https://www.huduser.gov/hudapi/public/usps?type=" +
            "2" +
            "&query=" +
            all_queries[i][0] +
            "&year=" +
            all_queries[i][1] +
            "&quarter=" +
            all_queries[i][2] 
        )


    if minimal == True:
        res = hud_do_query_calls.cw_do_query_calls(urls, [i[0] for i in all_queries],
                                [i[1] for i in all_queries], [i[2] for i in all_queries],
                                primary_geoid,
                                secondary_geoid,
                                key)
        if not res.empty:
            return(list(res.reset_index()["county"]))
        else:
            return([])

    return(hud_do_query_calls.cw_do_query_calls(urls, [i[0] for i in all_queries],
                                [i[1] for i in all_queries], [i[2] for i in all_queries],
                                primary_geoid,
                                secondary_geoid,
                                key).reset_index())

def hud_cw_zip_cbsa(zip: Union[int, str, list[int], list[str], tuple[int], tuple[str]],
                    year: Union[int, str, list[int], list[str], tuple[int], tuple[str]] = (date.today() - timedelta(days = 365)).strftime("%Y"),
                    quarter: Union[int, str, list[int], list[str], tuple[int], tuple[str]] = 1,
                    minimal: bool = False,
                    key: str = None) -> pd.DataFrame:
    """
    Function to query the Crosswalks API provided by US
    Department of Housing and Urban Development. This returns the crosswalk for
    zip to cbsa.

    Parameters
    ----------
    zip : 5 digit USPS ZIP code of the data to retrieve. E.g. 22031 for type
        functions 1 to 5 and 11 .

    year : Gets the year that this data was recorded. Can specify multiple
        years. Default is the previous year.
    
    quarter : Gets the quarter of the year that this data was recorded.
        Defaults to the first quarter of the year.

    minimal : Return just the crosswalked GEOIDs if true. Otherwise, return
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

    A dataframe mapping the zip code(s) to their corresponding crosswalked cbsa(s), including 
    data on their intersecting residential, business, other, and total address percentage.

    Examples
    --------

    >>> hud_cw_zip_cbsa(zip = "35213", year = "2018", quarter = "1")
    
    >>> hud_cw_zip_cbsa(zip = '35213', year = "2018", quarter = "1",
        minimal = True)
    """
    
    if(not hud_internet_online.internet_on()): raise ConnectionError("You currently do not have internet access.")
    
    if(key == None and os.getenv("HUD_KEY") != None):
        key = os.getenv("HUD_KEY")
        
    primary_geoid = "zip"
    secondary_geoid = "cbsa"

 
    args = hud_input_check.cw_input_check_cleansing(primary_geoid = primary_geoid,
                                                    secondary_geoid = secondary_geoid,
                                                    query = zip,
                                                    year = year,
                                                    quarter = quarter,
                                                    key = key)
    zip = args[0]
    year = args[1]
    quarter = args[2]
    key = args[3]


    if any(list(map(lambda x: len(x) != 5, zip))):
         raise ValueError("Zip inputs are not all of length 5")



    all_queries = list(itertools.product(zip, year, quarter))


    urls = []
    for i in range(len(all_queries)):
        urls.append(
            "https://www.huduser.gov/hudapi/public/usps?type=" +
            "3" +
            "&query=" +
            all_queries[i][0] +
            "&year=" +
            all_queries[i][1] +
            "&quarter=" +
            all_queries[i][2] 
        )


    if minimal == True:
        res = hud_do_query_calls.cw_do_query_calls(urls, [i[0] for i in all_queries],
                                [i[1] for i in all_queries], [i[2] for i in all_queries],
                                primary_geoid,
                                secondary_geoid,
                                key)
        if not res.empty:
            return(list(res.reset_index()["cbsa"]))
        else:
            return([])

    return(hud_do_query_calls.cw_do_query_calls(urls, [i[0] for i in all_queries],
                                [i[1] for i in all_queries], [i[2] for i in all_queries],
                                primary_geoid,
                                secondary_geoid,
                                key).reset_index())

def hud_cw_zip_cbsadiv(zip: Union[int, str, list[int], list[str], tuple[int], tuple[str]],
                       year: Union[int, str, list[int], list[str], tuple[int], tuple[str]] = (date.today() - timedelta(days = 365)).strftime("%Y"),
                       quarter: Union[int, str, list[int], list[str], tuple[int], tuple[str]] = 1,
                       minimal: bool = False,
                       key: str = None) -> pd.DataFrame:
    """
    Function to query the Crosswalks API provided by US
    Department of Housing and Urban Development. This returns the crosswalk for
    zip to cbsadiv. (Available 4th Quarter 2017 onwards)

    Parameters
    ----------
    zip : 5 digit USPS ZIP code of the data to retrieve. E.g. 22031 for type
        functions 1 to 5 and 11 .

    year : Gets the year that this data was recorded. Can specify multiple
        years. Default is the previous year.
    
    quarter : Gets the quarter of the year that this data was recorded.
        Defaults to the first quarter of the year.

    minimal : Return just the crosswalked GEOIDs if true. Otherwise, return
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

    A dataframe mapping the zip code(s) to their corresponding crosswalked cbsadiv(s), including 
    data on their intersecting residential, business, other, and total address percentage.

    Examples
    --------

    >>> hud_cw_zip_cbsadiv(zip = "35213", year = "2018", quarter = "1")
    
    >>> hud_cw_zip_cbsadiv(zip = "35213", year = "2018", quarter = "1",
        minimal = True)
    """

    if(not hud_internet_online.internet_on()): raise ConnectionError("You currently do not have internet access.")
    
    if(key == None and os.getenv("HUD_KEY") != None):
        key = os.getenv("HUD_KEY")
        
    primary_geoid = "zip"
    secondary_geoid = "cbsadiv"

    args = hud_input_check.cw_input_check_cleansing(primary_geoid = primary_geoid,
                                                    secondary_geoid = secondary_geoid,
                                                    query = zip,
                                                    year = year,
                                                    quarter = quarter,
                                                    key = key)
    zip = args[0]
    year = args[1]
    quarter = args[2]
    key = args[3]


    if any(list(map(lambda x: len(x) != 5, zip))):
         raise ValueError("Zip inputs are not all of length 5")



    all_queries = list(itertools.product(zip, year, quarter))


    urls = []
    for i in range(len(all_queries)):
        urls.append(
            "https://www.huduser.gov/hudapi/public/usps?type=" +
            "4" +
            "&query=" +
            all_queries[i][0] +
            "&year=" +
            all_queries[i][1] +
            "&quarter=" +
            all_queries[i][2] 
        )


    if minimal == True:
        res = hud_do_query_calls.cw_do_query_calls(urls, [i[0] for i in all_queries],
                                [i[1] for i in all_queries], [i[2] for i in all_queries],
                                primary_geoid,
                                secondary_geoid,
                                key)
        if not res.empty:
            return(list(res.reset_index()["cbsadiv"]))
        else:
            return([])

    return(hud_do_query_calls.cw_do_query_calls(urls, [i[0] for i in all_queries],
                                [i[1] for i in all_queries], [i[2] for i in all_queries],
                                primary_geoid,
                                secondary_geoid,
                                key))


def hud_cw_zip_cd(zip: Union[int, str, list[int], list[str], tuple[int], tuple[str]],
                  year: Union[int, str, list[int], list[str], tuple[int], tuple[str]] = (date.today() - timedelta(days = 365)).strftime("%Y"),
                  quarter: Union[int, str, list[int], list[str], tuple[int], tuple[str]] = 1,
                  minimal: bool = False,
                  key: str = None) -> pd.DataFrame:
    """
    Function to query the Crosswalks API provided by US
    Department of Housing and Urban Development. This returns the crosswalk for
    zip to cd. 

    Parameters
    ----------
    zip : 5 digit USPS ZIP code of the data to retrieve. E.g. 22031 for type
        functions 1 to 5 and 11 .

    year : Gets the year that this data was recorded. Can specify multiple
        years. Default is the previous year.
    
    quarter : Gets the quarter of the year that this data was recorded.
        Defaults to the first quarter of the year.

    minimal : Return just the crosswalked GEOIDs if true. Otherwise, return
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

    A dataframe mapping the zip code(s) to their corresponding crosswalked cd(s), including 
    data on their intersecting residential, business, other, and total address percentage.

    Examples
    --------

    >>> hud_cw_zip_cd(zip = "35213", year = "2018", quarter = "1")
    
    >>> hud_cw_zip_cd(zip = "35213", year = "2018", quarter = "1",
        minimal = True)
    """

    if(not hud_internet_online.internet_on()): raise ConnectionError("You currently do not have internet access.")
    
    if(key == None and os.getenv("HUD_KEY") != None):
        key = os.getenv("HUD_KEY")
        
    primary_geoid = "zip"
    secondary_geoid = "cd"

    args = hud_input_check.cw_input_check_cleansing(primary_geoid = primary_geoid,
                                                    secondary_geoid = secondary_geoid,
                                                    query = zip,
                                                    year = year,
                                                    quarter = quarter,
                                                    key = key)
    zip = args[0]
    year = args[1]
    quarter = args[2]
    key = args[3]


    if any(list(map(lambda x: len(x) != 5, zip))):
         raise ValueError("Zip inputs are not all of length 5")


    all_queries = list(itertools.product(zip, year, quarter))


    urls = []
    for i in range(len(all_queries)):
        urls.append(
            "https://www.huduser.gov/hudapi/public/usps?type=" +
            "5" +
            "&query=" +
            all_queries[i][0] +
            "&year=" +
            all_queries[i][1] +
            "&quarter=" +
            all_queries[i][2] 
        )


    if minimal == True:
        res = hud_do_query_calls.cw_do_query_calls(urls, [i[0] for i in all_queries],
                                [i[1] for i in all_queries], [i[2] for i in all_queries],
                                primary_geoid,
                                secondary_geoid,
                                key)
        if not res.empty:
            return(list(res.reset_index()["cd"]))
        else:
            return([])

    return(hud_do_query_calls.cw_do_query_calls(urls, [i[0] for i in all_queries],
                                [i[1] for i in all_queries], [i[2] for i in all_queries],
                                primary_geoid,
                                secondary_geoid,
                                key).reset_index())

def hud_cw_zip_countysub(zip: Union[int, str, list[int], list[str], tuple[int], tuple[str]],
                         year: Union[int, str, list[int], list[str], tuple[int], tuple[str]] = (date.today() - timedelta(days = 365)).strftime("%Y"),
                         quarter: Union[int, str, list[int], list[str], tuple[int], tuple[str]] = 1,
                         minimal: bool = False,
                         key: str = None) -> pd.DataFrame:
    """
    Function to query the Crosswalks API provided by US
    Department of Housing and Urban Development. This returns the crosswalk for
    zip to cd. 

    Parameters
    ----------
    zip : 5 digit USPS ZIP code of the data to retrieve. E.g. 22031 for type
        functions 1 to 5 and 11 .

    year : Gets the year that this data was recorded. Can specify multiple
        years. Default is the previous year.
    
    quarter : Gets the quarter of the year that this data was recorded.
        Defaults to the first quarter of the year.

    minimal : Return just the crosswalked GEOIDs if true. Otherwise, return
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

    A dataframe mapping the zip code(s) to their corresponding crosswalked cd(s), including 
    data on their intersecting residential, business, other, and total address percentage.

    Examples
    --------

    >>> hud_cw_zip_cd(zip = "35213", year = "2018", quarter = "1")
    
    >>> hud_cw_zip_cd(zip = "35213", year = "2018", quarter = "1",
        minimal = True)
    """

    if(not hud_internet_online.internet_on()): raise ConnectionError("You currently do not have internet access.")
    
    if(key == None and os.getenv("HUD_KEY") != None):
        key = os.getenv("HUD_KEY")
        
    primary_geoid = "zip"
    secondary_geoid = "countysub"

    args = hud_input_check.cw_input_check_cleansing(primary_geoid = primary_geoid,
                                                    secondary_geoid = secondary_geoid,
                                                    query = zip,
                                                    year = year,
                                                    quarter = quarter,
                                                    key = key)
    zip = args[0]
    year = args[1]
    quarter = args[2]
    key = args[3]


    if any(list(map(lambda x: len(x) != 5, zip))):
         raise ValueError("Zip inputs are not all of length 5")


    all_queries = list(itertools.product(zip, year, quarter))


    urls = []
    for i in range(len(all_queries)):
        urls.append(
            "https://www.huduser.gov/hudapi/public/usps?type=" +
            "11" +
            "&query=" +
            all_queries[i][0] +
            "&year=" +
            all_queries[i][1] +
            "&quarter=" +
            all_queries[i][2] 
        )


    if minimal == True:
        res = hud_do_query_calls.cw_do_query_calls(urls, [i[0] for i in all_queries],
                                [i[1] for i in all_queries], [i[2] for i in all_queries],
                                primary_geoid,
                                secondary_geoid,
                                key)
        if not res.empty:
            return(list(res.reset_index()["countysub"]))
        else:
            return([])

    return(hud_do_query_calls.cw_do_query_calls(urls, [i[0] for i in all_queries],
                                [i[1] for i in all_queries], [i[2] for i in all_queries],
                                primary_geoid,
                                secondary_geoid,
                                key).reset_index())

def hud_cw_tract_zip(tract: Union[int, str, list[int], list[str], tuple[int], tuple[str]],
                     year: Union[int, str, list[int], list[str], tuple[int], tuple[str]] = (date.today() - timedelta(days = 365)).strftime("%Y"),
                     quarter: Union[int, str, list[int], list[str], tuple[int], tuple[str]] = 1,
                     minimal: bool = False,
                     key: str = None) -> pd.DataFrame:
    """
    Function to query the Crosswalks API provided by US
    Department of Housing and Urban Development. This returns the crosswalk for
    tract to zip. 

    Parameters
    ----------
    tract : 11 digit unique 2000 or 2010 Census tract GEOID consisting of
         state FIPS + county FIPS + tract code. Eg: 51059461700  for type 6

    year : Gets the year that this data was recorded. Can specify multiple
        years. Default is the previous year.
    
    quarter : Gets the quarter of the year that this data was recorded.
        Defaults to the first quarter of the year.

    minimal : Return just the crosswalked GEOIDs if true. Otherwise, return
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

    A dataframe mapping the tract(s) to their corresponding crosswalked zip(s), including 
    data on their intersecting residential, business, other, and total address percentage.

    Examples
    --------

    >>> hud_cw_tract_zip(zip = "35213", year = "2018", quarter = "1")
    
    >>> hud_cw_tract_zip(zip = "35213", year = "2018", quarter = "1",
        minimal = True)
    """

    if(not hud_internet_online.internet_on()): raise ConnectionError("You currently do not have internet access.")

    if(key == None and os.getenv("HUD_KEY") != None):
        key = os.getenv("HUD_KEY")
        
    
    primary_geoid = "tract"
    secondary_geoid = "zip"

    args = hud_input_check.cw_input_check_cleansing(primary_geoid = primary_geoid,
                                                    secondary_geoid = secondary_geoid,
                                                    query = tract,
                                                    year = year,
                                                    quarter = quarter,
                                                    key = key)
    tract = args[0]
    year = args[1]
    quarter = args[2]
    key = args[3]


    if any(list(map(lambda x: len(x) != 11, tract))):
         raise ValueError("Tract inputs are not all of length 11")


    all_queries = list(itertools.product(tract, year, quarter))


    urls = []
    for i in range(len(all_queries)):
        urls.append(
            "https://www.huduser.gov/hudapi/public/usps?type=" +
            "6" +
            "&query=" +
            all_queries[i][0] +
            "&year=" +
            all_queries[i][1] +
            "&quarter=" +
            all_queries[i][2] 
        )


    if minimal == True:
        res = hud_do_query_calls.cw_do_query_calls(urls, [i[0] for i in all_queries],
                                [i[1] for i in all_queries], [i[2] for i in all_queries],
                                primary_geoid,
                                secondary_geoid,
                                key)
        if not res.empty:
            return(list(res.reset_index()["zip"]))
        else:
            return([])

    return(hud_do_query_calls.cw_do_query_calls(urls, [i[0] for i in all_queries],
                                [i[1] for i in all_queries], [i[2] for i in all_queries],
                                primary_geoid,
                                secondary_geoid,
                                key).reset_index())
  

def hud_cw_county_zip(county: Union[int, str, list[int], list[str], tuple[int], tuple[str]],
                      year: Union[int, str, list[int], list[str], tuple[int], tuple[str]] = (date.today() - timedelta(days = 365)).strftime("%Y"),
                      quarter: Union[int, str, list[int], list[str], tuple[int], tuple[str]] = 1,
                      minimal: bool = False,
                      key: str = None) -> pd.DataFrame:
    """
    Function to query the Crosswalks API provided by US
    Department of Housing and Urban Development. This returns the crosswalk for
    county to zip. 

    Parameters
    ----------
    county : 5 digit unique 2000 or 2010 Census county GEOID consisting of
          state FIPS + county FIPS. Eg: 51600 for type 7
    
    year : Gets the year that this data was recorded. Can specify multiple
        years. Default is the previous year.
    
    quarter : Gets the quarter of the year that this data was recorded.
        Defaults to the first quarter of the year.

    minimal : Return just the crosswalked GEOIDs if true. Otherwise, return
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

    A dataframe mapping the county(s) to their corresponding crosswalked zip(s), including 
    data on their intersecting residential, business, other, and total address percentage.

    Examples
    --------

    >>> hud_cw_county_zip(zip = "35213", year = "2018", quarter = "1")
    
    >>> hud_cw_county_zip(zip = "35213", year = "2018", quarter = "1",
        minimal = True)
    """

    if(not hud_internet_online.internet_on()): raise ConnectionError("You currently do not have internet access.")

    if(key == None and os.getenv("HUD_KEY") != None):
        key = os.getenv("HUD_KEY")
        
    primary_geoid = "county"
    secondary_geoid = "zip"

    args = hud_input_check.cw_input_check_cleansing(primary_geoid = primary_geoid,
                                                    secondary_geoid = secondary_geoid,
                                                    query = county,
                                                    year = year,
                                                    quarter = quarter,
                                                    key = key)
    county = args[0]
    year = args[1]
    quarter = args[2]
    key = args[3]


    if any(list(map(lambda x: len(x) != 5, county))):
         raise ValueError("County inputs are not all of length 5")


    all_queries = list(itertools.product(county, year, quarter))


    urls = []
    for i in range(len(all_queries)):
        urls.append(
            "https://www.huduser.gov/hudapi/public/usps?type=" +
            "7" +
            "&query=" +
            all_queries[i][0] +
            "&year=" +
            all_queries[i][1] +
            "&quarter=" +
            all_queries[i][2] 
        )


    if minimal == True:
        res = hud_do_query_calls.cw_do_query_calls(urls, [i[0] for i in all_queries],
                                [i[1] for i in all_queries], [i[2] for i in all_queries],
                                primary_geoid,
                                secondary_geoid,
                                key)
        if not res.empty:
            return(list(res.reset_index()["zip"]))
        else:
            return([])

    return(hud_do_query_calls.cw_do_query_calls(urls, [i[0] for i in all_queries],
                                [i[1] for i in all_queries], [i[2] for i in all_queries],
                                primary_geoid,
                                secondary_geoid,
                                key).reset_index())

def hud_cw_cbsa_zip(cbsa: Union[int, str, list[int], list[str], tuple[int], tuple[str]],
                    year: Union[int, str, list[int], list[str], tuple[int], tuple[str]] = (date.today() - timedelta(days = 365)).strftime("%Y"),
                    quarter: Union[int, str, list[int], list[str], tuple[int], tuple[str]] = 1,
                    minimal: bool = False,
                    key: str = None) -> pd.DataFrame:
    """
    Function to query the Crosswalks API provided by US
    Department of Housing and Urban Development. This returns the crosswalk for
    cbsa to zip. 

    Parameters
    ----------
    cbsa : 5 digit CBSA code for Micropolitan and Metropolitan Areas Eg: 
        10380 for type 8
    
    year : Gets the year that this data was recorded. Can specify multiple
        years. Default is the previous year.
    
    quarter : Gets the quarter of the year that this data was recorded.
        Defaults to the first quarter of the year.

    minimal : Return just the crosswalked GEOIDs if true. Otherwise, return
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

    A dataframe mapping the cbsa(s) to their corresponding crosswalked zip(s), including 
    data on their intersecting residential, business, other, and total address percentage.

    Examples
    --------

    >>> hud_cw_cbsa_zip(zip = "35213", year = "2018", quarter = "1")
    
    >>> hud_cw_cbsa_zip(zip = "35213", year = "2018", quarter = "1",
        minimal = True)
    """

    if(not hud_internet_online.internet_on()): raise ConnectionError("You currently do not have internet access.")
    
    if(key == None and os.getenv("HUD_KEY") != None):
        key = os.getenv("HUD_KEY")
    
    primary_geoid = "cbsa"
    secondary_geoid = "zip"

    args = hud_input_check.cw_input_check_cleansing(primary_geoid = primary_geoid,
                                                    secondary_geoid = secondary_geoid,
                                                    query = cbsa,
                                                    year = year,
                                                    quarter = quarter,
                                                    key = key)
    cbsa = args[0]
    year = args[1]
    quarter = args[2]
    key = args[3]


    if any(list(map(lambda x: len(x) != 5, cbsa))):
         raise ValueError("Cbsa inputs are not all of length 5")


    all_queries = list(itertools.product(cbsa, year, quarter))


    urls = []
    for i in range(len(all_queries)):
        urls.append(
            "https://www.huduser.gov/hudapi/public/usps?type=" +
            "8" +
            "&query=" +
            all_queries[i][0] +
            "&year=" +
            all_queries[i][1] +
            "&quarter=" +
            all_queries[i][2] 
        )


    if minimal == True:
        res = hud_do_query_calls.cw_do_query_calls(urls, [i[0] for i in all_queries],
                                [i[1] for i in all_queries], [i[2] for i in all_queries],
                                primary_geoid,
                                secondary_geoid,
                                key)
        if not res.empty:
            return(list(res.reset_index()["zip"]))
        else:
            return([])

    return(hud_do_query_calls.cw_do_query_calls(urls, [i[0] for i in all_queries],
                                [i[1] for i in all_queries], [i[2] for i in all_queries],
                                primary_geoid,
                                secondary_geoid,
                                key).reset_index())


def hud_cw_cbsadiv_zip(cbsadiv: Union[int, str, list[int], list[str], tuple[int], tuple[str]],
                       year: Union[int, str, list[int], list[str], tuple[int], tuple[str]] = (date.today() - timedelta(days = 365)).strftime("%Y"),
                       quarter: Union[int, str, list[int], list[str], tuple[int], tuple[str]] = 1,
                       minimal: bool = False,
                       key: str = None) -> pd.DataFrame:
    """
    Function to query the Crosswalks API provided by US
    Department of Housing and Urban Development. This returns the crosswalk for
    cbsadiv to zip. 

    Parameters
    ----------
    cbsadiv : 5-digit CBSA Division code which only applies to Metropolitan Areas.
    (Available 4th Quarter 2017 onwards)
    
    year : Gets the year that this data was recorded. Can specify multiple
        years. Default is the previous year.
    
    quarter : Gets the quarter of the year that this data was recorded.
        Defaults to the first quarter of the year.

    minimal : Return just the crosswalked GEOIDs if true. Otherwise, return
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

    A dataframe mapping the cbsadiv(s) to their corresponding crosswalked zip(s), including 
    data on their intersecting residential, business, other, and total address percentage.

    Examples
    --------

    >>> hud_cw_cbsadiv_zip(zip = "35213", year = "2018", quarter = "1")
    
    >>> hud_cw_cbsadiv_zip(zip = "35213", year = "2018", quarter = "1",
        minimal = True)
    """

    if(not hud_internet_online.internet_on()): raise ConnectionError("You currently do not have internet access.")

    if(key == None and os.getenv("HUD_KEY") != None):
        key = os.getenv("HUD_KEY")
        
    primary_geoid = "cbsadiv"
    secondary_geoid = "zip"

    args = hud_input_check.cw_input_check_cleansing(primary_geoid = primary_geoid,
                                                    secondary_geoid = secondary_geoid,
                                                    query = cbsadiv,
                                                    year = year,
                                                    quarter = quarter,
                                                    key = key)
    cbsadiv = args[0]
    year = args[1]
    quarter = args[2]
    key = args[3]


    if any(list(map(lambda x: len(x) != 5, cbsadiv))):
         raise ValueError("Cbsadiv inputs are not all of length 5")


    all_queries = list(itertools.product(cbsadiv, year, quarter))


    urls = []
    for i in range(len(all_queries)):
        urls.append(
            "https://www.huduser.gov/hudapi/public/usps?type=" +
            "9" +
            "&query=" +
            all_queries[i][0] +
            "&year=" +
            all_queries[i][1] +
            "&quarter=" +
            all_queries[i][2] 
        )


    if minimal == True:
        res = hud_do_query_calls.cw_do_query_calls(urls, [i[0] for i in all_queries],
                                [i[1] for i in all_queries], [i[2] for i in all_queries],
                                primary_geoid,
                                secondary_geoid,
                                key)
        if not res.empty:
            return(list(res.reset_index()["zip"]))
        else:
            return([])

    return(hud_do_query_calls.cw_do_query_calls(urls, [i[0] for i in all_queries],
                                [i[1] for i in all_queries], [i[2] for i in all_queries],
                                primary_geoid,
                                secondary_geoid,
                                key))


def hud_cw_cd_zip(cd: Union[int, str, list[int], list[str], tuple[int], tuple[str]],
                  year: Union[int, str, list[int], list[str], tuple[int], tuple[str]] = (date.today() - timedelta(days = 365)).strftime("%Y"),
                  quarter: Union[int, str, list[int], list[str], tuple[int], tuple[str]] = 1,
                  minimal: bool = False,
                  key: str = None) -> pd.DataFrame:
    """
    Function to query the Crosswalks API provided by US
    Department of Housing and Urban Development. This returns the crosswalk for
    cd to zip. 

    Parameters
    ----------
    cd :  4-digit GEOID for the Congressional District which consists of
        state FIPS + Congressional District code. Eg: 7200 for type 10
        
    year : Gets the year that this data was recorded. Can specify multiple
        years. Default is the previous year.
    
    quarter : Gets the quarter of the year that this data was recorded.
        Defaults to the first quarter of the year.

    minimal : Return just the crosswalked GEOIDs if true. Otherwise, return
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

    A dataframe mapping the cd(s) to their corresponding crosswalked zip(s), including 
    data on their intersecting residential, business, other, and total address percentage.

    Examples
    --------

    >>> hud_cw_cd_zip(zip = "35213", year = "2018", quarter = "1")
    
    >>> hud_cw_cd_zip(zip = "35213", year = "2018", quarter = "1",
        minimal = True)
    """
    
    if(not hud_internet_online.internet_on()): raise ConnectionError("You currently do not have internet access.")
    
    if(key == None and os.getenv("HUD_KEY") != None):
        key = os.getenv("HUD_KEY")
        
    primary_geoid = "cd"
    secondary_geoid = "zip"

    args = hud_input_check.cw_input_check_cleansing(primary_geoid = primary_geoid,
                                                    secondary_geoid = secondary_geoid,
                                                    query = cd,
                                                    year = year,
                                                    quarter = quarter,
                                                    key = key)
    cd = args[0]
    year = args[1]
    quarter = args[2]
    key = args[3]


    if any(list(map(lambda x: len(x) != 4, cd))):
         raise ValueError("Cd input are not all of length 4")


    all_queries = list(itertools.product(cd, year, quarter))


    urls = []
    for i in range(len(all_queries)):
        urls.append(
            "https://www.huduser.gov/hudapi/public/usps?type=" +
            "10" +
            "&query=" +
            all_queries[i][0] +
            "&year=" +
            all_queries[i][1] +
            "&quarter=" +
            all_queries[i][2] 
        )


    if minimal == True:
        res = hud_do_query_calls.cw_do_query_calls(urls, [i[0] for i in all_queries],
                                [i[1] for i in all_queries], [i[2] for i in all_queries],
                                primary_geoid,
                                secondary_geoid,
                                key)
        if not res.empty:
            return(list(res.reset_index()["zip"]))
        else:
            return([])

    return(hud_do_query_calls.cw_do_query_calls(urls, [i[0] for i in all_queries],
                                [i[1] for i in all_queries], [i[2] for i in all_queries],
                                primary_geoid,
                                secondary_geoid,
                                key).reset_index())


def hud_cw_countysub_zip(countysub: Union[int, str, list[int], list[str], tuple[int], tuple[str]],
                         year: Union[int, str, list[int], list[str], tuple[int], tuple[str]] = (date.today() - timedelta(days = 365)).strftime("%Y"),
                         quarter: Union[int, str, list[int], list[str], tuple[int], tuple[str]] = 1,
                         minimal: bool = False,
                         key: str = None) -> pd.DataFrame:
    """
    Function to query the Crosswalks API provided by US
    Department of Housing and Urban Development. This returns the crosswalk for
    countysub to zip. 

    Parameters
    ----------
    countysub :  4-digit GEOID for the Congressional District which consists of
        state FIPS + Congressional District code. Eg: 7200 for type 10
        (Available 2nd Quarter 2018 onwards)

    year : Gets the year that this data was recorded. Can specify multiple
        years. Default is the previous year.
    
    quarter : Gets the quarter of the year that this data was recorded.
        Defaults to the first quarter of the year.

    minimal : Return just the crosswalked GEOIDs if true. Otherwise, return
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

    A dataframe mapping the countysub(s) to their corresponding crosswalked zip(s), including 
    data on their intersecting residential, business, other, and total address percentage.

    Examples
    --------

    >>> hud_cw_countysub_zip(zip = "35213", year = "2018", quarter = "1")
    
    >>> hud_cw_countysub_zip(zip = "35213", year = "2018", quarter = "1",
        minimal = True)
    """

    if(not hud_internet_online.internet_on()): raise ConnectionError("You currently do not have internet access.")
    
    if(key == None and os.getenv("HUD_KEY") != None):
        key = os.getenv("HUD_KEY")
        
    primary_geoid = "countysub"
    secondary_geoid = "zip"

    args = hud_input_check.cw_input_check_cleansing(primary_geoid = primary_geoid,
                                                    secondary_geoid = secondary_geoid,
                                                    query = countysub,
                                                    year = year,
                                                    quarter = quarter,
                                                    key = key)
    countysub = args[0]
    year = args[1]
    quarter = args[2]
    key = args[3]


    if any(list(map(lambda x: len(x) != 10, countysub))):
         raise ValueError("Countysub inputs are not all of length 10")


    all_queries = list(itertools.product(countysub, year, quarter))


    urls = []
    for i in range(len(all_queries)):
        urls.append(
            "https://www.huduser.gov/hudapi/public/usps?type=" +
            "12" +
            "&query=" +
            all_queries[i][0] +
            "&year=" +
            all_queries[i][1] +
            "&quarter=" +
            all_queries[i][2] 
        )


    if minimal == True:
        res = hud_do_query_calls.cw_do_query_calls(urls, [i[0] for i in all_queries],
                                [i[1] for i in all_queries], [i[2] for i in all_queries],
                                primary_geoid,
                                secondary_geoid,
                                key)
        if not res.empty:
            return(list(res.reset_index()["zip"]))
        else:
            return([])
            
    return(hud_do_query_calls.cw_do_query_calls(urls, [i[0] for i in all_queries],
                                [i[1] for i in all_queries], [i[2] for i in all_queries],
                                primary_geoid,
                                secondary_geoid,
                                key).reset_index())