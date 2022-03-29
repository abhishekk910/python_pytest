import pytest
import mathlib

@pytest.mark.parametrize("input, output",[(5, 25), (6, 35), (7, 49)])
def test_multiplication_11(input, output):
   result = mathlib.cal_square(input) 
   assert result == output 