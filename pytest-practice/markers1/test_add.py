import pytest
from add import add


@pytest.mark.parametrize("ip1, ip2, op",
                         [('a', 'b','c'), (1,2,3), (1.2, 2.3, 3), ([1],[2],[1,2])],
                         ids = ["string", "numbers", "float", "lists"])
def test_f1(ip1, ip2, op):
    assert add(ip1,ip2) == op
