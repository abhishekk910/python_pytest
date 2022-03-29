import pytest 

def test_div_by_5(input_total):
    assert input_total % 5 == 0

def test_div_by_7(input_total):
    assert input_total % 7 == 0

def test_div_by_9(input_total):
    assert input_total % 9 == 0

def test_div_by_10(input_total):
    assert input_total % 10 == 0

