#similar to before menthod and after method in java
import pytest


@pytest.fixture()
def setup():  #before method
    print("I will be executed first")
    yield
    print("I am the teardown method") #aftermethod


def test_fixture(setup):
    print("I will execute test in the fixture method")



