import pytest


@pytest.mark.usefixtures("dataLoad")
class Example:
    def test_editprofile(self, dataLoad):
        print(dataLoad[0])
