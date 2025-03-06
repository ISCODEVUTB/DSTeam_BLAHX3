import unittest
from Gestion_Paquete.track import Track
from .delivery import Delivery


class TestDelivery(unittest.TestCase):
    def setUp(self):
        """This is executed before each test. Initializes data for Track which will be used for the tests later"""
        self.delivery = Delivery(
            order=140789,
            status="Despachado",
            track=Track(456123, "Dunno", 50, 20, "Despachado"),
            driver_id=105271640,
            position="Barranquilla",
        )

    def test_track_init(self):
        """Verify that the initial values are equal to the ones assigned for the test """
        self.assertEqual(
            self.delivery.order,
            140789,
            "The Delivery Number was not initialized correctly."
        )
        self.assertEqual(
            self.delivery.status,
            "Despachado",
            "The delivery status was not initialized correctly."
        )
        self.assertEqual(
            self.delivery.track.track_id,
            456123,
            "The track was not initialized correctly."
        )
        self.assertEqual(
            self.delivery.driver_id,
            105271640,
            "The driver ID was not initialized correctly."
        )
        self.assertEqual(
            self.delivery.position,
            "Barranquilla",
            "The position of the package was not initialized correctly."
        )


if __name__ == "__main__":
    unittest.main()
