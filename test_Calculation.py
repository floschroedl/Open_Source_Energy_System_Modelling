from Calculation import add
from Calculation import sub
from Calculation import div
from Calculation import mul

def test_add():
    assert add(1, 2) == 3
    assert add(4, 5) == 9
    assert add (101, 105) == 206

def test_sub():
    assert sub(5, 2) == 3
    assert sub(17, 11) == 6
    assert sub (206, 101) == 105

def test_div():
    assert div(10, 2) == 5
    assert div( 15, 5) == 3
    assert div (36, 6) == 6

def test_mul():
    assert mul(2, 3) == 6
    assert mul(3, 7) == 21
    assert mul(4, 8) == 32

