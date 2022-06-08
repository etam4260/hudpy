from datetime import date

from hudpy import hud_cw
from hudpy import hud_fmr
from hudpy import hud_user

import os

def hud_rec_cw_yr(key: str = None):
    """
    Ping the Crosswalk API provided by HUD User to determine the
    most recently released files. This will only ping for the last two
    years. This tests hud_cw_tract_zip(tract = 48201223100) as the
    endpoint query.

    See Also
    --------
    * hud_rec_cw_yr()
    * hud_rec_fmr_yr()
    * hud_rec_il_yr
  
    Returns
    -------
    A dictionary with the most recent year and quarter of crosswalk files.

    Examples
    --------

    >>> hud_rec_cw_yr()

    """
    if(key == None and os.getenv("HUD_KEY") != None):
        key = os.getenv("HUD_KEY")

    year = int(date.today().strftime("%Y"))
    month = int(date.today().strftime("%m"))

    if month >= 1 and month <= 3: 
        quarter = 1
    elif month >= 4 and month <= 6:
        quarter = 2
    elif month >= 7 and month <= 9:
        quarter = 3
    elif month >= 10 and month <= 12:
        quarter = 4

    # Ping HUD CW API. Set a limit for 8 pings or the two years from current one.

    i = 8
    while (i > 0):
        # It might be worthwhile to make this a little more robust by pinging
        # different CW files and making a percentage threshold on them.

        # TODO: Need to suppress messages and warnings...

        data = hud_cw.hud_cw_tract_zip(tract = 48201223100,
                                year = year,
                                quarter = quarter,
                                key = key
                                )

        if not data.empty: 
            return({"year": year, "quarter": quarter})
        
        if quarter > 1:
            quarter = quarter - 1
        else:
            year = year - 1
            quarter = 4

        i = i - 1
    

    return({"year": None, "quarter": None})




def hud_rec_fmr_yr(key: str = None): 
    
    """
    Ping the Fair Markets Rent API provided by HUD User to
    determine the most recently released files. This will only ping
    for the last two years. Will return years for county and metroarea
    resolution.

    See Also
    --------

    * hud_rec_cw_yr()
    * hud_rec_fmr_yr()
    * hud_rec_il_yr()

    Returns
    -------
    The most recent year for the fmr files for state, county, and
    metroarea queries.

    Examples
    --------
 
    >>> hud_rec_fmr_yr()

    """
    if(key == None and os.getenv("HUD_KEY") != None):
        key = os.getenv("HUD_KEY")

    year = int(date.today().strftime("%Y"))
    month = int(date.today().strftime("%m"))

    if month >= 1 and month <= 3: 
        quarter = 1
    elif month >= 4 and month <= 6:
        quarter = 2
    elif month >= 7 and month <= 9:
        quarter = 3
    elif month >= 10 and month <= 12:
        quarter = 4
    

    year_state = None
    year_county = None
    year_metroarea = None

    i = 8
    while (i > 0):

        if year_state == None:
            
            data = hud_user.hud_fmr("MD", year = year, key = key)

            if len(data) != 0:
                year_state = year

        if year_county == None:
            data = hud_fmr.hud_fmr_county_zip("5100199999", year = year, key = key)

            if not data.empty:
                year_county = year
            

        if year_metroarea == None:  
            data = hud_fmr.hud_fmr_metroarea_zip("METRO47900M47900", year = year, key = key)

            if not data.empty:
                year_metroarea = year
            

        if (quarter > 1):
            quarter = quarter - 1
        else:
            year = year - 1
            quarter = 4

        i = i - 1

    return({"state": year_state,
            "county": year_county,
            "metroarea": year_metroarea})
    



def hud_rec_il_yr(key:str = None):
    """
    Ping the Income Limits API provided by HUD User to
    determine the most recently released files. This will only ping
    for the last two years. Will return years for county and metroarea
    resolution.
    
    See Also
    --------

    * hud_rec_cw_yr()
    * hud_rec_fmr_yr()
    * hud_rec_il_yr()

    Returns
    -------
    The most recent year for the il files for state, county, and
    metroarea queries.

    Examples
    --------

    >>> hud_rec_il_yr()

    """
    if(key == None and os.getenv("HUD_KEY") != None):
        key = os.getenv("HUD_KEY")

    year = int(date.today().strftime("%Y"))
    month = int(date.today().strftime("%m"))

    if month >= 1 and month <= 3: 
        quarter = 1
    elif month >= 4 and month <= 6:
        quarter = 2
    elif month >= 7 and month <= 9:
        quarter = 3
    elif month >= 10 and month <= 12:
        quarter = 4

    year_state = None
    year_county = None
    year_metroarea = None

    i = 8
    while (i > 0):

        if year_state == None:
            
            data = hud_user.hud_il("MD", year = year, key = key)

            if not data.empty:
                year_state = year

        if year_county == None:
            data = hud_user.hud_il("5100199999", year = year, key = key)

            if not data.empty:
                year_county = year
            

        if year_metroarea == None:  
            data = hud_user.hud_il("METRO47900M47900", year = year, key = key)

            if not data.empty:
                year_metroarea = year
            

        if (quarter > 1):
            quarter = quarter - 1
        else:
            year = year - 1
            quarter = 4

        i = i - 1

    return({"state": year_state,
            "county": year_county,
            "metroarea": year_metroarea})
    