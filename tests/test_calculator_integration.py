import pytest
from unittest.mock import patch
from io import StringIO
from src.calculator import calculator, display_menu, get_numbers


class TestDisplayMenu:
    """Test cases for display_menu function"""
    
    def test_display_menu_output(self, capsys):
        display_menu()
        captured = capsys.readouterr()
        assert "Calculator Menu" in captured.out
        assert "1. Add" in captured.out
        assert "2. Subtract" in captured.out
        assert "3. Multiply" in captured.out
        assert "4. Divide" in captured.out
        assert "5. Exit" in captured.out


class TestGetNumbers:
    """Test cases for get_numbers function"""
    
    @patch('builtins.input', side_effect=['10', '5'])
    def test_get_numbers_valid_input(self, mock_input):
        num1, num2 = get_numbers()
        assert num1 == 10.0
        assert num2 == 5.0
    
    @patch('builtins.input', side_effect=['10.5', '3.2'])
    def test_get_numbers_float_input(self, mock_input):
        num1, num2 = get_numbers()
        assert num1 == 10.5
        assert num2 == 3.2
    
    @patch('builtins.input', side_effect=['abc'])
    def test_get_numbers_invalid_input(self, mock_input):
        with pytest.raises(ValueError):
            get_numbers()


class TestCalculatorIntegration:
    """Integration tests for calculator function"""
    
    @patch('builtins.input', side_effect=['1', '10', '5', 'n'])
    def test_calculator_addition(self, mock_input, capsys):
        calculator()
        captured = capsys.readouterr()
        assert "Result: 10.0 + 5.0 = 15.0" in captured.out
    
    @patch('builtins.input', side_effect=['2', '10', '5', 'n'])
    def test_calculator_subtraction(self, mock_input, capsys):
        calculator()
        captured = capsys.readouterr()
        assert "Result: 10.0 - 5.0 = 5.0" in captured.out
    
    @patch('builtins.input', side_effect=['3', '10', '5', 'n'])
    def test_calculator_multiplication(self, mock_input, capsys):
        calculator()
        captured = capsys.readouterr()
        assert "Result: 10.0 × 5.0 = 50.0" in captured.out
    
    @patch('builtins.input', side_effect=['4', '10', '5', 'n'])
    def test_calculator_division(self, mock_input, capsys):
        calculator()
        captured = capsys.readouterr()
        assert "Result: 10.0 ÷ 5.0 = 2.0" in captured.out
    
    @patch('builtins.input', side_effect=['4', '10', '0', 'n'])
    def test_calculator_division_by_zero(self, mock_input, capsys):
        calculator()
        captured = capsys.readouterr()
        assert "Cannot divide by zero" in captured.out
    
    @patch('builtins.input', side_effect=['6', '1', '5', '3', 'n'])
    def test_calculator_invalid_choice(self, mock_input, capsys):
        calculator()
        captured = capsys.readouterr()
        assert "Invalid choice" in captured.out
    
    @patch('builtins.input', side_effect=['1', 'abc', '10', '5', 'n'])
    def test_calculator_invalid_number_input(self, mock_input, capsys):
        calculator()
        captured = capsys.readouterr()
        assert "Invalid input" in captured.out
    
    @patch('builtins.input', side_effect=['5'])
    def test_calculator_exit(self, mock_input, capsys):
        calculator()
        captured = capsys.readouterr()
        assert "Goodbye" in captured.out
    
    @patch('builtins.input', side_effect=['1', '5', '3', 'y', '2', '10', '4', 'n'])
    def test_calculator_multiple_operations(self, mock_input, capsys):
        calculator()
        captured = capsys.readouterr()
        assert "Result: 5.0 + 3.0 = 8.0" in captured.out
        assert "Result: 10.0 - 4.0 = 6.0" in captured.out