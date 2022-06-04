from __future__ import annotations
from typing import Union

from datetime import date, timedelta

from hudpy import hud_get_recent_data 
from hudpy import hud_cw

def z_in_trt(zip : Union[int, str, list[int], list[str], tuple[int], tuple[str]],
             tract : Union[int, str, list[int], list[str], tuple[int], tuple[str]],
             year : None,
             quarter : None) -> bool:
    """
    Given a zip code and a tract, determine if they overlap
    using the crosswalk files. Overlap will be described if
    any residential, business, other, or total addresses reside in both.
    
    Parameters
    ----------
    
    zip : The zip to determine overlap with tract
    tract : The tract to determine overlap with zip
    year : The year of the crosswalk files.
    quarter : The quarter of the crosswalk files.

    See Also
    --------

     * z_in_trt()
     * z_in_cty()
     * z_in_cbsa()
     * z_in_cbsadiv()
     * z_in_ctysb()
     * z_in_cd()
     * trt_in_z()
     * cty_in_z()
     * cbsa_in_z()
     * cbsadiv_in_z()
     * cd_in_z()
     * ctysb_in_z()

    Returns 
    -------

    If zip(s) exist in the tract(s) specified, then True is returned.
     
    Examples
    --------
    
    >>> z_in_trt(zip = 71052, tract = 22031950600, year = 2019, quarter = 2)
    
    """

    if year == None or quarter == None: 
        args = hud_get_recent_data.hud_rec_cw_yr()
        
        if year == None:
            year = args[1]
        

        if quarter == None:
            quarter = args[2]
    

    args = hud_get_recent_data.hud_rec_cw_yr()

    # TODO: We might want to allow using names also..
    # There is a bit of overhead cost for doing individual queries because each
    # zip will need individual calls to hud_cw_zip_tract... Could optimize by
    # using internal functions...

    # Need to validate tract..
    tract = geo_is_infix_rhs_cleansing(query = tract,  geoid_type = "tract")

    res = []

    for i in range(len(zip)): 

        queried = geo_is_infix_query_and_get_warnings(query = zip[i],
                                                      f = hud_cw.hud_cw_zip_tract,
                                                      year = year,
                                                      quarter = quarter,
                                                      querytype = "zip")

        if any(queried in tract):
            res.append(True)
        else:
            res.append(False)

    return(res)
    



def z_in_cty(zip : Union[int, str, list[int], list[str], tuple[int], tuple[str]],
             county : Union[int, str, list[int], list[str], tuple[int], tuple[str]],
             year : None,
             quarter : None) -> bool:
    """
    Given a zip code and a county, determine if they overlap
    using the crosswalk files. Overlap will be described if
    any residential, business, other, or total addresses reside in both.
   
    Parameters
    ----------

    zip : The zip to determine overlap with county
    county : The county to determine overlap with zip
    year : The year of the crosswalk files.
    quarter : The quarter of the crosswalk files.

    See Also
    --------
    * z_in_trt()
    * z_in_cty()
    * z_in_cbsa()
    * z_in_cbsadiv()
    * z_in_ctysb()
    * z_in_cd()
    * trt_in_z()
    * cty_in_z()
    * cbsa_in_z()
    * cbsadiv_in_z()
    * cd_in_z()
    * ctysb_in_z()

    Returns 
    -------

    If zip(s) exist in the county(s) specified, then True is returned.
     

    Examples
    --------

    >>> z_in_cty(zip = 71052, county = 22031, year = 2019, quarter = 2)

    """

    if year == None or quarter == None: 
        args = hud_get_recent_data.hud_rec_cw_yr()
        
        if year == None:
            year = args[1]
        

        if quarter == None:
            quarter = args[2]
    

    args = hud_get_recent_data.hud_rec_cw_yr()

    county = geo_is_infix_rhs_cleansing(query = county,  geoid_type = "county")

    res = []

    for i in range(len(zip)): 

        queried = geo_is_infix_query_and_get_warnings(query = zip[i],
                                                      f = hud_cw.hud_cw_zip_county,
                                                      year = year,
                                                      quarter = quarter,
                                                      querytype = "zip")

        if any(queried in county):
            res.append(True)
        else:
            res.append(False)

    return(res)



def z_in_cbsa(zip : Union[int, str, list[int], list[str], tuple[int], tuple[str]],
              cbsa : Union[int, str, list[int], list[str], tuple[int], tuple[str]],
              year : None,
              quarter : None) -> bool:
    """
    Given a zip code and a cbsa, determine if they overlap
    using the crosswalk files. Overlap will be described if
    any residential, business, other, or total addresses reside in both.

    Parameters
    ----------

    zip : The zip to determine overlap with cbsa
    cbsa : The cbsa to determine overlap with zip
    year : The year of the crosswalk files.
    quarter : The quarter of the crosswalk files.
    
    See Also
    --------

    * z_in_trt()
    * z_in_cty()
    * z_in_cbsa()
    * z_in_cbsadiv()
    * z_in_ctysb()
    * z_in_cd()
    * trt_in_z()
    * cty_in_z()
    * cbsa_in_z()
    * cbsadiv_in_z()
    * cd_in_z()
    * ctysb_in_z()

    Returns 
    -------

    If zip(s) exist in the cbsa(s) specified, then True is returned.
     

    Examples
    --------

    >>> z_in_cbsa(zip = 71052, cbsa = 43340, year = 2019, quarter = 2)

    """


    if year == None or quarter == None: 
        args = hud_get_recent_data.hud_rec_cw_yr()
        
        if year == None:
            year = args[1]
        

        if quarter == None:
            quarter = args[2]
    

    args = hud_get_recent_data.hud_rec_cw_yr()

    cbsa = geo_is_infix_rhs_cleansing(query = cbsa,  geoid_type = "cbsa")

    res = []

    for i in range(len(zip)): 

        queried = geo_is_infix_query_and_get_warnings(query = zip[i],
                                                      f = hud_cw.hud_cw_zip_cbsa,
                                                      year = year,
                                                      quarter = quarter,
                                                      querytype = "zip")

        if any(queried in cbsa):
            res.append(True)
        else:
            res.append(False)

    return(res)



def z_in_cbsadiv(zip : Union[int, str, list[int], list[str], tuple[int], tuple[str]],
                 cbsadiv : Union[int, str, list[int], list[str], tuple[int], tuple[str]],
                 year : None,
                 quarter : None) -> bool :
    """
    Given a zip code and a cbsadiv, determine if they overlap
    using the crosswalk files. Overlap will be described if
    any residential, business, other, or total addresses reside in both.

    Parameters
    ----------

    zip : The zip to determine overlap with cbsadiv
    cbsadiv : The cbsadiv to determine overlap with zip
    year : The year of the crosswalk files.
    quarter : The quarter of the crosswalk files.
    
    See Also
    --------

    * z_in_trt()
    * z_in_cty()
    * z_in_cbsa()
    * z_in_cbsadiv()
    * z_in_ctysb()
    * z_in_cd()
    * trt_in_z()
    * cty_in_z()
    * cbsa_in_z()
    * cbsadiv_in_z()
    * cd_in_z()
    * ctysb_in_z()

    Returns 
    -------

    If zip(s) exist in the cbsadiv(s) specified, then True is returned.


    Examples
    --------
    
    >>> z_in_cbsadiv(zip = 71052, cbsadiv = 43340, year = 2019, quarter = 2)

    """


    if year == None or quarter == None: 
        args = hud_get_recent_data.hud_rec_cw_yr()
        
        if year == None:
            year = args[1]
        

        if quarter == None:
            quarter = args[2]
    

    args = hud_get_recent_data.hud_rec_cw_yr()

    cbsadiv = geo_is_infix_rhs_cleansing(query = cbsadiv,  geoid_type = "cbsadiv")

    res = []

    for i in range(len(zip)): 

        queried = geo_is_infix_query_and_get_warnings(query = zip[i],
                                                      f = hud_cw.hud_cw_zip_cbsadiv,
                                                      year = year,
                                                      quarter = quarter,
                                                      querytype = "zip")

        if any(queried in cbsadiv):
            res.append(True)
        else:
            res.append(False)

    return(res)



def z_in_ctysb(zip : Union[int, str, list[int], list[str], tuple[int], tuple[str]],
               countysub : Union[int, str, list[int], list[str], tuple[int], tuple[str]],
               year : None,
               quarter : None) -> bool:

    """
    Given a zip code and a countysub, determine if they overlap
    using the crosswalk files. Overlap will be described if
    any residential, business, other, or total addresses reside in both.

    Parameters
    ----------

    zip : The zip to determine overlap with countysub
    countysub : The countysub to determine overlap with zip
    year : The year of the crosswalk files.
    quarter : The quarter of the crosswalk files.
    
    See Also
    --------

    * z_in_trt()
    * z_in_cty()
    * z_in_cbsa()
    * z_in_cbsadiv()
    * z_in_ctysb()
    * z_in_cd()
    * trt_in_z()
    * cty_in_z()
    * cbsa_in_z()
    * cbsadiv_in_z()
    * cd_in_z()
    * ctysb_in_z()

    Returns 
    -------

    If zip(s) exist in the countysub(s) specified, then True is returned.
     

    Examples
    --------
    
    >>> z_in_ctysb(zip = 71052, countysub = 43340, year = 2019, quarter = 2)
    """
  
    if year == None or quarter == None: 
        args = hud_get_recent_data.hud_rec_cw_yr()
        
        if year == None:
            year = args[1]
        

        if quarter == None:
            quarter = args[2]
    

    args = hud_get_recent_data.hud_rec_cw_yr()

    countysub = geo_is_infix_rhs_cleansing(query = countysub,  geoid_type = "countysub")

    res = []

    for i in range(len(zip)): 

        queried = geo_is_infix_query_and_get_warnings(query = zip[i],
                                                      f = hud_cw.hud_cw_zip_countysub,
                                                      year = year,
                                                      quarter = quarter,
                                                      querytype = "zip")

        if any(queried in countysub):
            res.append(True)
        else:
            res.append(False)

    return(res)


def z_in_cd(zip : Union[int, str, list[int], list[str], tuple[int], tuple[str]],
            cd : Union[int, str, list[int], list[str], tuple[int], tuple[str]],
            year : None,
            quarter : None) -> bool:

    """
    Given a zip code and a congressional district, determine if they overlap
    using the crosswalk files. Overlap will be described if
    any residential, business, other, or total addresses reside in both.

    Parameters
    ----------

    zip : The zip to determine overlap with congressional district
    cd : The congressional district to determine overlap with zip
    year : The year of the crosswalk files.
    quarter : The quarter of the crosswalk files.
    
    See Also
    --------

    * z_in_trt()
    * z_in_cty()
    * z_in_cbsa()
    * z_in_cbsadiv()
    * z_in_ctysb()
    * z_in_cd()
    * trt_in_z()
    * cty_in_z()
    * cbsa_in_z()
    * cbsadiv_in_z()
    * cd_in_z()
    * ctysb_in_z()

    Returns 
    -------

    If zip(s) exist in the cd(s) specified, then True is returned.
     
    Examples
    --------
    
    >>> z_in_cd(zip = 71052, cd = 43340, year = 2019, quarter = 2)
    """

  
    if year == None or quarter == None: 
        args = hud_get_recent_data.hud_rec_cw_yr()
        
        if year == None:
            year = args[1]
        

        if quarter == None:
            quarter = args[2]
    

    args = hud_get_recent_data.hud_rec_cw_yr()

    cd = geo_is_infix_rhs_cleansing(query = cd,  geoid_type = "cd")

    res = []

    for i in range(len(zip)): 

        queried = geo_is_infix_query_and_get_warnings(query = zip[i],
                                                      f = hud_cw.hud_cw_zip_cd,
                                                      year = year,
                                                      quarter = quarter,
                                                      querytype = "zip")

        if any(queried in cd):
            res.append(True)
        else:
            res.append(False)

    return(res)








def trt_in_z(tract : Union[int, str, list[int], list[str], tuple[int], tuple[str]],
             zip : Union[int, str, list[int], list[str], tuple[int], tuple[str]],
             year : None,
             quarter : None) -> bool:
    """
    Given a tract and a zip code, determine if they overlap
    using the crosswalk files. Overlap will be described if
    any residential, business, other, or total addresses reside in both.

    Parameters
    ----------

    tract : The tract to determine overlap with zip
    zip : The zip to determine overlap with tract
    year : The year of the crosswalk files.
    quarter : The quarter of the crosswalk files.
    
    See Also
    --------

    * z_in_trt()
    * z_in_cty()
    * z_in_cbsa()
    * z_in_cbsadiv()
    * z_in_ctysb()
    * z_in_cd()
    * trt_in_z()
    * cty_in_z()
    * cbsa_in_z()
    * cbsadiv_in_z()
    * cd_in_z()
    * ctysb_in_z()

    Returns 
    -------

    If tract(s) exist in the zip(s) specified, then True is returned.
     

    Examples
    --------
    
    >>> trt_in_z(tract = 43340, zip = 71052, year = 2019, quarter = 2)
    """


    if year == None or quarter == None: 
        args = hud_get_recent_data.hud_rec_cw_yr()
        
        if year == None:
            year = args[1]
        

        if quarter == None:
            quarter = args[2]
    

    args = hud_get_recent_data.hud_rec_cw_yr()

    zip = geo_is_infix_rhs_cleansing(query = zip,  geoid_type = "zip")

    res = []

    for i in range(len(tract)): 

        queried = geo_is_infix_query_and_get_warnings(query = tract[i],
                                                      f = hud_cw.hud_cw_tract_zip,
                                                      year = year,
                                                      quarter = quarter,
                                                      querytype = "tract")

        if any(queried in tract):
            res.append(True)
        else:
            res.append(False)

    return(res)



def cty_in_z(county : Union[int, str, list[int], list[str], tuple[int], tuple[str]],
             zip : Union[int, str, list[int], list[str], tuple[int], tuple[str]],
             year : None,
             quarter : None) -> bool:
    """
    Given a county and a zip code, determine if they overlap
    using the crosswalk files. Overlap will be described if
    any residential, business, other, or total addresses reside in both.

    Parameters
    ----------

    county : The county to determine overlap with zip
    zip : The zip to determine overlap with county
    year : The year of the crosswalk files.
    quarter : The quarter of the crosswalk files.
    
    See Also
    --------

    * z_in_trt()
    * z_in_cty()
    * z_in_cbsa()
    * z_in_cbsadiv()
    * z_in_ctysb()
    * z_in_cd()
    * trt_in_z()
    * cty_in_z()
    * cbsa_in_z()
    * cbsadiv_in_z()
    * cd_in_z()
    * ctysb_in_z()

    Returns 
    -------

    If county(s) exist in the zip(s) specified, then True is returned.
     

    Examples
    --------
    
    >>> cty_in_z(county = 43340, zip = 71052, year = 2019, quarter = 2)
    """


    if year == None or quarter == None: 
        args = hud_get_recent_data.hud_rec_cw_yr()
        
        if year == None:
            year = args[1]
        

        if quarter == None:
            quarter = args[2]
    

    args = hud_get_recent_data.hud_rec_cw_yr()

    zip = geo_is_infix_rhs_cleansing(query = zip,  geoid_type = "zip")

    res = []

    for i in range(len(county)): 

        queried = geo_is_infix_query_and_get_warnings(query = county[i],
                                                      f = hud_cw.hud_cw_county_zip,
                                                      year = year,
                                                      quarter = quarter,
                                                      querytype = "county")

        if any(queried in county):
            res.append(True)
        else:
            res.append(False)

    return(res)




def cbsa_in_z(cbsa : Union[int, str, list[int], list[str], tuple[int], tuple[str]],
              zip : Union[int, str, list[int], list[str], tuple[int], tuple[str]],
              year : None,
              quarter : None) -> bool:

    """
    Given a cbsa and a zip code, determine if they overlap
    using the crosswalk files. Overlap will be described if
    any residential, business, other, or total addresses reside in both.

    Parameters
    ----------

    cbsa : The cbsa to determine overlap with zip
    zip : The zip to determine overlap with cbsa
    year : The year of the crosswalk files.
    quarter : The quarter of the crosswalk files.
    
    See Also
    --------

    * z_in_trt()
    * z_in_cty()
    * z_in_cbsa()
    * z_in_cbsadiv()
    * z_in_ctysb()
    * z_in_cd()
    * trt_in_z()
    * cty_in_z()
    * cbsa_in_z()
    * cbsadiv_in_z()
    * cd_in_z()
    * ctysb_in_z()

    Returns 
    -------

    If cbsa(s) exist in the zip(s) specified, then True is returned.
     

    Examples
    --------
    
    >>> cbsa_in_z(cbsa = 43340, zip = 71052, year = 2019, quarter = 2)
    """


    if year == None or quarter == None: 
        args = hud_get_recent_data.hud_rec_cw_yr()
        
        if year == None:
            year = args[1]
        

        if quarter == None:
            quarter = args[2]
    

    args = hud_get_recent_data.hud_rec_cw_yr()

    zip = geo_is_infix_rhs_cleansing(query = zip,  geoid_type = "zip")

    res = []

    for i in range(len(cbsa)): 

        queried = geo_is_infix_query_and_get_warnings(query = cbsa[i],
                                                      f = hud_cw.hud_cw_cbsa_zip,
                                                      year = year,
                                                      quarter = quarter,
                                                      querytype = "cbsa")

        if any(queried in cbsa):
            res.append(True)
        else:
            res.append(False)

    return(res)



def cbsadiv_in_z(cbsadiv : Union[int, str, list[int], list[str], tuple[int], tuple[str]],
                 zip : Union[int, str, list[int], list[str], tuple[int], tuple[str]],
                 year : None,
                 quarter : None) -> bool:    

    """
    Given a cbsadiv and a zip code, determine if they overlap
    using the crosswalk files. Overlap will be described if
    any residential, business, other, or total addresses reside in both.

    Parameters
    ----------

    cbsadiv : The cbsadiv to determine overlap with zip
    zip : The zip to determine overlap with cbsadiv
    year : The year of the crosswalk files.
    quarter : The quarter of the crosswalk files.
    
    See Also
    --------

    * z_in_trt()
    * z_in_cty()
    * z_in_cbsa()
    * z_in_cbsadiv()
    * z_in_ctysb()
    * z_in_cd()
    * trt_in_z()
    * cty_in_z()
    * cbsa_in_z()
    * cbsadiv_in_z()
    * cd_in_z()
    * ctysb_in_z()

    Returns 
    -------

    If cbsadiv(s) exist in the zip(s) specified, then True is returned.
     

    Examples
    --------
    
    >>> cbsadiv_in_z(cbsadiv = 43340, zip = 71052, year = 2019, quarter = 2)
    """

    if year == None or quarter == None: 
        args = hud_get_recent_data.hud_rec_cw_yr()
        
        if year == None:
            year = args[1]
        

        if quarter == None:
            quarter = args[2]
    

    args = hud_get_recent_data.hud_rec_cw_yr()

    zip = geo_is_infix_rhs_cleansing(query = zip,  geoid_type = "zip")

    res = []

    for i in range(len(cbsadiv)): 

        queried = geo_is_infix_query_and_get_warnings(query = cbsadiv[i],
                                                      f = hud_cw.hud_cw_cbsadiv_zip,
                                                      year = year,
                                                      quarter = quarter,
                                                      querytype = "cbsadiv")

        if any(queried in cbsadiv):
            res.append(True)
        else:
            res.append(False)

    return(res)



def cd_in_z(cd : Union[int, str, list[int], list[str], tuple[int], tuple[str]],
            zip : Union[int, str, list[int], list[str], tuple[int], tuple[str]],
            year : None,
            quarter : None) -> bool:  
    """
    Given a congressional district and a zip code, determine if they overlap
    using the crosswalk files. Overlap will be described if
    any residential, business, other, or total addresses reside in both.

    Parameters
    ----------

    cd  The congressional district to determine overlap with zip
    zip : The zip to determine overlap with congressional district
    year : The year of the crosswalk files.
    quarter : The quarter of the crosswalk files.
    
    See Also
    --------

    * z_in_trt()
    * z_in_cty()
    * z_in_cbsa()
    * z_in_cbsadiv()
    * z_in_ctysb()
    * z_in_cd()
    * trt_in_z()
    * cty_in_z()
    * cbsa_in_z()
    * cbsadiv_in_z()
    * cd_in_z()
    * ctysb_in_z()

    Returns 
    -------

    If cd(s) exist in the zip(s) specified, then True is returned.
     

    Examples
    --------
    
    >>> cd_in_z(cd = 43340, zip = 71052, year = 2019, quarter = 2)
    """


    if year == None or quarter == None: 
        args = hud_get_recent_data.hud_rec_cw_yr()
        
        if year == None:
            year = args[1]
        

        if quarter == None:
            quarter = args[2]
    

    args = hud_get_recent_data.hud_rec_cw_yr()

    zip = geo_is_infix_rhs_cleansing(query = zip,  geoid_type = "zip")

    res = []

    for i in range(len(cd)): 

        queried = geo_is_infix_query_and_get_warnings(query = cd[i],
                                                      f = hud_cw.hud_cw_cd_zip,
                                                      year = year,
                                                      quarter = quarter,
                                                      querytype = "cd")

        if any(queried in cd):
            res.append(True)
        else:
            res.append(False)

    return(res)



 
def ctysb_in_z(countysub : Union[int, str, list[int], list[str], tuple[int], tuple[str]],
               zip : Union[int, str, list[int], list[str], tuple[int], tuple[str]],
               year : None,
               quarter : None) -> bool:  
    """
    Given a countysub and a zip code, determine if they overlap
    using the crosswalk files. Overlap will be described if
    any residential, business, other, or total addresses reside in both.

    Parameters
    ----------

    countysub : The countysub to determine overlap with zip
    zip : The zip to determine overlap with countysub
    year : The year of the crosswalk files.
    quarter : The quarter of the crosswalk files.
    
    See Also
    --------

    * z_in_trt()
    * z_in_cty()
    * z_in_cbsa()
    * z_in_cbsadiv()
    * z_in_ctysb()
    * z_in_cd()
    * trt_in_z()
    * cty_in_z()
    * cbsa_in_z()
    * cbsadiv_in_z()
    * cd_in_z()
    * ctysb_in_z()

    Returns 
    -------

    If countysub(s) exist in the zip(s) specified, then True is returned.
     

    Examples
    --------
    
    >>> ctysb_in_z(countysub = 43340, zip = 71052, year = 2019, quarter = 2)
    """


    if year == None or quarter == None: 
        args = hud_get_recent_data.hud_rec_cw_yr()
        
        if year == None:
            year = args[1]
        

        if quarter == None:
            quarter = args[2]
    

    args = hud_get_recent_data.hud_rec_cw_yr()

    zip = geo_is_infix_rhs_cleansing(query = zip,  geoid_type = "zip")

    res = []

    for i in range(len(countysub)): 

        queried = geo_is_infix_query_and_get_warnings(query = countysub[i],
                                                      f = hud_cw.hud_cw_countysub_zip,
                                                      year = year,
                                                      quarter = quarter,
                                                      querytype = "countysub")

        if any(queried in countysub):
            res.append(True)
        else:
            res.append(False)

    return(res)




def geo_is_infix_rhs_cleansing(query, geoid_type):
    """
    #' @name geo_is_infix_rhs_cleansing
    #' @title geo_is_infix_rhs_cleansing
    #' @description Given a geographic identifier, described by the
    #'   crosswalk files, determine whether it is the right length and has
    #'   correct spacing.
    #'  query The geoid to query for
    #'  geoid_type The type of geoid, either:
    #'    1) zip,
    #'    2) tract,
    #'    3) cd,
    #'    4) cbsa,
    #'    5) cbsadiv,
    #'    6) county,
    #'    7) countysub
    #' @noRd
    #' @noMd
    """
    query <- unique(paste(trimws(as.character(query), which = "both")))

    if (geoid_type == "zip") {
    if (FALSE %in% numbers_only(query)) stop("\nZip inputs must only be numbers.",
                                                call. = FALSE)
    if (any(nchar(query) != 5)) stop("\nZip inputs are not all of length 5.",
                                        call. = FALSE)
    } else if (geoid_type == "tract") {
    if (FALSE %in% numbers_only(query)) stop("\nTract inputs must only be numbers.",
                                                call. = FALSE)
    if (any(nchar(query) != 11)) stop("\nTract inputs are not all of length 11.",
                                        call. = FALSE)
    } else if (geoid_type == "county") {
    if (FALSE %in% numbers_only(query)) stop("\nCounty inputs must only be numbers.",
                                                call. = FALSE)
    if (any(nchar(query) != 5)) stop("\nCounty inputs are not all of length 5.",
                                        call. = FALSE)
    } else if (geoid_type == "cbsa") {
    if (FALSE %in% numbers_only(query)) stop("\nCbsa inputs must only be numbers.",
                                            call. = FALSE)
    if (any(nchar(query) != 5)) stop("\nCbsa inputs are not all of length 5.",
                                    call. = FALSE)
    } else if (geoid_type == "cbsadiv") {
    if (FALSE %in% numbers_only(query)) stop("\nCbsadiv inputs must only be numbers.",
                                                call. = FALSE)
    if (any(nchar(query) != 5)) stop("\nCbsadiv inputs are not all of length 5.",
                                        call. = FALSE)
    } else if (geoid_type == "cd") {
    if (FALSE %in% numbers_only(query)) stop("\nCd inputs must only be numbers.",
                                                call. = FALSE)
    if (any(nchar(query) != 4)) stop("\nCd inputs are not all of length 4.",
                                        call. = FALSE)
    } else if (geoid_type == "countysub") {
    if (FALSE %in% numbers_only(query)) stop("\nCountysub inputs must only be numbers.",
                                                call. = FALSE)
    if (any(nchar(query) != 10)) stop("\nCountysub inputs are not all of length 10.",
                                        call. = FALSE)
    }
    return(query)




def geo_is_infix_query_and_get_warnings(query,
                                        f,
                                        year,
                                        quarter,
                                        querytype):

    """
    #' @name geo_is_infix_query_and_get_warnings
    #' @title geo_is_infix_query_and_get_warnings
    #' @description Giving a geoid to query for, make sure to call the core
    #'   hud_cw() functions to get the crosswalk output
    #'   but intercept it to make custom warning messages.
    #'  query The geoids to query for crosswalk
    #'  f The function used query the crosswalk files.
    #'  year The year to query for.
    #'  quarter The quarter to query for.
    #'  querytype The geoid user is querying for.
    #'    1) zip
    #'    2) tract
    #'    3) cbsa
    #'    4) cd
    #'    5) cbsadiv
    #'    6) countsub
    #'    7) county
    #' @noRd
    #' @noMd
    """
  
  
    res <- c()
    tryCatch(
    {
        res <- suppressMessages(f(query,
                minimal = TRUE,
                year = year,
                quarter = quarter))
    },
    error = function(cond)
    {
        stop(cond$message, call. = FALSE)
    },
    warning = function(cond)
    {
        # Might be more efficient to save the errored geoids when used instead
        # of having to regex it...
        warning(paste("\nThe ", querytype, " ", query ," inputted is not valid.",
                    " No data was found for year: ", year , " and quarter: ", quarter,
                    sep = ""
                ), call. = FALSE)

    }
    )
    return(res)
    

