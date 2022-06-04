import pytest
import os

from hudpy import hud_user

@pytest.mark.skipif(os.getenv("HUD_KEY") == None, reason="HUD_KEY not available.")
def test_chas_all_types():
    
    # Nation
    n = hud_user.hud_chas(1)
    assert len(n) == 1

    # State
    s = hud_user.hud_chas("2", state_id = "56")
    assert len(s) == 1

    # County
    c = hud_user.hud_chas("3", "51", "199")
    assert len(c) == 1

    # MCD
    mcd = hud_user.hud_chas("4", "51", 94087)
    assert len(mcd) == 1

    # place
    city = hud_user.hud_chas("5", "51", 48996)
    assert len(city) == 1


@pytest.mark.skipif(os.getenv("HUD_KEY") == None, reason="HUD_KEY not available.")
def test_chas_diff_years():
    # Only checking entire Nation CHAS and varying different year inputs.

    # 2014-2018
    # 2013-2017
    # 2012-2016
    # 2011-2015
    # 2010-2014
    # 2009-2013
    # 2008-2012
    # 2007-2011
    # 2006-2010

    y1 = hud_user.hud_chas(1, year = ["2014-2018", "2013-2017"])
    assert len(y1) == 2

    y2 = hud_user.hud_chas(1, year = ["2013-2017"])
    assert len(y2) == 1

    y3 = hud_user.hud_chas(1, year = ["2008-2012", "2007-2011", "2014-2018"])
    assert len(y3) == 3

    y4 = hud_user.hud_chas(1, year = ["2012-2016", "2007-2011"])
    assert len(y4) == 2

    y5 = hud_user.hud_chas(1, year = ["2014-2018", "2013-2017"])
    assert len(y5) == 2


