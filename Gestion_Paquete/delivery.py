from track import Track


class Delivery:
    def __init__(self, order: int, status: str, track: Track, driver_id: int, position: str):
        self.__order = order
        self.__status = status
        self.__track = track
        self.__driver_id = driver_id
        self.__position = position

    @property
    def order(self) -> int:
        return self.__order

    @property
    def status(self) -> str:
        return self.__status

    @property
    def track(self) -> Track:
        return self.__track

    @property
    def driver_id(self) -> int:
        return self.__driver_id

    @property
    def position(self) -> str:
        return self.__position

    def update_position(self, new_position: str):
        self.__position = new_position

    def __str__(self):
        return (f"Delivery(Order: {self.order}, Status: {self.status}, "
                f"Track: {self.track.track_id}, Driver: {self.driver_id}, "
                f"Position: {self.position})")
