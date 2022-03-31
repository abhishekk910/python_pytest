import add
import pytest 

@pytest.mark.parametrize('num1, num2, res',
[
    (7, 3, 10),
    ('Hello ', 'world', 'Hello World'),
    (2.2, 3.3, 5.5)
]
)
def test_add(num1, num2, res):
    assert add.add_func(num1, num2) == res 
