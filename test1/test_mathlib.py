import mathlib 

def test_calc_addition():
    output = mathlib.calc_addition(2, 4)
    assert output == 6 

def test_calc_substraction():
    output = mathlib.calc_substraction(10, 5)
    assert output == 5 

def test_calc_multiplication():
    output = mathlib.calc_multiplication(2, 4)
    assert output == 8

def test_calc_division():
    output = mathlib.calc_division(4, 4)
    assert output == 1
