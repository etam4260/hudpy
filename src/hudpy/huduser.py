import os
from datetime import date
from typing import Union
from pandas import DataFrame
import hudinternetonline
import hudinputcheck
import hudfmr

def hud_cw(type: Union[str, int],
           query: Union[int, str, list: int, list: str, tuple: Union[int, str]] = None,
           year: Union[int, str, list: int, list: str, tuple: Union[int, str]] = (date.today() - 365).strftime("%Y"),
           quarter: Union[int, str, list:, list: str, tuple: Union[int, str]] = 1,
           minimal: bool = False,
           key: str = os.getenv("HUD_KEY")) -> DataFrame:
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

    >>> hud_cw(type = 1, zip = '35213', year = c('2010'), quarter = c('1'))
    
    >>> hud_cw(type = 1, zip = '35213', year = c('2010'), quarter = c('1'),
        minimal = TRUE)
    """

    if(not hudinternetonline.internet_on()): raise ConnectionError("You currently do not have internet access.")


def hud_fmr(query: Union[int, str, list: int, list: str, tuple: Union[int, str]] = None,
            year: Union[int, str, list: int, list: str, tuple: Union[int, str]] = (date.today() - 365).strftime("%Y"),
            key: str = os.getenv("HUD_KEY")) -> DataFrame:
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

    >>> hud_fmr("VA", year=c(2021))

    >>> hud_fmr("5100199999", year=c(2021))

    >>> hud_fmr("METRO47900M47900", year=c(2018))
    """

    if(not hudinternetonline.internet_on()): raise ConnectionError("You currently do not have internet access.")

    args = hudinputcheck.fmr_il_input_check_cleansing(query, year, key)

    query = args[1]
    year = args[2]
    key = args[3]
    querytype = args[4]

    # If state query, will provide data at metro and county level
    # Call helper functions...
    if (querytype == "state"):
        # Merge county level data with metroarea data.
        return(list(counties = hudfmr.hud_fmr_state_counties(query, year, key),
                    metroareas = hudfmr.hud_fmr_state_metroareas(query, year, key)))
    elif querytype == "cbsa":
        # Returns zip level data.
        return(hudfmr.hud_fmr_metroarea_zip(query, year, key))
    elif querytype == "county":
        # Returns zip level data.
        return(hudfmr.hud_fmr_county_zip(query, year, key))
    


def hud_il(query: Union[int, str, list: int, list: str, tuple: Union[int, str]] = None,
           year: Union[int, str, list: int, list: str, tuple: Union[int, str]] = (date.today() - 365).strftime("%Y"),
           key: str = os.getenv("HUD_KEY")) -> DataFrame:
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

    >>> hud_il("VA", year=c(2021))

    >>> hud_il("5100199999", year=c(2021))

    >>> hud_il("METRO47900M47900", year=c(2018))
    """

    if(not hudinternetonline.internet_on()): raise ConnectionError("You currently do not have internet access.")


def hud_chas(type: Union[str, int],
             state_id: Union[int, str, list: int, list: str, tuple: Union[int, str]] = None,
             entity_id: Union[int, str, list: int, list: str, tuple: Union[int, str]] = None,
             year: Union[int, str, list: int, list: str, tuple: Union[int, str]] = (date.today() - 365).strftime("%Y"),
             key: str = os.getenv("HUD_KEY")) -> DataFrame:
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

    >>> hud_chas('2', state_id = '56')

    >>> hud_chas('3','51','199')

    >>> hud_chas('4', '51', 94087)

    >>> hud_chas('5', '51', 48996)

    """

    if(not hudinternetonline.internet_on()): raise ConnectionError("You currently do not have internet access.")
