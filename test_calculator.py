from calculator import add, subtract, multiply, divide
import pytest

# --- Tests for `add` ---
def test_add_positive_numbers():
    assert add(2, 3) == 5, "add(2, 3) should be 5"

def test_add_negative_numbers():
    assert add(-1, -1) == -2, "add(-1, -1) should be -2"

def test_add_mixed_numbers():
    assert add(-1, 1) == 0, "add(-1, 1) should be 0"

def test_add_zero():
    assert add(0, 0) == 0, "add(0, 0) should be 0"
    assert add(5, 0) == 5, "add(5, 0) should be 5"
    assert add(0, -3) == -3, "add(0, -3) should be -3"

# --- Tests for `subtract` ---
def test_subtract_positive_numbers():
    assert subtract(5, 3) == 2, "subtract(5, 3) should be 2"

def test_subtract_negative_numbers():
    assert subtract(-1, -1) == 0, "subtract(-1, -1) should be 0"

def test_subtract_mixed_numbers():
    assert subtract(1, -1) == 2, "subtract(1, -1) should be 2"
    assert subtract(-1, 1) == -2, "subtract(-1, 1) should be -2"

def test_subtract_zero():
    assert subtract(0, 0) == 0, "subtract(0, 0) should be 0"
    assert subtract(5, 0) == 5, "subtract(5, 0) should be 5"
    assert subtract(0, 3) == -3, "subtract(0, 3) should be -3"

# --- Tests for `multiply` ---
def test_multiply_positive_numbers():
    assert multiply(2, 3) == 6, "multiply(2, 3) should be 6"

def test_multiply_negative_numbers():
    assert multiply(-1, -1) == 1, "multiply(-1, -1) should be 1"
    assert multiply(-2, 3) == -6, "multiply(-2, 3) should be -6"

def test_multiply_by_zero():
    assert multiply(0, 5) == 0, "multiply(0, 5) should be 0"
    assert multiply(5, 0) == 0, "multiply(5, 0) should be 0"

def test_multiply_by_one():
    assert multiply(1, 5) == 5, "multiply(1, 5) should be 5"
    assert multiply(5, 1) == 5, "multiply(5, 1) should be 5"

# --- Tests for `divide` ---
def test_divide_positive_numbers():
    assert divide(10, 2) == 5.0, "divide(10, 2) should be 5.0"

def test_divide_negative_numbers():
    assert divide(-10, -2) == 5.0, "divide(-10, -2) should be 5.0"
    assert divide(10, -2) == -5.0, "divide(10, -2) should be -5.0"
    assert divide(-10, 2) == -5.0, "divide(-10, 2) should be -5.0"

def test_divide_by_one():
    assert divide(5, 1) == 5.0, "divide(5, 1) should be 5.0"

def test_divide_fractional_result():
    assert divide(5, 2) == 2.5, "divide(5, 2) should be 2.5"

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)
