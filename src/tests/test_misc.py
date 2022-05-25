import pytest
import os
from hudpy import hudmisc

@pytest.mark.skipif(os.getenv("HUD_KEY") == None, reason="HUD_KEY not available.")
def test_misc_mcd_in_state():
    mcd = hudmisc.hud_state_minor_civil_divisions("CA")
    assert len(mcd) > 1

    mcd = hudmisc.hud_state_minor_civil_divisions(["CA"])
    assert len(mcd) > 1


    mcd = hudmisc.hud_state_minor_civil_divisions("6")
    assert len(mcd) > 1

    mcd = hudmisc.hud_state_minor_civil_divisions(["6"])
    assert len(mcd) > 1


    mcd = hudmisc.hud_state_minor_civil_divisions("CA")
    assert len(mcd) > 1

    mcd = hudmisc.hud_state_minor_civil_divisions(["CA"])
    assert len(mcd) > 1

    with pytest.raises(ValueError) as e_info:
        hudmisc.hud_state_minor_civil_divisions("CA", "qdqdwq")


@pytest.mark.skipif(os.getenv("HUD_KEY") == None, reason="HUD_KEY not available.")
def test_misc_cities_in_state():
    cities = hudmisc.hud_state_places("NY")
    assert len(cities) >= 1

    cities = hudmisc.hud_state_places(["NY"])
    assert len(cities) >= 1

    cities = hudmisc.hud_state_places("Texas")
    assert len(cities) >= 1

    cities = hudmisc.hud_state_places(["Texas"])
    assert len(cities) >= 1

    cities = hudmisc.hud_state_places("8")
    assert len(cities) >= 1

    cities = hudmisc.hud_state_places(["8"])
    assert len(cities) >= 1

    with pytest.raises(ValueError) as e_info:
        hudmisc.hud_state_places("CA", "qdqdwq")


@pytest.mark.skipif(os.getenv("HUD_KEY") == None, reason="HUD_KEY not available.")
def test_misc_nation_states():

    states = hudmisc.hud_nation_states_territories()
    
    assert len(states) >= 1

    with pytest.raises(ValueError) as e_info:
        hudmisc.hud_nation_states_territories("CA", "qdqdwq")


@pytest.mark.skipif(os.getenv("HUD_KEY") == None, reason="HUD_KEY not available.")
def test_misc_counties_in_state():
    
    counties = hudmisc.hud_state_counties("MD")   
    assert len(counties) > 1

    counties = hudmisc.hud_state_counties(["MD"])   
    assert len(counties) > 1

    counties = hudmisc.hud_state_counties("Michigan")
    assert len(counties) > 1

    counties = hudmisc.hud_state_counties(["Michigan"])   
    assert len(counties) > 1

    counties = hudmisc.hud_state_counties("Washington")
    assert len(counties) > 1

    counties = hudmisc.hud_state_counties(["Washington"])
    assert len(counties) > 1

    with pytest.raises(ValueError) as e_info:
        hudmisc.hud_state_counties("CA", "qdqdwq")


@pytest.mark.skipif(os.getenv("HUD_KEY") == None, reason="HUD_KEY not available.")
def test_misc_small_areas_in_state():

    metro = hudmisc.hud_state_metropolitan("CA")
    assert len(metro) >= 1

    metro = hudmisc.hud_state_metropolitan("CA")
    assert len(metro) >= 1


    metro = hudmisc.hud_state_metropolitan("1")
    assert len(metro) >= 1

    metro = hudmisc.hud_state_metropolitan(["1"])
    assert len(metro) >= 1


    metro = hudmisc.hud_state_metropolitan("Ohio")
    assert len(metro) >= 1

    metro = hudmisc.hud_state_metropolitan(["Ohio"])
    assert len(metro) >= 1

    with pytest.raises(ValueError) as e_info:
        hudmisc.hud_state_metropolitan("CA", "qdqdwq")