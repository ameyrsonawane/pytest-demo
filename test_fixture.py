# Fixture provide a fixed baseline upon which test can reliably and repeatedly executed.
# @pytest.fixture()- Execute specific method before every test method
# @pytest.yield_fixture()- Execute specific method before and after every test method.


# @pytest.fixture()

'''import pytest

@pytest.fixture()
def setup():
    print("Before every method")

def testmethod1(setup):
    print("Method1")

def testmethod2():
    print("Method2")'''


# @pytest.yield_fixture()

import pytest

@pytest.yield_fixture()
def setup():
    print("Before every method")
    yield
    print("after every method")
def testmethod1(setup):
    print("Method1")

def testmethod2(setup):
    print("Method2")

# Examples

''''import pytest

@pytest.fixture()
def input_value():
    input=3
    return input.
def test_addition(input_value):
    assert input_value+5==8

def testmultiflication(input_value):
    assert input_value*5==15'''



