import hudpy
import pytest
import os
import hudpy.hudchas
import hudpy.hudmisc
@pytest.mark.skipif(os.getenv("HUD_KEY") == None, "HUD_KEY not available.")
def test_chas_nation():
    # First make simple query call to hud_chas_nation() with no arguments.
    # Will choose default 2014-2018.
    one_year = hudpy.hudchas.hud_chas_nation()
    # Just expect one row to return... weak check.
    assert len(one_year) == 1

    # Try querying multiple years from the nations
    two_years = hudpy.hudchas.hud_chas_nation(year = ["2014-2018", "2012-2016"])
    assert len(two_years) == 2
    
    # Try querying a year which is not allowed... should expect warning
    with pytest.raises(ValueError) as e_info:
        hudpy.hudchas.hud_chas_nation(year = ["2017-2022", "2321-142131"])
    with pytest.raises(ValueError) as e_info:
        # Try integer inputs. It should also throw warning.
        hudpy.hudchas.hud_chas_nation(year = [2018, 2019])


@pytest.mark.skipif(os.getenv("HUD_KEY") == None, "HUD_KEY not available.")
def test_chas_state():
    # Try querying for a state using abbreviation...
    # Try lowercase too... Try uppercase too...
    # Try weird cases...

    # None of these should throw errors...
    test = hudpy.hudchas.hud_chas_state(state = "VA")
    assert len(test) == 1
    
    test = hudpy.hudchas.hud_chas_state(state = "California")
    assert len(test) == 1
    
    test = hudpy.hudchas.hud_chas_state(state = "46")
    assert len(test) == 1
    
    test = hudpy.hudchas.hud_chas_state(state = "Ca")
    assert len(test) == 1
    
    test = hudpy.hudchas.hud_chas_state(state = "ca")
    assert len(test) == 1
    
    test = hudpy.hudchas.hud_chas_state(state = "CA")
    assert len(test) == 1
    
    test = hudpy.hudchas.hud_chas_state(state = "VIRGINIA")
    assert len(test) == 1
    
    test = hudpy.hudchas.hud_chas_state(state = "vIRGINIa")
    assert len(test) == 1
    
    # Try querying for all states in nation
    hudstates = hudpy.hudmisc.hud_nation_states_territories()
    hudstates = hudpy.hudmisc.hudstates[int(hudstates["state_num"]) < 57, ]
    hudstates = hudstates[hudstates["state_code"] != "DC", ]

    # Try to query for all state codes?
    all_state_abbr = hudpy.hudchas.hud_chas_state(hudstates["state_code"])
    assert len(all_state_abbr) == 1
    
    # Try to query for all state name?
    all_state_num = hudpy.hudchas.hud_chas_state(hudstates["state_num"])
    assert len(all_state_num) == 1


@pytest.mark.skipif(os.getenv("HUD_KEY") == None, "HUD_KEY not available.")
def test_chas_county():
    test = hudpy.hudchas.hud_chas_county(county = "06105")
    assert len(test) == 1
    # Query counties that have multiple...
    # Need to deal with cases when leading zero might get truncated.

    test = hudpy.hudchas.hud_chas_county(county = [6105, 6115])
    assert len(test) == 2

    test = hudpy.hudchas.hud_chas_county(county = ["06105", "06115"])
    assert len(test) == 2

    test = hudpy.hudchas.hud_chas_county(county = ["06105", "06115"],
                            year = ["2013-2017", "2014-2018"])
    assert len(test) == 4

    # Query for all counties in Maryland.
    all_md_counties = hudpy.hudmisc.hud_state_counties("MD")

    # Only use the first 5 numbers in fips code.

    all_md = hudpy.hudchas.hud_chas_county(county = map(lambda x: x[0:4], all_md_counties["fips_code"]))
    assert len(all_md) >= 1


@pytest.mark.skipif(os.getenv("HUD_KEY") == None, "HUD_KEY not available.")
def test_chas_mcd():

    # This will take a while...
    all_md = hudpy.hudchas.hud_chas_state_mcd("md")

    assert len(all_md) == 1

