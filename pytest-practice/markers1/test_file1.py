import pytest
import sys
import math

@pytest.mark.skip
def test_f1():
    res = sum(1,4)
    assert res == 10

@pytest.mark.skipif(sys.version_info < (4, 10), reason="use python 3.9")
def test_f2():
    res = "hello ".join("world")
    assert res == "Hello world"

@pytest.mark.xfail(sys.platform == "win32", reason = "just checking")
def test_f3():
    assert [1]+[2] == [1,2]
    raise Exception