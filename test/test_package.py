import unittest
from Gestion_Paquete.package import Package


class TestPackage(unittest.TestCase):
    def setUp(self):
        """This is executed before each test. Initializes data for Package which will be used for the tests later."""
        self.package = Package(
            package_id=123456,
            weight=10,
            dimensions="30x20x10",
            package_type="dimensioned"
        )

    def test_package_init(self):
        """Verify that the initial values are equal to the ones assigned for the test."""
        self.assertEqual(
            self.package.package_id,
            123456,
            "The package ID was not initialized correctly"
        )
        self.assertEqual(
            self.package.weight,
            10,
            "The package weight was not initialized correctly"
        )
        self.assertEqual(
            self.package.dimensions,
            "30x20x10",
            "The package dimensions were not initialized correctly"
        )
        self.assertEqual(
            self.package.package_type,
            "dimensioned",
            "The package type was not initialized correctly"
        )

    def test_calculate_price(self):
        """Ensure that the calculate_price function is working correctly."""

        message = "The price calculation is incorrect."
        # Test #1: Package with 10kg weight and dimensions "30x20x10".
        expected_price = 10 + 2 * 10 + len("30x20x10") * 0.5
        self.assertEqual(self.package.calculate_price(), expected_price, message)

        # Test #2: Package with 5kg weight and dimensions 2x5x5
        package2 = Package(123457, 5.2, "2x5x5", "basic")
        expected_price = 10 + 2 * 5.2 + len("2x5x5") * 0.5
        self.assertEqual(package2.calculate_price(), expected_price, message)

    def test_invalid_dimensions_format(self):
        """Verify that a ValueError exception is raised if the dimensions do not follow the correct format."""
        with self.assertRaises(ValueError, msg="The package must have three dimensions"):
            self.package.dimensions = "30x20"

        with self.assertRaises(ValueError, msg="The dimensions should be separated by 'x'"):
            self.package.dimensions = "2*5*5"

    def test_validate_dimensions_non_numeric(self):
        """Verify that a ValueError exception is raised if the dimensions contain non-numeric values."""
        with self.assertRaises(ValueError, msg="The only non-numeric characters allowed in dimensions are 'x'"):
            self.package.dimensions = "30x20a10"

        with self.assertRaises(ValueError, msg="Dimensions should not contain non-numeric values except for 'x'"):
            self.package.dimensions = "30x2ax10"

    def test_invalid_dimensions_empty(self):
        """Verify that a ValueError exception is raised if the dimensions are empty."""
        with self.assertRaises(ValueError):
            self.package.dimensions = ""

    def test_valid_dimensions(self):
        """Verify that no exception is raised for correct dimensions."""
        try:
            Package(123461, 10, "50x50x50", "dimensioned")  # Valid format
        except ValueError:
            self.fail("ValueError was raised for valid dimensions")


if __name__ == "__main__":
    unittest.main()
    
