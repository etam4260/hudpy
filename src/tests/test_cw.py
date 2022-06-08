import pytest
import os
from hudpy import hud_user
from hudpy import hud_misc

@pytest.mark.skipif(os.getenv("HUD_KEY") == None, reason="HUD_KEY not available.")
def test_cw_all_types():

    # Lets try a ZIP code in Alabama for now for 1 -> 5 as well as 11.
    zip_tract = hud_user.hud_cw(type = 1, query = "35213",
                      year = ["2010", "2011"], quarter = ["1"])

    assert len(zip_tract) >= 1


    zip_county = hud_user.hud_cw(type = "2", query = "35213",
                       year = ["2016", "2020"], quarter = ["2"])

    assert len(zip_county) >= 1


    zip_cbsa = hud_user.hud_cw(type = 3, query = 35213,
                     year = ["2012", "2011"], quarter = ["3"])

    assert len(zip_cbsa) >= 1


    zip_cbsadiv = hud_user.hud_cw(type = 4, query = "22031",
                        year = ["2017", "2019"], quarter = ["4"])

    assert len(zip_cbsadiv) >= 1


    zip_cd = hud_user.hud_cw(type = "5", query = "35213",
                   year = [2011, "2012"], quarter = ["1", "2"])

    assert len(zip_cd) >= 1


    tract_zip = hud_user.hud_cw(type = 6, query = "48201223100",
                      year = ["2017", "2010"],
                      quarter = ["1", "2", "3"])

    assert len(tract_zip) >= 1

    # Testing county to zip cross_walk. Assuming this to be the most popular.
    county_zip = hud_user.hud_cw(type = 7, query = "22031",
                       year = ["2010", "2011"],
                       quarter = ["1", "2", "3", "4"])

    assert len(county_zip) >= 1

    # Try all counties in MD
    county_zip = hud_user.hud_cw(type = 7,
                       query = list(map(lambda x: x[0:5], hud_misc.hud_state_counties("md")["fips_code"])),
                       year = ["2010"], quarter = ["1"])
  
    assert len(zip_county) >= 1

    # A core based Statistical Area to zip crosswalk.
    # CBSA defines Micropolitan and Metropolitan
    cbsa_zip = hud_user.hud_cw(type = 8, query = "10140",
                     year = ["2010", "2011"], quarter = ["2", "1"])

    assert len(cbsa_zip) >= 1

    # Must be a core base statistical area division code which apply to
    # metropolitan areas.
    cbsadiv_zip = hud_user.hud_cw(type = 9, query = "10380",
                        year = ["2017"], quarter = ["4"])

    assert len(cbsadiv_zip) >= 1


    cd_zip = hud_user.hud_cw(type = 10, query = "2202",
                   year = ["2010", "2011"], quarter = ["4", "3"])

    assert len(cd_zip) >= 1

    # Testing ZIP CODE _> COUNTYSUB
    zip_countysub = hud_user.hud_cw(type = 11, query = "35213",
                          year = ["2019", "2020"], quarter = ["2", "3"])

    assert len(zip_countysub) >= 1

    # User might not provide a "set" of years or quarters, so should make sure to
    # check that Sometimes the API might not provide data because out of range
    # years. Also testing Countysub _> ZIP
    # Not sure if R has a package for all these types of GEOIDs

    countysub_zip = hud_user.hud_cw(type = 12, query = "4606720300 ",
                          year = ["2019", "2019", "2019"],
                          quarter = ["4", "4"])

    assert len(countysub_zip) >= 1


@pytest.mark.skipif(os.getenv("HUD_KEY") == None, reason="HUD_KEY not available.")
def test_cw_diff_years():
    # Error when years are in the future
    with pytest.raises(ValueError) as e_info:
        hud_user.hud_cw(type = 7, query = "22031",
                         year = ["2010", "2011", "2024"],
                         quarter = ["1", "2", "3", "4"])
  
    # Error when quarters are not from 1 to 4
    with pytest.raises(ValueError) as e_info:
        hud_user.hud_cw(type = 7, query = "22031",
                         year = ["2010", "2011"],
                         quarter = ["1", "2", "3", "4", "5"])

@pytest.mark.skipif(os.getenv("HUD_KEY") == None, reason="HUD_KEY not available.")
def test_cw_wrong_query():
    with pytest.raises(ValueError) as e_info:
        hud_user.hud_cw(type = 7, query = "22031241231",
                      year = ["2010", "2011"],
                      quarter = ["1", "2", "3", "4"])

  # No zip code named 99999
    with pytest.warns(None) as e_info:
        hud_user.hud_cw(type = 1, query = "99999",
                        year = ["2010", "2011"],
                        quarter = ["1", "1", "2", "3", "4"])


@pytest.mark.skipif(os.getenv("HUD_KEY") == None, reason="HUD_KEY not available.")
def test_not_convert_int():
    # Character arguments that aren"t numbers in any of them. Throws errors.
    with pytest.raises(ValueError) as e_info:
        hud_user.hud_cw(type = "dwqji", query = "22031",
                        year = ["2010", "2011"],
                        quarter = ["1", "2", "3", "4"])
    with pytest.raises(ValueError) as e_info:
        hud_user.hud_cw(type = "7", query = "22031ada",
                        year = ["2010", "2011"],
                        quarter = ["1", "2", "3", "4"])
    with pytest.raises(ValueError) as e_info:
        hud_user.hud_cw(type = "7", query = "22031",
                        year = ["2010", "2011adaadda"],
                        quarter = ["1", "2ada", "3", "4"])
    with pytest.raises(ValueError) as e_info:
        hud_user.hud_cw(type = 7, query = "22031",
                        year = ["2010", "2011"],
                        quarter = ["1", "2as", "3", "4"])
