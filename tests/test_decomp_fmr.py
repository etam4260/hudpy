import hudpy
import pytest
import os


@pytest.mark.skipif(os.getenv("HUD_KEY") == "", "HUD_KEY not available.")
def test_fmr_state_metroareas():


@pytest.mark.skipif(os.getenv("HUD_KEY") == "", "HUD_KEY not available.")
def test_fmr_state_counties():


@pytest.mark.skipif(os.getenv("HUD_KEY") == "", "HUD_KEY not available.")
def test_fmr_county_zip():


@pytest.mark.skipif(os.getenv("HUD_KEY") == "", "HUD_KEY not available.")
def test_fmr_metroarea_zip():


if __name__ == '__main__':
    pytest.main()

