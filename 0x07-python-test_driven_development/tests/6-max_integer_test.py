#!/usr/bin/python3

import unittest
from max_integer import max_integer


class TestMaxInteger(unittest.TestCase):
    """Tests for the max_integer function."""

    def test_max_integer_standard(self):
        """Test a standard list of integers."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_integer_negative(self):
        """Test a list containing negative integers."""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_max_integer_single(self):
        """Test a single element list."""
        self.assertEqual(max_integer([7]), 7)

    def test_max_integer_empty(self):
        """Test an empty list."""
        self.assertIsNone(max_integer([]))

    def test_max_integer_beginning(self):
        """Test list with max at the beginning."""
        self.assertEqual(max_integer([10, 3, 2, 1]), 10)

    def test_max_integer_middle(self):
        """Test list with max in the middle."""
        self.assertEqual(max_integer([1, 3, 10, 2]), 10)

    def test_max_integer_with_duplicates(self):
        """Test list with duplicate max values."""
        self.assertEqual(max_integer([1, 10, 10, 2]), 10)

    def test_max_integer_non_integers(self):
        """Test list with non-integer values (should raise TypeError)."""
        with self.assertRaises(TypeError):
            max_integer([1, 2, "three", 4])


if __name__ == "__main__":
    unittest.main()
