#to convert a method into test method just add Test as prefix to method name
import pytest


def test_initialCheck():
    print("This is the first test")

#Fixturs- reusable code can be marked as fixers and use many times
#copy the fixture name and add is as an arrgument to ur actual test method wer we have ti use the ficture
#Fixtures has two types 1.function fixture, 2.module fixyre
# Scope=Function, Scope=Module, scope=class, class and module are almost same scope = session
#yeild keywprd is used to follow all the tear down sessions
@pytest.fixture(scope="function")
def preWork():
    print("I am a browser invoke")
    yield
    print("i will quit the browser")

def test_firstTestcase(preWork):
    print("This is the first test case to use fixture")

def test_useyeild(preWork):
    print("i excecute in use yield")