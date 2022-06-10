import pytest
import os
from hudpy import hud_geo_in_geo


@pytest.mark.skipif(os.getenv("HUD_KEY") == None, reason="HUD_KEY not available.")
def test_z_in_trt():
  # Invalid zipcode 34321 should throw warning...


    with pytest.warns(Warning) as e_info:
        assert hud_geo_in_geo.z_in_trt(zip = [35213, 34321], tract = ["01073010801"]) == [True, False]

    assert hud_geo_in_geo.z_in_trt(zip = [77032, 77396], tract = [24033800608]) == [False, False]

    assert hud_geo_in_geo.z_in_trt(zip = [20774, 20772], tract = [24033800608]) == [True, True]

    with pytest.raises(Exception) as e_info:
        hud_geo_in_geo.z_in_trt(zip = [20774, 1], tract = [24033800608])
    
    with pytest.raises(Exception) as e_info:
        hud_geo_in_geo.z_in_trt(zip = [20774, 20772], tract = [240338008])


@pytest.mark.skipif(os.getenv("HUD_KEY") == None, reason="HUD_KEY not available.")
def test_z_in_cty():
    assert hud_geo_in_geo.z_in_cty(zip = 71052, county = 22031) == [True]

    assert hud_geo_in_geo.z_in_cty(zip = [71049, 71052, 71419, 71027], county = 22031) == [True, True, True, True]

    with pytest.raises(Exception) as e_info:
        hud_geo_in_geo.z_in_cty(zip = [20774, 1], county = [24033800])

    with pytest.raises(Exception) as e_info:
        hud_geo_in_geo.z_in_cty(zip = [20774, 20772], county = [240338008])


@pytest.mark.skipif(os.getenv("HUD_KEY") == None, reason="HUD_KEY not available.")
def test_z_in_cbsa():

    assert hud_geo_in_geo.z_in_cbsa(zip = 71052, cbsa = 43340) == [True]

    assert hud_geo_in_geo.z_in_cbsa(zip = 98569, cbsa = 10140) == [True]

    hud_geo_in_geo.z_in_cbsa(zip = [98520, 98541, 98526, 98571, 98559, 98583], cbsa = 10140) == \
                [True, True, True, True, True, True]

    with pytest.raises(Exception) as e_info:
        hud_geo_in_geo.z_in_cbsa(zip = [98520, 12], cbsa = [10140])
    with pytest.raises(Exception) as e_info:
        hud_geo_in_geo.z_in_cbsa(zip = [20774, 12222], cbsa = [1014033])


@pytest.mark.skipif(os.getenv("HUD_KEY") == None, reason="HUD_KEY not available.")
def test_z_in_cbsadiv():
    with pytest.warns(Warning) as e_info:
        assert hud_geo_in_geo.z_in_cbsadiv(zip = 35235, cbsadiv = 13820) == [False]
        
    with pytest.warns(Warning) as e_info:
        assert hud_geo_in_geo.z_in_cbsadiv(zip = 35071, cbsadiv = 13820) == [False]

    with pytest.raises(Exception) as e_info:
        hud_geo_in_geo.z_in_cbsadiv(zip = [98520, 12], cbsadiv =[1014220])

    with pytest.raises(Exception) as e_info:
        hud_geo_in_geo.z_in_cbsadiv(zip = [20774, 122], cbsadiv = [1014033])


@pytest.mark.skipif(os.getenv("HUD_KEY") == None, reason="HUD_KEY not available.")
def test_z_in_ctysb():
    assert hud_geo_in_geo.z_in_ctysb(zip = 44214, countysub = 3910383426) == [True]

    assert hud_geo_in_geo.z_in_ctysb(zip = 44256, countysub = 3910383426) == [True]

    assert hud_geo_in_geo.z_in_ctysb(zip = [44273, 44256, 44254, 44217, 44215, 44251], \
                            countysub = 3910383426) == [True, True, True, True, True, True]
    
    with pytest.raises(Exception) as e_info:
        assert hud_geo_in_geo.z_in_ctysb(zip = [98520, 12], countysub = [1014220])
    
    with pytest.raises(Exception) as e_info:
        assert hud_geo_in_geo.z_in_ctysb(zip = [20774, 122], countysub = [1014033])


@pytest.mark.skipif(os.getenv("HUD_KEY") == None, reason="HUD_KEY not available.")
def test_z_in_cd():

    assert hud_geo_in_geo.z_in_cd(zip = 70072, cd = 2202) == [True]

    assert hud_geo_in_geo.z_in_cd(zip = 70117, cd = 2202) == [True]

    assert hud_geo_in_geo.z_in_cd(zip = [70743, 70808], cd = 2202) == [True, True]
    
    with pytest.raises(Exception) as e_info:
        hud_geo_in_geo.z_in_cd(zip = [98520, 12], cd = [1014220])
    
    with pytest.raises(Exception) as e_info:
        hud_geo_in_geo.z_in_cd(zip = [20774, 122], cd = [1014033])


@pytest.mark.skipif(os.getenv("HUD_KEY") == None, reason="HUD_KEY not available.")
def test_trt_in_z():
  # In this case we see that numeric inputs with leading zero get truncated..
  # need to fix that.

    assert hud_geo_in_geo.trt_in_z(tract = "01073005600", zip = 35213) == [True]

    assert hud_geo_in_geo.trt_in_z(tract = "01073002306", zip = 35213) == [True]

    assert hud_geo_in_geo.trt_in_z(tract = ["01073010805", "01073010801"], zip = 35213), [True, True]

    with pytest.raises(Exception) as e_info:
        hud_geo_in_geo.trt_in_z(tract = [98520, 12], zip = [1014220])
    
    with pytest.raises(Exception) as e_info:
        hud_geo_in_geo.trt_in_z(tract = [20774, 122], zip = [1014033])


@pytest.mark.skipif(os.getenv("HUD_KEY") == None, reason="HUD_KEY not available.")
def test_cty_in_z():

    assert hud_geo_in_geo.cty_in_z(county = 24027, zip = 21043) == [True]

    assert hud_geo_in_geo.cty_in_z(county = 24005, zip = 21043) == [True]

    assert hud_geo_in_geo.cty_in_z(county = [24027, 24005], zip = [21043]) == [True, True]

    with pytest.raises(Exception) as e_info:
        hud_geo_in_geo.cty_in_z(county = [98520, 12], zip = [1014220])
    
    with pytest.raises(Exception) as e_info:
        hud_geo_in_geo.cty_in_z(county = [20774, 122], zip = [1014033])


@pytest.mark.skipif(os.getenv("HUD_KEY") == None, reason="HUD_KEY not available.")
def test_cbsa_in_z():

    assert hud_geo_in_geo.cbsa_in_z(cbsa = 32300, zip = 24054) == [True]

    assert hud_geo_in_geo.cbsa_in_z(cbsa = 19260, zip = 24054) == [True]

    assert hud_geo_in_geo.cbsa_in_z(cbsa = [32300, 19260], zip = 24054) == \
                [True, True]
    
    
    with pytest.raises(Exception) as e_info:
        hud_geo_in_geo.cbsa_in_z(cbsa = [98520, 12], zip = [1014220])
    
    with pytest.raises(Exception) as e_info:
        hud_geo_in_geo.cbsa_in_z(cbsa = [20774, 122], zip = [1014033])



@pytest.mark.skipif(os.getenv("HUD_KEY") == None, reason="HUD_KEY not available.")
def test_cbsadiv_in_z():
    with pytest.warns(Warning) as e_info:
        assert hud_geo_in_geo.cbsadiv_in_z(cbsadiv = 32300, zip = 24054) == [False]
    with pytest.warns(Warning) as e_info:
        assert hud_geo_in_geo.cbsadiv_in_z(cbsadiv = 19260, zip = 24054) == [False]
    with pytest.warns(Warning) as e_info:
        hud_geo_in_geo.cbsadiv_in_z(cbsadiv = [32300, 19260], zip = 24054)


    with pytest.raises(Exception) as e_info:
        hud_geo_in_geo.cbsadiv_in_z(cbsadiv = [98520, 12], zip = 1014220)

    with pytest.raises(Exception) as e_info:
        hud_geo_in_geo.cbsadiv_in_z(cbsadiv = [20774, 122], zip = 1014033)


@pytest.mark.skipif(os.getenv("HUD_KEY") == None, reason="HUD_KEY not available.")
def test_cd_in_z():

    assert hud_geo_in_geo.cd_in_z(cd = 5109, zip = 24059) == [True]

    assert hud_geo_in_geo.cd_in_z(cd = 5105, zip = 24059) == [True]

    with pytest.warns(Warning) as e_info:
        assert hud_geo_in_geo.cd_in_z(cd = [5109, 5105, 5106, 4332], zip = 24059) == [True, True, True, False]

    with pytest.raises(Exception) as e_info:
        hud_geo_in_geo.cd_in_z(cd = [98520, 12], zip = [1014220])

    with pytest.raises(Exception) as e_info:
        hud_geo_in_geo.cd_in_z(cd = [20774, 122], zip = [1014033])


@pytest.mark.skipif(os.getenv("HUD_KEY") == None, reason="HUD_KEY not available.")
def test_ctysb_in_z():

    assert hud_geo_in_geo.ctysb_in_z(countysub = 3910371488, zip = 44273) == [True]

    assert hud_geo_in_geo.ctysb_in_z(countysub = 3916950666, zip = 44273) == [True]

    assert hud_geo_in_geo.ctysb_in_z(countysub = [3910383426, 3910330660], zip = 44273) == [True, True]

    with pytest.raises(Exception) as e_info:
        hud_geo_in_geo.ctysb_in_z(countysub = [98520, 12], zip = [1014220])

    with pytest.raises(Exception) as e_info:
        hud_geo_in_geo.ctysb_in_z(countysub = [20774, 122], zip = [1014033])
