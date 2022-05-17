import os
from typing import Union
import urllib3 
import pandas as pd
import hudpkgenv
import re
import json
import itertools
import huddoquerycalls

def hud_nation_states_territories(key: str = os.getenv("HUD_KEY")) -> pd.DataFrame:
    """
    #' @title hud_nation_states_territories
    #' @description Get a list of state and US territories
    #'   along with the corresponding fips code and
    #'   abbreviation.
    #' @param key The API key for this user. You must go to HUD and sign up for an
    #'   account and request for an API key.
    #' @keywords States Territories
    #' @returns A dataframe containing details of all the states and territories
    #'   in the US.
    """
    if type(key) != str:
        raise ValueError("\nKey should be a string")

    if(key == ""):
        raise ValueError("\nDid you forget to set the key. Please go to " + 
                         "Please go to https://www.huduser.gov/" +
                         "hudapi/public/register?comingfrom=1 to " +
                         "sign up and get a token. Save " +
                         "this to your environment using " +
                         "hud_set_key(your-key)")

    urls = "https://www.huduser.gov/hudapi/public/fmr/listStates"
    headers = {"Authorization": "Bearer " + key, "User-Agent": "https://github.com/etam4260/hudpy"}
    call = urllib3.http.request("GET", urls, headers = headers, timeout = 30)

    cont = json.loads(call.data.decode('utf-8'))    
    cont = pd.json_normalize(cont) 

    return(cont)



def hud_state_metropolitan(state: Union[int, str, list: int, list: str, tuple: Union[int, str]],
                           key: str = os.getenv("HUD_KEY")) -> pd.DataFrame:
    """
    #' @name hud_state_metropolitan
    #' @title hud_state_metropolitan
    #' @description Get a list of all metropolitan areas for this state with its
    #'   name and CBSA code.
    #' @param state The state to get all the metropolitan areas.
    #' @param key The API key for this user. You must go to HUD and sign up for an
    #'   account and request for an API key.
    #' @keywords CBSA
    #' @returns A dataframe containing details of metropolitan areas in US.
    """
    if not isinstance(state, Union[int, str, list: int, list: str, tuple: Union[int, str]].__args__) :
        raise ValueError("\nQuery should be int, str, or list or tuple of ints and strings.")

    state = [state] if isinstance(state, str) or isinstance(state, int) else state

    if type(key) != str:
        raise ValueError("\nKey should be a string")
    if(key == ""):
        raise ValueError("Did you forget to set the key. Please go to " + 
                            "Please go to https://www.huduser.gov/" +
                            "hudapi/public/register?comingfrom=1 to " +
                            "sign up and get a token. Save " +
                            "this to your environment using " +
                            "hud_set_key(your-key)")

    http = urllib3.PoolManager()
    
    urls = "https://www.huduser.gov/hudapi/public/fmr/listMetroAreas"
    headers = {"Authorization": "Bearer " + key, "User-Agent": "https://github.com/etam4260/hudpy"}
    call = http.request("GET", urls, headers = headers, timeout = 30)
    
    cont = json.loads(call.data.decode('utf-8'))    
    cont = pd.json_normalize(cont) 

    # Not vectorized so need to match 
    # each item in cont["area_name"] one by one...
    def parse_area_name(area):
        regex = re.match("^(.*),\\s([^ ]*)\\s(.*)", area)
        return(regex)

    # Do regex matching for all items inside of area_name
    # so items can be differentiated...
    regexec = cont["area_name"].apply(parse_area_name)

    metro_name = list()
    parsed_state = list()
    classifications = list()

    for i in range(len(cont["area_name"])):
        # Put each individual item in area column into their own list
        # before tacking it onto the final dataframe...
        metro_name.append(regexec[i].group(1))
        parsed_state.append(regexec[i].group(2))
        classifications.append(regexec[i].group(3))

    # now add the new columns
    cont["metro_name"] = metro_name
    cont["metro_state"] = parsed_state
    cont["classifications"] = classifications

    if all(map(len() == 2, state)):
        state = map(str.upper(), state)
    elif all(map(len() > 2, state)):
        state = map(str.capitalize(), state)

    if hudpkgenv.pkg_env["states"] == None:
        hudpkgenv.pkg_env["states"] = hud_nation_states_territories(key = key)
    
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

    cont = cont[cont["metro_state"].isin(state)]

    return(cont)



def hud_state_counties(state: Union[int, str, list: int, list: str, tuple: Union[int, str]],
                       key: str = os.getenv("HUD_KEY")) -> pd.DataFrame:
    """
    #' @name hud_state_counties
    #' @title hud_state_counties
    #' @description Get a list of all counties within a state.
    #' @param state The state to get all counties.
    #' @param key The API key for this user. You must go to HUD and sign up for
    #'  an account and request for an API key.
    #' @keywords Counties
    #' @returns A dataframe containing all counties within a state
    """
    if not isinstance(state, Union[int, str, list: int, list: str, tuple: Union[int, str]].__args__) :
        raise ValueError("\nQuery should be int, str, or list or tuple of ints and strings.")

    state = [state] if isinstance(state, str) or isinstance(state, int) else state

    if type(key) != str:
        raise ValueError("\nKey should be a string")
    if(key == ""):
        raise ValueError("Did you forget to set the key. Please go to " + 
                            "Please go to https://www.huduser.gov/" +
                            "hudapi/public/register?comingfrom=1 to " +
                            "sign up and get a token. Save " +
                            "this to your environment using " +
                            "hud_set_key(your-key)")

    if all(map(len() == 2, state)):
        state = map(str.upper(), state)
    elif all(map(len() > 2, state)):
        state = map(str.capitalize(), state)

    if hudpkgenv.pkg_env["states"] == None:
        hudpkgenv.pkg_env["states"] = hud_nation_states_territories(key = key)
    
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

    all_queries = list(itertools.product(["https://www.huduser.gov/hudapi/public/fmr/listCounties/"], state))
    
    urls = []
    for i in range(0, len(all_queries)):
        urls.append(
            all_queries[i][0] + 
            all_queries[i][1]
        )

    counties = huddoquerycalls.misc_do_query_call(urls, key)

    if (len(counties) > 1):
        return(counties)
    
    raise ValueError("Your key might be invalid or could not find counties for this state.")



def hud_state_places(state: Union[int, str, list: int, list: str, tuple: Union[int, str]],
                     key: str = os.getenv("HUD_KEY")) -> pd.DataFrame:
    """
    #' @name hud_state_places
    #' @title hud_state_places
    #' @description Get a list of all places in a state.
    #' @param state The state to get all places.
    #' @param key The API key for this user. You must go to HUD and sign up for
    #'  an account and request for an API key.
    #' @keywords places.
    #' @returns A dataframe containing details of places in a state.
    """

    if not isinstance(state, Union[int, str, list: int, list: str, tuple: Union[int, str]].__args__) :
        raise ValueError("\nQuery should be int, str, or list or tuple of ints and strings.")

    state = [state] if isinstance(state, str) or isinstance(state, int) else state

    if type(key) != str:
        raise ValueError("\nKey should be a string")
    if(key == ""):
        raise ValueError("Did you forget to set the key. Please go to " + 
                            "Please go to https://www.huduser.gov/" +
                            "hudapi/public/register?comingfrom=1 to " +
                            "sign up and get a token. Save " +
                            "this to your environment using " +
                            "hud_set_key(your-key)")
                            
    if all(map(len() == 2, state)):
        state = map(str.upper(), state)
    elif all(map(len() > 2, state)):
        state = map(str.capitalize(), state)

    if hudpkgenv.pkg_env["states"] == None:
        hudpkgenv.pkg_env["states"] = hud_nation_states_territories(key = key)
    
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

    all_queries = list(itertools.product(["https://www.huduser.gov/hudapi/public/fmr/listCities/"], state))
    
    urls = []
    for i in range(0, len(all_queries)):
        urls.append(
            all_queries[i][0] + 
            all_queries[i][1]
        )

    places = huddoquerycalls.misc_do_query_call(urls, key)

    if (len(places) > 1):
        return(places)
    
    raise ValueError("Your key might be invalid or could not find places for this state.")



def hud_state_minor_civil_divisions(state: Union[int, str, list: int, list: str, tuple: Union[int, str]],
                                    key: str = os.getenv("HUD_KEY")) -> pd.DataFrame:
    """
    #' @name hud_state_minor_civil_divisions
    #' @title hud_state_minor_civil_divisions
    #' @description Get a list of all minor civil divisions in a state
    #' @param state The state to get all MCD.
    #' @param key The API key for this user. You must go to HUD and sign up for
    #'  an account and request for an API key.
    #' @keywords CBSA
    #' @returns A dataframe containing details of minor civil divisions in a state.
    #' @examples
    """

    if not isinstance(state, Union[int, str, list: int, list: str, tuple: Union[int, str]].__args__) :
        raise ValueError("\nQuery should be int, str, or list or tuple of ints and strings.")

    state = [state] if isinstance(state, str) or isinstance(state, int) else state

    if type(key) != str:
        raise ValueError("\nKey should be a string")
    if(key == ""):
        raise ValueError("Did you forget to set the key. Please go to " + 
                            "Please go to https://www.huduser.gov/" +
                            "hudapi/public/register?comingfrom=1 to " +
                            "sign up and get a token. Save " +
                            "this to your environment using " +
                            "hud_set_key(your-key)")
                            
    if all(map(len() == 2, state)):
        state = map(str.upper(), state)
    elif all(map(len() > 2, state)):
        state = map(str.capitalize(), state)

    if hudpkgenv.pkg_env["states"] == None:
        hudpkgenv.pkg_env["states"] = hud_nation_states_territories(key = key)
    
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

    all_queries = list(itertools.product(["https://www.huduser.gov/hudapi/public/fmr/listMCDs/"], state))
    
    urls = []
    for i in range(0, len(all_queries)):
        urls.append(
            all_queries[i][0] + 
            all_queries[i][1]
        )

    mcd = huddoquerycalls.misc_do_query_call(urls, key)

    if (len(mcd) > 1):
        return(mcd)
    
    raise ValueError("Your key might be invalid or could not find mcds for this state.")