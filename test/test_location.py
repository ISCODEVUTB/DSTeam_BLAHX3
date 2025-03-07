1import unittest
from src.location import Location


class TestLocation(unittest.TestCase):

    def setUp(self):
        """This is executed before each test. Initializes data for Location which will be used for the tests later"""
        self.location = Location(
            country="Colombia",
            department="Bolivar",
            city="Cartagena de Indias",
            address1="Cra. 11 #39-21, San Diego",
            address2="La Serrezuela",
            zip_code=130001
        )

    def test_init(self):
        """Verify that the initial values are equal to the ones assigned for the test """
        # assertEqual (primer valor, segundo valor, mensaje) Compara los valores y muestra un mensaje si no son iguales.
        self.assertEqual(
            self.location.country,
            "Colombia",
            "The country was not initialized correctly."
        )
        self.assertEqual(
            self.location.department,
            "Bolivar",
            "The department was not initialized correctly."
        )
        self.assertEqual(
            self.location.city,
            "Cartagena de Indias",
            "The city was not initialized correctly."
        )
        self.assertEqual(
            self.location.address1,
            "Cra. 11 #39-21, San Diego",
            "Address 1 was not initialized correctly."
        )
        self.assertEqual(
            self.location.address2,
            "La Serrezuela",
            "Address 2 was not initialized correctly.")
        self.assertEqual(
            self.location.zip_code,
            130001,
            "The zip code was not initialized correctly."
        )

    def test_zip_code_type_error(self):
        """Verify that a TypeError is raised when the entered zip code is not an integer"""
        with self.assertRaises(
            TypeError, msg="The zip code must be an integer"
        ):
            self.location.zip_code = 300015.5

        with self.assertRaises(
            TypeError, msg="The zip code must be an integer"
        ):
            self.location.zip_code = 300004.0

        with self.assertRaises(
            TypeError, msg="The zip code must be an integer"
        ):
            self.location.zip_code = "Juan"

    def test_zip_code_value_error(self):
        """Verify that a ValueError is raised when the entered zip code is not positive"""
        with self.assertRaises(ValueError):
            self.location.zip_code = 0

        with self.assertRaises(ValueError):
            self.location.zip_code = -5


if __name__ == "__main__":
    unittest.main()
