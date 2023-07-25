import pytest


def test_first_test():
    print("Hello")


@pytest.mark.smoke
def test_seconndtest():
    print("Good Morning")


def test_calculation():
    a = 3;
    b = 4;


    assert a*b == 12, "Multiplication success"



def test_crossbrowserfn(crossbrowser):
    print(crossbrowser)
    print(crossbrowser[1])