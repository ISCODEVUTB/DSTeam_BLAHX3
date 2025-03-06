class Track:
    def __init__(self, track_id: int, track_type: str, max_weight: float, current_weight: float, status: str):
        self.__track_id = track_id
        self.__track_type = track_type
        self.__max_weight = max_weight
        self.__current_weight = current_weight
        self.__status = status

    @property
    def track_id(self) -> int:
        return self.__track_id

    @track_id.setter
    def track_id(self, value: int):
        self.__track_id = value

    @property
    def track_type(self) -> str:
        return self.__track_type

    @track_type.setter
    def track_type(self, value: str):
        self.__track_type = value

    @property
    def max_weight(self) -> float:
        return self.__max_weight

    @max_weight.setter
    def max_weight(self, value: float):
        self.__max_weight = value

    @property
    def current_weight(self) -> float:
        return self.__current_weight

    @current_weight.setter
    def current_weight(self, value: float):
        self.__current_weight = value

    @property
    def status(self) -> str:
        return self.__status

    @status.setter
    def status(self, value: str):
        self.__status = value

    def __str__(self):
        return (f"Track(ID: {self.track_id}, Type: {self.track_type}, "
                f"Max Weight: {self.max_weight}, Current Weight: {self.current_weight}, "
                f"Status: {self.status})")


def main():
    track_example = Track(456123, "Dunno", 50, 20, "Entregado")
    print(track_example)


if __name__ == '__main__':
    main()
