import unittest

from mult_table import find_primes, seive_of_eratosthenes, create_mult_table

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

class TestSieve(unittest.TestCase):
    def test_returns_primes(self):
        expected = [True, True, True, True, False, True, False, True, False, False, False]
        actual = seive_of_eratosthenes(10)
        self.assertEqual(expected,actual)

    def test_does_not_return_invalid_primes(self):
        expected = [True,True,True,True,True,True,True]
        actual = seive_of_eratosthenes(6)
        self.assertNotEqual(expected,actual)

class TestCreatTable(unittest.TestCase):
    def test_returns_table(self):
        expected = ["\t2\t3\t5", "2\t4\t6\t10", "3\t6\t9\t15", "5\t10\t15\t25"]
        actual = create_mult_table(3)
        self.assertEqual(expected,actual)

    def test_does_not_return_bad_tables(self):
        expected = ["\t2\t3\t5", "2\t4\t6\t11", "3\t6\t9\t15"]
        actual = create_mult_table(2)
        self.assertNotEqual(expected,actual)

if __name__ == '__main__':
    unittest.main()
