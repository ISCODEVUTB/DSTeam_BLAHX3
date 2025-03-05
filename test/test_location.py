import unittest
from location import Location

class TestLocation(unittest.TestCase):

    def setUp(self):
        """Se ejecuta antes de cada prueba. Inicializar datos para Location con los cuales se van a hacer las pruebas posteriormente"""
        self.location = Location(
            country = "Colombia",
            department = "Bolivar",
            city = "Cartagena de Indias",
            address1 = "Cra. 11 #39-21, San Diego",
            address2 = "La Serrezuela",
            zipCode = 130001
        )

    def tearDown(self):
        """Se ejecuta luego de todas las pruebas"""
        self.location = Location(
            country="",
            department="",
            city="",
            address1="",
            address2="",
            zipCode=0
        )

    def test_init(self):
        """Verificar que los valores iniciales sean iguales a los asignados para la prueba"""
        message = "Error de Inicializacion"
        # assertEqual(first value, second value, message) Compara valores y mensaje en caso de que no sean iguales
        self.assertEqual(self.location.country, "Colombia", message)
        self.assertEqual(self.location.department == "Bolivar", message)
        self.assertEqual(self.location.city == "Cartagena de Indias", message)
        self.assertEqual(self.location.address1 == "Cra. 11 #39-21, San Diego", message)
        self.assertEqual(self.location.address2 == "La Serrezuela", message)
        self.assertEqual(self.location.zipCode == 130001, message)

    def test_setters_getters(self):
        """Verificar el correcto funcionamiento de los setters y getters"""

if _name_ == "_main_":
    unittest.main()
