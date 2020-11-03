import unittest
from Calculator.calculator import calculator
from CSVReader.csv_reader import CSVReader

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, calculator)
'''
    def test_add_method_calculator(self):
        test_data = CSVReader('./TestData/Addition.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), float(row['Result']))
            self.assertEqual(self.calculator.result, float(row['Result']))

    def test_subtract_method_calculator(self):
        test_data = CSVReader('./TestData/Subtraction.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.subtract(row['Value 2'], row['Value 1']), float(row['Result']))
            self.assertEqual(self.calculator.result,float(row['Result']))

    def test_multiplication_method_calculator(self):
        test_data = CSVReader('./TestData/Multiplication.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.multiply(row['Value 1'], row['Value 2']), float(row['Result']))
            self.assertEqual(self.calculator.result,float(row['Result']))

    def test_division_method_calculator(self):
        test_data = CSVReader('./TestData/Division.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.divide(row['Value 2'], row['Value 1']), float(row['Result']))
            self.assertEqual(self.calculator.result, float(row['Result']))

    def test_square_method_calculator(self):
        test_data = CSVReader('./TestData/Square.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.square(row['Value 1']), float(row['Result']))
            self.assertEqual(self.calculator.result, float(row['Result']))

    def test_squareRoot_method_calculator(self):
        test_data = CSVReader('./TestData/Subtraction.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.squareRoot(row['Value 1']), float(row['Result']))
            self.assertEqual(self.calculator.result, float(row['Result']))'''

if __name__ == '__main__':
    unittest.main()