from __future__ import annotations
from typing import Union

import os
from datetime import date, timedelta
import pandas as pd

from hudpy import hud_input_check
from hudpy import hud_cw

def crosswalk(data: pd.DataFrame,
              geoid: str,
              geoid_col: Union[int, str, list[int], list[str], tuple[int], tuple[str]],
              cw_geoid: str,
              cw_geoid_col: Union[int, str, list[int], list[str], tuple[int], tuple[str]] = None, 
              method: Union[str, None] = None,
              year: Union[int, str, list[int], list[str], tuple[int], tuple[str]] = (date.today() - timedelta(days = 365)).strftime("%Y"),
              quarter: Union[int, str, list[int], list[str], tuple[int], tuple[str]] = 1,
              key: str = None) -> pd.DataFrame:
    """
    Function to crosswalk a dataframe using the US Department of Housing and Urban Development 
    crosswalk files. This function assumes data is well formed. For just obtaining the 
    datasets used for crosswalking look at the hud_cw family of functions within this package.

    Parameters
    ----------
    data : A dataset with rows describing measurements at a zip,
        county, county subdivision (countysub), congressional district (cd),
        census tract, core base statistical area (cbsa), or core based
        statistical area division (cbsadiv) geoid.
        1) zip
        2) tract
        3) county
        4) countysub
        5) cbsa
        6) cbsadiv
        7) cd

    geoid : The current geoid that the dataset is described in: must be
        zip, county, countysub, cd,
        tract, cbsa, or cbsadiv geographic id.
        1) zip
        2) tract
        3) county
        4) countysub
        5) cbsa
        6) cbsadiv
        7) cd

    geoid_col : The column containing the geographic identifier; must be
        zip, county, county subdivision (countysub), congressional district (cd),
        census tract, core base statistical area (cbsa), and core based
        statistical area division (cbsadiv) geoid.
        Supply either the name of the column or the index.
        All elements in this column must be numbers only at the proper length.
        For example, zip codes must be 5 digit numbers.

    cw_geoid :  The geoid to crosswalk the dataset to; must be
        zip, county, county subdivision (countysub), congressional district (cd),
        census tract, core base statistical area (cbsa), or core based
        statistical area division (cbsadiv) geoid.
        1) zip
        2) tract
        3) county
        4) countysub
        5) cbsa
        6) cbsadiv
        7) cd

    method : The allocation method to use: residential,
        business, other, or total. If method is empty, no allocation
        method will be applied -- the crosswalk file will just be merged
        to the dataset.
        1) res
        2) bus
        3) tot
        4) oth

    year : The year to query for

    quarter : The quarter of year(s) to query for.

    key : The key obtain from HUD USER website.

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
    --------
    A dataframe with the crosswalked geoids if method or cw_geoid_col are set to None, else a 
    dataframe containing the crosswalk geoids and cw_geoid_cols allocated based on method ratio.

    Examples
    --------
    
    >>> sample = data.frame(population = c(42134, 12413, 13132),
                          county = c(24047, 24045, 24043))
    
    >>> crosswalk(data = sample, geoid = "county", geoid_col = "county",
               cw_geoid = "zip")
    
    >>> crosswalk(data = sample, geoid = "county", geoid_col = "county",
               cw_geoid = "zip", cw_geoid_col = "population", method = "res")
    
    >>> crosswalk(data = sample, geoid = "county", geoid_col = "county",
               cw_geoid = "zip", cw_geoid_col = "population", method = "bus")
    
    >>> crosswalk(data = sample, geoid = "county", geoid_col = "county",
               cw_geoid = "zip", cw_geoid_col = "population", method = "bus",
               year = 2018, quarter = 1)

    """
    
    if(key == None and os.getenv("HUD_KEY") != None):
        key = os.getenv("HUD_KEY")
        
        
    args = hud_input_check.crosswalk_a_dataset_input_check_cleansing(data = data, geoid = geoid, geoid_col = geoid_col,
                                            cw_geoid = cw_geoid, cw_geoid_col = cw_geoid_col, method = method,
                                            year = year,
                                            quarter = quarter, key = key)

    geoid = args[0]
    geoid_col = args[1]
    
    cw_geoid = args[2]
    cw_geoid_col = args[3]

    method = args[4]
    
    year = args[5]
    quarter = args[6]
    
    key = args[7]

   
    if geoid == "zip" and cw_geoid in ["county", "countysub", "tract",
                                       "cbsa", "cbsadiv", "cd"]:
        if cw_geoid == "county":
            cw_data = hud_cw.hud_cw_zip_county(list(data[geoid_col]), year = year,
                                        quarter = quarter, key = key)
        elif cw_geoid == "countysub":
            cw_data = hud_cw.hud_cw_zip_countysub(list(data[geoid_col]), year = year,
                                            quarter = quarter, key = key)
        elif cw_geoid == "cd":
            cw_data = hud_cw.hud_cw_zip_cd(list(data[geoid_col]), year = year,
                                    quarter = quarter, key = key)
        elif cw_geoid == "tract":
            cw_data = hud_cw.hud_cw_zip_tract(list(data[geoid_col]), year = year,
                                        quarter = quarter, key = key)
        elif cw_geoid == "cbsa":
            cw_data = hud_cw.hud_cw_zip_cbsa(list(data[geoid_col]), year = year,
                                        quarter = quarter, key = key)
        elif cw_geoid == "cbsadiv":
            cw_data = hud_cw.hud_cw_zip_cbsadiv(list(data[geoid_col]), year = year,
                                            quarter = quarter, key = key)

    elif geoid == "county" and cw_geoid == "zip":
        cw_data = hud_cw.hud_cw_county_zip(list(data[geoid_col]), year = year,
                                        quarter = quarter, key = key)
    elif geoid == "countysub" and cw_geoid == "zip":
        cw_data = hud_cw.hud_cw_countysub_zip(list(data[geoid_col]), year = year,
                                        quarter = quarter, key = key)
    elif geoid == "cd" and cw_geoid == "zip":
        cw_data = hud_cw.hud_cw_cd_zip(list(data[geoid_col]), year = year,
                                quarter = quarter, key = key)
    elif geoid == "tract" and cw_geoid == "zip":
        cw_data = hud_cw.hud_cw_tract_zip(list(data[geoid_col]), year = year,
                                    quarter = quarter, key = key)
    elif geoid == "cbsa" and cw_geoid == "zip":
        cw_data = hud_cw.hud_cw_cbsa_zip(list(data[geoid_col]), year = year,
                                quarter = quarter, key = key)
    elif geoid == "cbsadiv" and cw_geoid == "zip":
        cw_data = hud_cw.hud_cw_cbsadiv_zip(list(data[geoid_col]), year = year,
                                    quarter = quarter, key = key)
    else:
        raise ValueError("\nCrosswalk from {} to {} is not supported.".format(geoid, cw_geoid))



    # If no columns are provides, assume just want to merge...
    # If no method is provided, assume merge and crosswalk
    
    if cw_geoid_col == None or method == None:
        
        print("\n* No method or cw_geoid_col specified: will just merge the datasets.")
        
        cw_data[geoid] = cw_data[geoid].astype(str)
        data[geoid_col] = data[geoid_col].astype(str)

        return(pd.merge(cw_data, data, left_on = geoid, right_on = geoid_col))

    elif cw_geoid_col != None and method != None:
        
        cw_data[geoid] = cw_data[geoid].astype(str)
        data[geoid_col] = data[geoid_col].astype(str)
        
        merged = pd.merge(cw_data, data, left_on = geoid, right_on = geoid_col)

        # clear memory
        cw_data = None
        data = None

        # apply method to columns specified.
        if method == "residential" or method == "res" or method == "res_ratio":
            print("\n* Applying allocation method based on residential address percentage.")
        
            for i in range((merged.shape[0])): 
                merged.loc[i, cw_geoid_col] = merged.loc[i, cw_geoid_col].multiply(merged.loc[i, "res_ratio"], axis = "index")

        elif method == "business" or method == "bus" or method == "bus_ratio":
            print("\n* Applying allocation method based on business address percentage.")
            
            for i in range((merged.shape[0])): 
                merged.loc[i, cw_geoid_col] = merged.loc[i, cw_geoid_col].multiply(merged.loc[i, "bus_ratio"], axis = "index")

        elif method == "other" or method == "oth" or method == "oth_ratio":
            print("\n* Applying allocation method based on other address percentage.")
            
            for i in range((merged.shape[0])): 
                merged.loc[i, cw_geoid_col] = merged.loc[i, cw_geoid_col].multiply(merged.loc[i, "oth_ratio"], axis = "index")

        elif method == "total" or method == "tot" or method == "tot_ratio":
            print("\n* Applying allocation method based on total address percentage.")
            
            for i in range((merged.shape[0])): 
                merged.loc[i, cw_geoid_col] = merged.loc[i, cw_geoid_col].multiply(merged.loc[i, "tot_ratio"], axis = "index")

        else:
            print("\nThe method or columns selected might be invalid. Check the documentation.")

        return(merged)
    return(None)