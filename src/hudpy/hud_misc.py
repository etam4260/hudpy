from __future__ import annotations
from typing import Union

import urllib3 
import pandas as pd

import os
import re
import json
import itertools

from hudpy import hud_pkg_env
from hudpy import hud_do_query_calls
from hudpy import hud_internet_online
from hudpy import hud_download_bar

def hud_nation_states_territories(key: str = None) -> pd.DataFrame:
    """ 
    Function to query misc API provided by the US Department of Housing and Urban Development. This returns
    all the states and territories in the US along with some associated metadata.

    Parameters
    ----------
    key : The API key for this user. You must go to HUD and sign up for an
        account and request for an API key.

    See Also
    --------
    
    * hud_nation_states_territories()
    * hud_state_metropolitan()
    * hud_state_counties()
    * hud_state_places()
    * hud_state_minor_civil_divisions()

    Returns
    -------
    This returns all the states and territories in the US along with some associated metadata.  

    Examples
    --------

    >>> hud_nation_states_territories()
   
    """
    
    if key == None and os.getenv("HUD_KEY") != None:
        key = os.getenv("HUD_KEY")    
    
    
    if hud_pkg_env.pkg_env["internet_on"] == False: 
        if not hud_internet_online.internet_on():
            raise ConnectionError("You currently do not have internet access.")
        else:
            hud_pkg_env.pkg_env["internet_on"] == True
            
            
    if type(key) != str:
        raise ValueError("\nKey should be a string")

    if key == "":
        raise ValueError("\nDid you forget to set the key. " + 
                         "Please go to https://www.huduser.gov/" +
                         "hudapi/public/register?comingfrom=1 to " +
                         "sign up and get a token. Save " +
                         "this to your environment using " +
                         "hud_set_key(your-key)")

    urls = "https://www.huduser.gov/hudapi/public/fmr/listStates"
    headers = {"Authorization": "Bearer " + key, "User-Agent": "https://github.com/etam4260/hudpy"}
    
    if hud_pkg_env.pkg_env["pool_manager"] == None: hud_pkg_env.pkg_env["pool_manager"] = urllib3.PoolManager()
    
    hud_download_bar.download_bar(done = 1, total = 1, current = urls, error = 0)
    
    call = hud_pkg_env.pkg_env["pool_manager"].request("GET", urls, headers = headers)

    if int(call.status) != 200:
        raise ValueError("No data returned: your key might be invalid.")

    cont = json.loads(call.data.decode('utf-8'))   
    cont = pd.json_normalize(cont) 
 
    cont["state_num"] = cont["state_num"].astype("float").astype("int").astype("str")
    
    return(cont)



def hud_state_metropolitan(state: Union[int, str, list[int], list[str], tuple[int], tuple[str]],
                           key: str = None) -> pd.DataFrame:
    """
    Function to query misc API provided by the US Department of Housing and Urban Development. 
    Get all metropolitan areas for queried states with their name and CBSA code.

    Parameters
    ----------

    state : The states to query for metropolitan areas. Can be provided as the full name, fip code or
        abbreviation.

    key : The API key for this user. You must go to HUD and sign up for an
        account and request for an API key.

    See Also
    --------
    
    * hud_nation_states_territories()
    * hud_state_metropolitan()
    * hud_state_counties()
    * hud_state_places()
    * hud_state_minor_civil_divisions()

    Returns
    -------
    
    Returns a dataframe containing details of metropolitan areas from queried states.
    
    Examples
    --------

    >>> hud_state_metropolitan("VA")

    """
    if(key == None and os.getenv("HUD_KEY") != None):
        key = os.getenv("HUD_KEY")
        
        
    if hud_pkg_env.pkg_env["internet_on"] == False: 
        if not hud_internet_online.internet_on():
            raise ConnectionError("You currently do not have internet access.")
        else:
            hud_pkg_env.pkg_env["internet_on"] == True
            
            
    if not isinstance(state, (int, str, list)) :
        raise ValueError("\nQuery should be int, str, or list or tuple of ints and strings.")

    state = [state] if isinstance(state, str) or isinstance(state, int) else state

    if type(key) != str:
        raise ValueError("\nKey should be a string")
    if key == "":
        raise ValueError("Did you forget to set the key. " + 
                            "Please go to https://www.huduser.gov/" +
                            "hudapi/public/register?comingfrom=1 to " +
                            "sign up and get a token. Save " +
                            "this to your environment using " +
                            "hud_set_key(your-key)")
    
    urls = "https://www.huduser.gov/hudapi/public/fmr/listMetroAreas"
    headers = {"Authorization": "Bearer " + key, "User-Agent": "https://github.com/etam4260/hudpy"}
    
    if hud_pkg_env.pkg_env["pool_manager"] == None: hud_pkg_env.pkg_env["pool_manager"] = urllib3.PoolManager()
    
    call = hud_pkg_env.pkg_env["pool_manager"].request("GET", urls, headers = headers)
    
    if int(call.status) != 200:
        raise ValueError("No data returned: your key might be invalid or some states are not valid.")
        
    cont = json.loads(call.data.decode('utf-8'))    
    cont = pd.json_normalize(cont) 
    
    hud_download_bar.download_bar(done = 1, total = 1, current = urls, error = 0)
    
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

    if all(list(map(lambda x: len(x) == 2, state))):
        state = list(map(lambda x: str.upper(x), state))
    elif all(list(map(lambda x: len(x) > 2, state))):
        state = list(map(lambda x: str.capitalize(x), state))

    if hud_pkg_env.pkg_env["states"].empty:
        hud_pkg_env.pkg_env["states"] = hud_nation_states_territories(key = key)
        hud_pkg_env.pkg_env["states"]["state_num"] = hud_pkg_env.pkg_env["states"]["state_num"].astype("float").astype("int").astype("str")
    
    for i in range(0, len(state)):
        if state[i] not in hud_pkg_env.pkg_env["states"].values:
        
            raise ValueError("There is no matching fips code for " + state[i])

    if len(set(state).intersection(set(hud_pkg_env.pkg_env["states"]["state_name"]))) != 0: 
        # Not sure if this is right syntax... need to test it...
        state = list(hud_pkg_env.pkg_env["states"][hud_pkg_env.pkg_env["states"]["state_name"].isin(state)]["state_code"])
    if len(set(state).intersection(set(hud_pkg_env.pkg_env["states"]["state_code"]))) != 0:   
        state = list(hud_pkg_env.pkg_env["states"][hud_pkg_env.pkg_env["states"]["state_code"].isin(state)]["state_code"]) 
    if len(set(state).intersection(set(hud_pkg_env.pkg_env["states"]["state_num"]))) != 0:  
        state = list(hud_pkg_env.pkg_env["states"][hud_pkg_env.pkg_env["states"]["state_num"].isin(state)]["state_code"])   
    
    cont = cont[cont["metro_state"].isin(state)]

    return(cont.reset_index())



def hud_state_counties(state: Union[int, str, list[int], list[str], tuple[int], tuple[str]],
                       key: str = None) -> pd.DataFrame:
    """
    Function to query misc API provided by the US Department of Housing and Urban Development. 
    Get all counties for queried states with their name and fips code.

    Parameters
    ----------

    state : The states to query for counties. Can be provided as the full name, fip code or
        abbreviation.

    key : The API key for this user. You must go to HUD and sign up for an
        account and request for an API key.

    See Also
    --------
    
    * hud_nation_states_territories()
    * hud_state_metropolitan()
    * hud_state_counties()
    * hud_state_places()
    * hud_state_minor_civil_divisions()

    Returns
    -------
    
    Returns a dataframe containing details of counties from queried states.
    
    Examples
    --------

    >>> hud_state_counties("CA")
    >>> hud_state_counties("Virginia")
    >>> hud_state_counties("51")
    """
    
    if key == None and os.getenv("HUD_KEY") != None:
        key = os.getenv("HUD_KEY")
    
    if hud_pkg_env.pkg_env["internet_on"] == False: 
        if not hud_internet_online.internet_on():
            raise ConnectionError("You currently do not have internet access.")
        else:
            hud_pkg_env.pkg_env["internet_on"] == True
            
    if not isinstance(state, (int, str, list)) :
        raise ValueError("\nQuery should be int, str, or list or tuple of ints and strings.")

    state = [state] if isinstance(state, str) or isinstance(state, int) else state

    if type(key) != str:
        raise ValueError("\nKey should be a string")
    if key == "":
        raise ValueError("Did you forget to set the key. " + 
                            "Please go to https://www.huduser.gov/" +
                            "hudapi/public/register?comingfrom=1 to " +
                            "sign up and get a token. Save " +
                            "this to your environment using " +
                            "hud_set_key(your-key)")

    if all(list(map(lambda x: len(x) == 2, state))):
        state = list(map(lambda x: str.upper(x), state))
    elif all(list(map(lambda x: len(x) > 2, state))):
        state = list(map(lambda x: str.capitalize(x), state))


    if hud_pkg_env.pkg_env["states"].empty:
        hud_pkg_env.pkg_env["states"] = hud_nation_states_territories(key = key)
        hud_pkg_env.pkg_env["states"]["state_num"] = hud_pkg_env.pkg_env["states"]["state_num"].astype("float").astype("int").astype("str")
    
    for i in range(0, len(state)):
        if state[i] not in hud_pkg_env.pkg_env["states"].values:
            raise ValueError("There is no matching fips code for " + state[i])

    if len(set(state).intersection(set(hud_pkg_env.pkg_env["states"]["state_name"]))) != 0: 
        # Not sure if this is right syntax... need to test it...
        state = list(hud_pkg_env.pkg_env["states"][hud_pkg_env.pkg_env["states"]["state_name"].isin(state)]["state_code"])
    if len(set(state).intersection(set(hud_pkg_env.pkg_env["states"]["state_code"]))) != 0:   
        state = list(hud_pkg_env.pkg_env["states"][hud_pkg_env.pkg_env["states"]["state_code"].isin(state)]["state_code"]) 
    if len(set(state).intersection(set(hud_pkg_env.pkg_env["states"]["state_num"]))) != 0:  
        state = list(hud_pkg_env.pkg_env["states"][hud_pkg_env.pkg_env["states"]["state_num"].isin(state)]["state_code"])   

    all_queries = list(itertools.product(["https://www.huduser.gov/hudapi/public/fmr/listCounties/"], state))
    
    urls = []
    for i in range(0, len(all_queries)):
        urls.append(
            all_queries[i][0] + 
            all_queries[i][1]
        )

    counties = hud_do_query_calls.misc_do_query_calls(urls, key)

    if len(counties) > 1:
        return(counties.reset_index())
    
    raise ValueError("Your key might be invalid or could not find counties for this state.")



def hud_state_places(state: Union[int, str, list[int], list[str], tuple[int], tuple[str]],
                     key: str = None) -> pd.DataFrame:
    """
    Function to query misc API provided by the US Department of Housing and Urban Development. 
    Get all places for queried states with their name and place code.

    Parameters
    ----------

    state : The states to query for places. Can be provided as the full name, fip code or
        abbreviation.

    key : The API key for this user. You must go to HUD and sign up for an
        account and request for an API key.

    See Also
    --------
    
    * hud_nation_states_territories()
    * hud_state_metropolitan()
    * hud_state_counties()
    * hud_state_places()
    * hud_state_minor_civil_divisions()

    Returns
    -------
    
    Returns a dataframe containing details of places from queried states.
    
    Examples
    --------

    >>> hud_state_places("CA")
    >>> hud_state_places("Virginia")
    >>> hud_state_places("51")
    """
    if key == None and os.getenv("HUD_KEY") != None:
        key = os.getenv("HUD_KEY")
        
        
    if hud_pkg_env.pkg_env["internet_on"] == False: 
        if not hud_internet_online.internet_on():
            raise ConnectionError("You currently do not have internet access.")
        else:
            hud_pkg_env.pkg_env["internet_on"] == True
            
            
    if not isinstance(state, (int, str, list)) :
        raise ValueError("\nQuery should be int, str, or list or tuple of ints and strings.")

    state = [state] if isinstance(state, str) or isinstance(state, int) else state

    if type(key) != str:
        raise ValueError("\nKey should be a string")
    if key == "":
        raise ValueError("Did you forget to set the key. " + 
                            "Please go to https://www.huduser.gov/" +
                            "hudapi/public/register?comingfrom=1 to " +
                            "sign up and get a token. Save " +
                            "this to your environment using " +
                            "hud_set_key(your-key)")
                            
    if all(list(map(lambda x: len(x) == 2, state))):
        state = list(map(lambda x: str.upper(x), state))
    elif all(list(map(lambda x: len(x) > 2, state))):
        state = list(map(lambda x: str.capitalize(x), state))


    if hud_pkg_env.pkg_env["states"].empty:
        hud_pkg_env.pkg_env["states"] = hud_nation_states_territories(key = key)
        hud_pkg_env.pkg_env["states"]["state_num"] = hud_pkg_env.pkg_env["states"]["state_num"].astype("float").astype("int").astype("str")
        
    for i in range(0, len(state)):
        if state[i] not in hud_pkg_env.pkg_env["states"].values:
            raise ValueError("There is no matching fips code for " + state[i])

    if len(set(state).intersection(set(hud_pkg_env.pkg_env["states"]["state_name"]))) != 0: 
        # Not sure if this is right syntax... need to test it...
        state = list(hud_pkg_env.pkg_env["states"][hud_pkg_env.pkg_env["states"]["state_name"].isin(state)]["state_num"])
    if len(set(state).intersection(set(hud_pkg_env.pkg_env["states"]["state_code"]))) != 0:   
        state = list(hud_pkg_env.pkg_env["states"][hud_pkg_env.pkg_env["states"]["state_code"].isin(state)]["state_num"]) 
    if len(set(state).intersection(set(hud_pkg_env.pkg_env["states"]["state_num"]))) != 0:  
        state = list(hud_pkg_env.pkg_env["states"][hud_pkg_env.pkg_env["states"]["state_num"].isin(state)]["state_num"])   
    all_queries = list(itertools.product(["https://www.huduser.gov/hudapi/public/chas/listCities/"], state))
    
    urls = []
    for i in range(0, len(all_queries)):
        urls.append(
            all_queries[i][0] + 
            str(int(float(all_queries[i][1])))
        )

    places = hud_do_query_calls.misc_do_query_calls(urls, key)

    if len(places) > 1:
        return(places.reset_index())
    
    raise ValueError("Your key might be invalid or could not find places for this state.")



def hud_state_minor_civil_divisions(state: Union[int, str, list[int], list[str], tuple[int], tuple[str]],
                                    key: str = None) -> pd.DataFrame:
    """
    Function to query misc API provided by the US Department of Housing and Urban Development. 
    Get all minor civil divisions for queried states with their name and mcd code.

    Parameters
    ----------

    state : The states to query for mcds. Can be provided as the full name, fip code or
        abbreviation.

    key : The API key for this user. You must go to HUD and sign up for an
        account and request for an API key.

    See Also
    --------
    
    * hud_nation_states_territories()
    * hud_state_metropolitan()
    * hud_state_counties()
    * hud_state_places()
    * hud_state_minor_civil_divisions()

    Returns
    -------
    
    Returns a dataframe containing details of mcds from queried states.
    
    Examples
    --------

    >>> hud_state_minor_civil_divisions("CA")
    >>> hud_state_minor_civil_divisions("Virginia")
    >>> hud_state_minor_civil_divisions("51")
    """
    
    if key == None and os.getenv("HUD_KEY") != None:
        key = os.getenv("HUD_KEY")
        
        
    if hud_pkg_env.pkg_env["internet_on"] == False: 
        if not hud_internet_online.internet_on():
            raise ConnectionError("You currently do not have internet access.")
        else:
            hud_pkg_env.pkg_env["internet_on"] == True
            
            
    if not isinstance(state, (int, str, list)) :
        raise ValueError("\nQuery should be int, str, or list or tuple of ints and strings.")

    state = [state] if isinstance(state, str) or isinstance(state, int) else state

    if type(key) != str:
        raise ValueError("\nKey should be a string")
    if key == "":
        raise ValueError("Did you forget to set the key. " + 
                            "Please go to https://www.huduser.gov/" +
                            "hudapi/public/register?comingfrom=1 to " +
                            "sign up and get a token. Save " +
                            "this to your environment using " +
                            "hud_set_key(your-key)")
                    
            
    if all(list(map(lambda x: len(x) == 2, state))):
        state = list(map(lambda x: str.upper(x), state))
    elif all(list(map(lambda x: len(x) > 2, state))):
        state = list(map(lambda x: str.capitalize(x), state))


    if hud_pkg_env.pkg_env["states"].empty:
        hud_pkg_env.pkg_env["states"] = hud_nation_states_territories(key = key)
        hud_pkg_env.pkg_env["states"]["state_num"] = hud_pkg_env.pkg_env["states"]["state_num"].astype("float").astype("int").astype("str")
        
    for i in range(0, len(state)):
        if state[i] not in hud_pkg_env.pkg_env["states"].values:
            raise ValueError("There is no matching fips code for " + state[i])

    if len(set(state).intersection(set(hud_pkg_env.pkg_env["states"]["state_name"]))) != 0: 
        # Not sure if this is right syntax... need to test it...
        state = list(hud_pkg_env.pkg_env["states"][hud_pkg_env.pkg_env["states"]["state_name"].isin(state)]["state_num"])
    if len(set(state).intersection(set(hud_pkg_env.pkg_env["states"]["state_code"]))) != 0:   
        state = list(hud_pkg_env.pkg_env["states"][hud_pkg_env.pkg_env["states"]["state_code"].isin(state)]["state_num"]) 
    if len(set(state).intersection(set(hud_pkg_env.pkg_env["states"]["state_num"]))) != 0:  
        state = list(hud_pkg_env.pkg_env["states"][hud_pkg_env.pkg_env["states"]["state_num"].isin(state)]["state_num"])   
    all_queries = list(itertools.product(["https://www.huduser.gov/hudapi/public/chas/listMCDs/"], state))
    
    urls = []
    for i in range(0, len(all_queries)):
        urls.append(
            all_queries[i][0] + 
            str(int(float(all_queries[i][1])))
        )
        
  
    mcd = hud_do_query_calls.misc_do_query_calls(urls, key)
  
    if len(mcd) > 1:
        return(mcd.reset_index())
    
    raise ValueError("Your key might be invalid or could not find mcds for this state.")