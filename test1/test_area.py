import pytest 
import area

def test_area():
    output = area.area_of_rectangle(10, 20)
    assert output == 200

def test_perimeter():
    output = area.perimeter_of_rectangle(10, 15)
    assert output == 50

