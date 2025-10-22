import pytest
from src.utils import add, subtract, multiply, divide


class TestAdd:
    """Test cases for add function"""

    def test_add_two_numbers(self):
        assert add(2, 3) == 5

    def test_add_multiple_numbers(self):
        assert add(1, 2, 3, 4, 5) == 15

    def test_add_negative_numbers(self):
        assert add(-1, -2, -3) == -6

    def test_add_mixed_numbers(self):
        assert add(10, -5, 3) == 8

    def test_add_zero(self):
        assert add(0, 0, 0) == 0

    def test_add_single_number(self):
        assert add(5) == 5

    def test_add_no_arguments(self):
        assert add() == 0

    def test_add_floats(self):
        assert add(1.5, 2.5, 3.0) == 7.0


class TestSubtract:
    """Test cases for subtract function"""

    def test_subtract_two_numbers(self):
        assert subtract(10, 3) == 7

    def test_subtract_multiple_numbers(self):
        assert subtract(20, 5, 3, 2) == 10

    def test_subtract_negative_numbers(self):
        assert subtract(-5, -3) == -2

    def test_subtract_to_negative(self):
        assert subtract(5, 10) == -5

    def test_subtract_single_number(self):
        assert subtract(5) == 5

    def test_subtract_no_arguments(self):
        assert subtract() == 0

    def test_subtract_floats(self):
        assert subtract(10.5, 2.5, 1.0) == 7.0


class TestMultiply:
    """Test cases for multiply function"""

    def test_multiply_two_numbers(self):
        assert multiply(3, 4) == 12

    def test_multiply_multiple_numbers(self):
        assert multiply(2, 3, 4) == 24

    def test_multiply_by_zero(self):
        assert multiply(5, 0) == 0

    def test_multiply_negative_numbers(self):
        assert multiply(-2, -3) == 6

    def test_multiply_mixed_signs(self):
        assert multiply(-2, 3, -4) == 24

    def test_multiply_single_number(self):
        assert multiply(5) == 5

    def test_multiply_no_arguments(self):
        assert multiply() == 0

    def test_multiply_floats(self):
        assert multiply(2.5, 4.0) == 10.0


class TestDivide:
    """Test cases for divide function"""

    def test_divide_two_numbers(self):
        assert divide(10, 2) == 5

    def test_divide_multiple_numbers(self):
        assert divide(100, 2, 5) == 10

    def test_divide_to_float(self):
        assert divide(10, 4) == 2.5

    def test_divide_negative_numbers(self):
        assert divide(-10, 2) == -5

    def test_divide_by_zero_raises_error(self):
        with pytest.raises(ZeroDivisionError):
            divide(10, 0)

    def test_divide_single_argument_raises_error(self):
        with pytest.raises(ValueError):
            divide(10)

    def test_divide_no_arguments_raises_error(self):
        with pytest.raises(ValueError):
            divide()

    def test_divide_floats(self):
        assert divide(10.0, 2.5) == 4.0

    def test_divide_multiple_with_zero_raises_error(self):
        with pytest.raises(ZeroDivisionError):
            divide(100, 5, 0, 2)
