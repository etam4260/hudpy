def hud_cw():
    """
    #' @name hud_cw
    #' @title hud_cw
    #' @description This function queries the Crosswalks API provided by
    #'   US Department of Housing and Urban Development.
    #' @param type Must be a number between 1 and 12 depending on the Crosswalk
    #'   type. You can also supply the string name.
    #'   1) zip-tract
    #'   2) zip-county
    #'   3) zip-cbsa
    #'   4) zip-cbsadiv (Available 4th Quarter 2017 onwards)
    #'   5) zip-cd
    #'   6) tract-zip
    #'   7) county-zip
    #'   8) cbsa-zip
    #'   9) cbsadiv-zip (Available 4th Quarter 2017 onwards)
    #'   10) cd-zip
    #'   11) zip-countysub (Available 2nd Quarter 2018 onwards)
    #'   12) countysub-zip (Available 2nd Quarter 2018 onwards)
    #' @param query
    #'   5 digit USPS ZIP code of the data to retrieve.
    #'   E.g. 22031 for type 1 to 5 and 11 .
    #'   or
    #'   11 digit unique 2000 or 2010 Census tract GEOID consisting of
    #'   state FIPS + county FIPS + tract code. Eg: 51059461700  for type 6
    #'   or
    #'   5 digit unique 2000 or 2010 Census county GEOID consisting of
    #'   state FIPS + county FIPS. Eg: 51600 for type 7
    #'   or
    #'   5 digit CBSA code for Micropolitan and Metropolitan Areas
    #'   Eg: 10380 for type 8
    #'   or
    #'   5-digit CBSA Division code which only applies to Metropolitan Areas.
    #'   Eg: 35614 for type 9
    #'   or
    #'   4-digit GEOID for the Congressional District which consists of
    #'   state FIPS + Congressional District code. Eg: 7200 for type 10
    #'   or
    #'   10-digit GEOID for the County sub Eg: 4606720300 for type 12
    #' @param year Gets the year that this data was recorded.
    #'   Can specify multiple years. Default is the
    #'   previous year.
    #' @param quarter Gets the quarter of the year that this data was recorded.
    #'   Defaults to the first quarter of the year.
    #' @param minimal Return just the crosswalked GEOIDs if true. Otherwise, return
    #'   all fields. This does not remove duplicates.
    #' @param key The API key for this user. You must go to HUD and sign up for
    #'   an account and request for an API key.
    #' @keywords Crosswalks API
    #' @returns This function returns a dataframe containing CROSSWALK data for
    #'   a particular GEOID. These measurements include res-ratio, bus-ratio,
    #'   oth-ratio, tot-ratio. For more details on these measurements, visit
    #'   https://www.huduser.gov/portal/dataset/uspszip-api.html
    """


def hud_fmr():
    """
    #' @name hud_fmr
    #' @title hud_fmr
    #' @description This function queries the Fair Markets Rent API provided by
    #'   US Department of Housing and Urban Development. Querying a
    #'   state provides a list containing two dataframes: one with fmr at a county
    #'   level resolution and the other fmr at a metroarea level resolution.
    #'   Querying a county or cbsa will provide data at a zip code resolution
    #'   if geoids are classified as a small area.
    #' @param query Can provide either a 5 digit FIPS code + 99999 at end,
    #'   state abbreviation, or CBSA code.
    #' @param year Gets the year that this data was recorded.
    #'   Can specify multiple years. Default is the
    #'   previous year.
    #' @param key The API key for this user. You must go to HUD and sign up
    #'   for an account and request for an API key.
    #' @keywords Fair Markets Rent API
    #' @returns This function returns a dataframe containing FAIR MARKETS RENT data
    #'   for a particular county or state. For county level data, these measurements
    #'   include the county_name, counties_msa, town_name, metro_status, metro_name,
    #'   smallarea_status, basicdata, Efficiency, One-Bedroom, Two-Bedroom,
    #'   Three-Bedroom, Four-Bedroom, and year. For more details about these
    #'   measurements, go to https://www.huduser.gov/portal/dataset/fmr-api.html For
    #'   state level data, these measurements will be the same as county level data,
    #'   but will return a dataframe with the individual measurements for each
    #'   individual county within the state.
    """



def hud_il():
    """
    #' @name hud_il
    #' @title hud_il
    #' @description This function queries the Income Limits API provided by
    #'   US Department of Housing and Urban Development.
    #' @param query  Querying a
    #'   state provides the IL measurement for that state level resolution. Querying
    #'   Querying a county or cbsa will provide data at a county and
    #'   cbsa resolution, respectively.
    #' @param year Gets the year that this data was recorded.
    #'   Can specify multiple years. Default is the
    #'   previous year.
    #' @param key The API key for this user. You must go to HUD and sign up for
    #'   an account and request for an API key.
    #' @keywords Income Limits API
    #' @returns This function returns a dataframe containing INCOME LIMITS data
    #'   for a particular county or state. For county level data, these measurements
    #'   include the county_name, counties_msa, town_name, metro_status, metro_name,
    #'   year, median_income, very_low+, extremely_low+, and low+. For more details
    #'   about these measurements, go to
    #'   https://www.huduser.gov/portal/dataset/fmr-api.html
    """



def hud_chas():
    """
    #' @name hud_chas
    #' @title hud_chas
    #' @description This function queries the CHAS API provided by US Department
    #'   of Housing and Urban Development
    #' @param type Queries the data based off:
    #'   1 - Nation
    #'   2 - State
    #'   3 - County
    #'   4 - MCD
    #'   5 - Place
    #' @param state_id For types 2,3,4,5, you must provide a stateId. For 3,4,5
    #' @param entity_id For types 3,4,5, you must provide a fips code
    #' @param year Gets the year that this data was recorded. Defaults to 2014-2018.
    #'   There are specific year ranges that are only accepted.
    #'   2014-2018
    #'   2013-2017
    #'   2012-2016
    #'   2011-2015
    #'   2010-2014
    #'   2009-2013
    #'   2008-2012
    #'   2007-2011
    #'   2006-2010
    #' @param key The API key for this user. You must go to HUD and sign up for an
    #'   account and request for an API key.
    #' @keywords Comprehensive Housing Affordability Strategy (CHAS) API
    #' @returns This function returns a dataframe containing CHAS data for a
    #'   particular state. For more details about these measurements, go to
    #'   https://www.huduser.gov/portal/dataset/chas-api.html
    """