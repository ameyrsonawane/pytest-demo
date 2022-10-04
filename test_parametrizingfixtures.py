import pytest

@pytest.mark.parametrize("a,b,final",[(2,6,8),(2,6,11),(19,3,22)])

def testaddition(a,b,final):
    assert a+b==final