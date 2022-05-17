import hudinputcheck
import hudcw
import os
from typing import Union
from datetime import date
import pandas as pd


def crosswalk(data: pd.DataFrame,
              geoid: str,
              geoid_col: Union[int, str, list:int, list:str, None],
              cw_geoid: str,
              cw_geoid_col: Union[int, str, list:int, list:str, None] = None, 
              method: Union[str, None] = None,
              year: Union[int, str, list: int, list: str, tuple: Union[int, str]] = (date.today() - 365).strftime("%Y"),
              quarter: Union[int, str, list:, list: str, tuple: Union[int, str]] = 1,
              key: str = os.getenv("HUD_KEY")) -> pd.DataFrame:
    """
    #' @name crosswalk
    #' @title crosswalk
    #' @description Using the US Housing and Urban Development crosswalk files,
    #'  crosswalk an entire dataset.
    #'  Currently supported crosswalks:
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
    #' @param data A dataset with rows describing measurements at a zip,
    #'   county, county subdivision (countysub), congressional district (cd),
    #'   census tract, core base statistical area (cbsa), or core based
    #'   statistical area division (cbsadiv) geoid.
    #'   1) zip
    #'   2) tract
    #'   3) county
    #'   4) countysub
    #'   5) cbsa
    #'   6) cbsadiv
    #'   7) cd
    #' @param geoid The current geoid that the dataset is described in: must be
    #'   zip, county, countysub, cd,
    #'   tract, cbsa, or cbsadiv geographic id.
    #'   1) zip
    #'   2) tract
    #'   3) county
    #'   4) countysub
    #'   5) cbsa
    #'   6) cbsadiv
    #'   7) cd
    #' @param geoid_col The column containing the geographic identifier; must be
    #'   zip, county, county subdivision (countysub), congressional district (cd),
    #'   census tract, core base statistical area (cbsa), and core based
    #'   statistical area division (cbsadiv) geoid.
    #'   Supply either the name of the column or the index.
    #'   All elements in this column must be numbers only at the proper length.
    #'   For example, zip codes must be 5 digit numbers.
    #' @param cw_geoid The geoid to crosswalk the dataset to; must be
    #'   zip, county, county subdivision (countysub), congressional district (cd),
    #'   census tract, core base statistical area (cbsa), or core based
    #'   statistical area division (cbsadiv) geoid.
    #'   1) zip
    #'   2) tract
    #'   3) county
    #'   4) countysub
    #'   5) cbsa
    #'   6) cbsadiv
    #'   7) cd
    #' @param cw_geoid_col The columns in the dataset to distribute
    #'   according to method ratio.
    #'   If method is empty, no allocation method will be applied --
    #'   the crosswalk file will just be merged to the dataset.
    #'   All elements in these columns must be numbers only.
    #' @param method The allocation method to use: residential,
    #'   business, other, or total. If method is empty, no allocation
    #'   method will be applied -- the crosswalk file will just be merged
    #'   to the dataset.
    #'   1) res
    #'   2) bus
    #'   3) tot
    #'   4) oth
    #' @param year The year measurement was taken.
    #' @param quarter The quarter of year measurement was taken.
    #' @param key The key obtain from HUD USER website.
    #' @returns A dataframe containing the crosswalked dataset.
    """

    args = hudinputcheck.crosswalk_a_dataset_input_check_cleansing(data, geoid, geoid_col,
                                            cw_geoid, cw_geoid_col, method,
                                            year,
                                            quarter, key)

    geoid = args[1]
    geoid_col = args[2]
    cw_geoid = args[3]

    cw_geoid_col = args[4]

    method = args[5]
    year = args[6]
    quarter = args[7]
    key = args[8]


    if geoid == "zip" and cw_geoid in list("county", "countysub", "tract",
                                       "cbsa", "cbsadiv", "cd"):
        if cw_geoid == "county":
            cw_data = hudcw.hud_cw_zip_county(data[geoid_col], year = year,
                                        quarter = quarter, key = key)
        elif cw_geoid == "countysub":
            cw_data = hudcw.hud_cw_zip_countysub(data[geoid_col], year = year,
                                            quarter = quarter, key = key)
        elif cw_geoid == "cd":
            cw_data = hudcw.hud_cw_zip_cd(data[geoid_col], year = year,
                                    quarter = quarter, key = key)
        elif cw_geoid == "tract":
            cw_data = hudcw.hud_cw_zip_tract(data[geoid_col], year = year,
                                        quarter = quarter, key = key)
        elif cw_geoid == "cbsa":
            cw_data = hudcw.hud_cw_zip_cbsa(data[geoid_col], year = year,
                                        quarter = quarter, key = key)
        elif cw_geoid == "cbsadiv":
            cw_data = hudcw.hud_cw_zip_cbsadiv(data[geoid_col], year = year,
                                            quarter = quarter, key = key)

    elif geoid == "county" and cw_geoid == "zip":
        cw_data = hudcw.hud_cw_county_zip(data[geoid_col], year = year,
                                        quarter = quarter, key = key)
    elif geoid == "countysub" and cw_geoid == "zip":
        cw_data = hudcw.hud_cw_countysub_zip(data[geoid_col], year = year,
                                        quarter = quarter, key = key)
    elif geoid == "cd" and cw_geoid == "zip":
        cw_data = hudcw.hud_cw_cd_zip(data[geoid_col], year = year,
                                quarter = quarter, key = key)
    elif geoid == "tract" and cw_geoid == "zip":
        cw_data = hudcw.hud_cw_tract_zip(data[geoid_col], year = year,
                                    quarter = quarter, key = key)
    elif geoid == "cbsa" and cw_geoid == "zip":
        cw_data = hudcw.hud_cw_cbsa_zip(data[geoid_col], year = year,
                                quarter = quarter, key = key)
    elif geoid == "cbsadiv" and cw_geoid == "zip":
        cw_data = hudcw.hud_cw_cbsadiv_zip(data[geoid_col], year = year,
                                    quarter = quarter, key = key)
    else:
        raise ValueError("\nCrosswalk from {} to {} is not supported.".format(geoid, cw_geoid))



    # If no columns are provides, assume just want to merge...
    # If no method is provided, assume merge and crosswalk
    if cw_geoid_col == None or method == None:
        
        print("\n* No method or cw_geoid_col specified: will just merge the datasets.")
     
        return(pd.merge(cw_data, data, left_on = 6, right_on = geoid_col))

    elif cw_geoid_col != None and method != None:

        merged = pd.merge(cw_data, data, left_on = 6, right_one = geoid_col)

        # clear memory
        cw_data = None
        data = None

        # apply method to columns specified.
        if method == "residential" or method == "res" or method == "res_ratio":
            print("\n* Applying allocation method based on residential address percentage.")

            for i in range((merged.shape[0])): 
                merged[i, cw_geoid_col] <- float(merged[i, cw_geoid_col]) * float(merged[i, "res_ratio"])

        elif method == "business" or method == "bus" or method == "bus_ratio":
            print("\n* Applying allocation method based on business address percentage.")
            
            for i in range((merged.shape[0])): 
                merged[i, cw_geoid_col] <- float(merged[i, cw_geoid_col]) * float(merged[i, "bus_ratio"])

        elif method == "other" or method == "oth" or method == "oth_ratio":
            print("\n* Applying allocation method based on other address percentage.")
            
            for i in range((merged.shape[0])): 
                merged[i, cw_geoid_col] <- float(merged[i, cw_geoid_col]) * float(merged[i, "oth_ratio"])
            
        elif method == "total" or method == "tot" or method == "tot_ratio":
            print("\n* Applying allocation method based on total address percentage.")
            
            for i in range((merged.shape[0])): 
                merged[i, cw_geoid_col] <- float(merged[i, cw_geoid_col]) * float(merged[i, "tot_ratio"])

        else:
            print("\nThe method or columns selected might be invalid. Check the documentation.")
            return(merged)

    return(None)