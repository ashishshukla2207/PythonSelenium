import pytest


@pytest.mark.skip
def test_firsttest():
    msg = "Hello"
    assert msg == "Hi", "Test Failed because string mismatched"


@pytest.mark.smoke
def test_Calculation2():
    a = 4;
    b = 3;

    assert a + 2 == 6, "Addition match"
    print("TestPass")


@pytest.mark.xfail
def test_calculatesqr():
    l = 23
    assert l**2 == 546, "Correct"


def test_add(setup):
    print("I do what my method say")