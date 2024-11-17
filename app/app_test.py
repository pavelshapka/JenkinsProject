from app import add, sub, mul

def test_add():
    assert add(5., 7.) == 12.

def test_sub():
    assert sub(5., 7.) == -2.

def test_mul():
    assert mul(5., 7.) == 35.