import unittest
from paqueges.Gestion_Paquete.track import Track


class TestPackage(unittest.TestCase):
    def setUp(self):
        """ Se ejecuta antes de cada prueba.
            Inicializa datos para Track con los cuales se van a hacer las pruebas posteriormente"""
        self.track = Track(
            track_id=456710,
            track_type="Tipo",
            max_weight=80,
            current_weight=15,
            status="Entregado"
        )

    def test_track_init(self):
        """Verificar que los valores iniciales sean iguales a los asignados para la prueba"""
        self.assertEqual(
            self.track.track_id,
            456710,
            "El ID del track no se inicializó correctamente"
        )
        self.assertEqual(
            self.track.track_type,
            "Tipo",
            "El tipo del track no se inicializó correctamente"
        )
        self.assertEqual(
            self.track.max_weight,
            80,
            "El peso máximo del paquete no se inicializó correctamente"
        )
        self.assertEqual(
            self.track.current_weight,
            15,
            "El peso del paquete no se inicializó correctamente"
        )
        self.assertEqual(
            self.track.status,
            "Entregado",
            "El estado del paquete no se inicializó correctamente"
        )


if __name__ == "__main__":
    unittest.main()
