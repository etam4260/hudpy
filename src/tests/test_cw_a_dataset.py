import pytest
import os
import pandas as pd

from hudpy import hud_dataset_cw

@pytest.mark.skipif(os.getenv("HUD_KEY") == None, reason="HUD_KEY not available.")
def test_simple_cw():
    
    data = {'mes': [1232, 2453, 4564], 'zip': [21206, 21224, 20854]}
    sample = pd.DataFrame(data)

    
    cw = hud_dataset_cw.crosswalk(sample, "zip", "zip", "county",
                                 year = 2018,
                                 quarter = 1)
    assert len(cw) >= 1

    cw = hud_dataset_cw.crosswalk(sample, "zip", "zip", "county", "mes", "res",
                                 2018, 1)
    
    assert len(cw) >= 1

    cw = hud_dataset_cw.crosswalk(sample, "zip", "zip", "county", "mes", "bus",
                            2018, 1)
    assert len(cw) >= 1

    cw = hud_dataset_cw.crosswalk(sample, "zip", "zip", "county", "mes", "oth",
                                2018, 1)
    assert len(cw) >= 1

    cw = hud_dataset_cw.crosswalk(sample, "zip", "zip", "county", "mes", "tot",
                                2018, 1)
    assert len(cw) >= 1


    cw = hud_dataset_cw.crosswalk(sample, "zip", "zip", "tract",
                                 year = 2018,
                                 quarter = 1)
    assert len(cw) >= 1



    cw = hud_dataset_cw.crosswalk(sample, "zip", "zip", "tract", "mes", "res",
                                 2018, 1)
    assert len(cw) >= 1

    cw = hud_dataset_cw.crosswalk(sample, "zip", "zip", "tract", "mes", "bus",
                            2018, 1)
    assert len(cw) >= 1

    cw = hud_dataset_cw.crosswalk(sample, "zip", "zip", "tract", "mes", "oth",
                                2018, 1)
    assert len(cw) >= 1

    cw = hud_dataset_cw.crosswalk(sample, "zip", "zip", "tract", "mes", "tot",
                                2018, 1)
    assert len(cw) >= 1




    cw = hud_dataset_cw.crosswalk(sample, "zip", "zip", "cbsa", "mes", "res",
                                 2018, 1)
    assert len(cw) >= 1

    cw = hud_dataset_cw.crosswalk(sample, "zip", "zip", "cbsa", "mes", "bus",
                            2018, 1)
    assert len(cw) >= 1

    cw = hud_dataset_cw.crosswalk(sample, "zip", "zip", "cbsa", "mes", "oth",
                                2018, 1)
    assert len(cw) >= 1

    cw = hud_dataset_cw.crosswalk(sample, "zip", "zip", "cbsa", "mes", "tot",
                                2018, 1)
    assert len(cw) >= 1



    cw = hud_dataset_cw.crosswalk(sample, "zip", "zip", "cbsadiv", "mes", "res",
                                 2018, 1)
    assert len(cw) >= 1

    cw = hud_dataset_cw.crosswalk(sample, "zip", "zip", "cbsadiv", "mes", "bus",
                            2018, 1)
    assert len(cw) >= 1

    cw = hud_dataset_cw.crosswalk(sample, "zip", "zip", "cbsadiv", "mes", "oth",
                                2018, 1)
    assert len(cw) >= 1

    cw = hud_dataset_cw.crosswalk(sample, "zip", "zip", "cbsadiv", "mes", "tot",
                                2018, 1)
    assert len(cw) >= 1



    cw = hud_dataset_cw.crosswalk(sample, "zip", "zip", "cd", "mes", "res",
                                 2018, 1)
    assert len(cw) >= 1

    cw = hud_dataset_cw.crosswalk(sample, "zip", "zip", "cd", "mes", "bus",
                            2018, 1)
    assert len(cw) >= 1

    cw = hud_dataset_cw.crosswalk(sample, "zip", "zip", "cd", "mes", "oth",
                                2018, 1)
    assert len(cw) >= 1

    cw = hud_dataset_cw.crosswalk(sample, "zip", "zip", "cd", "mes", "tot",
                                2018, 1)
    assert len(cw) >= 1



    cw = hud_dataset_cw.crosswalk(sample, "zip", "zip", "cd", "mes", "res",
                                 2018, 1)
    assert len(cw) >= 1

    cw = hud_dataset_cw.crosswalk(sample, "zip", "zip", "cd", "mes", "bus",
                            2018, 1)
    assert len(cw) >= 1

    cw = hud_dataset_cw.crosswalk(sample, "zip", "zip", "cd", "mes", "oth",
                                2018, 1)
    assert len(cw) >= 1

    cw = hud_dataset_cw.crosswalk(sample, "zip", "zip", "cd", "mes", "tot",
                                2018, 1)
    assert len(cw) >= 1

@pytest.mark.skipif(os.getenv("HUD_KEY") == None, reason="HUD_KEY not available.")
def test_awkward_cw():
    sample = pd.DataFrame({"mes": [1232, 1232, 1232], "zip": [21206, 21206, 21206]})

    cw = hud_dataset_cw.crosswalk(sample, "zip", "zip", "county", year = 2018,
              quarter = 1)

    cw = hud_dataset_cw.crosswalk(sample, "zip", "zip", "county", "mes", "res",
              2018, 1)

    sample = pd.DataFrame({"mes": [1232, 1232, 1232], "zip": [21206, 21206, 21206767]})

    with pytest.raises(ValueError) as e_info:
        hud_dataset_cw.crosswalk(sample, "zip", "zip", "county", year = 2018,
                                          quarter = 1)