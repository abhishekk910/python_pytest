import pytest 

@pytest.fixture(scope="module")
def fixture_func():
    print("Opening the database connection")
    yield
    print("Closing the database connection")


def test_ename(fixture_func):
    print("Fetching Employee name from db") 

def test_eid(fixture_func):
    print("Fetching Employee id from db") 

def test_erole(fixture_func):
    print("Fetching Employee role from db") 