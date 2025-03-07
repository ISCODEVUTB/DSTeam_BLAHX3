import unittest
from unittest.mock import patch
from src.users import User
from src.location import Location
from src.package import Package
from src.order import Order
from main import new_user, new_location, new_package, show_packages, delete_package


class TestMainFunctions(unittest.TestCase):
    def test_new_user(self):
        """Test new_user function"""
        user_location = Location("USA", "California", "Los Angeles", "Main St", "Apt 2", 90212)
        user = new_user("Gracie", "Abrams", "1944682", "gracie.abrams@gmail.com", user_location, "Gatito123*")

        self.assertEqual(user.name, "Gracie")
        self.assertEqual(user.last_name, "Abrams")
        self.assertEqual(user.national_id, "1944682")
        self.assertEqual(user.email, "gracie.abrams@gmail.com")
        self.assertEqual(user.location.country, "USA")
        self.assertEqual(user.location.zip_code, 90212)

    def test_new_location(self):
        """Test new_location function"""
        location = new_location("USA", "California", "Los Angeles", "Main St", "Apt 2", 90212)

        self.assertEqual(location.country, "USA")
        self.assertEqual(location.department, "California")
        self.assertEqual(location.city, "Los Angeles")
        self.assertEqual(location.address1, "Main St")
        self.assertEqual(location.zip_code, 90001)

    def test_new_package(self):
        """Test new_package function"""
        package = new_package(5.2, 2, 5, 5)
        self.assertEqual(package.weight, 5.2)
        self.assertEqual(package.length, 2)
        self.assertEqual(package.width, 5)
        self.assertEqual(package.height, 5)

    @patch("builtins.print")  # Parcheamos `print` para interceptar las salidas
    def test_show_packages(self, mock_print):
        """Test show_packages function with mocked data"""
        user_location = Location("USA", "California", "Los Angeles", "Main St", "Apt 2", 90212)
        user = new_user("Gracie", "Abrams", "1944682", "gracie.abrams@gmail.com", user_location, "Gatito123*")
        package1 = Package(5.2, 2, 5, 5)
        package2 = Package(10, 3, 4.1, 6.8)
        package_list = [package1, package2]

        # Mock print to test what is being output
        show_packages(package_list, user)
        mock_print.assert_any_call("Packages due to be sent to: Gracie Abrams")
        mock_print.assert_any_call(f"Package 1\n{package1}\n")
        mock_print.assert_any_call(f"Package 2\n{package2}\n")

    @patch("builtins.input")  # Mocking inputs for delete_package
    @patch("builtins.print")  # Mocking print for output
    def test_delete_package_update(self, mock_print, mock_input):
        """Test delete_package function with mocked input"""
        package1 = Package(5.2, 2, 5, 5)
        package2 = Package(10, 3, 4.1, 6.8)
        package_list = [package1, package2]

        # Simulate the input to select a package to delete
        mock_input.return_value = package1.package_id

        # Deleting package should update the list
        result = delete_package(package_list)
        self.assertEqual(result, 1)  # Package was deleted
        self.assertEqual(len(package_list), 1)  # Only one package should remain
        mock_print.assert_any_call("Package deleted successfully")

    @patch("builtins.input")  # Mocking inputs for delete_package
    @patch("builtins.print")  # Mocking print for output
    def test_delete_package_invalid_id(self, mock_print, mock_input):
        """Test delete_package function for an invalid ID with mocked input"""
        package1 = Package(5.2, 2, 5, 5)
        package2 = Package(10, 3, 4.1, 6.8)
        package_list = [package1, package2]

        # Test in case an ID is invalid
        mock_input.return_value = "invalid_id"
        result = delete_package(package_list)
        self.assertEqual(result, 0)  # Invalid package ID, should not delete any package
        mock_print.assert_any_call("Invalid package ID. No package deleted.")


if __name__ == '__main__':
    unittest.main()
