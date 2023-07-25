import pytest

from pytestDemo.BaseClass import BaseClass

@pytest.mark.usefixtures("dataLoad")
class TestExample2(BaseClass):
    def test_editProfile(self, dataLoad):
        log= self.getLogger()
        print(dataLoad)
        log.info(print(dataLoad[0]))
        log.info(print(dataLoad[1]))