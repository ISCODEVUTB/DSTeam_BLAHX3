import unittest
from random import randbytes
from Gestion_Paquete.package import Package
from Gestion_Paquete.package_types import PackageTypes

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
        """Verify that the initial values are equal to the ones assigned for the test."""
        self.assertEqual(
            self.package.weight,
            10,
            "The package weight was not initialized correctly."
        )
        self.assertEqual(
            self.package.dimensions,
            "2.0x1.5x0.5",
            "The package dimensions were not initialized correctly."
        )
        self.assertEqual(
            self.package.package_type,
            PackageTypes.ESTANDAR.name,
            "The package type was not initialized correctly."
        )

    def test_calculate_price(self):
        """Ensure that the calculate_price function is working correctly."""
        message = "The price calculation is incorrect."
        # Test #1: Package with 10kg weight and dimensions "2.0x1.5x0.5"
        expected_price = 10 + 2 * 10 + (2.0 * 1.5 * 0.5) * 0.5  # Base price + weight factor + size factor
        self.assertEqual(self.package.calculate_price(), expected_price, message)

        # Test #2: Package with 5kg weight and dimensions 2x5x5
        package2 = Package(5.2, 2, 5, 5)
        expected_price = 10 + 2 * 5.2 + (2 * 5 * 5) * 0.5
        self.assertEqual(package2.calculate_price(), expected_price, message)

    def test_invalid_height_negative(self):
        """Ensure that a ValueError is raised when an invalid height is provided."""
        with self.assertRaises(ValueError, msg="Height must be a positive number."):
            self.package.height = -1  # Invalid height (negative value)
    
    def test_invalid_height_zero(self):
        """Ensure that a ValueError is raised when an invalid height is provided."""
        with self.assertRaises(ValueError, msg="Height must be grater than zero."):
            self.package.height = 0  # Invalid height (negative value)
    
    def test_invalid_length_negative(self):
        with self.assertRaises(ValueError, msg="Length must be a positive number."):
            self.package.length = -1  # Invalid length (negative value)
    
    def test_invalid_length_zero(self):
        with self.assertRaises(ValueError, msg="Length must be greater than zero."):
            self.package.length = 0  # Invalid length (zero value)
    
    def test_invalid_width_negative(self):
        with self.assertRaises(ValueError, msg="Width must be a positive number."):
            self.package.width = -1  # Invalid width (negative value)
    
    def test_invalid_width_zero(self):
        with self.assertRaises(ValueError, msg="Width must be greater than zero."):
            self.package.width = 0  # Invalid width (zero value)
    
    def test_invalid_weight_negative(self):
        with self.assertRaises(ValueError, msg="Weight must be a positive number."):
            self.package.weight = -1  # Invalid weight (negative value)
    
    def test_invalid_weight_zero(self):
        with self.assertRaises(ValueError, msg="Weight must be greater than zero."):
            self.package.weight = 0  # Invalid weight (zero value)

    def test_invalid_package_type(self):
        """Test to ensure the package type is correctly initialized."""
        package_invalid_type = Package(15, 1.0, 2.0, 0.5)
        self.assertEqual(package_invalid_type.package_type, PackageTypes.ESTANDAR.name)

    def test_package_id(self):
        """Test that the package ID is unique and generated correctly."""
        package_id1 = self.package.package_id
        package_id2 = Package(5.2, 2, 5, 5).package_id
        self.assertNotEqual(package_id1, package_id2, "Package IDs should be unique.")


if __name__ == "__main__":
    unittest.main()
