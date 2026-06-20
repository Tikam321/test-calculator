from calculator import add, subtract, multiply, divide


def test_add():
    assert add(2, 3) == 5, "add(2, 3) should be 5"


def test_subtract():
    assert subtract(5, 3) == 2, "subtract(5, 3) should be 2"


def test_multiply():
    assert multiply(2, 3) == 6, "multiply(2, 3) should be 6"


def test_divide():
    assert divide(10, 2) == 5, "divide(10, 2) should be 5"


def test_divide_by_zero():
    try:
        divide(10, 0)
        assert False, "Should raise ValueError"
    except ValueError:
        pass
