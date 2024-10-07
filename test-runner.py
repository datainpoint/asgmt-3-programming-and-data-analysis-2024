import unittest
import importlib

class TestAssignmentThree(unittest.TestCase):
    def test_01_return_shape_name(self):
        self.assertEqual(asgmt.return_shape_name(0), 'Circle')
        self.assertEqual(asgmt.return_shape_name(3), 'Triangle')
        self.assertEqual(asgmt.return_shape_name(4), 'Rectangle')
        self.assertEqual(asgmt.return_shape_name(5), 'Pentagon')
        self.assertEqual(asgmt.return_shape_name(6), 'Hexagon')
    def test_02_count_of_positives(self):
        self.assertEqual(asgmt.count_of_positives([0, 1, 2, 3]), 3)
        self.assertEqual(asgmt.count_of_positives([-3, -2, -1, 0, 1, 2, 3]), 3)
        self.assertEqual(asgmt.count_of_positives([0, 1, 2, 3, 4, 5]), 5)
        self.assertEqual(asgmt.count_of_positives([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]), 5)
        self.assertEqual(asgmt.count_of_positives([-6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]), 5)
        self.assertEqual(asgmt.count_of_positives([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6]), 6)
    def test_03_sum_of_negatives(self):
        self.assertEqual(asgmt.sum_of_negatives([-3, -2, -1, 0]), -6)
        self.assertEqual(asgmt.sum_of_negatives([-3, -2, -1, 0, 1, 2, 3]), -6)
        self.assertEqual(asgmt.sum_of_negatives([-5, -4, -3, -2, -1, 0]), -15)
        self.assertEqual(asgmt.sum_of_negatives([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]), -15)
        self.assertEqual(asgmt.sum_of_negatives([-3, -2, -1, 0, 1, 2, 3, 4]), -6)
        self.assertEqual(asgmt.sum_of_negatives([-4, -3, -2, -1, 0, 1, 2, 3, 4]), -10)
    def test_04_return_with_fizz_buzz_rule(self):
        self.assertEqual(asgmt.return_with_fizz_buzz_rule(1), 1)
        self.assertEqual(asgmt.return_with_fizz_buzz_rule(2), 2)
        self.assertEqual(asgmt.return_with_fizz_buzz_rule(3), 'Fizz')
        self.assertEqual(asgmt.return_with_fizz_buzz_rule(5), 'Buzz')
        self.assertEqual(asgmt.return_with_fizz_buzz_rule(6), 'Fizz')
        self.assertEqual(asgmt.return_with_fizz_buzz_rule(7), 7)
        self.assertEqual(asgmt.return_with_fizz_buzz_rule(8), 8)
        self.assertEqual(asgmt.return_with_fizz_buzz_rule(9), 'Fizz')
        self.assertEqual(asgmt.return_with_fizz_buzz_rule(10), 'Buzz')
        self.assertEqual(asgmt.return_with_fizz_buzz_rule(11), 11)
        self.assertEqual(asgmt.return_with_fizz_buzz_rule(12), 'Fizz')
        self.assertEqual(asgmt.return_with_fizz_buzz_rule(13), 13)
        self.assertEqual(asgmt.return_with_fizz_buzz_rule(14), 14)
        self.assertEqual(asgmt.return_with_fizz_buzz_rule(15), 'Fizz Buzz')
        self.assertEqual(asgmt.return_with_fizz_buzz_rule(16), 16)
        self.assertEqual(asgmt.return_with_fizz_buzz_rule(17), 17)
    def test_05_return_first_n_fizz_buzz(self):
        self.assertEqual(asgmt.return_first_n_fizz_buzz(2),
                         [1, 2])
        self.assertEqual(asgmt.return_first_n_fizz_buzz(3),
                         [1, 2, 'Fizz'])
        self.assertEqual(asgmt.return_first_n_fizz_buzz(4),
                         [1, 2, 'Fizz', 4])
        self.assertEqual(asgmt.return_first_n_fizz_buzz(6),
                         [1, 2, 'Fizz', 4, 'Buzz', 'Fizz'])
        self.assertEqual(asgmt.return_first_n_fizz_buzz(15),
                         [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'Fizz Buzz'])
    def test_06_range_fizz_buzz(self):
        self.assertEqual(asgmt.range_fizz_buzz(1, 5), [1, 2, 'Fizz', 4])
        self.assertEqual(asgmt.range_fizz_buzz(3, 5), ['Fizz', 4])
        self.assertEqual(asgmt.range_fizz_buzz(1, 6), [1, 2, 'Fizz', 4, 'Buzz'])
        self.assertEqual(asgmt.range_fizz_buzz(3, 6), ['Fizz', 4, 'Buzz'])
        self.assertEqual(asgmt.range_fizz_buzz(1, 16), 
                         [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'Fizz Buzz'])
        self.assertEqual(asgmt.range_fizz_buzz(13, 16), [13, 14, 'Fizz Buzz'])
    def test_07_retrieve_middle_elements(self):
        self.assertEqual(asgmt.retrieve_middle_elements([2, 3, 5]), 3)
        self.assertEqual(asgmt.retrieve_middle_elements([2, 3, 5, 7]), (3, 5))
        self.assertEqual(asgmt.retrieve_middle_elements([2, 3, 5, 7, 11]), 5)
        self.assertEqual(asgmt.retrieve_middle_elements([2, 3, 5, 7, 11, 13]), (5, 7))
        self.assertEqual(asgmt.retrieve_middle_elements([2, 3, 5, 7, 11, 13, 17]), 7)
        self.assertEqual(asgmt.retrieve_middle_elements([2, 3, 5, 7, 11, 13, 17, 19]), (7, 11))
    def test_08_median(self):
        self.assertEqual(asgmt.median([2, 3, 5]), 3)
        self.assertEqual(asgmt.median([2, 3, 5, 7, 11]), 5)
        self.assertEqual(asgmt.median([2, 3, 5, 7, 11, 13]), 6.0)
        self.assertEqual(asgmt.median([11, 13, 17, 2, 3, 5, 7]), 7)
        self.assertEqual(asgmt.median([7, 11, 13, 17, 19, 2, 3, 5]), 9.0)
    def test_09_collect_divisors(self):
        self.assertEqual(asgmt.collect_divisors(1), [1])
        self.assertEqual(asgmt.collect_divisors(2), [1, 2])
        self.assertEqual(asgmt.collect_divisors(3), [1, 3])
        self.assertEqual(asgmt.collect_divisors(4), [1, 2, 4])
        self.assertEqual(asgmt.collect_divisors(5), [1, 5])
        self.assertEqual(asgmt.collect_divisors(6), [1, 2, 3, 6])
        self.assertEqual(asgmt.collect_divisors(7), [1, 7])
    def test_10_is_prime(self):
        self.assertFalse(asgmt.is_prime(1))
        self.assertTrue(asgmt.is_prime(2))
        self.assertTrue(asgmt.is_prime(3))
        self.assertFalse(asgmt.is_prime(4))
        self.assertTrue(asgmt.is_prime(5))
        self.assertFalse(asgmt.is_prime(6))
        self.assertTrue(asgmt.is_prime(7))

asgmt = importlib.import_module("asgmt")
suite = unittest.TestLoader().loadTestsFromTestCase(TestAssignmentThree)
runner = unittest.TextTestRunner(verbosity=2)
test_results = runner.run(suite)
number_of_failures = len(test_results.failures)
number_of_errors = len(test_results.errors)
number_of_test_runs = test_results.testsRun
number_of_successes = number_of_test_runs - (number_of_failures + number_of_errors)
print("You've got {} successes among {} questions.".format(number_of_successes, number_of_test_runs))