import unittest
from Gestion_Paquete.users import User
from Gestion_Paquete.package import Package
from Gestion_Paquete.order import Order
from Gestion_Paquete.location import Location
from Gestion_Paquete.order_status import OrderStatus


class TestOrder(unittest.TestCase):
    def setUp(self):
        """This is executed before each test. Initializes data for Order which will be used for the tests later"""
        # Setup the mock Users (sender and receiver)
        sender_location = Location("Colombia", "Bolivar", "Cartagena", "CRA", "address", 130001)
        receiver_location = Location("Colombia", "Atlantico", "Barranquilla", "CRA prueba", "address prueba", 80007)

        self.sender = User("Alex", "Prens", "1944682", "a@gmail.com", sender_location, "Gatito123*")
        self.receiver = User("John", "Doe", "9102478", "john_doe@gmail.com", receiver_location, "Test*321")

        # Setup mock Packages
        self.package1 = Package(15, 1.0, 2.0, 3.0)
        self.package2 = Package(5, 2.0, 3.0, 4.0)

        # Setup the Order with packages and users
        self.order = Order(
            sender=self.sender,
            receiver=self.receiver,
            packages=[self.package1, self.package2]
        )

    def test_order_init(self):
        """Verify that the initial values are equal to the ones assigned for the test"""
        self.assertEqual(self.order.sender, self.sender, "The receiver was not initialized correctly.")
        self.assertEqual(self.order.receiver, self.receiver, "The receiver was not initialized correctly.")
        self.assertEqual(len(self.order.packages), 2, "The number of packages was not initialized correctly.")
        self.assertEqual(self.order.status, OrderStatus.PENDING.name, "The order status was not initialized correctly.")

    def test_add_package(self):
        """Verify that a new package can be added to the order"""
        new_package = Package(20, 10.0, 6.0, 1.5)
        self.order.add_package(new_package)

        self.assertIn(new_package, self.order.packages, "The package was not added correctly.")
        self.assertEqual(len(self.order.packages), 3, "The number of packages did not update correctly after adding.")

    def test_remove_package(self):
        """Verify that a package can be removed from the order"""
        self.order.remove_package(self.package1.package_id)

        # Assert that the package with ID 101 is no longer in the list
        removed_package = next((pkg for pkg in self.order.packages if pkg.package_id == self.package1.package_id), None)
        self.assertIsNone(removed_package, "The package was not removed correctly.")
        self.assertEqual(len(self.order.packages), 1, "The number of packages did not update correctly after removal.")

    def test_invalid_remove_package(self):
        """Verify that attempting to remove a non-existing package ID does not alter the order"""
        initial_package_count = len(self.order.packages)
        self.order.remove_package("19999")  # No package with ID 19999 exists

        # Assert that the package count remains the same
        self.assertEqual(len(self.order.packages), initial_package_count, "The package list was incorrectly altered.")


if __name__ == "__main__":
    unittest.main()
    
