import urllib3

def chas_do_query_calls():
    """
    #' @name chas_do_query_calls
    #' @title chas_do_query_calls
    #' @description Helper function for making the query calls to CHAS
    #' API endpoint.
    #' @param urls The urls to query for.
    #' @param key The key obtain from HUD USER website.
    #' @returns A dataframe of all the response bodies.
    """


def cw_do_query_calls():
    """
    #' @name cw_do_query_calls
    #' @title cw_do_query_calls
    #' @description Helper function for queries to the crosswalk API.
    #' @param urls The url endpoints to query for.
    #' @param primary_geoid The first geoid part of a function call. For example,
    #'   hud_cw_zip_tract() has zip as first GEOID and tract as second GEOID.
    #' @param secondary_geoid The second geoid part of a function call.
    #' @param key The key needed to query the HUD API
    #' @returns A data frame of all the results made from the query.
    """


def misc_do_query_calls():
    """
    #' @name misc_do_query_call
    #' @title misc_do_query_call
    #' @description Make queries calls given a list of urlss
    #' @param urls The urlss to query for.
    #' @param key The API key for this user. You must go to HUD and sign up for
    #'   an account and request for an API key.
    #' @returns A dataframe containing all queried rows.
    """