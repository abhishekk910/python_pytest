import pytest 

def func_add(x):
    return x + 5

def test_func():
    assert func_add(9) == 10

