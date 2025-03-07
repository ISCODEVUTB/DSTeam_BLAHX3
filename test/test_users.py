import unittest
import os
from src.location import Location
from src.users import User
import bcrypt


class TestUser(unittest.TestCase):

    def setUp(self):
        """ This is executed before each test.
            Initializes data for Location and User which will be used for the tests later. """
        self.location = Location(
            country="Colombia",
            department="Bolivar",
            city="Cartagena de Indias",
            address1="Cra. 11 #39-21, San Diego",
            address2="La Serrezuela",
            zip_code=130001
        )

        # Get the password from the environment variable (if not defined, a default password is used)
        password = os.getenv("USER_PASSWORD", "default_password")
        self.user = User(
            name="Joe",
            last_name="Doe",
            national_id="1037186420",
            email="joedoe@hotmail.com",
            address=self.location,
            password=password
        )

    def test_user_init(self):
        """Verify that the initial values are equal to the ones assigned for the test"""
        # assertEqual(first value, second value, message) Compares values and displays a message if they are not equal
        self.assertEqual(
            self.user.name,
            "Joe",
            "The first name was not initialized correctly."
        )
        self.assertEqual(
            self.user.last_name,
            "Doe",
            "The last name was not initialized correctly."
        )
        self.assertEqual(
            self.user.national_id,
            "1037186420",
            "The national ID was not initialized correctly."
        )
        self.assertEqual(
            self.user.email,
            "joedoe@hotmail.com",
            "The email was not initialized correctly."
        )
        self.assertEqual(
            self.user.address,
            self.location,
            "The address was not initialized correctly."
        )

    def test_password_hashpwd(self):
        """Verify that the hashpwd function creates a hash of the password"""
        original_password = self.user._password
        hashed_password = self.user.hashpwd(original_password)
        # Check that the password is not equal to the hash
        self.assertNotEqual(
            original_password,
            hashed_password,
            "The password should not be equal to the hash"
        )
        # Check that the created hash matches the original password
        self.assertTrue(
            bcrypt.checkpw(original_password, hashed_password),
            "The password hash does not match the original."
        )


if __name__ == "__main__":
    unittest.main()
