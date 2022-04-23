from datetime import date
import os 

def hud_cw_zip_tract(zip, year = (date.today() - 365).strftime("%Y"),
                             quarter = 1, minimal = False,
                             key = os.getenv("HUD_KEY")):
    """
    #' @name hud_cw_zip_tract
    #' @title hud_cw_zip_tract
    #' @description This function queries the Crosswalks API provided by US
    #'   Department of Housing and Urban Development. This returns the crosswalk for
    #'   zip to tract.
    #' @param zip 5 digit USPS ZIP code of the data to retrieve. E.g. 22031 for type
    #'   1 to 5 and 11 .
    #' @param year Gets the year that this data was recorded. Can specify multiple
    #'   years. Default is the previous year.
    #' @param quarter Gets the quarter of the year that this data was recorded.
    #'   Defaults to the first quarter of the year.
    #' @param minimal Return just the crosswalked GEOIDs if true. Otherwise, return
    #'   all fields. This does not remove duplicates.
    #' @param key The API key for this user. You must go to HUD and sign up for an
    #'   account and request for an API key.
    #' @returns This function returns a dataframe containing CROSSWALK data for a
    #'   particular GEOID. These measurements include res-ratio, bus-ratio,
    #'   oth-ratio, tot-ratio. For more details on these measurements, visit
    #'   https://www.huduser.gov/portal/dataset/uspszip-api.html
    """

def hud_cw_zip_county(zip, year = (date.today() - 365).strftime("%Y"),
                             quarter = 1, minimal = False,
                             key = os.getenv("HUD_KEY")):
    """
    #' @name hud_cw_zip_county
    #' @title hud_cw_zip_county
    #' @description This function queries the Crosswalks API provided by
    #'   US Department of Housing and Urban Development. This
    #'   returns the crosswalk for zip to county.
    #' @param zip 5 digit USPS ZIP code of the data to retrieve. E.g. 22031 for type
    #'   1 to 5 and 11 .
    #' @param year Gets the year that this data was recorded.
    #'   Can specify multiple years. Default is the
    #'   previous year.
    #' @param quarter Gets the quarter of the year that this data was recorded.
    #'   Defaults to the first quarter of the year.
    #' @param minimal Return just the crosswalked GEOIDs if true. Otherwise, return
    #'   all fields. This does not remove duplicates.
    #' @param key The API key for this user. You must go to HUD and sign up for an
    #'   account and request for an API key.
    #' @returns This function returns a dataframe containing CROSSWALK data for
    #'   a particular GEOID. These measurements include res-ratio, bus-ratio,
    #'   oth-ratio, tot-ratio. For more details on these measurements, visit
    #'   https://www.huduser.gov/portal/dataset/uspszip-api.html
    """

def hud_cw_zip_cbsa (zip, year = (date.today() - 365).strftime("%Y"),
                             quarter = 1, minimal = False,
                             key = os.getenv("HUD_KEY")):
    """
    #' @name hud_cw_zip_cbsa
    #' @title hud_cw_zip_cbsa
    #' @description This function queries the Crosswalks API provided by US
    #'   Department of Housing and Urban Development. This returns the crosswalk for
    #'   zip to cbsa.
    #' @param zip 5 digit USPS ZIP code of the data to retrieve. E.g. 22031 for type
    #'   1 to 5 and 11 .
    #' @param year Gets the year that this data was recorded. Can specify multiple
    #'   years. Default is the previous year.
    #' @param quarter Gets the quarter of the year that this data was recorded.
    #'   Defaults to the first quarter of the year.
    #' @param minimal Return just the crosswalked GEOIDs if true. Otherwise, return
    #'   all fields. This does not remove duplicates.
    #' @param key The API key for this user. You must go to HUD and sign up for an
    #'   account and request for an API key.
    #' @returns This function returns a dataframe containing CROSSWALK data for a
    #'   particular GEOID. These measurements include res-ratio, bus-ratio,
    #'   oth-ratio, tot-ratio. For more details on these measurements, visit
    #'   https://www.huduser.gov/portal/dataset/uspszip-api.html
    """

def hud_cw_zip_cbsadiv(zip, year = (date.today() - 365).strftime("%Y"),
                             quarter = 1, minimal = False,
                             key = os.getenv("HUD_KEY")):
    """
    #' @name hud_cw_zip_cbsadiv
    #' @title hud_cw_zip_cbsadiv
    #' @description This function queries the Crosswalks API provided by US
    #'   Department of Housing and Urban Development. This returns the crosswalk for
    #'   zip to cbsadiv. (Available 4th Quarter 2017 onwards)
    #' @param zip 5 digit USPS ZIP code of the data to retrieve. E.g. 22031 for type
    #'   1 to 5 and 11 .
    #' @param year Gets the year that this data was recorded. Can specify multiple
    #'   years. Default is the previous year.
    #' @param quarter Gets the quarter of the year that this data was recorded.
    #'   Defaults to the first quarter of the year.
    #' @param minimal Return just the crosswalked GEOIDs if true. Otherwise, return
    #'   all fields. This does not remove duplicates.
    #' @param key The API key for this user. You must go to HUD and sign up for an
    #'   account and request for an API key.
    #' @returns This function returns a dataframe containing CROSSWALK data for
    #'   a particular GEOID. These measurements include res-ratio, bus-ratio,
    #'   oth-ratio, tot-ratio. For more details on these measurements, visit
    #'   https://www.huduser.gov/portal/dataset/uspszip-api.html
    """

def hud_cw_zip_cd(zip, year = (date.today() - 365).strftime("%Y"),
                             quarter = 1, minimal = False,
                             key = os.getenv("HUD_KEY")):
    """
    #' @name hud_cw_zip_cd
    #' @title hud_cw_zip_cd
    #' @description This function queries the Crosswalks API provided by US
    #'   Department of Housing and Urban Development. This returns the crosswalk for
    #'   zip to congressional district.
    #' @param zip 5 digit USPS ZIP code of the data to retrieve. E.g. 22031 for type
    #'   1 to 5 and 11 .
    #' @param year Gets the year that this data was recorded. Can specify multiple
    #'   years. Default is the previous year.
    #' @param quarter Gets the quarter of the year that this data was recorded.
    #'   Defaults to the first quarter of the year.
    #' @param minimal Return just the crosswalked GEOIDs if true. Otherwise, return
    #'   all fields. This does not remove duplicates.
    #' @param key The API key for this user. You must go to HUD and sign up for an
    #'   account and request for an API key.
    #' @returns This function returns a dataframe containing CROSSWALK data for a
    #'   particular GEOID. These measurements include res-ratio, bus-ratio,
    #'   oth-ratio, tot-ratio. For more details on these measurements, visit
    #'   https://www.huduser.gov/portal/dataset/uspszip-api.html
    """

def hud_cw_zip_countysub(zip, year = (date.today() - 365).strftime("%Y"),
                             quarter = 1, minimal = False,
                             key = os.getenv("HUD_KEY")):
    """
    #' @name hud_cw_zip_countysub
    #' @title hud_cw_zip_countysub
    #' @description This function queries the Crosswalks API provided by US
    #'   Department of Housing and Urban Development. This returns the crosswalk for
    #'   zip to countysub. (Available 2nd Quarter 2018 onwards)
    #' @param zip 5 digit USPS ZIP code of the data to retrieve. E.g. 22031 for type
    #'   1 to 5 and 11 .
    #' @param year Gets the year that this data was recorded. Can specify multiple
    #'   years. Default is the previous year.
    #' @param quarter Gets the quarter of the year that this data was recorded.
    #'   Defaults to the first quarter of the year.
    #' @param minimal Return just the crosswalked GEOIDs if true. Otherwise, return
    #'   all fields. This does not remove duplicates.
    #' @param key The API key for this user. You must go to HUD and sign up for an
    #'   account and request for an API key.
    #' @returns This function returns a dataframe containing CROSSWALK data for
    #'   a particular GEOID. These measurements include res-ratio, bus-ratio,
    #'   oth-ratio, tot-ratio. For more details on these measurements, visit
    #'   https://www.huduser.gov/portal/dataset/uspszip-api.html
    """

def hud_cw_tract_zip(tract, year = (date.today() - 365).strftime("%Y"),
                             quarter = 1, minimal = False,
                             key = os.getenv("HUD_KEY")):
    """
    #' @name hud_cw_tract_zip
    #' @title hud_cw_tract_zip
    #' @description This function queries the Crosswalks API provided by US
    #'   Department of Housing and Urban Development. This returns the crosswalk for
    #'   tract to zip.
    #' @param tract 11 digit unique 2000 or 2010 Census tract GEOID consisting of
    #'   state FIPS + county FIPS + tract code. Eg: 51059461700  for type 6
    #' @param year Gets the year that this data was recorded. Can specify multiple
    #'   years. Default is the previous year.
    #' @param quarter Gets the quarter of the year that this data was recorded.
    #'   Defaults to the first quarter of the year.
    #' @param minimal Return just the crosswalked GEOIDs if true. Otherwise, return
    #'   all fields. This does not remove duplicates.
    #' @param key The API key for this user. You must go to HUD and sign up for an
    #'   account and request for an API key.
    #' @returns This function returns a dataframe containing CROSSWALK data for a
    #'   particular GEOID. These measurements include res-ratio, bus-ratio,
    #'   oth-ratio, tot-ratio. For more details on these measurements, visit
    #'   https://www.huduser.gov/portal/dataset/uspszip-api.html
    """
  
def hud_cw_county_zip(county, year = (date.today() - 365).strftime("%Y"),
                             quarter = 1, minimal = False,
                             key = os.getenv("HUD_KEY")):
    """
    #' @name hud_cw_county_zip
    #' @title hud_cw_county_zip
    #' @description This function queries the Crosswalks API provided by
    #'   US Department of Housing and Urban Development. This
    #'   returns the crosswalk for county to zip.
    #' @param county
    #'   5 digit unique 2000 or 2010 Census county GEOID consisting of
    #' state FIPS + county FIPS. Eg: 51600 for type 7
    #' @param year Gets the year that this data was recorded. Can specify multiple
    #'   years. Default is the previous year.
    #' @param quarter Gets the quarter of the year that this data was recorded.
    #'   Defaults to the first quarter of the year.
    #' @param minimal Return just the crosswalked GEOIDs if true. Otherwise, return
    #'   all fields. This does not remove duplicates.
    #' @param key The API key for this user. You must go to HUD and sign up for an
    #'   account and request for an API key.
    #' @returns This function returns a dataframe containing CROSSWALK data for
    #'   a particular GEOID. These measurements include res-ratio, bus-ratio,
    #'   oth-ratio, tot-ratio. For more details on these measurements, visit
    #'   https://www.huduser.gov/portal/dataset/uspszip-api.html
    """

def hud_cw_cbsa_zip(cbsa, year = (date.today() - 365).strftime("%Y"),
                             quarter = 1, minimal = False,
                             key = os.getenv("HUD_KEY")):
    """
    #' @name hud_cw_cbsa_zip
    #' @title hud_cw_cbsa_zip
    #' @description This function queries the Crosswalks API provided by
    #'   US Department of Housing and Urban Development. This
    #' returns the crosswalk for cbsa to zip.
    #' @param cbsa 5 digit CBSA code for Micropolitan and Metropolitan Areas Eg:
    #'   10380 for type 8
    #' @param year Gets the year that this data was recorded. Can specify multiple
    #'   years. Default is the previous year.
    #' @param quarter Gets the quarter of the year that this data was recorded.
    #'   Defaults to the first quarter of the year.
    #' @param minimal Return just the crosswalked GEOIDs if true. Otherwise, return
    #'   all fields. This does not remove duplicates.
    #' @param key The API key for this user. You must go to HUD and sign up for an
    #'   account and request for an API key.
    #' @returns This function returns a dataframe containing CROSSWALK data for
    #'   a particular GEOID. These measurements include res-ratio, bus-ratio,
    #'   oth-ratio, tot-ratio. For more details on these measurements, visit
    #'   https://www.huduser.gov/portal/dataset/uspszip-api.html
    """

def hud_cw_cbsadiv_zip(cbsadiv, year = (date.today() - 365).strftime("%Y"),
                             quarter = 1, minimal = False,
                             key = os.getenv("HUD_KEY")):
    """
    #' @name hud_cw_cbsadiv_zip
    #' @title hud_cw_cbsadiv_zip
    #' @description This function queries the Crosswalks API provided by
    #'   US Department of Housing and Urban Development. This
    #'   returns the crosswalk for cbsadiv to zip.
    #'   (Available 4th Quarter 2017 onwards)
    #' @param cbsadiv
    #'   5-digit CBSA Division code which only applies to Metropolitan Areas.
    #' @param year Gets the year that this data was recorded. Can specify multiple
    #'   years. Default is the previous year.
    #' @param quarter Gets the quarter of the year that this data was recorded.
    #'   Defaults to the first quarter of the year.
    #' @param minimal Return just the crosswalked GEOIDs if true. Otherwise, return
    #'   all fields. This does not remove duplicates.
    #' @param key The API key for this user. You must go to HUD and sign up for an
    #'   account and request for an API key.
    #' @returns This function returns a dataframe containing CROSSWALK data for
    #'   a particular GEOID. These measurements include res-ratio, bus-ratio,
    #'   oth-ratio, tot-ratio. For more details on these measurements, visit
    #'   https://www.huduser.gov/portal/dataset/uspszip-api.html
    """

def hud_cw_cd_zip(cd, year = (date.today() - 365).strftime("%Y"),
                             quarter = 1, minimal = False,
                             key = os.getenv("HUD_KEY")):
    """
    #' @name hud_cw_cd_zip
    #' @title hud_cw_cd_zip
    #' @description This function queries the Crosswalks API provided by
    #'   US Department of Housing and Urban Development. This
    #'   returns the crosswalk for cbsadiv to zip.
    #' @param cd
    #'  4-digit GEOID for the Congressional District which consists of
    #'  state FIPS + Congressional District code. Eg: 7200 for type 10
    #' @param year Gets the year that this data was recorded.
    #'   Can specify multiple years. Default is the
    #' previous year.
    #' @param quarter Gets the quarter of the year that this data was recorded.
    #'   Defaults to the first quarter of the year.
    #' @param minimal Return just the crosswalked GEOIDs if true. Otherwise, return
    #'   all fields. This does not remove duplicates.
    #' @param key The API key for this user. You must go to HUD and sign up for an
    #'   account and request for an API key.
    #' @returns This function returns a dataframe containing CROSSWALK data for
    #'   a particular GEOID. These measurements include res-ratio, bus-ratio,
    #'   oth-ratio, tot-ratio. For more details on these measurements, visit
    #'   https://www.huduser.gov/portal/dataset/uspszip-api.html
    """
    
def hud_cw_countysub_zip(countysub, year = (date.today() - 365).strftime("%Y"),
                             quarter = 1, minimal = False,
                             key = os.getenv("HUD_KEY")):
    """
    #' @name hud_cw_zip_countysub
    #' @title hud_cw_zip_countysub
    #' @description This function queries the Crosswalks API provided by US
    #'   Department of Housing and Urban Development. This returns the crosswalk for
    #'   zip to countysub. (Available 2nd Quarter 2018 onwards)
    #' @param zip 5 digit USPS ZIP code of the data to retrieve. E.g. 22031 for type
    #'   1 to 5 and 11 .
    #' @param year Gets the year that this data was recorded. Can specify multiple
    #'   years. Default is the previous year.
    #' @param quarter Gets the quarter of the year that this data was recorded.
    #'   Defaults to the first quarter of the year.
    #' @param minimal Return just the crosswalked GEOIDs if true. Otherwise, return
    #'   all fields. This does not remove duplicates.
    #' @param key The API key for this user. You must go to HUD and sign up for an
    #'   account and request for an API key.
    #' @returns This function returns a dataframe containing CROSSWALK data for
    #'   a particular GEOID. These measurements include res-ratio, bus-ratio,
    #'   oth-ratio, tot-ratio. For more details on these measurements, visit
    #'   https://www.huduser.gov/portal/dataset/uspszip-api.html
    """