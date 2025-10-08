import math
import pytest
from calculator import sqrt, factorial, ln, power

def test_sqrt():
    assert pytest.approx(sqrt(4)) == 2
    assert pytest.approx(sqrt(2)) == math.sqrt(2)

def test_sqrt_negative():
    with pytest.raises(ValueError):
        sqrt(-1)

def test_factorial():
    assert factorial(5) == 120
    assert factorial(0) == 1

def test_factorial_negative():
    with pytest.raises(ValueError):
        factorial(-3)

def test_factorial_float_error():
    with pytest.raises(ValueError):
        factorial(4.5)

def test_ln():
    assert pytest.approx(ln(math.e)) == 1

def test_ln_nonpositive():
    with pytest.raises(ValueError):
        ln(0)

def test_power():
    assert pytest.approx(power(2, 3)) == 8
    assert pytest.approx(power(9, 0.5)) == 3
