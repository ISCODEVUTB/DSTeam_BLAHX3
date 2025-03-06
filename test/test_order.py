import unittest
from Gestion_Paquete.users import User
from Gestion_Paquete.package import Package
from Gestion_Paquete.order import Order
from Gestion_Paquete.location import Location


class TestOrder(unittest.TestCase):
    def setUp(self):
        """This is executed before each test. Initializes data for Order which will be used for the tests later"""
        # Setup the mock User
        alex_location = Location("Colombia", "Bolivar", "Cartagena", "CRA", "Danis", 130001)
        self.user = User("Alex", "Prens", "1944682", "a@gmail.com", alex_location, "Gatito123*")

        # Setup some mock Packages
        self.package1 = Package(10001, 25, "30x20x10", "basic")
        self.package2 = Package(10002, 10, "50x50x50", "dimensioned")

        # Setup the Order with packages and user
        self.order = Order(
            order_id=10001,
            user=self.user,
            packages=[self.package1, self.package2],
            status="Pending"
        )

    def test_order_init(self):
        """Verify that the initial values are equal to the ones assigned for the test"""
        self.assertEqual(self.order.order_id, 10001, "The order ID was not initialized correctly.")
        self.assertEqual(self.order.user, self.user, "The user was not initialized correctly.")
        self.assertEqual(len(self.order.packages), 2, "The number of packages was not initialized correctly.")
        self.assertEqual(self.order.status, "Pending", "The order status was not initialized correctly.")

    def test_add_package(self):
        """Verify that a new package can be added to the order"""
        new_package = Package(10003, 3.5, "5x2x7", "standard")
        self.order.add_package(new_package)

        # Assert that the new package is added
        self.assertIn(new_package, self.order.packages, "The package was not added correctly.")
        self.assertEqual(len(self.order.packages), 3, "The number of packages did not update correctly after adding.")

    def test_remove_package(self):
        """Verify that a package can be removed from the order"""
        self.order.remove_package(10001)

        # Assert that the package with ID 101 is no longer in the list
        removed_package = next((pkg for pkg in self.order.packages if pkg.package_id == 10001), None)
        self.assertIsNone(removed_package, "The package was not removed correctly.")
        self.assertEqual(len(self.order.packages), 1, "The number of packages did not update correctly after removal.")

    def test_invalid_remove_package(self):
        """Verify that attempting to remove a non-existing package ID does not alter the order"""
        initial_package_count = len(self.order.packages)
        self.order.remove_package(19999)  # No package with ID 19999 exists

        # Assert that the package count remains the same
        self.assertEqual(len(self.order.packages), initial_package_count, "The package list was incorrectly altered.")


if __name__ == "__main__":
    unittest.main()
