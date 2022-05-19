import hudpy
import pytest
import os


@pytest.mark.skipif(os.getenv("HUD_KEY") == "", "HUD_KEY not available.")
def test_omni_fmr_state_query():


@pytest.mark.skipif(os.getenv("HUD_KEY") == "", "HUD_KEY not available.")
def test_omni_fmr_county_query():


@pytest.mark.skipif(os.getenv("HUD_KEY") == "", "HUD_KEY not available.")
def test_omni_fmr_small_area():


@pytest.mark.skipif(os.getenv("HUD_KEY") == "", "HUD_KEY not available.")
def test_omni_fmr_diff_years():

    


if __name__ == '__main__':
    pytest.main()