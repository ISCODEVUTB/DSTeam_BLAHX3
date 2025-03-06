from random import randbytes

class Location:
    def __init__(self, country: str, department: str, city: str,
                 address1: str, address2: str, zip_code: int):
        """
        Initializes a new instance of the Location class.

        Args:
            country (str): The country of the location.
            department (str): The department or state of the location.
            city (str): The city of the location.
            address1 (str): The main address line.
            address2 (str): The secondary address line.
            zip_code (int): The postal code of the location.

        Attributes:
            __id (str): A unique identifier for the location.
            __country (str): The country of the location.
            __department (str): The department or state of the location.
            __city (str): The city of the location.
            __address1 (str): The main address line.
            __address2 (str): The secondary address line.
            __zip_code (int): The postal code of the location.
        """
        self.__id = randbytes(5).hex()  # Generate a unique ID for the location
        self.__country = country
        self.__department = department
        self.__city = city
        self.__address1 = address1
        self.__address2 = address2
        self.zip_code = zip_code  # Uses the setter to validate the zip_code

    @property
    def location_id(self) -> str:
        """
        Gets the location's ID.

        Returns:
            str: The unique ID of the location.
        """
        return self.__id

    @property
    def country(self) -> str:
        """
        Gets the country of the location.

        Returns:
            str: The name of the country.
        """
        return self.__country
    
    @country.setter
    def country(self, value: str):
        """
        Sets the country of the location.

        Args:
            value (str): The new country name.
        """
        self.__country = value
    
    @property
    def department(self) -> str:
        """
        Gets the department or state of the location.

        Returns:
            str: The name of the department.
        """
        return self.__department
    
    @department.setter
    def department(self, value: str):
        """
        Sets the department or state of the location.

        Args:
            value (str): The new department name.
        """
        self.__department = value
    
    @property
    def city(self) -> str:
        """
        Gets the city of the location.

        Returns:
            str: The name of the city.
        """
        return self.__city
    
    @city.setter
    def city(self, value: str):
        """
        Sets the city of the location.

        Args:
            value (str): The new city name.
        """
        self.__city = value
    
    @property
    def address1(self) -> str:
        """
        Gets the first address line of the location.

        Returns:
            str: The first address line.
        """
        return self.__address1
    
    @address1.setter
    def address1(self, value: str):
        """
        Sets the first address line of the location.

        Args:
            value (str): The new value for the first address line.
        """
        self.__address1 = value
    
    @property
    def address2(self) -> str:
        """
        Gets the second address line of the location.

        Returns:
            str: The second address line.
        """
        return self.__address2
    
    @address2.setter
    def address2(self, value: str):
        """
        Sets the second address line of the location.

        Args:
            value (str): The new value for the second address line.
        """
        self.__address2 = value
    
    @property
    def zip_code(self) -> int:
        """
        Gets the postal code of the location.

        Returns:
            int: The postal code.
        """
        return self.__zip_code
    
    @zip_code.setter
    def zip_code(self, value: int):
        """
        Sets the postal code of the location. Validates that it is a positive integer.

        Args:
            value (int): The new postal code.

        Raises:
            TypeError: If the postal code is not an integer.
            ValueError: If the postal code is not positive.
        """
        if not isinstance(value, int):
            raise TypeError("The postal code must be an integer.")
        if value <= 0:
            raise ValueError("The postal code must be a positive value.")
        self.__zip_code = value
    
    def __str__(self):
        """
        String representation of the location.

        Returns:
            str: A string containing all the details of the location.
        """
        return f"ID: {self.location_id}\nCountry: {self.country}\nDepartment: {self.department}\nCity: {self.city}\nAddress-1: {self.address1}\nAddress-2: {self.address2}\nZip-Code: {self.zip_code}"


def main():
    """
    Main entry point of the program.

    This function tests the Location class.
    """
    try:
        # Testing the Location class
        alex_location = Location("Colombia", "Bolivar", "Cartagena", "CRA", "Blas", 130001)
        print(alex_location)

        # Testing postal code validation with an invalid code
        invalid_location = Location("Colombia", "Bolivar", "Cartagena", "CRA", "Blas", -130001)  # This should raise a ValueError
    except Exception as e:
        print(f"Error: {e}")


if __name__ == '__main__':
    main()
