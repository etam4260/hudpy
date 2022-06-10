from __future__ import annotations
from typing import Union
import os
from datetime import date, timedelta

from hudpy import hud_get_recent_data 
from hudpy import hud_cw
from hudpy import hud_input_check
from hudpy import hud_pkg_env

from distutils.log import warn

def z_in_trt(zip : Union[int, str, list[int], list[str], tuple[int], tuple[str]],
             tract : Union[int, str, list[int], list[str], tuple[int], tuple[str]],
             year = None,
             quarter = None,
             key = None
             ) -> list:
    """
    Given zip code(s) and tract(s), determine if they overlap
    using the crosswalk files. Overlap will be described if
    any residential, business, other, or total addresses reside in both.
    
    Parameters
    ----------
    
    zip : The zip(s) to determine overlap with tract(s).

    tract : The tract(s) to determine overlap with zip(s).

    year : Gets the year that this data was recorded. Can specify multiple
        years. Default is the previous year.
    
    quarter : Gets the quarter of the year that this data was recorded.
        Defaults to the first quarter of the year.

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

    if(key == None and os.getenv("HUD_KEY") != None):
        key = os.getenv("HUD_KEY")

    if year == None or quarter == None: 
        
        if hud_pkg_env.pkg_env["rec_cw"] == None:
            args = hud_get_recent_data.hud_rec_cw_yr()
            hud_pkg_env.pkg_env["rec_cw"] = args

        # Store in pkg envrionment and retrieve when necessary
        if year == None:
            year =  hud_pkg_env.pkg_env["rec_cw"] ["year"]
        
        if quarter == None:
            quarter = hud_pkg_env.pkg_env["rec_cw"] ["quarter"]
    

    # TODO: We might want to allow using names also..
    # There is a bit of overhead cost for doing individual queries because each
    # zip will need individual calls to hud_cw_zip_tract... Could optimize by
    # using internal functions...

    # Need to validate tract..
    cleaned = hud_input_check.cw_input_check_cleansing( primary_geoid = "tract",
                                                        secondary_geoid = "zip",
                                                        query = tract, year = year,
                                                        quarter = quarter,
                                                        key = os.getenv("HUD_KEY"))


    tract = cleaned[0]
    year = cleaned[1]
    quarter = cleaned[2]
    key = cleaned[3]


    if any(list(map(lambda x: len(x) != 11, tract))):
         raise ValueError("Tract input is not all of length 11")


    res = []
    zip = [str(zip)] if isinstance(zip, str) or isinstance(zip, int) else list(map(lambda x: str(x), list(map(lambda x: str(x), zip))))
    
    for i in range(len(zip)): 

        queried = geo_is_infix_query_and_get_warnings(query = zip[i],
                                                      f = hud_cw.hud_cw_zip_tract,
                                                      year = year,
                                                      quarter = quarter,
                                                      querytype = "zip",
                                                      key = key
                                                      )

        if any(q in tract for q in queried):
            res.append(True)
        else:
            res.append(False)
    
    return(res)
    



def z_in_cty(zip : Union[int, str, list[int], list[str], tuple[int], tuple[str]],
             county : Union[int, str, list[int], list[str], tuple[int], tuple[str]],
             year = None,
             quarter = None,
             key = None
             ) -> bool:
    """
    Given zip code(s) and county(s), determine if they overlap
    using the crosswalk files. Overlap will be described if
    any residential, business, other, or total addresses reside in both.
   
    Parameters
    ----------

    zip : The zip(s) to determine overlap with county(s).

    county : The county(s). to determine overlap with zip(s).

    year : Gets the year that this data was recorded. Can specify multiple
        years. Default is the previous year.
    
    quarter : Gets the quarter of the year that this data was recorded.
        Defaults to the first quarter of the year.


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
    if(key == None and os.getenv("HUD_KEY") != None):
        key = os.getenv("HUD_KEY")

    if year == None or quarter == None: 
        
        if hud_pkg_env.pkg_env["rec_cw"] == None:
            args = hud_get_recent_data.hud_rec_cw_yr()
            hud_pkg_env.pkg_env["rec_cw"] = args

        # Store in pkg envrionment and retrieve when necessary
        if year == None:
            year =  hud_pkg_env.pkg_env["rec_cw"] ["year"]
        
        if quarter == None:
            quarter = hud_pkg_env.pkg_env["rec_cw"] ["quarter"]
    
    

    cleaned = hud_input_check.cw_input_check_cleansing( primary_geoid = "county",
                                                        secondary_geoid = "zip",
                                                        query = county, year = year,
                                                        quarter = quarter,
                                                        key = os.getenv("HUD_KEY"))


    county = cleaned[0]
    year = cleaned[1]
    quarter = cleaned[2]
    key = cleaned[3]

    
    if any(list(map(lambda x: len(x) != 5, county))):
         raise ValueError("County input is not all of length 5")

    res = []
    zip = [str(zip)] if isinstance(zip, str) or isinstance(zip, int) else list(map(lambda x: str(x), list(map(lambda x: str(x), zip))))
    
    for i in range(len(zip)): 

        queried = geo_is_infix_query_and_get_warnings(query = zip[i],
                                                      f = hud_cw.hud_cw_zip_county,
                                                      year = year,
                                                      quarter = quarter,
                                                      querytype = "zip",
                                                      key = key
                                                      )

        if any(q in county for q in queried):
            res.append(True)
        else:
            res.append(False)

    return(res)



def z_in_cbsa(zip : Union[int, str, list[int], list[str], tuple[int], tuple[str]],
              cbsa : Union[int, str, list[int], list[str], tuple[int], tuple[str]],
              year = None,
              quarter = None,
              key = None
              ) -> bool:
    """
    Given a zip code(s) and a cbsa(s), determine if they overlap
    using the crosswalk files. Overlap will be described if
    any residential, business, other, or total addresses reside in both.

    Parameters
    ----------

    zip : The zip(s) to determine overlap with cbsa(s).

    cbsa : The cbsa(s) to determine overlap with zip(s).

    year : Gets the year that this data was recorded. Can specify multiple
        years. Default is the previous year.
    
    quarter : Gets the quarter of the year that this data was recorded.
        Defaults to the first quarter of the year.

    
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
    if(key == None and os.getenv("HUD_KEY") != None):
        key = os.getenv("HUD_KEY")

    if year == None or quarter == None: 
        if hud_pkg_env.pkg_env["rec_cw"] == None:
            args = hud_get_recent_data.hud_rec_cw_yr()
            hud_pkg_env.pkg_env["rec_cw"] = args

        # Store in pkg envrionment and retrieve when necessary
        if year == None:
            year =  hud_pkg_env.pkg_env["rec_cw"] ["year"]
        
        if quarter == None:
            quarter = hud_pkg_env.pkg_env["rec_cw"] ["quarter"]
    
    
    cleaned = hud_input_check.cw_input_check_cleansing( primary_geoid = "cbsa",
                                                        secondary_geoid = "zip",
                                                        query = cbsa, year = year,
                                                        quarter = quarter,
                                                        key = os.getenv("HUD_KEY"))


    cbsa = cleaned[0]
    year = cleaned[1]
    quarter = cleaned[2]
    key = cleaned[3]

    
    if any(list(map(lambda x: len(x) != 5, cbsa))):
         raise ValueError("Cbsa input is not all of length 5")
  
    res = []
    zip = [str(zip)] if isinstance(zip, str) or isinstance(zip, int) else list(map(lambda x: str(x), list(map(lambda x: str(x), zip))))
    
    for i in range(len(zip)): 

        queried = geo_is_infix_query_and_get_warnings(query = zip[i],
                                                      f = hud_cw.hud_cw_zip_cbsa,
                                                      year = year,
                                                      quarter = quarter,
                                                      querytype = "zip",
                                                      key = key
                                                      )

        if any(q in cbsa for q in queried):
            res.append(True)
        else:
            res.append(False)

    return(res)



def z_in_cbsadiv(zip : Union[int, str, list[int], list[str], tuple[int], tuple[str]],
                 cbsadiv : Union[int, str, list[int], list[str], tuple[int], tuple[str]],
                 year = None,
                 quarter = None,
                 key = None
                 ) -> bool :
    """
    Given zip code(s) and cbsadiv(s), determine if they overlap
    using the crosswalk files. Overlap will be described if
    any residential, business, other, or total addresses reside in both.

    Parameters
    ----------

    zip : The zip(s) to determine overlap with cbsadiv(s).

    cbsadiv : The cbsadiv(s) to determine overlap with zip(s).

    year : Gets the year that this data was recorded. Can specify multiple
        years. Default is the previous year.
    
    quarter : Gets the quarter of the year that this data was recorded.
        Defaults to the first quarter of the year.

    
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
    if(key == None and os.getenv("HUD_KEY") != None):
        key = os.getenv("HUD_KEY")

    if year == None or quarter == None: 
        if hud_pkg_env.pkg_env["rec_cw"] == None:
            args = hud_get_recent_data.hud_rec_cw_yr()
            hud_pkg_env.pkg_env["rec_cw"] = args

        # Store in pkg envrionment and retrieve when necessary
        if year == None:
            year =  hud_pkg_env.pkg_env["rec_cw"] ["year"]
        
        if quarter == None:
            quarter = hud_pkg_env.pkg_env["rec_cw"] ["quarter"]
    
    
      
    cleaned = hud_input_check.cw_input_check_cleansing( primary_geoid = "cbsadiv",
                                                        secondary_geoid = "zip",
                                                        query = cbsadiv, year = year,
                                                        quarter = quarter,
                                                        key = os.getenv("HUD_KEY"))


    cbsadiv = cleaned[0]
    year = cleaned[1]
    quarter = cleaned[2]
    key = cleaned[3]

    
    if any(list(map(lambda x: len(x) != 5, cbsadiv))):
         raise ValueError("Cbsadiv input is not all of length 5")
  
    res = []
    zip = [str(zip)] if isinstance(zip, str) or isinstance(zip, int) else list(map(lambda x: str(x), list(map(lambda x: str(x), zip))))
    
    for i in range(len(zip)): 

        queried = geo_is_infix_query_and_get_warnings(query = zip[i],
                                                      f = hud_cw.hud_cw_zip_cbsadiv,
                                                      year = year,
                                                      quarter = quarter,
                                                      querytype = "zip",
                                                      key = key
                                                      )

        if any(q in cbsadiv for q in queried):
            res.append(True)
        else:
            res.append(False)

    return(res)



def z_in_ctysb(zip : Union[int, str, list[int], list[str], tuple[int], tuple[str]],
               countysub : Union[int, str, list[int], list[str], tuple[int], tuple[str]],
               year = None,
               quarter = None,
               key = None
               ) -> bool:

    """
    Given zip code(s) and countysub(s), determine if they overlap
    using the crosswalk files. Overlap will be described if
    any residential, business, other, or total addresses reside in both.

    Parameters
    ----------

    zip : The zip(s) to determine overlap with countysub(s).
    
    countysub : The countysub(s) to determine overlap with zip(s).
    
    year : Gets the year that this data was recorded. Can specify multiple
        years. Default is the previous year.
    
    quarter : Gets the quarter of the year that this data was recorded.
        Defaults to the first quarter of the year.

    
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
    if(key == None and os.getenv("HUD_KEY") != None):
        key = os.getenv("HUD_KEY")

    if year == None or quarter == None: 
        if hud_pkg_env.pkg_env["rec_cw"] == None:
            args = hud_get_recent_data.hud_rec_cw_yr()
            hud_pkg_env.pkg_env["rec_cw"] = args

        # Store in pkg envrionment and retrieve when necessary
        if year == None:
            year =  hud_pkg_env.pkg_env["rec_cw"] ["year"]
        
        if quarter == None:
            quarter = hud_pkg_env.pkg_env["rec_cw"] ["quarter"]
    

  
      
    cleaned = hud_input_check.cw_input_check_cleansing( primary_geoid = "countysub",
                                                        secondary_geoid = "zip",
                                                        query = countysub, year = year,
                                                        quarter = quarter,
                                                        key = os.getenv("HUD_KEY"))


    countysub = cleaned[0]
    year = cleaned[1]
    quarter = cleaned[2]
    key = cleaned[3]

    
    if any(list(map(lambda x: len(x) != 10, countysub))):
         raise ValueError("Countysub input is not all of length 10")
  
    res = []
    zip = [str(zip)] if isinstance(zip, str) or isinstance(zip, int) else list(map(lambda x: str(x), list(map(lambda x: str(x), zip))))
    
    for i in range(len(zip)): 

        queried = geo_is_infix_query_and_get_warnings(query = zip[i],
                                                      f = hud_cw.hud_cw_zip_countysub,
                                                      year = year,
                                                      quarter = quarter,
                                                      querytype = "zip",
                                                      key = key
                                                      )

        if any(q in countysub for q in queried):
            res.append(True)
        else:
            res.append(False)

    return(res)


def z_in_cd(zip : Union[int, str, list[int], list[str], tuple[int], tuple[str]],
            cd : Union[int, str, list[int], list[str], tuple[int], tuple[str]],
            year = None,
            quarter = None,
            key = None
            ) -> bool:

    """
    Given zip code(s) and congressional district(S), determine if they overlap
    using the crosswalk files. Overlap will be described if
    any residential, business, other, or total addresses reside in both.

    Parameters
    ----------

    zip : The zip(s) to determine overlap with congressional district(s).

    cd : The congressional district(s) to determine overlap with zip(s).

    year : Gets the year that this data was recorded. Can specify multiple
        years. Default is the previous year.
    
    quarter : Gets the quarter of the year that this data was recorded.
        Defaults to the first quarter of the year.

    
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

    if(key == None and os.getenv("HUD_KEY") != None):
        key = os.getenv("HUD_KEY")

    if year == None or quarter == None: 
        if hud_pkg_env.pkg_env["rec_cw"] == None:
            args = hud_get_recent_data.hud_rec_cw_yr()
            hud_pkg_env.pkg_env["rec_cw"] = args

        # Store in pkg envrionment and retrieve when necessary
        if year == None:
            year =  hud_pkg_env.pkg_env["rec_cw"] ["year"]
        
        if quarter == None:
            quarter = hud_pkg_env.pkg_env["rec_cw"] ["quarter"]
    

    
    cleaned = hud_input_check.cw_input_check_cleansing( primary_geoid = "cd",
                                                        secondary_geoid = "zip",
                                                        query = cd, year = year,
                                                        quarter = quarter,
                                                        key = os.getenv("HUD_KEY"))


    cd = cleaned[0]
    year = cleaned[1]
    quarter = cleaned[2]
    key = cleaned[3]

    
    if any(list(map(lambda x: len(x) != 4, cd))):
         raise ValueError("Cd input is not all of length 4")
  
    res = []
    zip = [str(zip)] if isinstance(zip, str) or isinstance(zip, int) else list(map(lambda x: str(x), list(map(lambda x: str(x), zip))))
    
    for i in range(len(zip)): 

        queried = geo_is_infix_query_and_get_warnings(query = zip[i],
                                                      f = hud_cw.hud_cw_zip_cd,
                                                      year = year,
                                                      quarter = quarter,
                                                      querytype = "zip",
                                                      key = key
                                                      )

        if any(q in cd for q in queried):
            res.append(True)
        else:
            res.append(False)

    return(res)








def trt_in_z(tract : Union[int, str, list[int], list[str], tuple[int], tuple[str]],
             zip : Union[int, str, list[int], list[str], tuple[int], tuple[str]],
             year = None,
             quarter = None,
             key = None
             ) -> bool:
    """
    Given tract(s) and zip code(s), determine if they overlap
    using the crosswalk files. Overlap will be described if
    any residential, business, other, or total addresses reside in both.

    Parameters
    ----------

    tract : The tract(s) to determine overlap with zip(s).

    zip : The zip(s). to determine overlap with tract(s).

    year : Gets the year that this data was recorded. Can specify multiple
        years. Default is the previous year.
    
    quarter : Gets the quarter of the year that this data was recorded.
        Defaults to the first quarter of the year.

    
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
    if(key == None and os.getenv("HUD_KEY") != None):
        key = os.getenv("HUD_KEY")

    if year == None or quarter == None: 
        if hud_pkg_env.pkg_env["rec_cw"] == None:
            args = hud_get_recent_data.hud_rec_cw_yr()
            hud_pkg_env.pkg_env["rec_cw"] = args

        # Store in pkg envrionment and retrieve when necessary
        if year == None:
            year =  hud_pkg_env.pkg_env["rec_cw"] ["year"]
        
        if quarter == None:
            quarter = hud_pkg_env.pkg_env["rec_cw"] ["quarter"]
    

    cleaned = hud_input_check.cw_input_check_cleansing( primary_geoid = "zip",
                                                        secondary_geoid = "tract",
                                                        query = zip, year = year,
                                                        quarter = quarter,
                                                        key = os.getenv("HUD_KEY"))


    zip = cleaned[0]
    year = cleaned[1]
    quarter = cleaned[2]
    key = cleaned[3]

    
    if any(list(map(lambda x: len(x) != 5, zip))):
         raise ValueError("Zip input is not all of length 5")
  
    res = []
    tract = [str(tract)] if isinstance(tract, str) or isinstance(tract, int) else list(map(lambda x: str(x), list(map(lambda x: str(x), tract))))
    
    for i in range(len(tract)): 

        queried = geo_is_infix_query_and_get_warnings(query = tract[i],
                                                      f = hud_cw.hud_cw_tract_zip,
                                                      year = year,
                                                      quarter = quarter,
                                                      querytype = "tract",
                                                      key = key
                                                      )

        if any(q in zip for q in queried):
            res.append(True)
        else:
            res.append(False)

    return(res)



def cty_in_z(county : Union[int, str, list[int], list[str], tuple[int], tuple[str]],
             zip : Union[int, str, list[int], list[str], tuple[int], tuple[str]],
             year = None,
             quarter = None,
             key = None
             ) -> bool:
    """
    Given county(s) and zip code(s), determine if they overlap
    using the crosswalk files. Overlap will be described if
    any residential, business, other, or total addresses reside in both.

    Parameters
    ----------

    county : The county(s) to determine overlap with zip(s).

    zip : The zip(s) to determine overlap with county(s).

    year : Gets the year that this data was recorded. Can specify multiple
        years. Default is the previous year.
    
    quarter : Gets the quarter of the year that this data was recorded.
        Defaults to the first quarter of the year.

    
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

    if(key == None and os.getenv("HUD_KEY") != None):
        key = os.getenv("HUD_KEY")

    if year == None or quarter == None: 
        if hud_pkg_env.pkg_env["rec_cw"] == None:
            args = hud_get_recent_data.hud_rec_cw_yr()
            hud_pkg_env.pkg_env["rec_cw"] = args

        # Store in pkg envrionment and retrieve when necessary
        if year == None:
            year =  hud_pkg_env.pkg_env["rec_cw"] ["year"]
        
        if quarter == None:
            quarter = hud_pkg_env.pkg_env["rec_cw"] ["quarter"]
    

  
    cleaned = hud_input_check.cw_input_check_cleansing( primary_geoid = "zip",
                                                        secondary_geoid = "county",
                                                        query = zip, year = year,
                                                        quarter = quarter,
                                                        key = os.getenv("HUD_KEY"))


    zip = cleaned[0]
    year = cleaned[1]
    quarter = cleaned[2]
    key = cleaned[3]

    
    if any(list(map(lambda x: len(x) != 5, zip))):
         raise ValueError("Zip input is not all of length 5")
  
    res = []
    county = [str(county)] if isinstance(county, str) or isinstance(county, int) else list(map(lambda x: str(x), list(map(lambda x: str(x), county))))
    
    for i in range(len(county)): 

        queried = geo_is_infix_query_and_get_warnings(query = county[i],
                                                      f = hud_cw.hud_cw_county_zip,
                                                      year = year,
                                                      quarter = quarter,
                                                      querytype = "county",
                                                      key = key
                                                      )

        if any(q in zip for q in queried):
            res.append(True)
        else:
            res.append(False)

    return(res)




def cbsa_in_z(cbsa : Union[int, str, list[int], list[str], tuple[int], tuple[str]],
              zip : Union[int, str, list[int], list[str], tuple[int], tuple[str]],
              year = None,
              quarter = None,
              key = None
              ) -> bool:

    """
    Given cbsa(s) and zip code(s), determine if they overlap
    using the crosswalk files. Overlap will be described if
    any residential, business, other, or total addresses reside in both.

    Parameters
    ----------

    cbsa : The cbsa(s) to determine overlap with zip(s).

    zip : The zip(s) to determine overlap with cbsa(s).

    year : Gets the year that this data was recorded. Can specify multiple
        years. Default is the previous year.
    
    quarter : Gets the quarter of the year that this data was recorded.
        Defaults to the first quarter of the year.

    
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
    if(key == None and os.getenv("HUD_KEY") != None):
        key = os.getenv("HUD_KEY")

    if year == None or quarter == None: 
        if hud_pkg_env.pkg_env["rec_cw"] == None:
            args = hud_get_recent_data.hud_rec_cw_yr()
            hud_pkg_env.pkg_env["rec_cw"] = args

        # Store in pkg envrionment and retrieve when necessary
        if year == None:
            year =  hud_pkg_env.pkg_env["rec_cw"] ["year"]
        
        if quarter == None:
            quarter = hud_pkg_env.pkg_env["rec_cw"] ["quarter"]
    

    
    cleaned = hud_input_check.cw_input_check_cleansing( primary_geoid = "zip",
                                                        secondary_geoid = "cbsa",
                                                        query = zip, year = year,
                                                        quarter = quarter,
                                                        key = os.getenv("HUD_KEY"))


    zip = cleaned[0]
    year = cleaned[1]
    quarter = cleaned[2]
    key = cleaned[3]

    
    if any(list(map(lambda x: len(x) != 5, zip))):
         raise ValueError("Zip input is not all of length 5")
  
    res = []
    cbsa = [str(cbsa)] if isinstance(cbsa, str) or isinstance(cbsa, int) else list(map(lambda x: str(x), list(map(lambda x: str(x), cbsa))))
    
    for i in range(len(cbsa)): 

        queried = geo_is_infix_query_and_get_warnings(query = cbsa[i],
                                                      f = hud_cw.hud_cw_cbsa_zip,
                                                      year = year,
                                                      quarter = quarter,
                                                      querytype = "cbsa",
                                                      key = key
                                                      )

        if any(q in zip for q in queried):
            res.append(True)
        else:
            res.append(False)

    return(res)



def cbsadiv_in_z(cbsadiv : Union[int, str, list[int], list[str], tuple[int], tuple[str]],
                 zip : Union[int, str, list[int], list[str], tuple[int], tuple[str]],
                 year = None,
                 quarter = None,
                 key = None
                 ) -> bool:    

    """
    Given cbsadiv(s) and zip code(s), determine if they overlap
    using the crosswalk files. Overlap will be described if
    any residential, business, other, or total addresses reside in both.

    Parameters
    ----------

    cbsadiv : The cbsadiv(s) to determine overlap with zip(s).

    zip : The zip(s). to determine overlap with cbsadiv(s).

    year : Gets the year that this data was recorded. Can specify multiple
        years. Default is the previous year.
    
    quarter : Gets the quarter of the year that this data was recorded.
        Defaults to the first quarter of the year.

    
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
    if(key == None and os.getenv("HUD_KEY") != None):
        key = os.getenv("HUD_KEY")

    if year == None or quarter == None: 
        if hud_pkg_env.pkg_env["rec_cw"] == None:
            args = hud_get_recent_data.hud_rec_cw_yr()
            hud_pkg_env.pkg_env["rec_cw"] = args

        # Store in pkg envrionment and retrieve when necessary
        if year == None:
            year =  hud_pkg_env.pkg_env["rec_cw"] ["year"]
        
        if quarter == None:
            quarter = hud_pkg_env.pkg_env["rec_cw"] ["quarter"]

    
    cleaned = hud_input_check.cw_input_check_cleansing( primary_geoid = "zip",
                                                        secondary_geoid = "cbsadiv",
                                                        query = zip, year = year,
                                                        quarter = quarter,
                                                        key = os.getenv("HUD_KEY"))


    zip = cleaned[0]
    year = cleaned[1]
    quarter = cleaned[2]
    key = cleaned[3]

    
    if any(list(map(lambda x: len(x) != 5, zip))):
         raise ValueError("Zip input is not all of length 5")
  
    res = []
    cbsadiv = [str(cbsadiv)] if isinstance(cbsadiv, str) or isinstance(cbsadiv, int) else list(map(lambda x: str(x), list(map(lambda x: str(x), cbsadiv))))
    
    for i in range(len(cbsadiv)): 

        queried = geo_is_infix_query_and_get_warnings(query = cbsadiv[i],
                                                      f = hud_cw.hud_cw_cbsadiv_zip,
                                                      year = year,
                                                      quarter = quarter,
                                                      querytype = "cbsadiv",
                                                      key = key
                                                      )

        if any(q in zip for q in queried):
            res.append(True)
        else:
            res.append(False)

    return(res)



def cd_in_z(cd : Union[int, str, list[int], list[str], tuple[int], tuple[str]],
            zip : Union[int, str, list[int], list[str], tuple[int], tuple[str]],
            year = None,
            quarter = None,
            key = None
            ) -> bool:  
    """
    Given congressional district(s) and zip code(s), determine if they overlap
    using the crosswalk files. Overlap will be described if
    any residential, business, other, or total addresses reside in both.

    Parameters
    ----------

    cd  The congressional district(s) to determine overlap with zip(s).

    zip : The zip(s) to determine overlap with congressional district(s).

    year : Gets the year that this data was recorded. Can specify multiple
        years. Default is the previous year.
    
    quarter : Gets the quarter of the year that this data was recorded.
        Defaults to the first quarter of the year.

    
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

    if(key == None and os.getenv("HUD_KEY") != None):
        key = os.getenv("HUD_KEY")

    if year == None or quarter == None: 
        if hud_pkg_env.pkg_env["rec_cw"] == None:
            args = hud_get_recent_data.hud_rec_cw_yr()
            hud_pkg_env.pkg_env["rec_cw"] = args

        # Store in pkg envrionment and retrieve when necessary
        if year == None:
            year =  hud_pkg_env.pkg_env["rec_cw"] ["year"]
        
        if quarter == None:
            quarter = hud_pkg_env.pkg_env["rec_cw"] ["quarter"]
    

    cleaned = hud_input_check.cw_input_check_cleansing( primary_geoid = "zip",
                                                        secondary_geoid = "cd",
                                                        query = zip, year = year,
                                                        quarter = quarter,
                                                        key = os.getenv("HUD_KEY"))

    zip = cleaned[0]
    year = cleaned[1]
    quarter = cleaned[2]
    key = cleaned[3]
    
    if any(list(map(lambda x: len(x) != 5, zip))):
         raise ValueError("Zip input is not all of length 5")
  
    res = []
    cd = [str(cd)] if isinstance(cd, str) or isinstance(cd, int) else list(map(lambda x: str(x), list(map(lambda x: str(x), cd))))
    
    for i in range(len(cd)): 

        queried = geo_is_infix_query_and_get_warnings(query = cd[i],
                                                      f = hud_cw.hud_cw_cd_zip,
                                                      year = year,
                                                      quarter = quarter,
                                                      querytype = "cd",
                                                      key = key
                                                      )

        if any(q in zip for q in queried):
            res.append(True)
        else:
            res.append(False)

    return(res)



 
def ctysb_in_z(countysub : Union[int, str, list[int], list[str], tuple[int], tuple[str]],
               zip : Union[int, str, list[int], list[str], tuple[int], tuple[str]],
               year = None,
               quarter = None,
               key = None
               ) -> bool:  
    """
    Given countysub(s) and zip code(s), determine if they overlap
    using the crosswalk files. Overlap will be described if
    any residential, business, other, or total addresses reside in both.

    Parameters
    ----------

    countysub : The countysub(s) to determine overlap with zip(s).

    zip : The zip(s). to determine overlap with countysub(s).

    year : Gets the year that this data was recorded. Can specify multiple
        years. Default is the previous year.
    
    quarter : Gets the quarter of the year that this data was recorded.
        Defaults to the first quarter of the year.

      
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
    if(key == None and os.getenv("HUD_KEY") != None):
        key = os.getenv("HUD_KEY")

    if year == None or quarter == None: 
        if hud_pkg_env.pkg_env["rec_cw"] == None:
            args = hud_get_recent_data.hud_rec_cw_yr()
            hud_pkg_env.pkg_env["rec_cw"] = args

        # Store in pkg envrionment and retrieve when necessary
        if year == None:
            year =  hud_pkg_env.pkg_env["rec_cw"] ["year"]
        
        if quarter == None:
            quarter = hud_pkg_env.pkg_env["rec_cw"] ["quarter"]
    

  
    cleaned = hud_input_check.cw_input_check_cleansing( primary_geoid = "zip",
                                                        secondary_geoid = "countysub",
                                                        query = zip, year = year,
                                                        quarter = quarter,
                                                        key = os.getenv("HUD_KEY"))


    zip = cleaned[0]
    year = cleaned[1]
    quarter = cleaned[2]
    key = cleaned[3]

    
    if any(list(map(lambda x: len(x) != 5, zip))):
         raise ValueError("Zip input is not all of length 5")
  
    res = []
    countysub = [str(countysub)] if isinstance(countysub, str) or isinstance(countysub, int) else list(map(lambda x: str(x), list(map(lambda x: str(x), countysub))))
    
    for i in range(len(countysub)): 

        queried = geo_is_infix_query_and_get_warnings(query = countysub[i],
                                                      f = hud_cw.hud_cw_countysub_zip,
                                                      year = year,
                                                      quarter = quarter,
                                                      querytype = "countysub",
                                                      key = key
                                                      )

        if any(q in zip for q in queried):
            res.append(True)
        else:
            res.append(False)

    return(res)



def geo_is_infix_query_and_get_warnings(query,
                                        f,
                                        year,
                                        quarter,
                                        querytype,
                                        key):

    """
    Giving a geoid to query for, make sure to call the core
    hud_cw() functions to get the crosswalk output
    but intercept it to make custom warning messages.

    Parameters
    ----------
    query : The geoids to query for crosswalk
    
    f : The function used query the crosswalk files.
    
    year : The year to query for.
    
    quarter : The quarter to query for.
    
    querytype : The geoid user is querying for.
    1) zip
    2) tract
    3) cbsa
    4) cd
    5) cbsadiv
    6) countsub
    7) county
    """
  
    res = []
    try:
        res = f(query,
                minimal = True,
                year = year,
                quarter = quarter,
                key = key
                )
    
    except ValueError as e: 
        raise ValueError(str(e))
    
    except RuntimeWarning as e:
    
        # Might be more efficient to save the errored geoids when used instead
        # of having to regex it...
        warn("\nThe " +  querytype + " " + query + " inputted is not valid." +
                    " No data was found for year: " + year +  " and quarter: " + quarter,
                    sep = ""
                )


    return(res)
    

