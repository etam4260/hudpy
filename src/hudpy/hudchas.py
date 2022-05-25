from __future__ import annotations
from typing import Union

from datetime import date, timedelta
import os 
import itertools

from hudpy import hudinternetonline
from hudpy import hudinputcheck
from hudpy import huddoquerycalls
from hudpy import hudpkgenv
from hudpy import hudmisc

def hud_chas_nation(year: Union[int, str, list[int], list[str], tuple[int], tuple[str]] = (date.today() - timedelta(days = 365)).strftime("%Y"),
                    key: str = os.getenv("HUD_KEY")):
    """
    Function to query Comprehensive Housing and Affordability (CHAS) API provided
    by the US Department of Housing and Urban Development. This returns CHAS measurements
    for the entire nation.

    Parameters
    ----------

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
    This returns CHAS data for the entire nation.

    Examples
    --------

    >>> hud_chas_nation()
   
    """


    args = hudinputcheck.chas_input_check_cleansing(year = year, key = key)
    year = args[[1]]
    key = args[[2]]

    urls = "https://www.huduser.gov/hudapi/public/chas?type=" + "1" + "&year=" + year

    return(huddoquerycalls.chas_do_query_calls(urls, key = key))


def hud_chas_state(state: Union[int, str, list[int], list[str], tuple[int], tuple[str]],
                   year: Union[int, str, list[int], list[str], tuple[int], tuple[str]] = (date.today() - timedelta(days = 365)).strftime("%Y"), 
                   key: str = os.getenv("HUD_KEY")):
    """
    Function to query Comprehensive Housing and Affordability (CHAS) API provided
    by the US Department of Housing and Urban Development. This returns CHAS measurements
    for state(s)

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
    This returns CHAS data for state(s) query.

    Examples
    --------

    >>> hud_chas_state("MD")
   
    >>> hud_chas_state("24")

    >>> hud_chas_state("Maryland")

    """
    
    args = hudinputcheck.chas_input_check_cleansing(state, year, key)
    state = args[[1]]
    year = args[[2]]
    key = args[[3]]

    # Assume abbreviation or fips code if length of 2. Captitalize does not
    # affect numbers. Assume full state name if length more than 2
    if all(map(len() == 2, state)):
        state = map(str.upper(), state)
    elif all(map(len() > 2, state)):
        state = map(str.capitalize(), state)

    if hudpkgenv.pkg_env["states"] == None:
        hudpkgenv.pkg_env["states"] = hudmisc.hud_nation_states_territories(key = key)
        hudpkgenv.pkg_env["states"]["state_num"] = hudpkgenv.pkg_env["states"]["state_num"].astype("float").astype("int").astype("str")
        
    for i in range(0, len(state)):
        if state[i] not in hudpkgenv.pkg_env["states"]:
            raise ValueError("There is no matching fips code for " + state[i])

    if len(set.intersection(state, hudpkgenv.pkg_env["states"]["state_name"])) != 0: 
        # Not sure if this is right syntax... need to test it...
        state = hudpkgenv.pkg_env["states"].loc(hudpkgenv.pkg_env["states"]["state_name"].isin(state))[2]
    if len(set.intersection(state, hudpkgenv.pkg_env["states"]["state_code"])) != 0:   
        state = hudpkgenv.pkg_env["states"].loc(hudpkgenv.pkg_env["states"]["state_code"].isin(state))[2]
    if len(set.intersection(state, hudpkgenv.pkg_env["states"]["state_num"])) != 0:  
        state = hudpkgenv.pkg_env["states"].loc(hudpkgenv.pkg_env["states"]["state_num"].isin(state))[2]


    all_queries = list(itertools.product(["https://www.huduser.gov/hudapi/public/chas?type=2"], state, ["&year="], year))
    
    urls = []
    for i in range(0, len(all_queries)):
        urls.append(
            all_queries[i][0] + 
            all_queries[i][1] +
            all_queries[i][2] +
            all_queries[i][3]
        )


    return huddoquerycalls.chas_do_query_calls(urls, key = key)

def hud_chas_county(county: Union[int, str, list[int], list[str], tuple[int], tuple[str]],
                    year: Union[int, str, list[int], list[str], tuple[int], tuple[str]] = (date.today() - timedelta(days = 365)).strftime("%Y"), 
                    key: str = os.getenv("HUD_KEY")):
    """
    Function to query Comprehensive Housing and Affordability (CHAS) API provided
    by the US Department of Housing and Urban Development. This returns CHAS measurements
    for county(s).

    Parameters
    ----------

    county : The county(s) to query for CHAS. Must be provided as a 5 digit fips code.

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
    This returns CHAS data for state(s) query.

    Examples
    --------

    >>> hud_chas_county(county = [06105, 06113])

    >>> hud_chas_county(county = ["06105", "06113"], year = 2020)

    """

    args = hudinputcheck.chas_input_check_cleansing(county, year, key)
    county = args[[1]]
    year = args[[2]]
    key = args[[3]]

    # Try to fix the counties that have lost leading zeros in them...
    # county = add_leading_zeros(geoid_type = "county", county)

    # The first 2 are state fip. Last 3 are county fip.
    state_fip = map(lambda x: int(x[1,2]), county)
    county_fip = map(lambda x: int(x[3,5]), county)

    check_county = county + "99999"

    if hudpkgenv.pkg_env["states"] == None:
        hudpkgenv.pkg_env["states"] = hudmisc.hud_nation_states_territories(key = key)
        hudpkgenv.pkg_env["states"]["state_num"] = hudpkgenv.pkg_env["states"]["state_num"].astype("float").astype("int").astype("str")
        
        
    for i in range(0, len(state_fip)):
        if state_fip[i] not in hudpkgenv.pkg_env["states"]:
            raise ValueError("\nThere is no matching fips code for " + state_fip[i])

    for i in range(0, len(county_fip)):
        if county_fip[i] not in hudpkgenv.pkg_env["states"]["fips_code"]:
            raise ValueError("\nThere is no matching county FIPs code for",
                             "one of the inputted counties")
    
    all_queries = list(itertools.product(["https://www.huduser.gov/hudapi/public/chas?type=3&stateId="],
                                         state_fip, ["&entityId="],
                                         county_fip, ["&year="], year))
    
    urls = []
    for i in range(0, len(all_queries)):
        urls.append(
            all_queries[i][0] + 
            all_queries[i][1] +
            all_queries[i][2] +
            all_queries[i][3] +
            all_queries[i][4] +
            all_queries[i][5] 
        )


    return huddoquerycalls.chas_do_query_calls(urls, key = key)

def hud_chas_state_mcd(state: Union[int, str, list[int], list[str], tuple[int], tuple[str]],
                       year: Union[int, str, list[int], list[str], tuple[int], tuple[str]] = (date.today() - timedelta(days = 365)).strftime("%Y"), 
                       key: str = os.getenv("HUD_KEY")):
    """
    Function to query Comprehensive Housing and Affordability (CHAS) API provided
    by the US Department of Housing and Urban Development. This returns CHAS measurements
    for minor civil divisions(s).

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
    This returns CHAS data minor civil division(s) for state(s) query.

    Examples
    --------

    >>> hud_chas_state_mcd("VA", year = c("2014-2018","2013-2017"))

    """


def hud_chas_state_place(state: Union[int, str, list[int], list[str], tuple[int], tuple[str]],
                         year: Union[int, str, list[int], list[str], tuple[int], tuple[str]] = (date.today() - timedelta(days = 365)).strftime("%Y"), 
                         key: str = os.getenv("HUD_KEY")):
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

    >>> hud_chas_state_place("VA", year = c("2014-2018","2013-2017"))

    """
    
