from __future__ import annotations
from typing import Union

from datetime import date, timedelta
import os 
import itertools

from hudpy import hud_internet_online
from hudpy import hud_input_check
from hudpy import hud_do_query_calls
from hudpy import hud_pkg_env
from hudpy import hud_misc

def hud_chas_nation(year: Union[int, str, list[int], list[str], tuple[int], tuple[str]] = "2014-2018",
                    key: str = None):
    """
    Function to query Comprehensive Housing and Affordability (CHAS) API provided
    by the US Department of Housing and Urban Development. This returns CHAS measurements
    for the entire nation.

    Parameters
    ----------

    year : The year(s) to query for.
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
    This returns CHAS data for the entire nation.

    Examples
    --------

    >>> hud_chas_nation()
   
    """
    if hud_pkg_env.pkg_env["internet_on"] == False: 
        if not hud_internet_online.internet_on():
            raise ConnectionError("You currently do not have internet access.")
        else:
            hud_pkg_env.pkg_env["internet_on"] == True
            
    if(key == None and os.getenv("HUD_KEY") != None):
        key = os.getenv("HUD_KEY")

    args = hud_input_check.chas_input_check_cleansing(query = None, year = year, key = key)
    year = args[0]
    key = args[1]

    all_queries = list(itertools.product(["https://www.huduser.gov/hudapi/public/chas?type=1"], 
                                         ["&year="], year))
    
    urls = []
    for i in range(len(all_queries)):
        urls.append(
            all_queries[i][0] + 
            all_queries[i][1] +
            all_queries[i][2] 
        )

    return(hud_do_query_calls.chas_do_query_calls(urls, key = key))


def hud_chas_state(state: Union[int, str, list[int], list[str], tuple[int], tuple[str]],
                   year: Union[int, str, list[int], list[str], tuple[int], tuple[str]] = "2014-2018", 
                   key: str = None):
    """
    Function to query Comprehensive Housing and Affordability (CHAS) API provided
    by the US Department of Housing and Urban Development. This returns CHAS measurements
    for state(s)

    Parameters
    ----------

    state : The state(s) to query for CHAS. Can be provided as the full name, fip code or
        abbreviation.

    year : The year(s) to query for.
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
    This returns CHAS data for state(s) query.

    Examples
    --------

    >>> hud_chas_state("MD")
   
    >>> hud_chas_state("24")

    >>> hud_chas_state("Maryland")

    """
    
    if hud_pkg_env.pkg_env["internet_on"] == False: 
        if not hud_internet_online.internet_on():
            raise ConnectionError("You currently do not have internet access.")
        else:
            hud_pkg_env.pkg_env["internet_on"] == True
            
    if(key == None and os.getenv("HUD_KEY") != None):
        key = os.getenv("HUD_KEY")


    args = hud_input_check.chas_input_check_cleansing(state, year, key)
    state = args[0]
    year = args[1]
    key = args[2]
  
    # Assume abbreviation or fips code if length of 2. Captitalize does not
    # affect numbers. Assume full state name if length more than 2
    if all(map(lambda x: len(x) == 2, state)):
        state = list(map(lambda x: str.upper(x), state))
    elif all(map(lambda x: len(x) > 2, state)):
        state = list(map(lambda x: x[0:1].upper() + x[1:len(x)].lower(), state))

    if hud_pkg_env.pkg_env["states"].empty:
        hud_pkg_env.pkg_env["states"] = hud_misc.hud_nation_states_territories(key = key)
        hud_pkg_env.pkg_env["states"]["state_num"] = hud_pkg_env.pkg_env["states"]["state_num"].astype("float").astype("int").astype("str")
        
    for i in range(0, len(state)):
        if state[i] not in hud_pkg_env.pkg_env["states"].values:
            raise ValueError("There is no matching fips code for " + str(state[i]))

    if len(set(state).intersection(set(hud_pkg_env.pkg_env["states"]["state_name"]))) != 0: 
        # Not sure if this is right syntax... need to test it...
        state = list(hud_pkg_env.pkg_env["states"][hud_pkg_env.pkg_env["states"]["state_name"].isin(state)]["state_num"])
    if len(set(state).intersection(set(hud_pkg_env.pkg_env["states"]["state_code"]))) != 0:   
        state = list(hud_pkg_env.pkg_env["states"][hud_pkg_env.pkg_env["states"]["state_code"].isin(state)]["state_num"]) 
    if len(set(state).intersection(set(hud_pkg_env.pkg_env["states"]["state_num"]))) != 0:  
        state = list(hud_pkg_env.pkg_env["states"][hud_pkg_env.pkg_env["states"]["state_num"].isin(state)]["state_num"])   
    
  
    
    all_queries = list(itertools.product(["https://www.huduser.gov/hudapi/public/chas?type=2&stateId="], 
                                         state, ["&year="], year))
    
    urls = []
    for i in range(len(all_queries)):
        urls.append(
            all_queries[i][0] + 
            all_queries[i][1] +
            all_queries[i][2] +
            all_queries[i][3]
        )
  

    return hud_do_query_calls.chas_do_query_calls(urls, key = key)



def hud_chas_county(county: Union[int, str, list[int], list[str], tuple[int], tuple[str]],
                    year: Union[int, str, list[int], list[str], tuple[int], tuple[str]] = "2014-2018", 
                    key: str = None):
    """
    Function to query Comprehensive Housing and Affordability (CHAS) API provided
    by the US Department of Housing and Urban Development. This returns CHAS measurements
    for county(s).

    Parameters
    ----------

    county : The county(s) to query for CHAS. Must be provided as a 5 digit fips code.

    year : The year(s) to query for.
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
    This returns CHAS data for state(s) query.

    Examples
    --------

    >>> hud_chas_county(county = ["06105", "06113"])

    >>> hud_chas_county(county = ["06105", "06113"], year = 2020)

    """
    if hud_pkg_env.pkg_env["internet_on"] == False: 
        if not hud_internet_online.internet_on():
            raise ConnectionError("You currently do not have internet access.")
        else:
            hud_pkg_env.pkg_env["internet_on"] == True
            
    if key == None and os.getenv("HUD_KEY") != None:
        key = os.getenv("HUD_KEY")

    args = hud_input_check.chas_input_check_cleansing(county, year, key)
    county = args[0]
    year = args[1]
    key = args[2]

    # Try to fix the counties that have lost leading zeros in them...
    # county = add_leading_zeros(geoid_type = "county", county)

    # The first 2 are state fip. Last 3 are county fip.
    state_fip = list(map(lambda x:  str(x[0:2]).lstrip('0') if len(x) == 5 else (str(x[0:1]) if len(x) == 4 else "") , county))
    county_fip = list(map(lambda x: str(x[2:5]).lstrip('0') if len(x) == 5 else (str(x[1:4]) if len(x) == 4 else "") , county))

    check_county = list(map(lambda x: x + "99999", county))

    if hud_pkg_env.pkg_env["states"].empty:
        hud_pkg_env.pkg_env["states"] = hud_misc.hud_nation_states_territories(key = key)
        hud_pkg_env.pkg_env["states"]["state_num"] = hud_pkg_env.pkg_env["states"]["state_num"].astype("float").astype("int").astype("str")
        
        
    for i in range(0, len(state_fip)):
        if state_fip[i] not in hud_pkg_env.pkg_env["states"].values:
            raise ValueError("\nThere is no matching fips code for " + str(state_fip[i]))

    all_queries = list(itertools.product(["https://www.huduser.gov/hudapi/public/chas?type=3&stateId="],
                                         state_fip, ["&year="], year))
    
    urls = []
    for i in range(0, len(all_queries)):
        urls.append(
            all_queries[i][0] + 
            all_queries[i][1] +
            "&entityId=" +
            county_fip[i % len(county_fip)]+
            all_queries[i][2] +
            all_queries[i][3] 
        )


    return hud_do_query_calls.chas_do_query_calls(urls, key = key)

def hud_chas_state_mcd(state: Union[int, str, list[int], list[str], tuple[int], tuple[str]],
                       year: Union[int, str, list[int], list[str], tuple[int], tuple[str]] = "2014-2018", 
                       key: str = None):
    """
    Function to query Comprehensive Housing and Affordability (CHAS) API provided
    by the US Department of Housing and Urban Development. This returns CHAS measurements
    for minor civil divisions(s).

    Parameters
    ----------

    state : The state(s) to query for CHAS. Can be provided as the full name, fip code or
         abbreviation.

    year : The year(s) to query for.
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
    This returns CHAS data minor civil division(s) for state(s) query.

    Examples
    --------

    >>> hud_chas_state_mcd("VA", year = ["2014-2018", "2013-2017"])

    """
    
    if hud_pkg_env.pkg_env["internet_on"] == False: 
        if not hud_internet_online.internet_on():
            raise ConnectionError("You currently do not have internet access.")
        else:
            hud_pkg_env.pkg_env["internet_on"] == True
            
    if key == None and os.getenv("HUD_KEY") != None:
        key = os.getenv("HUD_KEY")

    args = hud_input_check.chas_input_check_cleansing(query = state, year = year, key = key)
    state = args[0]
    year = args[1]
    key = args[2]

    if all(map(lambda x: len(x) == 2, state)):
        state = list(map(lambda x: str.upper(x), state))
    elif all(map(lambda x: len(x) > 2, state)):
        state = list(map(lambda x: x[0:1].upper() + x[1:len(x)].lower(), state))

    if hud_pkg_env.pkg_env["states"].empty:
        hud_pkg_env.pkg_env["states"] = hud_misc.hud_nation_states_territories(key = key)
        hud_pkg_env.pkg_env["states"]["state_num"] = hud_pkg_env.pkg_env["states"]["state_num"].astype("float").astype("int").astype("str")
        
    for i in range(0, len(state)):
        if state[i] not in hud_pkg_env.pkg_env["states"].values:
            raise ValueError("\nThere is no matching fips code for " + str(state[i]))

    if len(set(state).intersection(set(hud_pkg_env.pkg_env["states"]["state_name"]))) != 0: 
        # Not sure if this is right syntax... need to test it...
        state = list(hud_pkg_env.pkg_env["states"][hud_pkg_env.pkg_env["states"]["state_name"].isin(state)]["state_num"])
    if len(set(state).intersection(set(hud_pkg_env.pkg_env["states"]["state_code"]))) != 0:   
        state = list(hud_pkg_env.pkg_env["states"][hud_pkg_env.pkg_env["states"]["state_code"].isin(state)]["state_num"]) 
    if len(set(state).intersection(set(hud_pkg_env.pkg_env["states"]["state_num"]))) != 0:  
        state = list(hud_pkg_env.pkg_env["states"][hud_pkg_env.pkg_env["states"]["state_num"].isin(state)]["state_num"])   
    
    # Get all mcds using state inputs...
    
    minor_civil_divisions = hud_misc.hud_state_minor_civil_divisions(state)["entityId"]

    all_queries = list(itertools.product(["https://www.huduser.gov/hudapi/public/chas?type=4&stateId="],
                                          state,
                                          ["&year="],
                                          year))
    
    urls = []
    for i in range(0, len(all_queries)):
        urls.append(
            all_queries[i][0] + 
            all_queries[i][1] +
            "&entityId=" +
            minor_civil_divisions[i % len(minor_civil_divisions)] +
            all_queries[i][2] +
            all_queries[i][3] 
        )


    return hud_do_query_calls.chas_do_query_calls(urls, key = key)


def hud_chas_state_place(state: Union[int, str, list[int], list[str], tuple[int], tuple[str]],
                         year: Union[int, str, list[int], list[str], tuple[int], tuple[str]] = "2014-2018", 
                         key: str = None):
    """
    #' @name hud_chas_state_place
    #' @title hud_chas_state_place
    #' @description Returns CHAS for all places in a state.
    #' @param state The state name, abbreviation, or fips code. Make sure if state
    #'   fips is 1 digit number, do not include leading 0.
    #' @param year The years to query for.
    #'  * year = "2014-2018"
    #'  * year = "2013-2017"
    #'  * year = "2012-2016"
    #'  * year = "2011-2015"
    #'  * year = "2010-2014"
    #'  * year = "2009-2013"
    #'  * year = "2008-2012"
    #'  * year = "2007-2011"
    #'  * year = "2006-2010"
    #' @param key The key obtain from HUD USER website.
    #' @returns Returns a dataframe with CHAS data for places.

    Function to query Comprehensive Housing and Affordability (CHAS) API provided
    by the US Department of Housing and Urban Development. This returns CHAS measurements
    for place(s).

    Parameters
    ----------

    state : The state(s) to query for CHAS. Can be provided as the full name, fip code or
         abbreviation.

    year : The year(s) to query for.

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
    This returns CHAS data in places for state(s) query.

    Examples
    --------

    >>> hud_chas_state_place("VA", year = ["2014-2018","2013-2017"])

    """
    
    if hud_pkg_env.pkg_env["internet_on"] == False: 
        if not hud_internet_online.internet_on():
            raise ConnectionError("You currently do not have internet access.")
        else:
            hud_pkg_env.pkg_env["internet_on"] == True
            
    if key == None and os.getenv("HUD_KEY") != None:
        key = os.getenv("HUD_KEY")

    args = hud_input_check.chas_input_check_cleansing(state, year = year, key = key)
    state = args[0]
    year = args[1]
    key = args[2]

    if all(map(lambda x: len(x) == 2, state)):
        state = list(map(lambda x: str.upper(x), state))
    elif all(map(lambda x: len(x) > 2, state)):
        state = list(map(lambda x: x[0:1].upper() + x[1:len(x)].lower(), state))

    if hud_pkg_env.pkg_env["states"].empty:
        hud_pkg_env.pkg_env["states"] = hud_misc.hud_nation_states_territories(key = key)
        hud_pkg_env.pkg_env["states"]["state_num"] = hud_pkg_env.pkg_env["states"]["state_num"].astype("float").astype("int").astype("str")
        
    for i in range(0, len(state)):
        if state[i] not in hud_pkg_env.pkg_env["states"].values:
            raise ValueError("\nThere is no matching fips code for " + str(state[i]))

    if len(set(state).intersection(set(hud_pkg_env.pkg_env["states"]["state_name"]))) != 0: 
        # Not sure if this is right syntax... need to test it...
        state = list(hud_pkg_env.pkg_env["states"][hud_pkg_env.pkg_env["states"]["state_name"].isin(state)]["state_num"])
    if len(set(state).intersection(set(hud_pkg_env.pkg_env["states"]["state_code"]))) != 0:   
        state = list(hud_pkg_env.pkg_env["states"][hud_pkg_env.pkg_env["states"]["state_code"].isin(state)]["state_num"]) 
    if len(set(state).intersection(set(hud_pkg_env.pkg_env["states"]["state_num"]))) != 0:  
        state = list(hud_pkg_env.pkg_env["states"][hud_pkg_env.pkg_env["states"]["state_num"].isin(state)]["state_num"])   
    
    places = hud_misc.hud_state_places(state)["entityId"]

    all_queries = list(itertools.product(["https://www.huduser.gov/hudapi/public/chas?type=4&stateId="],
                                          state,
                                          ["&year="],
                                          year))

    urls = []
    for i in range(0, len(all_queries)):
        urls.append(
            all_queries[i][0] + 
            all_queries[i][1] +
            ["&entityId="],
            places[i % len(places)],
            all_queries[i][2] +
            all_queries[i][3] 
        )


    return hud_do_query_calls.chas_do_query_calls(urls, key = key)
