import unittest 
from unittest import TestCase
from price_discount import discount  

class TestDiscount(TestCase):

    def test_list_of_three_prices(self):
        prices = [10, 4, 20]
        expected_discount = 4
        self.assertEqual(expected_discount, discount(prices))

    def test_list_of_four_prices(self):
        prices = [10, 4, 20, 2]
        expected_discount = 2
        self.assertEqual(expected_discount, discount(prices))

    def test_list_of_two_prices(self):
        prices = [10, 2]
        expected_discount = 0
        self.assertEqual(expected_discount, discount(prices))

    def test_list_with_empty_list(self):
        prices = []
        expected_discount = 0
        self.assertEqual(expected_discount, discount(prices))

    def test_list_with_empty_list(self):
        prices = []
        expected_discount = 0
        self.assertEqual(expected_discount, discount(prices))

    def discount_called_with_strings(self):
        self.fail('finish this test')

    def discount_called_with_float(self):
        self.fail('finish this test')
    # TODO more unit tests here. Each test should test one scenario


if __name__ == '__main__':
    unittest.main()