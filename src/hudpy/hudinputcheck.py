from enum import unique
from datetime import date
import hudpkgenv
from typing import Union
import hudinputcheck

def chas_input_check_cleansing(query: Union[int, str, list: int, list: str, tuple: Union[int, str]],
                               year: Union[int, str, list: int, list: str, tuple: Union[int, str]],
                               key: str) -> list:
    """
    #' @name chas_input_check_cleansing
    #' @title chas_input_check_cleansing
    #' @description Helper function used to clean user inputted variables for all
    #'    decomposed CHAS functions.
    #' @param query
    #'   The inputted GEOID.
    #' @param year The years to query for.
    #' @param key The key obtain from HUD USER website.
    #' @returns The cleansed input arguments.
    """
    
    if not isinstance(query, Union[int, str, list: int, list: str, tuple: Union[int, str]].__args__) :
        raise ValueError("\nQuery should be int, str, or list or tuple of ints and strings.")

    if not isinstance(year, Union[int, str, list: int, list: str, tuple: Union[int, str]].__args__) :
        raise ValueError("\nYear should be int, str, or list or tuple of ints and strings.")

    if type(key) != str:
        raise ValueError("\nKey should be a string")

    year = [year] if isinstance(year, str) or isinstance(year, int) else year
    query = [query] if isinstance(query, str) or isinstance(query, int) else query


    if(len(key) != 1):
        raise ValueError("\nThere seems to be multiple keys specified.")

    if(key == ""):
        raise ValueError("\nDid you forget to set the key. Please go to " + 
                         "Please go to https://www.huduser.gov/" +
                         "hudapi/public/register?comingfrom=1 to " +
                         "sign up and get a token. Save " +
                         "this to your environment using " +
                         "hud_set_key(your-key)")

    key = unique(map(str.strip(), key))
    year = unique(map(str.strip(), year))

    possible_years = list("2014-2018", "2013-2017",
                          "2012-2016", "2011-2015",
                          "2010-2014", "2009-2013",
                          "2008-2012", "2007-2011",
                          "2006-2010")

    for i in range(1, len(year)):
        if year[i] not in possible_years:
            raise ValueError("\nOne of the years does not fall into the values" +
                             "expected")
    if query is not None:
        if type(query) != list and type(query) != tuple:
            raise ValueError("")

        query = unique(map(str.strip(), query))
        return(list(query, year, key))    
    
    return(list(year, key))


def cw_input_check_cleansing(query: Union[int, str, list: int, list: str, tuple: Union[int, str]],
                             year: Union[int, str, list: int, list: str, tuple: Union[int, str]],
                             quarter: Union[int, str, list: int, list: str, tuple: Union[int, str]],
                             key: str) -> list:
    """
    #' @name cw_input_check_cleansing
    #' @title cw_input_check_cleansing
    #' @description Helper function used to clean user inputted variables for all
    #' Crosswalk functions.
    #' @param query
    #'   The inputted GEOID.
    #' @param year The years to query for.
    #' @param quarter The quarters to query for.
    #' @param key The key obtain from HUD USER website.
    #' @returns The cleansed input arguments.
    """
    
    if not isinstance(query, Union[int, str, list: int, list: str, tuple: Union[int, str]].__args__) :
        raise ValueError("\nQuery should be int, str, or list or tuple of ints and strings.")

    if not isinstance(year, Union[int, str, list: int, list: str, tuple: Union[int, str]].__args__) :
        raise ValueError("\nYear should be int, str, or list or tuple of ints and strings.")

    if not isinstance(quarter, Union[int, str, list: int, list: str, tuple: Union[int, str]].__args__) :
        raise ValueError("\nQuarter should be int, str, or list or tuple of ints and strings.")
    
    if type(key) != str:
        raise ValueError("\nKey should be a string")

    query = [query] if isinstance(query, str) or isinstance(query, int) else query
    year = [year] if isinstance(year, str) or isinstance(year, int) else year
    quarter =  [quarter] if isinstance(quarter, str) or isinstance(quarter, int) else quarter

    if(len(key) != 1):
        raise ValueError("\nThere seems to be multiple keys specified.")

    if(key == ""):
        raise ValueError("\nDid you forget to set the key. Please go to " + 
                         "Please go to https://www.huduser.gov/" +
                         "hudapi/public/register?comingfrom=1 to " +
                         "sign up and get a token. Save " +
                         "this to your environment using " +
                         "hud_set_key(your-key)")
    
    key = unique(map(str.strip(), key))
    year = unique(map(str.strip(), year))
    quarter = unique(map(str.strip(), quarter))
    query = unique(map(str.strip(), query))

    if False in map(str.isdecimal(), query):
        raise ValueError("\nGeoid query input must only be numbers")
    if False in map(str.isdecimal(), year):
        raise ValueError("\nYear input must only be numbers")
    if False in map(str.isdecimal(), quarter):
        raise ValueError("\nQuarter input must only be numbers")

    for i in range(1, len(quarter)):
        if int(quarter[i]) > 4 or int(quarter[i]) < 1:
            raise ValueError("\nQuarters must be from 1 to 4")

    for i in range(1, len(year)):
        if year[i] > date.year:
            raise ValueError("\nA year seems to be in the future?")

    return(list(query, year, quarter, key))



def fmr_il_input_check_cleansing(query: Union[int, str, list: int, list: str, tuple: Union[int, str]],
                                 year: Union[int, str, list: int, list: str, tuple: Union[int, str]],
                                 key: str) -> list:
    """
    #' @name fmr_il_input_check_cleansing
    #' @title fmr_il_input_check_cleansing
    #' @description Helper function used to clean user inputted variables for all
    #'   Fair markets rent and Income Limits datasets.
    #' @param query
    #'   The inputted GEOID.
    #' @param year The years to query for.
    #' @param key The key obtain from HUD USER website.
    #' @returns The cleansed input arguments.
    """
    if not isinstance(query, Union[int, str, list: int, list: str, tuple: Union[int, str]].__args__) :
        raise ValueError("\nQuery should be int, str, or list or tuple of ints and strings.")

    if not isinstance(year, Union[int, str, list: int, list: str, tuple: Union[int, str]].__args__) :
        raise ValueError("\nYear should be int, str, or list or tuple of ints and strings.")

    if type(key) != str:
        raise ValueError("\nKey should be a string")

    query = [query] if isinstance(query, str) or isinstance(query, int) else query
    year = [year] if isinstance(year, str) or isinstance(year, int) else year


    if not isinstance(query, Union[int, str, list: int, list: str, tuple: Union[int, str]].__args__) :
        raise ValueError("\nQuery should be int, str, or list or tuple of ints and strings.")

    if not isinstance(year, Union[int, str, list: int, list: str, tuple: Union[int, str]].__args__) :
        raise ValueError("\nYear should be int, str, or list or tuple of ints and strings.")

    if(len(key) != 1):
        raise ValueError("\nThere seems to be multiple keys specified.")

    if(key == ""):
        raise ValueError("\nDid you forget to set the key. Please go to " + 
                         "Please go to https://www.huduser.gov/" +
                         "hudapi/public/register?comingfrom=1 to " +
                         "sign up and get a token. Save " +
                         "this to your environment using " +
                         "hud_set_key(your-key)")
    
    key = unique(map(str.strip(), key))
    year = unique(map(str.strip(), year))
    query = unique(map(str.strip(), query))

    if False in map(str.isdecimal(), query):
        raise ValueError("\nGeoid query input must only be numbers")
    if False in map(str.isdecimal(), year):
        raise ValueError("\nYear input must only be numbers")

    for i in range(1, len(year)):
        if year[i] > date.year:
            raise ValueError("\nA year seems to be in the future?")

    if all(map(len() == 2, query)):
        query = map(str.upper(), query)
    elif all(map(len() > 2, query)):
        query = map(str.capitalize(), query)

    if hudpkgenv.pkg_env["states"] == None:
        hudpkgenv.pkg_env["states"] = hudinputcheck.hud_nation_states_territories(key = key)
    
    if len(set.intersection(query, hudpkgenv.pkg_env["states"]["state_name"])) != 0: 
        query = hudpkgenv.pkg_env["states"].loc(hudpkgenv.pkg_env["states"]["state_name"].isin(query))[2]
    if len(set.intersection(query, hudpkgenv.pkg_env["states"]["state_code"])) != 0:   
        query = hudpkgenv.pkg_env["states"].loc(hudpkgenv.pkg_env["states"]["state_code"].isin(query))[2]
    if len(set.intersection(query, hudpkgenv.pkg_env["states"]["state_num"])) != 0:  
        query = hudpkgenv.pkg_env["states"].loc(hudpkgenv.pkg_env["states"]["state_num"].isin(query))[2]

    if all(map(len() == 10, query)):
        querytype = "county"
    elif all(map(len() == 2, query)):
        querytype = "state"
    elif all(map(len() == 16), query):
        querytype = "cbsa"
    else:
        raise ValueError("\nThere is no matching fips code for one of the inputted states")

    return(list(query, year, key, [querytype]))



def crosswalk_a_dataset_input_check_cleansing(data,
                                              geoid: Union[int, str],
                                              geoid_col: Union[int, str],
                                              cw_geoid: str, 
                                              cw_geoid_col : Union[int, str], 
                                              method: str, 
                                              year: Union[int, str], 
                                              quarter: Union[int, str], 
                                              key: str) -> list:
    """
    #' @name crosswalk_a_dataset_input_check_cleansing
    #' @title crosswalk_a_dataset_input_check_cleansing
    #' @description Helper function used to clean inputs for the
    #'   crosswalk() function.
    #' @param data A dataset with rows describing measurements at a zip, county,
    #'   countysub, cd,
    #'   tract, cbsa, or cbsadiv geographic level.
    #' @param geoid The current geoid that the dataset is described in: must be zip,
    #'   county, countysub, cd,
    #'   tract, cbsa, or cbsadiv geographic level.
    #' @param geoid_col The column containing the geographic identifier;
    #'   must be zip, county, countysub, cd,
    #'   tract, cbsa, or cbsadiv geographic level.
    #'   Supply either the name of the column
    #'   or the index.
    #' @param cw_geoid The geoid to crosswalk the dataset to.
    #' @param method The allocation method to use: residential,
    #'   business, other, or total
    #' @param year The year measurement was taken.
    #' @param quarter The quarter of year measurement was taken.
    #' @param key The key obtain from HUD USER website.
    #' @returns The cleansed input arguments.
    """

    if len(geoid) > 1 or len(geoid_col) > 1 or \
       len(year) > 1 or len(quarter) > 1:
        raise ValueError("\nMake sure geoid, geoid_col, year, and quarter arguments are of length 1.")

    if type(key) != str:
        raise ValueError("\nKey should be a string")

    if(len(key) != 1):
        raise ValueError("\nThere seems to be multiple keys specified.")

    if(key == ""):
        raise ValueError("\nDid you forget to set the key. Please go to " + 
                         "Please go to https://www.huduser.gov/" +
                         "hudapi/public/register?comingfrom=1 to " +
                         "sign up and get a token. Save " +
                         "this to your environment using " +
                         "hud_set_key(your-key)")

    args = cw_input_check_cleansing(query = data[geoid_col],
                                    year = year,
                                    quarter = quarter,
                                    key = key
                                    )

    return(list(geoid, geoid_col, cw_geoid, cw_geoid_col, method, 
                args[2], args[3], args[4]))
    