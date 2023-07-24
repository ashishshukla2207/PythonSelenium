#this file will only have fixture and it will be available to all the files in the folder
#this saves us from writing same fixture again an again

import pytest


@pytest.fixture(scope= "class")
def setup():  #before method
    print("I will be executed first")
    yield
    print("I am the teardown method") #aftermethod



#use @pytest.usefixture(setup) to pass it to all methods at once
#   @pytest.usefixture(setup scope=class)  only once setup will run




@pytest.fixture()
def dataLoad():
    return ["ashish", "shukla", "ashishshukla"]


@pytest.fixture(params =["chrome", "IE", "Safari"])
def crossbrowser(request):
    return request.param