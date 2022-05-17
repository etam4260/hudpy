import urllib3
import pandas as pd
import huddownloadbar
import json
import hudinternetonline

def chas_do_query_calls(urls, key: str) -> pd.DataFrame:
    """
    #' @name chas_do_query_calls
    #' @title chas_do_query_calls
    #' @description Helper function for making the query calls to CHAS
    #' API endpoint.
    #' @param urls The urls to query for.
    #' @param key The key obtain from HUD USER website.
    #' @returns A dataframe of all the response bodies.
    """

    if(not hudinternetonline.internet_on()): raise ConnectionError("You currently do not have internet access.")

    list_res = list()
    error_urls = list()

    all_measurements = list("geoname", "sumlevel", "year",
                            "A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8", "A9",
                            "A10", "A11", "A12", "A13", "A14", "A15", "A16", "A17",
                            "A18",
                            "B1", "B2", "B3", "B4", "B5", "B6", "B7",
                            "B8", "B9",
                            "C1", "C2", "C3", "C4", "C5", "C6",
                            "D1", "D2", "D3",
                            "D4", "D5", "D6", "D7", "D8", "D9", "D10", "D11", "D12",
                            "E1", "E2", "E3", "E5", "E6", "E7", "E9", "E10", "E11",
                            "E13", "E14", "E15", "E17", "E18", "E19", "E21", "E22",
                            "E23",
                            "F1", "F2", "F3", "F5", "F6", "F7", "F9", "F10", "F11",
                            "F13", "F14", "F15", "F17", "F18", "F19", "F21", "F22",
                            "F23",
                            "G1", "G2", "G3", "G5", "G6", "G7", "G9", "G10", "G11",
                            "G13", "G14", "G15", "G17", "G18", "G19",
                            "H1", "H2", "H4", "H5", "H7", "H8", "H10", "H11", "H13",
                            "H14", "H16",
                            "I1", "I2", "I4", "I5", "I7", "I8", "I10", "I11",
                            "I13", "I14", "I16",
                            "J1", "J2", "J4", "J5", "J7", "J8", "J10",
                            "J11", "J13", "J14", "J16")

    for i in range(len(urls)):

        url = urls[i]

        headers = {"Authorization": "Bearer " + key, "User-Agent": "https://github.com/etam4260/hudpy"}
        call = urllib3.http.request("GET", url, headers = headers, timeout = 30)

        cont = json.loads(call.data.decode('utf-8'))    
        cont = pd.json_normalize(cont) 

        huddownloadbar.download_bar(i, len(urls))

        if "error" in cont.columns or len(cont) == 0:
            # Need to output a single error message instead of a bunch when
            # something bad occurs. Append to list of errored urls.
            error_urls = error_urls.append(url)
        else:
            not_measured = all_measurements[all_measurements not in cont[1].columns]
            # Check this CHAS data does not have data defined for
            # all expected fields. If so fill them in with NA's.
        if len(not_measured) >= 1:
            extra_mes = pd.repeat(None, len(not_measured))
            extra_mes.names = not_measured

            list_res[[i]] <- c(unlist(cont[[1]]), extra_mes)
        else:
            list_res[[i]] <- unlist(cont[[1]])
        
    print("\n")

def cw_do_query_calls() -> pd.DataFrame:
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

    if(not hudinternetonline.internet_on()): raise ConnectionError("You currently do not have internet access.")


def misc_do_query_calls() -> pd.DataFrame:
    """
    #' @name misc_do_query_call
    #' @title misc_do_query_call
    #' @description Make queries calls given a list of urlss
    #' @param urls The urlss to query for.
    #' @param key The API key for this user. You must go to HUD and sign up for
    #'   an account and request for an API key.
    #' @returns A dataframe containing all queried rows.
    """    
    
    if(not hudinternetonline.internet_on()): raise ConnectionError("You currently do not have internet access.")
