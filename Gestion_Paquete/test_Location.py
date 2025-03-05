import unittest
from location import Location

class TestLocation(unittest.TestCase):
    def test_init(self):
        """Ejecuta el constructor de la clase Location"""
        self.location = Location(
            country = "Colombia",
            department = "Bolivar",
            city = "Cartagena de Indias",
            address1 = "Cra. 11 #39-21, San Diego",
            address2 = "La Serrezuela",
            zipCode = 130001
        )

if __name__ == "__main__":
    unittest.main()

