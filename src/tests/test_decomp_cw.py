import hudpy
import pytest
import os

from hudpy import hud_cw
from hudpy import hud_misc


@pytest.mark.skipif(os.getenv("HUD_KEY") == None, reason="HUD_KEY not available.")
def test_cw_zip_tract():
    res = hud_cw.hud_cw_zip_tract(zip = "35213",
                                year = ["2010"], quarter = ["1"])
    assert len(res) >= 1
    
    with pytest.raises(ValueError) as e_info:
        hud_cw.hud_cw_zip_tract(zip = "3521334",
                                year = ["2010"], quarter = ["1"])

    with pytest.raises(ValueError) as e_info:
        hud_cw.hud_cw_zip_tract(zip = ["3521334", "32133"],
                                year = ["2010"], quarter = ["1"])

    res = hud_cw.hud_cw_zip_tract(zip = "35213", year = ["2010"],
                           quarter = ["1"], minimal = True)          
    assert len(res) >= 1


@pytest.mark.skipif(os.getenv("HUD_KEY") == None, reason="HUD_KEY not available.")
def test_cw_zip_county():

    res = hud_cw.hud_cw_zip_county(zip = 35213, year = ["2020"], quarter = ["2"])
    assert len(res) >= 1

    with pytest.raises(ValueError) as e_info:
        hud_cw.hud_cw_zip_county(zip = "3521334",
                                    year = ["2010"], quarter = ["1"])
    with pytest.raises(ValueError) as e_info:
        hud_cw.hud_cw_zip_county(zip = ["3521334", "32133"],
                                    year = ["2010"], quarter = ["1"])

    res = hud_cw.hud_cw_zip_county(zip = "35213", year = ["2010"],
                            quarter = ["1"], minimal = True)
    assert len(res) >= 1


@pytest.mark.skipif(os.getenv("HUD_KEY") == None, reason="HUD_KEY not available.")
def test_cw_zip_cbsa():
    
    res = hud_cw.hud_cw_zip_cbsa(zip = 35213, year = ["2020"], quarter = ["2"])
    assert len(res) >= 1
    with pytest.raises(ValueError) as e_info:
        hud_cw.hud_cw_zip_cbsa(zip = "3521334",
                                    year = ["2010"], quarter = ["1"])
    with pytest.raises(ValueError) as e_info:
        hud_cw.hud_cw_zip_cbsa(zip = ["3521334", "32133"],
                                    year = ["2010"], quarter = ["1"])

    res = hud_cw.hud_cw_zip_cbsa(zip = "35213", year = ["2010"],
                            quarter = ["1"], minimal = True)
    assert len(res) >= 1


@pytest.mark.skipif(os.getenv("HUD_KEY") == None, reason="HUD_KEY not available.")
def test_cw_zip_cbsadiv():

    res = hud_cw.hud_cw_zip_cbsadiv(zip = 22031, year = ["2020"], quarter = ["2"])
    assert len(res) >= 1
    
    with pytest.raises(ValueError) as e_info:
        hud_cw.hud_cw_zip_cbsadiv(zip = "3521334",
                                    year = ["2018"], quarter = ["1"])
    with pytest.raises(ValueError) as e_info:
        hud_cw.hud_cw_zip_cbsadiv(zip = ["3521334", "32133"],
                                    year = ["2018"], quarter = ["1"])

    res = hud_cw.hud_cw_zip_cbsadiv(zip = "22031", year = ["2020"],
                            quarter = ["2"], minimal = True)
    assert len(res) >= 1


@pytest.mark.skipif(os.getenv("HUD_KEY") == None, reason="HUD_KEY not available.")
def test_cw_zip_cd():
    
    res = hud_cw.hud_cw_zip_cd(zip = 35213, year = ["2020"], quarter = ["2"])
    assert len(res) >= 1
    with pytest.raises(ValueError) as e_info:
        hud_cw.hud_cw_zip_cd(zip = "3521334",
                                    year = ["2010"], quarter = ["1"])
    with pytest.raises(ValueError) as e_info:
        hud_cw.hud_cw_zip_cd(zip = ["3521334", "32133"],
                                    year = ["2010"], quarter = ["1"])

    res = hud_cw.hud_cw_zip_cd(zip = "35213", year = ["2010"],
                            quarter = ["1"], minimal = True)
    assert len(res) >= 1


@pytest.mark.skipif(os.getenv("HUD_KEY") == None, reason="HUD_KEY not available.")
def test_cw_tract_zip():
    
    res = hud_cw.hud_cw_tract_zip(tract = 48201223100, year = ["2020"], quarter = ["2"])
    assert len(res) >= 1

    with pytest.raises(ValueError) as e_info:
        hud_cw.hud_cw_tract_zip(tract = "4820122310033",
                                    year = ["2010"], quarter = ["1"])
    with pytest.raises(ValueError) as e_info:
        hud_cw.hud_cw_tract_zip(tract = ["35", "32133"],
                                    year = ["2010"], quarter = ["1"])

    res = hud_cw.hud_cw_tract_zip(tract = "48201223100", year = ["2010"],
                            quarter = ["1"], minimal = True)
    assert len(res) >= 1


@pytest.mark.skipif(os.getenv("HUD_KEY") == None, reason="HUD_KEY not available.")
def test_cw_county_zip():

    res = hud_cw.hud_cw_county_zip(county = "22031", year = ["2010"], quarter = ["1"])
    assert len(res) >= 1

    with pytest.raises(ValueError) as e_info:
        hud_cw.hud_cw_county_zip(county = "3521334",
                                 year = ["2010"], quarter = ["1"])

    with pytest.raises(ValueError) as e_info:
        hud_cw.hud_cw_county_zip(county = ["3521334", "32133"],
                                 year = ["2010"], quarter = ["1"])

    res = hud_cw.hud_cw_county_zip(county = "22031", year = ["2010"],
                           quarter = ["1"], minimal = True)
    
    assert len(res) >= 1


    all_md_counties = hud_misc.hud_state_counties("md")
    all_md = hud_cw.hud_cw_county_zip(county = list(map(lambda x: x[0:5], all_md_counties["fips_code"])),
                              year = ["2010"], quarter = ["1"])
    
    assert len(all_md) >= 1

@pytest.mark.skipif(os.getenv("HUD_KEY") == None, reason="HUD_KEY not available.")
def test_cw_cbsa_zip():

    res = hud_cw.hud_cw_cbsa_zip(cbsa = "10140", year = ["2010"], quarter = ["1"])
    assert len(res) >= 1

    with pytest.raises(ValueError) as e_info:
        hud_cw.hud_cw_cbsa_zip(cbsa = "3521334",
                                 year = ["2010"], quarter = ["1"])

    with pytest.raises(ValueError) as e_info:
        hud_cw.hud_cw_cbsa_zip(cbsa = ["3521334", "32133"],
                                 year = ["2010"], quarter = ["1"])

    res = hud_cw.hud_cw_cbsa_zip(cbsa = "10140", year = ["2010"],
                           quarter = ["1"], minimal = True)
    
    assert len(res) >= 1

@pytest.mark.skipif(os.getenv("HUD_KEY") == None, reason="HUD_KEY not available.")
def test_cw_cbsadiv_zip():

    res = hud_cw.hud_cw_cbsadiv_zip(cbsadiv = "10380", year = ["2017"], quarter = ["4"])
    assert len(res) >= 1

    with pytest.raises(ValueError) as e_info:
        hud_cw.hud_cw_cbsadiv_zip(cbsadiv = "3521334",
                                 year = ["2017"], quarter = ["4"])

    with pytest.raises(ValueError) as e_info:
        hud_cw.hud_cw_cbsadiv_zip(cbsadiv = ["3521334", "32133"],
                                 year = ["2017"], quarter = ["4"])

    res = hud_cw.hud_cw_cbsadiv_zip(cbsadiv = 10380, year = ["2017"],
                           quarter = ["4"], minimal = True)
    
    assert len(res) >= 1

@pytest.mark.skipif(os.getenv("HUD_KEY") == None, reason="HUD_KEY not available.")
def test_cw_cd_zip():
    
    res = hud_cw.hud_cw_cd_zip(cd= "2202", year = ["2010"], quarter = ["1"])
    assert len(res) >= 1

    with pytest.raises(ValueError) as e_info:
        hud_cw.hud_cw_cd_zip(cd = "3521334",
                                 year = ["2010"], quarter = ["1"])

    with pytest.raises(ValueError) as e_info:
        hud_cw.hud_cw_cd_zip(cd = ["3521334", "32133"],
                                 year = ["2010"], quarter = ["1"])

    res = hud_cw.hud_cw_cd_zip(cd = 2202, year = ["2010"],
                           quarter = ["1"], minimal = True)
    
    assert len(res) >= 1

@pytest.mark.skipif(os.getenv("HUD_KEY") == None, reason="HUD_KEY not available.")
def test_cw_zip_countysub():
    res = hud_cw.hud_cw_zip_countysub(zip = "35213",
                                year = ["2019"], quarter = ["1"])
    assert len(res) >= 1
    
    with pytest.raises(ValueError) as e_info:
        hud_cw.hud_cw_zip_countysub(zip = "3521334",
                                year = ["2010"], quarter = ["1"])

    with pytest.raises(ValueError) as e_info:
        hud_cw.hud_cw_zip_countysub(zip = ["3521334", "32133"],
                                year = ["2010"], quarter = ["1"])

    res = hud_cw.hud_cw_zip_countysub(zip = "35213", year = ["2019"],
                           quarter = ["1"], minimal = True)          
    assert len(res) >= 1


@pytest.mark.skipif(os.getenv("HUD_KEY") == None, reason="HUD_KEY not available.")
def test_cw_countysub_zip():
    res = hud_cw.hud_cw_countysub_zip(countysub = "4606720300 ", year = ["2019"], quarter = ["1"])
    assert len(res) >= 1

    with pytest.raises(ValueError) as e_info:
        hud_cw.hud_cw_countysub_zip(countysub = "4606720",
                                 year = ["2010"], quarter = ["1"])

    with pytest.raises(ValueError) as e_info:
        hud_cw.hud_cw_countysub_zip(countysub = ["3521334", "32133"],
                                 year = ["2010"], quarter = ["1"])

    res = hud_cw.hud_cw_countysub_zip(countysub = 4606720300, year = ["2019"],
                           quarter = ["1"], minimal = True)
    
    assert len(res) >= 1
