import unittest
from Gestion_Paquete.package import Package

class TestPackage(unittest.TestCase):
    def setUp(self):
        """Se ejecuta antes de cada prueba. Inicializa datos para Package con los cuales se van a hacer las pruebas posteriormente"""
        self.package = Package(
            package_id = 123456,
            weight = 10,
            dimensions = "30x20x10",
            package_type = "dimensionado"
        )

    def test_package_init(self):
        """Verificar que los valores iniciales sean iguales a los asignados para la prueba"""
        self.assertEqual(
            self.package.package_id,
            123456,
            "El ID del paquete no se inicializó correctamente"
        )
        self.assertEqual(
            self.package.weight,
            10,
            "El peso del paquete no se inicializó correctamente"
        )
        self.assertEqual(
            self.package.dimensions,
            "30x20x10",
            "Las dimensiones del paquete no se inicializó correctamente"
        )
        self.assertEqual(
            self.package.package_type,
            "dimensionado",
            "El tipo del paquete no se inicializó correctamente"
        )

    def test_calculate_price(self):
        """Asegura que la función calculate_price esté funcionado correctamente"""

        message = "El cálculo del precio es incorrecto."
        # Test # 1: Paquete con peso de 10kg y dimensiones "30x20x10".
        expected_price = 10 + 2 * 10 + len("30x20x10") * 0.5
        self.assertEqual (self.package.calculate_price(), expected_price, message)

        # Test #2: Paquete con peso de 5kg y dimensiones 2*5*5
        package2 = Package(123457, 5.2, "2x5x5", "basico")
        expected_price = 10 + 2 * 5.2 + len("2x5x5") * 0.5
        self.assertEqual (package2.calculate_price(), expected_price, message)

    def test_invalid_dimensions_format(self):
        """Verifica que se lance una excepción ValueError si las dimensiones no cuentan con el formato"""
        with self.assertRaises(ValueError, msg = "El paquete debe poseer tres dimensiones"):
            self.package.dimensions = "30x20"

        with self.assertRaises(ValueError, msg = "Las dimensiones se deben dividir por un 'x'"):
            self.package.dimensions = "2*5*5"

    def test_validate_dimensions_non_numeric(self):
        """Verifica que se lance una excepción ValueError si las dimensiones contiene valores no numéricos"""
        with self.assertRaises(ValueError, msg = "Los únicos caracteres no numéricos que poseen las dimensiones son 'x'"):
            self.package.dimensions = "30x20a10"

        with self.assertRaises(ValueError, msg = "Las dimensiones no contienen valores no numéricos, excepto 'x'"):
            self.package.dimensions = "30x2ax10"

    def test_invalid_dimensions_empty(self):
        """Verifica que se lance una excepción ValueError si las dimensiones están vacías"""
        with self.assertRaises(ValueError):
            self.package.dimensions = ""

    def test_valid_dimensions(self):
        """Verifica que no se lance una excepción para dimensiones correctas"""
        try:
            Package(123461, 10, "50x50x50", "dimensionado")  # Formato válido
        except ValueError:
            self.fail("Se lanzó ValueError para dimensiones válidas")


if __name__ == "__main__":
    unittest.main()
