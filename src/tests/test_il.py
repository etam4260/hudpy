import pytest
import os
from hudpy import huduser
from hudpy import hudmisc

@pytest.mark.skipif(os.getenv("HUD_KEY") == None, reason="HUD_KEY not available.")
def test_il_state_queries():
    va = huduser.hud_il("VA", 2021)
    assert len(va) >= 1

    md = huduser.hud_il("MD", 2020)
    assert len(md) >= 1
    
    ca = huduser.hud_il("CA", 2019)
    assert len(ca) >= 1
    
    al = huduser.hud_il("AL", 2018)
    assert len(al) >= 1
    

    mult_state = huduser.hud_il(["AL","MD","CA"], [2018, 2017, 2019])
    assert len(mult_state) >= 1

    with pytest.warns(None) as e_info:
        huduser.hud_il("PR")

    with pytest.warns(None) as e_info:
        huduser.hud_il("DC")

    hud_states = hudmisc.hud_nation_states_territories()
    hud_states = hud_states[hud_states["state_num"] < 57]
    hud_states = hud_states[hud_states["state_code"] != "DC"]

    all_state_full = huduser.hud_il(list(hud_states["state_name"]))
    assert len(all_state_full) >= 1

    all_state_abbr = huduser.hud_il(list(hud_states["state_code"]))
    assert len(all_state_abbr) >= 1

    all_state_num = huduser.hud_il(list(hud_states["state_num"]))
    assert len(all_state_num) >= 1

    # check that they are all identical
    assert all_state_full.equals(all_state_abbr) and \
           all_state_full.equals(all_state_num) and \
           all_state_num.equals(all_state_abbr) 
    

@pytest.mark.skipif(os.getenv("HUD_KEY") == None, reason="HUD_KEY not available.")
def test_il_county_queries():
    county = huduser.hud_il("5100199999", 2020)
    assert len(county) >= 1 

    county = huduser.hud_il("5100199999", 2019)
    assert len(county) >= 1 

    county = huduser.hud_il("5100199999", 2018)
    assert len(county) >= 1 

    all_md_counties = hudmisc.hud_state_counties("MD")

    all_md = huduser.hud_il(list(all_md_counties["fips_code"]))
    assert len(all_md) == len(list(all_md_counties["fips_code"]))


@pytest.mark.skipif(os.getenv("HUD_KEY") == None, reason="HUD_KEY not available.")
def test_il_small_area_queries():
    sa1 = huduser.hud_il("METRO47900M47900", year = 2018)
    assert len(sa1) >= 1

    sa2 = huduser.hud_il("METRO29180N22001", year = 2019)
    assert len(sa2) >= 1
    
    sa3 = huduser.hud_il("METRO10380M10380", year = 2020)
    assert len(sa3) >= 1

    all_md_metro = hudmisc.hud_state_metropolitan("MD")
    all_md = huduser.hud_il(list(all_md_metro["cbsa_code"]))

    assert len(all_md) == len(all_md_metro["cbsa_code"])


@pytest.mark.skipif(os.getenv("HUD_KEY") == None, reason="HUD_KEY not available.")
def test_il_diff_years():
    y1 = huduser.hud_il("VA", 2021)
    assert len(y1) == 1

    y1 = huduser.hud_il("WY", [2021, 2019])
    assert len(y1) == 2

    y1 = huduser.hud_il("MD", [2021, 2018])
    assert len(y1) == 2

    y1 = huduser.hud_il("CA", [2021, 2018])
    assert len(y1) == 2

    y1 = huduser.hud_il("NY", [2021, 2021])
    assert len(y1) == 1