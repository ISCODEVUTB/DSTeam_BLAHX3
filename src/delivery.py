from src.track import Track


class Delivery:
    def __init__(self, order: int, status: str, track: Track, driver_id: int, position: int):
        self.__order = order
        self.__status = status
        self.__track = track
        self.__driver_id = driver_id
        self.__position = position

    @property
    def order(self) -> int:
        return self.__order

    @order.setter
    def order(self, value: int):
        self.__order = value

    @property
    def status(self) -> str:
        return self.__status

    @status.setter
    def status(self, value: str):
        self.__status = value

    @property
    def track(self) -> Track:
        return self.__track

    @track.setter
    def track(self, value: Track):
        self.__track = value

    @property
    def driver_id(self) -> int:
        return self.__driver_id

    @driver_id.setter
    def driver_id(self, value: int):
        self.__driver_id = value

    @property
    def position(self) -> str:
        return self.__position

    @position.setter
    def position(self, value: str):
        self.__position = value

    def update_position(self, new_position: str):
        self.__position = new_position

    def __str__(self):
        return (f"Delivery(Order: {self.order}, Status: {self.status}, "
                f"Track: {self.track.track_id}, Driver: {self.driver_id}, "
                f"Position: {self.position})")
