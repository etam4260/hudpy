import hudpy
import pytest
import hudpy.huddatasetcw
import pandas as pd

def test_simple_cw():
    sample = pd.DataFrame(mes = list(1232, 2453, 4564),
                          zip = list(21206, 21224, 20854))

    cw = hudpy.huddatasetcw.crosswalk(sample, "zip", "zip", "county",
                                 year = 2018,
                                 quarter = 1)
    assert len(cw) >= 1

    cw = hudpy.huddatasetcw.crosswalk(sample, "zip", "zip", "county", "mes", "res",
                                 2018, 1)
    assert len(cw) >= 1





def test_awkward_cw():


if __name__ == '__main__':
    pytest.main()
