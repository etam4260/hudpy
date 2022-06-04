import pytest
import os
from hudpy import hud_fmr

@pytest.mark.skipif(os.getenv("HUD_KEY") == None, reason="HUD_KEY not available.")
def test_fmr_state_metroareas():
    va = hud_fmr.hud_fmr_state_metroareas("VA", year = [2021])
    assert len(va) >= 1

    md = hud_fmr.hud_fmr_state_metroareas("MD", year = ["2021"])
    assert len(md) >= 1
    
    ca = hud_fmr.hud_fmr_state_metroareas("CA", year = [2021])
    assert len(ca) >= 1
    
    al = hud_fmr.hud_fmr_state_metroareas("AL", year = [2021])
    assert len(al) >= 1


@pytest.mark.skipif(os.getenv("HUD_KEY") == None, reason="HUD_KEY not available.")
def test_fmr_state_counties():
    va = hud_fmr.hud_fmr_state_counties("VA", year = [2021])
    assert len(va) >= 1

    md = hud_fmr.hud_fmr_state_counties("MD", year = ["2021"])
    assert len(md) >= 1

    ca = hud_fmr.hud_fmr_state_counties("CA", year = [2021])
    assert len(ca) >= 1

    al = hud_fmr.hud_fmr_state_counties("AL", year = [2021])
    assert len(al) >= 1

@pytest.mark.skipif(os.getenv("HUD_KEY") == None, reason="HUD_KEY not available.")
def test_fmr_county_zip():
    c1 = hud_fmr.hud_fmr_county_zip("5100199999", year = [2021])
    assert len(c1) >= 1
    
    c2 = hud_fmr.hud_fmr_county_zip("5100199999", year = ["2021"])
    assert len(c2) >= 1
    
    c3 = hud_fmr.hud_fmr_county_zip("5151099999", year = [2021])
    assert len(c3) >= 1
    
@pytest.mark.skipif(os.getenv("HUD_KEY") == None, reason="HUD_KEY not available.")
def test_fmr_metroarea_zip():
    sa1 = hud_fmr.hud_fmr_metroarea_zip("METRO47900M47900", year = [2018])
    assert len(sa1) >= 1
    
    sa2 = hud_fmr.hud_fmr_metroarea_zip("METRO29180N22001", year = [2019])
    assert len(sa2) >= 1
    
    sa3 = hud_fmr.hud_fmr_metroarea_zip("METRO10380M10380", year = [2020])
    assert len(sa3) >= 1
