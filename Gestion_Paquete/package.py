class Package:
    def __init__(self, package_id: int, weight: float, dimensions: str, package_type: str):
        self.__package_id = package_id
        self.__weight = weight
        self.__dimensions = dimensions
        self.__package_type = package_type
        self.validate_dimensions(dimensions)

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
        self.validate_dimensions(value)  # Validar dimensiones antes de establecer
        self.__dimensions = value

    @property
    def package_type(self) -> str:
        return self.__package_type

    @package_type.setter
    def package_type(self, value: str):
        self.__package_type = value

    def validate_dimensions(self, dimensions: str):
        # Simple validation for dimensions format (e.g., "LxWxH")
        if len(dimensions.split('x')) != 3:
            raise ValueError("There must be three dimensions apart by x")
        if not all(x.isdigit() for x in dimensions.split('x')):
            raise ValueError("Dimensions must be in the format 'LxWxH' with numeric values.")

    def calculate_price(self) -> float:
        base_price = 10
        weight_factor = 2 * self.__weight
        size_factor = len(self.__dimensions) * 0.5
        return base_price + weight_factor + size_factor

    def __str__(self):
        return (f"Package(ID: {self.package_id}, Weight: {self.weight} kg, "
                f"Dimensions: {self.dimensions}, Type: {self.package_type}, "
                f"Price: ${self.calculate_price():.2f})")

def main():
    package_example = Package(10487, 25, "25x24x20", "basico")
    print(package_example)

if __name__ == '__main__':
    main()
