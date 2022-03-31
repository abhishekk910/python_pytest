import pytest

def test_f1():
    a = 10
    b = 12
    assert a+2 == b

def test_f2():
    a = "pytest"
    assert a.upper() == "PYTEST"


def test_f3():
    assert False

def test_login_fb():
    print("Logging into FB")

class TestDemo():
    def test_f3(self):
        assert False

    def test_f4(self):
        assert True 
