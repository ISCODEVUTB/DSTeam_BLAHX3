"""
Module containing user's location-related functionality.

This module defines the Location class, which represents an address with 
specific attributes such as country, department, city, address1, address2,
and zip code. 

Imports:
    randbytes (random): Generates random bytes for unique identifiers.

Classes:
    - Location: Represents an address with an ID, country, department, 
    city, address1, address2, and zip code.
"""
from random import randbytes

class Location:
    def __init__(self, country: str, department: str, city: str,
                 address1: str, address2: str, zip_code: int):
        """
        Initializes a new Location instance.

        Args:
            country (str): The country of the location.
            department (str): The department or state of the location.
            city (str): The city of the location.
            address1 (str): The primary address line.
            address2 (str): The secondary address line.
            zip_code (int): The postal or ZIP code of the location.

        Attributes:
            __id (str): A unique identifier for the location.
            __country (str): The country of the location.
            __department (str): The department or state of the location.
            __city (str): The city of the location.
            __address1 (str): The primary address line.
            __address2 (str): The secondary address line.
            __zip_code (int): The postal or ZIP code of the location.
        """
        self.__id = randbytes(5).hex() # Generate a unique location ID
        self.__country = country
        self.__department = department
        self.__city = city
        self.__address1 = address1
        self.__address2 = address2
        self.__zip_code = zip_code
    
    @property
    def location_id(self) -> str:
        """
        Gets the lcoation's unique identifier.

        Returns:
            str: The location's ID as a string.
        """
        return self.__id

    @property
    def country(self) -> str:
        """
        Gets the country of the location.

        Returns:
            str: The country name.
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
        Gets the department of the location.

        Returns:
            str: The department name.
        """
        return self.__department
    
    @department.setter
    def department(self, value: str):
        """
        Sets the department of the location.

        Args:
            value (str): The new department name.
        """
        self.__department = value
    
    @property
    def city(self) -> str:
        """
        Returns the city of the location.

        Returns:
            str: The city name.
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
        Gets the first address of the location.

        Returns:
            str: The first address a string.
        """
        return self.__address1
    
    @address1.setter
    def address1(self, value: str):
        """
        Sets the first address of the location.

        Args:
            value (str): The new fist address name.
        """
        self.__address1 = value
    
    @property
    def address2(self) -> str:
        """
        Gets the second address of the location.

        Returns:
            str: The second address as a string.
        """
        return self.__address2
    
    @address2.setter
    def address2(self, value: str):
        """
        Sets the second address of the location.

        Args:
            value (str): The new second address name.
        """
        self.__address2 = value
    
    @property
    def zip_code(self) -> int:
        """
        Gets the zip code of the location.

        Returns:
            int: The zip code number.
        """
        return self.__zip_code
    
    @zip_code.setter
    def zip_code(self, value: int):
        """
        Sets the zip code of the location.

        Args:
            value (int): The new zip code number.
        """
        self.__zip_code = value
    
    def __str__(self):
        return f"ID: {self.location_id}\nCountry: {self.country}\nDepartment: {self.department}\nCity: {self.city}\nAddress-1: {self.address1}\nAddress-2: {self.address2}\nZip-Code: {self.zip_code}"
    

def main():
    """
    Main entry point of the program.

    This function tests the Location class.
    """
    alex_location = Location("Colombia", "Bolivar", "Cartagena", "CRA", "Blas", 130001)
    print (alex_location)

if __name__ == '__main__':
    main()
