import unittest
from Gestion_Paquete.package import Package

class TestPackage(unittest.TestCase):
    def setUp(self):
        """Se ejecuta antes de cada prueba. Inicializar datos para Package con los cuales se van a hacer las pruebas posteriormente"""
        self.package = Package(
            package_id = 123456,
            weight = 10,
            dimensions = "30*20*10",
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
            "30*20*10",
            "Las dimensiones del paquete no se inicializó correctamente"
        )
        self.assertEqual(
            self.package.package_type,
            "dimensionado",
            "El tipo del paquete no se inicializó correctamente"
        )

    def test_calculate_price(self):
        """Asegurarse que la función calculate_price esté funcionado correctamente"""

        message = "El cálculo del precio es incorrecto."
        # Test # 1: Paquete con peso de 10kg y dimensiones "30*20*10".
        # Cálculo manual del precio
        # base_price = 10
        # weight_factor = 2 * 10 = 20
        # size_ factor = 10 * 0.5 = 5 (La longitud de dimensiones es 10 porque se cuentan las comillas que estable que el dato es string
        # price = base_price + weight_factor + size_factor = 10 + 20 + 5 = 35
        expected_price = 10 + 2*10 + len("30+20*10")*0.5
        self.assertEqual (self.package.calculate_price(), expected_price, message)

        # Test #2: Paquete con peso de 5kg y dimensiones 2*5*5
        package2 = Package(123457, 5.2, "2*5*5", "basico")
        expected_price = 10 + 2*5.2 + len("2*5*5")*0.5
        self.assertEqual (package2.calculate_price(), expected_price, message)


if __name__ == "__main__":
    unittest.main()
