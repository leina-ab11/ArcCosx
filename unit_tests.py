"""Unit tests for the arccos(x) calculator."""
import unittest
from helper_math_functions import arccos_maclaurin, is_nan, ConvergenceError, PI
from gui import to_degrees, format_result
from user_input import read_input


class TestArcCosMaclaurin(unittest.TestCase):
    """Tests for the arccos(x) math function and helper functions."""
    def test_arccos_maclaurin_valid_inputs(self):
        """Valid inputs return arccos to 3 decimals (FR-8, NFR-2)."""
        self.assertAlmostEqual(arccos_maclaurin(1), 0.0, places=3)
        self.assertAlmostEqual(arccos_maclaurin(-1), PI, places=3)
        self.assertAlmostEqual(arccos_maclaurin(0), PI / 2, places=3)
        self.assertAlmostEqual(arccos_maclaurin(
            0.5), 1.0471975511965979, places=3)
        self.assertAlmostEqual(arccos_maclaurin(-0.5),
                               2.0943951023931957, places=3)

    def test_arccos_maclaurin_invalid_inputs(self):
        """Invalid/out of domain inputs return arccos to 3 decimals"""
        with self.assertRaises(ValueError):
            arccos_maclaurin(2)
        with self.assertRaises(ValueError):
            arccos_maclaurin(-2)
        with self.assertRaises(ValueError):
            arccos_maclaurin(150)

    def test_is_nan(self):
        """Detects NaN and rejects real numbers."""
        self.assertTrue(is_nan(float('nan')))
        self.assertFalse(is_nan(5))
        self.assertFalse(is_nan(-3.14))

    def test_arccos_maclaurin_cap_raises(self):
        """Hitting the iteration cap raises ConvergenceError (P5 safety net)."""
        with self.assertRaises(ConvergenceError):
            arccos_maclaurin(0, max_iterations=2)


class TestGuiLogic(unittest.TestCase):
    """Tests for the GUI's conversion and formatting logic."""
    def test_to_degrees_known_values(self):
        """Radians convert correctly to degrees (FR-4)."""
        self.assertAlmostEqual(to_degrees(PI), 180.0, places=3)
        self.assertAlmostEqual(to_degrees(PI / 2), 90.0, places=3)

    def test_format_result_three_decimals(self):
        """Result shows 3 decimals in both radians and degrees (FR-5)."""
        text = format_result(1.0471975, 60.0)
        self.assertIn("1.047", text)
        self.assertIn("60.000", text)
        self.assertIn("Rad", text)
        self.assertIn("Degrees", text)


class TestReadInput(unittest.TestCase):
    """Tests for user input parsing and validation."""

    def test_valid_number_accepted(self):
        """Valid real numbers in domain are returned (FR-1)."""
        self.assertEqual(read_input("0.5"), 0.5)
        self.assertEqual(read_input("-1"), -1.0)

    def test_non_numeric_raises(self):
        """Non-numeric input raises ValueError (FR-3)."""
        with self.assertRaises(ValueError):
            read_input("abc")
        with self.assertRaises(ValueError):
            read_input("")

    def test_out_of_domain_raises(self):
        """Out-of-domain input raises ValueError (FR-2)."""
        with self.assertRaises(ValueError):
            read_input("2")

    def test_nan_rejected(self):
        """'nan' is rejected, not accepted as a float."""
        with self.assertRaises(ValueError):
            read_input("nan")


if __name__ == '__main__':
    unittest.main()
