import pytest

def test_with_data_fixture(five_fixture):
    print("\nRunning test_with_data_fixture: {}".format(five_fixture))
    assert five_fixture == 8

@pytest.fixture
def five_fixture():
    print("\n(Returning" . five_fixture . " from data_fixture)")
    return 5