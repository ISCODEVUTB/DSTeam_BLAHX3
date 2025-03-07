1import unittest
from random import randbytes
from src.package import Package
from src.package_types import PackageTypes


class TestPackage(unittest.TestCase):
    def setUp(self):
        """This is executed before each test. Initializes data for Package which will be used for the tests later."""
        self.package = Package(
            weight=10.0,
            length=2.0,
            width=1.5,
            height=0.5
        )

    def test_package_init(self):
        """Verify that the initial values are correct."""
        self.assertEqual(self.package.weight, 10, "Incorrect weight initialization.")
        self.assertEqual(self.package.dimensions, "2.0x1.5x0.5", "Incorrect dimensions initialization.")
        self.assertEqual(self.package.package_type, PackageTypes.ESTANDAR.name, "Incorrect package type.")

    def test_calculate_price(self):
        """Ensure that the calculate_price function works correctly."""
        expected_price = 10 + 2 * 10 + (2.0 * 1.5 * 0.5) * 0.5
        self.assertEqual(self.package.calculate_price(), expected_price, "Incorrect price calculation.")

        package2 = Package(5.2, 2, 5, 5)
        expected_price = 10 + 2 * 5.2 + (2 * 5 * 5) * 0.5
        self.assertEqual(package2.calculate_price(), expected_price, "Incorrect price calculation.")

    def test_invalid_height_negative(self):
        """Ensure ValueError is raised for negative height."""
        with self.assertRaises(ValueError):
            Package(10, 2, 1.5, -1)

    def test_invalid_height_zero(self):
        """Ensure ValueError is raised for zero height."""
        with self.assertRaises(ValueError):
            Package(10, 2, 1.5, 0)

    def test_invalid_length_negative(self):
        with self.assertRaises(ValueError):
            Package(10, -1, 1.5, 0.5)

    def test_invalid_length_zero(self):
        with self.assertRaises(ValueError):
            Package(10, 0, 1.5, 0.5)

    def test_invalid_width_negative(self):
        with self.assertRaises(ValueError):
            Package(10, 2, -1, 0.5)

    def test_invalid_width_zero(self):
        with self.assertRaises(ValueError):
            Package(10, 2, 0, 0.5)

    def test_invalid_weight_negative(self):
        with self.assertRaises(ValueError):
            Package(-1, 2, 1.5, 0.5)

    def test_invalid_weight_zero(self):
        with self.assertRaises(ValueError):
            Package(0, 2, 1.5, 0.5)

    def test_invalid_package_type(self):
        """Ensure package type is correctly assigned."""
        package_invalid_type = Package(15, 1.0, 2.0, 0.5)
        self.assertEqual(package_invalid_type.package_type, PackageTypes.ESTANDAR.name)

    def test_package_id(self):
        """Ensure that package ID is unique."""
        package_id1 = self.package.package_id
        package_id2 = Package(5.2, 2, 5, 5).package_id
        self.assertNotEqual(package_id1, package_id2, "Package IDs should be unique.")


if __name__ == "__main__":
    unittest.main()

