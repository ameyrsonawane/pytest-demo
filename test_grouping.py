import pytest

@pytest.mark.sanity
def testfirstname():
    print("Amey")


@pytest.mark.sanity
def testmiddlename():
    print("Rajendra")

@pytest.mark.regression
def testsurname():
    print("Sonawane")

@pytest.mark.regression
def testminus():
    assert 5-2==3

@pytest.mark.sanity
def testaddition():
    assert 7+3==11

@pytest.mark.regression
def testdivision():
    assert 10/2==5

@pytest.mark.skip
def testselenium():
    print("Pass")

@pytest.mark.xfail
def testyes():
    print("Pass")


@pytest.mark.xfail
def testno():
    print("Pass")

@pytest.mark.sanity
def testok():
    print("Pass")