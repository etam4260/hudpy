import hudpy
import pytest
import os

@pytest.mark.skipif(os.getenv("HUD_KEY") == "", "HUD_KEY not available.")
def test_chas_nation():

@pytest.mark.skipif(os.getenv("HUD_KEY") == "", "HUD_KEY not available.")
def test_chas_state():

@pytest.mark.skipif(os.getenv("HUD_KEY") == "", "HUD_KEY not available.")
def test_chas_county():

@pytest.mark.skipif(os.getenv("HUD_KEY") == "", "HUD_KEY not available.")
def test_chas_mcd():


if __name__ == '__main__':
    pytest.main()
