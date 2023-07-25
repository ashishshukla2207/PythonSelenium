#this file will only have fixture and it will be available to all the files in the folder
#this saves us from writing same fixture again an again

import pytest


@pytest.fixture(scope= "class")
def setup():  #before method
    print("I will be executed first")
    yield
    print("I am the teardown method") #aftermethod



#use @pytestDemo.usefixture(setup) to pass it to all methods at once
#   @pytestDemo.usefixture(setup scope=class)  only once setup will run




@pytest.fixture(scope= "class")
def dataLoad():
    print("User profile data is being created")
    return ["ashish", "shukla", "ashishshukla"]



@pytest.fixture(params =[("chrome", "Ashish", "Shukla"), "IE", ("Safari", "Hello")])
def crossbrowser(request):
    return request.param