import unittest
from Gestion_Paquete.location import Location

class TestLocation(unittest.TestCase):

    def setUp(self):
        """Se ejecuta antes de cada prueba. Inicializar datos para Location con los cuales se van a hacer las pruebas posteriormente"""
        self.location = Location(
            country = "Colombia",
            department = "Bolivar",
            city = "Cartagena de Indias",
            address1 = "Cra. 11 #39-21, San Diego",
            address2 = "La Serrezuela",
            zip_code = 130001
        )

    def test_init(self):
        """Verificar que los valores iniciales sean iguales a los asignados para la prueba"""
        # assertEqual (primer valor, segundo valor, mensaje) Compara los valores y muestra un mensaje si no son iguales.
        self.assertEqual(
            self.location.country,
            "Colombia",
            "El país no se inicializó correctamente."
        )
        self.assertEqual(
            self.location.department,
            "Bolivar",
            "El departamento no se inicializó correctamente."
        )
        self.assertEqual(
            self.location.city,
            "Cartagena de Indias",
            "La ciudad no se inicializó correctamente."
        )
        self.assertEqual(
            self.location.address1,
            "Cra. 11 #39-21, San Diego",
            "La dirección 1 no se inicializó correctamente."
        )
        self.assertEqual(
            self.location.address2,
            "La Serrezuela",
            "La dirección 2 no se inicializó correctamente.")
        self.assertEqual(
            self.location.zip_code,
            130001,
            "El código postal no se inicializó correctamente."
        )

    def test_zip_code_type_error(self):
        """Verifica que se lanza un TypeError cuando el código postal ingresado no es un número entero"""
        with self.assertRaises(TypeError, msg = "El código postal debe ser un número entero"):
            self.location.zip_code = 300015.5

        with self.assertRaises(TypeError, msg = "El código postal debe ser un número entero"):
            self.location.zip_code = 300004.0

        with self.assertRaises(TypeError, msg = "El código postal debe ser un número entero"):
            self.location.zip_code = "Juan"

    def test_zip_code_value_error(self):
        """Verifica que se lanza un ValueError cuando el código postal ingresado no es positivo"""
        with self.assertRaises(ValueError):
            self.location.zip_code = 0

        with self.assertRaises(ValueError):
            self.location.zip_code = -5


if __name__ == "__main__":
    unittest.main()
