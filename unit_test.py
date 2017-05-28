import unittest

from mult_table import find_primes

class TestFindPrimes(unittest.TestCase):
    def test_returns_primes_norm(self):
        expected = [2,3,5,7,11]
        actual = find_primes(5)
        self.assertEqual(expected, actual)

    def test_returns_primes(self):
        expected = [2,3,5,7,11,13,17,19,23,29]
        actual = find_primes(10)
        self.assertEqual(expected, actual)

    def test_does_not_return_invalid_primes(self):
        expected = [2,3,5,7,10]
        actual = find_primes(5)
        self.assertNotEqual(expected,actual)

    def test_small_numbers(self):
        expected = [2]
        actual = find_primes(1)
        self.assertEqual(expected, actual)

    def test_small_numbers_2(self):
        expected = [2,3]
        actual = find_primes(2)
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
