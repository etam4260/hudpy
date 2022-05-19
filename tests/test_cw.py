import hudpy
import pytest
import os

@pytest.mark.skipif(os.getenv("HUD_KEY") == "", "HUD_KEY not available.")
def test_cw_all_types():

@pytest.mark.skipif(os.getenv("HUD_KEY") == "", "HUD_KEY not available.")
def test_cw_diff_years():

@pytest.mark.skipif(os.getenv("HUD_KEY") == "", "HUD_KEY not available.")
def test_cw_wrong_query():

@pytest.mark.skipif(os.getenv("HUD_KEY") == "", "HUD_KEY not available.")
def test_not_convert_int():


if __name__ == '__main__':
    pytest.main()
