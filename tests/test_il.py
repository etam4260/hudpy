from hashlib import md5
from nis import cat
import hudpy.huduser
import hudpy.hudmisc
import pytest

@pytest.mark.skipif(os.getenv("HUD_KEY") == 0, "HUD_KEY not available.")
def test_il_state_queries():
    va = hudpy.huduser.hud_il("VA", 2021)
    assert len(va) >= 1

    md = hudpy.huduser.hud_il("MD", 2020)
    assert len(va) >= 1
    
    ca = hudpy.huduser.hud_il("CA", 2019)
    assert len(va) >= 1
    
    al = hudpy.huduser.hud_il("AL", 2018)
    assert len(va) >= 1
    

    mult_state = hudpy.huduser.hud_il(["AL","MD","CA"], [2018, 2017, 2019])
    assert len(mult_state) >= 1

    with pytest.raises(ValueError) as e_info:
        hudpy.huduser.hud_il("PR")

    with pytest.raises(ValueError) as e_info:
        hudpy.huduser.hud_il("DC")

    hud_states = hudpy.hudmisc.hud_nation_states_territories()
    hud_states = hud_states[hud_states["state_num"] < 57]
    hud_states = hud_states[hud_states["state_code"] != "DC"]

    
    
    # check that they are all identical

    
@pytest.mark.skipif(os.getenv("HUD_KEY") == 0, "HUD_KEY not available.")
def test_il_county_queries():

@pytest.mark.skipif(os.getenv("HUD_KEY") == 0, "HUD_KEY not available.")
def test_il_small_area_queries():

@pytest.mark.skipif(os.getenv("HUD_KEY") == 0, "HUD_KEY not available.")
def test_il_diff_years():

if __name__ == '__main__':
    pytest.main()