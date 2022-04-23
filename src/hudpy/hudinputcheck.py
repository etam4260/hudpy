from ast import Raise
from enum import unique
from click import MissingParameter

from langcodes import warnings

def chas_input_check_cleansing(query, year, key):
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
    if type(year) != list and type(year) != tuple or type(key != list and type(key) != tuple):
        raise ValueError("Make sure all inputs are of type list or tuple.")
    
    if(len(key) != 1):
        raise ValueError("There seems to be multiple keys specified.")

    if(key == ""):
        raise ValueError("Did you forget to set the key. Please go to " + 
                         "Please go to https://www.huduser.gov/" +
                         "hudapi/public/register?comingfrom=1 to " +
                         "sign up and get a token. Save " +
                         "this to your environment using " +
                         "hud_set_key(your-key)")
    
    key = unique(map(str.strip(), key))
    year = unique(map(str.strip(), year))

    possible_years = list("2014-2018", "2013-2017", "2012-2016", "2011-2015",
                       "2010-2014", "2009-2013", "2008-2012", "2007-2011",
                       "2006-2010")

    for i in range(1, len(year)):
        if year[i] not in possible_years:
            raise ValueError("One of the years does not fall into the values" +
                             "expected")
    if query is not None:
        if type(query) != list and type(query) != tuple:
            raise ValueError("")

        query = unique(map(str.strip(), query))
        return(list(query, year, key))    
    
    return(list(year, key))


def cw_input_check_cleansing(query, year, quarter, key):
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



def fmr_il_input_check_cleansing(query, year, key):
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

def crosswalk_a_dataset_input_check_cleansing():
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


