import unittest
from Utilities.type_checker import is_valid_number

class MyTestCase(unittest.TestCase):

    def test_valid_whole_positive_number_string(self):
        self.assertTrue(is_valid_number("12345"))
        self.assertTrue(is_valid_number("123456"))

    def test_valid_negative_number_string(self):
        self.assertTrue(is_valid_number("-12345"))

    def test_invalid_negative_number_mixed_with_string(self):
        self.assertFalse(is_valid_number("-12-12"))
        self.assertFalse(is_valid_number("-12asdf"))
        self.assertFalse(is_valid_number("12asdf"))

    def test_alphabetical_string_negative(self):
        self.assertFalse(is_valid_number("asdf"))
        self.assertFalse(is_valid_number("-asdf"))

    def test_valid_decimal_number(self):
        self.assertTrue(is_valid_number("33.33"))

    def test_invalid_decimal_number(self):
        self.assertFalse(is_valid_number("33..33"))


if __name__ == '__main__':
    unittest.main()
