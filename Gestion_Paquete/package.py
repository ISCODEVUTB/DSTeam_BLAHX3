class Package:
    def __init__(self, package_id: int, weight: float, dimensions: str, package_type: str):
        self.__package_id = package_id
        self.__weight = weight
        self.__dimensions = dimensions
        self.__package_type = package_type

    @property
    def package_id(self) -> int:
        return self.__package_id

    @package_id.setter
    def package_id(self, value: int):
        self.__package_id = value

    @property
    def weight(self) -> float:
        return self.__weight

    @weight.setter
    def weight(self, value: float):
        self.__weight = value

    @property
    def dimensions(self) -> str:
        return self.__dimensions

    @dimensions.setter
    def dimensions(self, value: str):
        self.__dimensions = value

    @property
    def package_type(self) -> str:
        return self.__package_type

    @package_type.setter
    def package_type(self, value: str):
        self.__package_type = value

    def calculate_price(self) -> float:
        base_price = 10
        weight_factor = 2 * self.__weight
        size_factor = len(self.__dimensions) * 0.5
        return base_price + weight_factor + size_factor

    def __str__(self):
        return f"Package(ID: {self.__package_id}, Weight: {self.__weight} kg, Dimensions: {self.__dimensions}, Type: {self.__package_type}, Price: ${self.calculate_price():.2f})"

def main():
    try_package = Package(10487, 25, "25*24", "basico")
    print(try_package)

if __name__ == '__main__':
    main()
