import pytest
import os

from hudpy import hud_chas
from hudpy import hud_misc

@pytest.mark.skipif(os.getenv("HUD_KEY") == None, reason="HUD_KEY not available.")
def test_chas_nation():
    # First make simple query call to hud_chas_nation() with no arguments.
    # Will choose default 2014-2018.
    one_year = hud_chas.hud_chas_nation()
    # Just expect one row to return... weak check.
    assert len(one_year) == 1

    # Try querying multiple years from the nations
    two_years = hud_chas.hud_chas_nation(year = ["2014-2018", "2012-2016"])
    assert len(two_years) == 2
    
    # Try querying a year which is not allowed... should expect warning
    with pytest.raises(ValueError) as e_info:
        hud_chas.hud_chas_nation(year = ["2017-2022", "2321-142131"])
    with pytest.raises(ValueError) as e_info:
        # Try integer inputs. It should also throw warning.
        hud_chas.hud_chas_nation(year = [2018, 2019])


@pytest.mark.skipif(os.getenv("HUD_KEY") == None, reason="HUD_KEY not available.")
def test_chas_state():
    # Try querying for a state using abbreviation...
    # Try lowercase too... Try uppercase too...
    # Try weird cases...

    # None of these should throw errors...
    test = hud_chas.hud_chas_state(state = "VA")
    assert len(test) == 1
    
    test = hud_chas.hud_chas_state(state = "California")
    assert len(test) == 1
    
    test = hud_chas.hud_chas_state(state = "46")
    assert len(test) == 1
    
    test = hud_chas.hud_chas_state(state = "Ca")
    assert len(test) == 1
    
    test = hud_chas.hud_chas_state(state = "ca")
    assert len(test) == 1
    
    test = hud_chas.hud_chas_state(state = "CA")
    assert len(test) == 1
    
    test = hud_chas.hud_chas_state(state = "VIRGINIA")
    assert len(test) == 1
    
    test = hud_chas.hud_chas_state(state = "vIRGINIa")
    assert len(test) == 1
    
    hud_states = hud_misc.hud_nation_states_territories()
    hud_states["state_num"] = list(map(lambda x: int(x), hud_states["state_num"]))
    hud_states = hud_states[hud_states["state_num"] < 57]
    hud_states = hud_states[hud_states["state_code"] != "DC"]


    # Try to query for all state codes?
    all_state_abbr = hud_chas.hud_chas_state(list(hud_states["state_code"]))
    assert len(all_state_abbr) == len(hud_states)
    
    # Try to query for all state name?
    all_state_num = hud_chas.hud_chas_state(list(hud_states["state_num"]))
    assert len(all_state_num) == len(hud_states)


@pytest.mark.skipif(os.getenv("HUD_KEY") == None, reason="HUD_KEY not available.")
def test_chas_county():
    test = hud_chas.hud_chas_county(county = "06105")
    assert len(test) == 1
    # Query counties that have multiple...
    # Need to deal with cases when leading zero might get truncated.

    test = hud_chas.hud_chas_county(county = [6105, 6115])
    assert len(test) == 2

    test = hud_chas.hud_chas_county(county = ["06105", "06115"])
    assert len(test) == 2

    test = hud_chas.hud_chas_county(county = ["06105", "06115"],
                            year = ["2013-2017", "2014-2018"])
    assert len(test) == 4

    # Query for all counties in Maryland.
    all_md_counties = hud_misc.hud_state_counties("MD")

    # Only use the first 5 numbers in fips code.

    all_md = hud_chas.hud_chas_county(county = list(map(lambda x: x[0:5], all_md_counties["fips_code"])))
    assert len(all_md) >= 1


@pytest.mark.skipif(os.getenv("HUD_KEY") == None, reason="HUD_KEY not available.")
def test_chas_mcd():

    # This will take a while...
    all_md = hud_chas.hud_chas_state_mcd("md")

    assert len(all_md) >= 1

