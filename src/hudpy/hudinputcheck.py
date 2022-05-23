from __future__ import annotations

from datetime import date
from typing import Union

from hudpy import hudpkgenv
from hudpy import hudinputcheck

def chas_input_check_cleansing(query: Union[int, str, list[int], list[str], tuple[int], tuple[str]],
                               year: Union[int, str, list[int], list[str], tuple[int], tuple[str]],
                               key: str) -> list[list]:
    """
    Helper function to clean user inputted variables for all
    CHAS (Comprehensive Housing and Affordability)[hud_chas] function calls.

    Parameters
    ----------

    query : The inputted geoid. This is likely state, county, or place, or mcd geoids.

    year : The year(s) input to query for.

    key : The API key for this user. 

    Returns
    -------

    This returns a list of the cleaned user inputs.

    """
    
    if not isinstance(query, (int, str, list)) :
        raise ValueError("\nQuery should be int, str, or list or tuple of ints and strings.")

    if not isinstance(year, (int, str, list)) :
        raise ValueError("\nYear should be int, str, or list or tuple of ints and strings.")
    
    if key == None:
        raise ValueError("\nIt looks like the HUD_KEY was not set: use hud_set_key().")
        
    if type(key) != str:
        raise ValueError("\nKey should be a string")

    year = [str(year)] if isinstance(year, str) or isinstance(year, int) else list(map(lambda x: str(x), year))
    query = [str(query)] if isinstance(query, str) or isinstance(query, int) else list(map(lambda x: str(x), query))

    if(key == ""):
        raise ValueError("\nDid you forget to set the key. Please go to " + 
                         "Please go to https://www.huduser.gov/" +
                         "hudapi/public/register?comingfrom=1 to " +
                         "sign up and get a token. Save " +
                         "this to your environment using " +
                         "hud_set_key(your-key)")

    year = list(set(map(lambda x: str.strip(x), year)))

    possible_years = list("2014-2018", "2013-2017",
                          "2012-2016", "2011-2015",
                          "2010-2014", "2009-2013",
                          "2008-2012", "2007-2011",
                          "2006-2010")

    for i in range(0, len(year)):
        if int(year[i]) not in possible_years:
            raise ValueError("\nOne of the years does not fall into the values" +
                             "expected")
    if query is not None:
        if type(query) != list and type(query) != tuple:
            raise ValueError("")

        query = map(lambda x: str.strip(x), query)
        return(list(query, year, key))    
    
    return([year, key])


def cw_input_check_cleansing(query: Union[int, str, list[int], list[str], tuple[int], tuple[str]],
                             year: Union[int, str, list[int], list[str], tuple[int], tuple[str]],
                             quarter: Union[int, str, list[int], list[str], tuple[int], tuple[str]],
                             key: str) -> list[list]:
    """
    Helper function to clean user inputted variables for all
    crosswalk[hud_cw] function calls.

    Parameters
    ----------

    query : The inputted geoid(s). This includes:
        1) zipcode
        2) tract
        3) county
        4) countysub
        5) cbsa
        6) cbsadiv

    year : The year(s) input to query for.

    quarter : The quarter(s) input to query for.

    key : The API key for this user. 

    Returns
    -------

    This returns a list of the cleaned user inputs.
    """
    
    if not isinstance(query, (int, str, list)):
        raise ValueError("\nQuery should be int, str, or list or tuple of ints and strings.")

    if not isinstance(year, (int, str, list)) :
        raise ValueError("\nYear should be int, str, or list or tuple of ints and strings.")

    if not isinstance(quarter, (int, str, list)) :
        raise ValueError("\nQuarter should be int, str, or list or tuple of ints and strings.")
    
    if key == None:
        raise ValueError("\nIt looks like the HUD_KEY was not set: use hud_set_key().")
        
    if type(key) != str:
        raise ValueError("\nKey should be a string")
    
    query = [str(query)] if isinstance(query, str) or isinstance(query, int) else list(map(lambda x: str(x), list(map(lambda x: str(x), query))))
    year = [str(year)] if isinstance(year, str) or isinstance(year, int) else list(map(lambda x: str(x), year))
    quarter =  [str(quarter)] if isinstance(quarter, str) or isinstance(quarter, int) else list(map(lambda x: str(x), quarter))
    
    
    if(key == ""):
        raise ValueError("\nDid you forget to set the key. Please go to " + 
                         "Please go to https://www.huduser.gov/" +
                         "hudapi/public/register?comingfrom=1 to " +
                         "sign up and get a token. Save " +
                         "this to your environment using " +
                         "hud_set_key(your-key)")
    
    year = list(set(map(lambda x: str.strip(x), year)))
    query = list(set(map(lambda x: str.strip(x), query)))
    quarter = list(set(map(lambda x: str.strip(x), quarter)))

    if False in map(lambda x: str.isdecimal(x), query):
        raise ValueError("\nGeoid query input must only be numbers")
    if False in map(lambda x: str.isdecimal(x), year):
        raise ValueError("\nYear input must only be numbers")
    if False in map(lambda x: str.isdecimal(x), quarter):
        raise ValueError("\nQuarter input must only be numbers")

    for i in range(0, len(quarter)):
        if int(quarter[i]) > 4 or int(quarter[i]) < 1:
            raise ValueError("\nQuarters must be from 1 to 4")

    for i in range(0, len(year)):
        if int(year[i]) > int(date.today().strftime("%Y")):
            raise ValueError("\nA year seems to be in the future?")

    return([query, year, quarter, key])



def fmr_il_input_check_cleansing(query: Union[int, str, list[int], list[str], tuple[int], tuple[str]],
                                 year: Union[int, str, list[int], list[str], tuple[int], tuple[str]],
                                 key: str) -> list[list]:
    """
    Helper function to clean user inputted variables for all
    fair markets rent[hud_fmr] and income limits[hud_il] function calls.

    Parameters
    ----------

    query : The inputted geoid. This is likely state, county, cbsa geoids.

    year : The year(s) input to query for.

    key : The API key for this user. 

    Returns
    -------

    This returns a list of the cleaned user inputs.
    """
    if not isinstance(query, (int, str, list)) :
        raise ValueError("\nQuery should be int, str, or list or tuple of ints and strings.")

    if not isinstance(year, (int, str, list)) :
        raise ValueError("\nYear should be int, str, or list or tuple of ints and strings.")
    
    if key == None:
        raise ValueError("\nIt looks like the HUD_KEY was not set: use hud_set_key().")
       
    if type(key) != str:
        raise ValueError("\nKey should be a string")

    query = [str(query)] if isinstance(query, str) or isinstance(query, int) else list(map(lambda x: str(x), query))
    year = [str(year)] if isinstance(year, str) or isinstance(year, int) else list(map(lambda x: str(x), year))


    if(key == ""):
        raise ValueError("\nDid you forget to set the key. Please go to " + 
                         "Please go to https://www.huduser.gov/" +
                         "hudapi/public/register?comingfrom=1 to " +
                         "sign up and get a token. Save " +
                         "this to your environment using " +
                         "hud_set_key(your-key)")
    
    key = list(set(map(lambda x: str.strip(x), key)))
    year = list(set(map(lambda x: str.strip(x), year)))
    query = list(set(map(lambda x: str.strip(x), query)))

    if False in map(lambda x: str.isdecimal(x), query):
        raise ValueError("\nGeoid query input must only be numbers")
    if False in map(lambda x: str.isdecimal(x), year):
        raise ValueError("\nYear input must only be numbers")

    for i in range(0, len(year)):
        if int(year[i]) > int(date.today().strftime("%Y")):
            raise ValueError("\nA year seems to be in the future?")

    if all(map(lambda x: len(x) == 2, query)):
        query = map(lambda x: str.upper(x), query)
    elif all(map(lambda x: len(x) > 2, query)):
        query = map(lambda x: str.capitalize(x), query)

    if hudpkgenv.pkg_env["states"] == None:
        hudpkgenv.pkg_env["states"] = hudinputcheck.hud_nation_states_territories(key = key)
    
    if len(set.intersection(query, hudpkgenv.pkg_env["states"]["state_name"])) != 0: 
        query = hudpkgenv.pkg_env["states"].loc(hudpkgenv.pkg_env["states"]["state_name"].isin(query))[2]
    if len(set.intersection(query, hudpkgenv.pkg_env["states"]["state_code"])) != 0:   
        query = hudpkgenv.pkg_env["states"].loc(hudpkgenv.pkg_env["states"]["state_code"].isin(query))[2]
    if len(set.intersection(query, hudpkgenv.pkg_env["states"]["state_num"])) != 0:  
        query = hudpkgenv.pkg_env["states"].loc(hudpkgenv.pkg_env["states"]["state_num"].isin(query))[2]

    if all(map(lambda x: len(x) == 10, query)):
        querytype = "county"
    elif all(map(lambda x: len(x) == 2, query)):
        querytype = "state"
    elif all(map(lambda x: len(x) == 16), query):
        querytype = "cbsa"
    else:
        raise ValueError("\nThere is no matching fips code for one of the inputted states")

    return([query, year, key, [querytype]])



def crosswalk_a_dataset_input_check_cleansing(data,
                                              geoid: Union[int, str],
                                              geoid_col: Union[int, str],
                                              cw_geoid: str, 
                                              cw_geoid_col : Union[int, str], 
                                              method: str, 
                                              year: Union[int, str], 
                                              quarter: Union[int, str], 
                                              key: str) -> list[list]:
    """
    Helper function to clean user inputted variables for the crosswalk() function.

    Parameters
    ----------

    data : A dataframe with rows describing measurements at a
        zip, county, countysub, cd, tract,
        cbsa, or cbsadiv geoid.

    geoid : The current geoid that the dataset is described in: must be zip,
        county, countysub, cd,
        tract, cbsa, or cbsadiv geographic level.

    geoid_col : The column containing the geographic identifier;
        must be zip, county, countysub, cd,
        tract, cbsa, or cbsadiv geographic level.
        Supply either the name of the column
        or the index.

    cw_geoid : The geoid to crosswalk the dataset to.
 
    method :  The allocation method to use: residential,
        business, other, or total

    year : The year(s) input to query for.

    quarter : The quarter(s) input to query for.

    key : The API key for this user. 

    Returns
    -------

    This returns a list of the cleaned user inputs.

    """

    if len(geoid) > 1 or len(geoid_col) > 1 or \
       len(year) > 1 or len(quarter) > 1:
        raise ValueError("\nMake sure geoid, geoid_col, year, and quarter arguments are of length 1.")
    if key == None:
        raise ValueError("\nIt looks like the HUD_KEY was not set: use hud_set_key().")
       
    if type(key) != str:
        raise ValueError("\nKey should be a string")

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

    return([geoid, geoid_col, cw_geoid, cw_geoid_col, method, 
                args[2], args[3], args[4]])
    