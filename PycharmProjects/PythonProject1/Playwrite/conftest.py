import pytest

#what ever fixtures are declared here in conftest file
#it will have access to all the file within that directory
@pytest.fixture(scope="session")
def user_cred_fixture(request):
    return request.param
#*******************************************
#key feature of PYTEST is that it gives us option to use something called
# "REQUEST" : is a parameter, global request parameter used to access global environment variables as well as local Pytest variables

