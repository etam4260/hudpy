def hud_chas_nation():
    """
    #' @name hud_chas_nation
    #' @title hud_chas_nation
    #' @param year The years to query for.
    #'  * year = "2014-2018"
    #'  * year = "2013-2017"
    #'  * year = "2012-2016"
    #'  * year = "2011-2015"
    #'  * year = "2010-2014"
    #'  * year = "2009-2013"
    #'  * year = "2008-2012"
    #'  * year = "2007-2011"
    #'  * year = "2006-2010"
    #' @param key The key obtain from HUD USER website.
    #' @description Returns CHAS data for the entire nation.
    #' @returns Returns a dataframe with CHAS data for the entire nation.
    """

def hud_chas_state():
    """
    #' @name hud_chas_state
    #' @title hud_chas_state
    #' @description Returns CHAS data for a state.
    #' @param state The state to query for. Can supply as abbreviation, whole name,
    #'   or as geoid.
    #' @param year The years to query for.
    #'  * year = "2014-2018"
    #'  * year = "2013-2017"
    #'  * year = "2012-2016"
    #'  * year = "2011-2015"
    #'  * year = "2010-2014"
    #'  * year = "2009-2013"
    #'  * year = "2008-2012"
    #'  * year = "2007-2011"
    #'  * year = "2006-2010"
    #' @param key The key obtain from HUD USER website.
    #' @returns Returns a dataframe with CHAS data for a particular state.
    """


def hud_chas_county():
    """
    #' @name hud_chas_county
    #' @title hud_chas_county
    #' @description Returns CHAS data for counties.
    #' @param county The county to query for. Must supply a geoid. 2 digit state fip
    #'   + 3 digit county fip. hud_state_counties() will show an extra 99999 at the
    #'   end. Just remove that.
    #' @param year The years to query for.
    #'  * year = "2014-2018"
    #'  * year = "2013-2017"
    #'  * year = "2012-2016"
    #'  * year = "2011-2015"
    #'  * year = "2010-2014"
    #'  * year = "2009-2013"
    #'  * year = "2008-2012"
    #'  * year = "2007-2011"
    #'  * year = "2006-2010"
    #' @param key The key obtain from HUD USER website.
    #' @returns Returns a dataframe with CHAS data for counties.
    """

def hud_chas_state_mcd():
    """
    #' @name hud_chas_state_mcd
    #' @title hud_chas_state_mcd
    #' @description Returns CHAS data for all mcds in a state.
    #' @param state The state name, abbreviation, or fips code.
    #' @param year The years to query for.
    #'  * year = "2014-2018"
    #'  * year = "2013-2017"
    #'  * year = "2012-2016"
    #'  * year = "2011-2015"
    #'  * year = "2010-2014"
    #'  * year = "2009-2013"
    #'  * year = "2008-2012"
    #'  * year = "2007-2011"
    #'  * year = "2006-2010"
    #' @param key The key obtain from HUD USER website.
    #' @returns Returns a dataframe with CHAS data for mcds.
    """

def hud_chas_state_place():
    """
    #' @name hud_chas_state_place
    #' @title hud_chas_state_place
    #' @description Returns CHAS for all places in a state.
    #' @param state The state name, abbreviation, or fips code. Make sure if state
    #'   fips is 1 digit number, do not include leading 0.
    #' @param year The years to query for.
    #'  * year = "2014-2018"
    #'  * year = "2013-2017"
    #'  * year = "2012-2016"
    #'  * year = "2011-2015"
    #'  * year = "2010-2014"
    #'  * year = "2009-2013"
    #'  * year = "2008-2012"
    #'  * year = "2007-2011"
    #'  * year = "2006-2010"
    #' @param key The key obtain from HUD USER website.
    #' @returns Returns a dataframe with CHAS data for places.
    """