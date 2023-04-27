import pytest
from app.calc import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator()

# тест сложения
    def test_adding_calculation_pass(self):
        assert self.calc.adding(5, 2) == 7

# тест вычитания
    def test_subtraction_calculation_pass(self):
        assert self.calc.subtraction(12, 4) == 8

# тест умножения
    def test_multiply_calculate_pass(self):
        assert self.calc.multiply(5, 2) == 10

# тест деления
    def test_division_calculate_pass(self):
        assert self.calc.division(15, 3) == 5