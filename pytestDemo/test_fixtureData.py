#similar to before menthod and after method in java
import pytest



@pytest.mark.usefixtures("setup")
class TestExample:


    def test_fixture(self):
        print("I will execute test in the fixture method")


    def test_fixtureDemo1(self):
        print("I am part of fixture demo")

    def test_fixtureDemo2(self):
        print("I am part of fixture demo")

    def test_fixtureDemo3(self):
        print("I am part of fixture demo")

    def test_fixtureDemo4(self):
        print("I am part of fixture demo")


