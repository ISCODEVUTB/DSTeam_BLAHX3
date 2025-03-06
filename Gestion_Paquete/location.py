class Location:
    """Represents a location."""

    def __init__(self, country: str, department: str, city: str,
                 address1: str, address2: str, zip_code: int):
        """Initializes a Location instance."""
        self.__country = country
        self.__department = department
        self.__city = city
        self.__address1 = address1
        self.__address2 = address2
        self.__zip_code = zip_code


    @property
    def country(self) -> str:
        """Returns the country associated with the location."""
        return self.__country


    @country.setter
    def country(self, value: str):
        """Sets the country of the location."""
        self.__country = value


    @property
    def department(self) -> str:
        """Returns the department associated with the location."""
        return self.__department


    @department.setter
    def department(self, value: str):
        """Sets the department of the location."""
        self.__department = value


    @property
    def city(self) -> str:
        """Returns the city associated with the location."""
        return self.__city


    @city.setter
    def city(self, value: str):
        """Sets the city of the location."""
        self.__city = value


    @property
    def address1(self) -> str:
        """Returns the primary address."""
        return self.__address1


    @address1.setter
    def address1(self, value: str):
        """Sets the primary address."""
        self.__address1 = value


    @property
    def address2(self) -> str:
        """Returns the secondary address."""
        return self.__address2
    

    @address2.setter
    def address2(self, value: str):
        """Sets the secondary address."""
        self.__address2 = value


    @property
    def zip_code(self) -> int:
        """Returns the zip code of the location."""
        return self.__zip_code



    @zip_code.setter
    def zip_code(self, value: int):
        """Sets the zip code, ensuring it is a positive integer."""
        if not isinstance(value, int):
            raise TypeError("Zip code must be an integer.")

        if value <= 0:
            raise ValueError("Zip code must be a positive integer.")

        self.__zip_code = value


    def __str__(self):
        """Returns a string representation of the location."""
        return (f"Country: {self.country}, Department: {self.department}, City: {self.city}, "
                f"Address 1: {self.address1}, Address 2: {self.address2}, Zip Code: {self.zip_code}")



def main():
    """Creates a Location instance and prints its details."""
    alex_location = Location("Colombia", "Bolivar", "Cartagena", "CRA", "Blas", 130001)
    print(alex_location)



if __name__ == '__main__':
    main()
