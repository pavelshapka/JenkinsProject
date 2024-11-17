from app import add, sub

def test_add():
    assert add(5., 7.) == 12.

def test_sub():
    assert sub(5., 7.) == -2.