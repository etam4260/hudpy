import hudpy
import pytest
import os

@pytest.mark.skipif(os.getenv("HUD_KEY") == "", "HUD_KEY not available.")
def test_chas_all_types():

@pytest.mark.skipif(os.getenv("HUD_KEY") == "", "HUD_KEY not available.")
def test_chas_diff_years():



if __name__ == '__main__':
    pytest.main()

