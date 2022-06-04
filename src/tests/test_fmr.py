import pytest
import os
from hudpy import hud_user

@pytest.mark.skipif(os.getenv("HUD_KEY") == None, reason="HUD_KEY not available.")
def test_omni_fmr_state_query():
    
    va = hud_user.hud_fmr("VA", year = [2021])
    assert len(va) >= 1
    
    md = hud_user.hud_fmr("MD", year = ["2021"])
    assert len(md) >= 1

    ca = hud_user.hud_fmr("CA", year = [2021])
    assert len(ca) >= 1 

    al = hud_user.hud_fmr("AL", year = [2021])
    assert len(al) >= 1
    

@pytest.mark.skipif(os.getenv("HUD_KEY") == None, reason="HUD_KEY not available.")
def test_omni_fmr_county_query():
   
    c1 = hud_user.hud_fmr("5100199999", year = [2021])
    assert len(c1) >= 1
    
    c2 = hud_user.hud_fmr("5100199999", year = ["2021"])
    assert len(c2) >= 1
    
    c3 = hud_user.hud_fmr("5151099999", year = [2021])
    assert len(c3) >= 1
    

@pytest.mark.skipif(os.getenv("HUD_KEY") == None, reason="HUD_KEY not available.")
def test_omni_fmr_small_area():
    
    sa1 = hud_user.hud_fmr("METRO47900M47900", year = [2018])
    assert len(sa1) >= 1
    
    sa2 = hud_user.hud_fmr("METRO29180N22001", year = [2019])
    assert len(sa2) >= 1
    
    sa3 = hud_user.hud_fmr("METRO10380M10380", year = [2020])
    assert len(sa3) >= 1


@pytest.mark.skipif(os.getenv("HUD_KEY") == None, reason="HUD_KEY not available.")
def test_omni_fmr_diff_years():
    
    y1 = hud_user.hud_fmr("AL", year = [2020])
    assert len(y1) >= 1
    
    y2 = hud_user.hud_fmr("AL", year = [2021, 2020, 2019, 2018])
    assert len(y2) >= 1
    
    y3 = hud_user.hud_fmr("MD", year = [2020, "2019", 2018])
    assert len(y3) >= 1
    
    y4 = hud_user.hud_fmr("AL", year = [2020, 2020, 2020, 2020])
    assert len(y4) >= 1
    
    y5 = hud_user.hud_fmr("AL", year = [2017])
    assert len(y5) >= 1 
