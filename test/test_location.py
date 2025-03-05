import unittest
from Gestion_Paquete.location import Location

class TestLocation(unittest.TestCase):

    def setUp(self):
        """Inicializa una instancia de Location antes de cada prueba."""
        self.location = Location(
            country="Colombia",
            department="Bolívar",
            city="Cartagena de Indias",
            address1="Cra. 11 #39-21, San Diego",
            address2="La Serrezuela",
            zipCode=130001
        )

    def test_init(self):
        """Verificar que los valores iniciales sean correctos."""
        message = "Error de inicialización"
        self.assertEqual(self.location.country, "Colombia", message)
        self.assertEqual(self.location.department, "Bolívar", message)
        self.assertEqual(self.location.city, "Cartagena de Indias", message)
        self.assertEqual(self.location.address1, "Cra. 11 #39-21, San Diego", message)
        self.assertEqual(self.location.address2, "La Serrezuela", message)
        self.assertEqual(self.location.zipCode, 130001, message)

    def test_setters_getters(self):
        """Verificar que los setters y getters funcionen correctamente."""
        self.location.country = "Argentina"
        self.location.department = "Buenos Aires"
        self.location.city = "CABA"
        self.location.address1 = "Av. 9 de Julio"
        self.location.address2 = "Obelisco"
        self.location.zipCode = 1000

        self.assertEqual(self.location.country, "Argentina")
        self.assertEqual(self.location.department, "Buenos Aires")
        self.assertEqual(self.location.city, "CABA")
        self.assertEqual(self.location.address1, "Av. 9 de Julio")
        self.assertEqual(self.location.address2, "Obelisco")
        self.assertEqual(self.location.zipCode, 1000)

if __name__ == "__main__":
    unittest.main()
