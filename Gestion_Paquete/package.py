"""
Module containing package-related functionality.

This module defines the Package class, which represents a package with 
specific attributes such as weight, dimensions, and type. 

Imports:
    - randbytes (from random): Generates a random package ID.
    - PackageTypes (from package_types): Enum defining package types.

Classes:
    - Package: Represents a package with an ID, weight, dimensions, and type.
"""
from random import randbytes
from Gestion_Paquete.package_types import PackageTypes


class Package:
    def __init__(self, weight: float, length: float, width: float, height: float):
        """
        Initializes a Package instance.

        Args:
            weight (float): The weight of the package in kilograms.
            dimensions (str): The dimensions of the package (LxWxH).
        
        Attributes:
            __package_id (str): A unique identifier for the package.
            __weight (float): The weight of the package in kilograms.
            __dimensions (str): The dimensions of the package (LxWxH).
            __package_type (str): The type of package, determined dynamically.
        """
        self.__package_id = randbytes(5).hex()  # Generate a unique package ID
        self.__weight = weight
        self.__length = length
        self.__width = width
        self.__height = height
        self.__package_type = self.typing_package()

    @property
    def package_id(self) -> str:
        """
        Gets the unique package ID.
        
        Returns:
            str: The package's unique identifier.
        """
        return self.__package_id

    @property
    def weight(self) -> float:
        """
        Gets the package weight.
        
        Returns:
            float: The package's weight.
        """
        return self.__weight

    @weight.setter
    def weight(self, value: float):
        """
        Sets the weight of the package.

        Args:
            value (float): The new weight of the package.
        """
        self.__weight = value

    @property
    def dimensions(self) -> str:
        """
        Gets the package dimensions (LxWxH).
        
        Returns:
            str: The package's dimensions (LxWxH).
        """
        return f"{self.__length}x{self.__width}x{self.__height}"

    @property
    def length(self) -> float:
        """
        Gets the length of the package.

        Returns:
            float: The length of the package in meters.
        """
        return self.__length

    @length.setter
    def length(self, value: float):
        """
        Sets the length of the package.

        Args:
            value (float): The new length in meters.
        """
        self.__length = value

    @property
    def width(self) -> float:
        """
        Gets the width of the package.

        Returns:
            float: The width of the package in meters.
        """
        return self.__width

    @width.setter
    def width(self, value: float):
        """
        Sets the width of the package.

        Args:
            value (float): The new width in meters.
        """
        self.__width = value

    @property
    def height(self) -> float:
        """
        Gets the height of the package.

        Returns:
            float: The height of the package in meters.
        """
        return self.__height

    @height.setter
    def height(self, value: float):
        """
        Sets the height of the package.

        Args:
            value (float): The new height in meters.
        """
        if value <= 0:
            raise ValueError("Height must be a positive number.")
        self.__height = value

    @property
    def package_type(self) -> str:
        """
        Gets the type of package.
        
        Returns:
            str: The package's type as a string.
        """
        return self.__package_type.name

    def typing_package(self) -> PackageTypes:
        """
        Determines the type of package.

        Currently, this method defaults to `PackageTypes.ESTANDAR` 
        because the validation criteria for categorizing package types 
        have not been implemented yet.

        Returns:
            PackageTypes: The type of the package (currently defaults to ESTANDAR).
        """
        return PackageTypes.ESTANDAR

    def calculate_price(self) -> float:
        """
        Calculates the shipping price based on weight and dimensions.

        Returns:
            float: The total shipping cost.

        Pricing Model:
            - Base price: $10
            - Weight factor: $2 per kg
            - Size factor: $0.5 per cubic meter (L * W * H)
            - Minimum price: $10
            - Maximum price cap: $500
        """
        base_price = 10
        weight_factor = 2 * self.__weight

        size_factor = (self.length * self.width * self.height) * 0.5  # Cost per cubic meter

        total_price = base_price + weight_factor + size_factor

        # Apply pricing limits
        return max(10, min(total_price, 500))

    def __str__(self):
        return f"Package(ID: {self.package_id}\nWeight: {self.weight} kg\nDimensions: {self.dimensions}\nType: {self.package_type}\nPrice: ${self.calculate_price():.2f})"


def main():
    """
    Main entry point of the program.

    This function tests the Package class.
    """
    try_package = Package(25, "25*24")
    print(try_package)


if __name__ == '__main__':
    main()
