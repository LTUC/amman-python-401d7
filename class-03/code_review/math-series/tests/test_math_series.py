from math_series import __version__

from math_series.series import sum_series

def test_version():
    assert __version__ == '0.1.0'

def test_sum_series_as_fib():
    expected = 5 # n=5 (0,1,1,2,3,5)
    actual = sum_series(5)
    assert expected == actual

def test_sum_series_as_lucas():
    expected = 18 # n=6 (2,1,3,4,7,11,18,29)
    actual = sum_series(6, 2, 1)
    assert expected == actual


# RED GREEEN REFACTOR