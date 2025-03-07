import unittest
from src.track import Track


class TestTrack(unittest.TestCase):
    def setUp(self):
        """This is executed before each test. Initializes data for Track which will be used for the tests later"""
        self.track = Track(
            track_id=456710,
            track_type="Tipo",
            max_weight=80,
            current_weight=15,
            status="Entregado"
        )

    def test_track_init(self):
        """Verify that the initial values are equal to the ones assigned for the test """
        self.assertEqual(
            self.track.track_id,
            456710,
            "The ID track was not initialized correctly."
        )
        self.assertEqual(
            self.track.track_type,
            "Tipo",
            "The track type was not initialized correctly."
        )
        self.assertEqual(
            self.track.max_weight,
            80,
            "The max weight was not initialized correctly."
        )
        self.assertEqual(
            self.track.current_weight,
            15,
            "The current weight was not initialized correctly."
        )
        self.assertEqual(
            self.track.status,
            "Entregado",
            "The package status was not initialized correctly."
        )


if __name__ == "__main__":
    unittest.main()
