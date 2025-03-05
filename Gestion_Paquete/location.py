class Location(object):
    def __init__(self, country: str, department: str, city: str,
                 address1: str, address2: str, zip_code: int):  
        self.__country = country
        self.__department = department
        self.__city = city
        self.__address1 = address1
        self.__address2 = address2
        self.__zip_code = zip_code  

    @property
    def country(self) -> str:
        return self.__country
    
    @country.setter
    def country(self, value: str):
        self.__country = value
    
    @property
    def department(self) -> str:
        return self.__department
    
    @department.setter
    def department(self, value: str):
        self.__department = value
    
    @property
    def city(self) -> str:
        return self.__city
    
    @city.setter
    def city(self, value: str):
        self.__city = value
    
    @property
    def address1(self) -> str:
        return self.__address1
    
    @address1.setter
    def address1(self, value: str):
        self.__address1 = value
    
    @property
    def address2(self) -> str:
        return self.__address2
    
    @address2.setter
    def address2(self, value: str):
        self.__address2 = value
    
    #
    @property
    def zip_code(self) -> int:
        return self.__zip_code
    
    @zip_code.setter
    def zip_code(self, value):
        if not isinstance(value, int):
            raise TypeError("El código postal debe ser un número entero")
        if value <= 0:
            raise ValueError("El código postal debe ser un número entero positivo")
        self.__zip_code = value

    def __str__(self):
        return (f"Country: {self.country}, Department: {self.department}, City: {self.city}, "
                f"Address 1: {self.address1}, Address 2: {self.address2}, Zip Code: {self.zip_code}")

# PRUEBA DE LA CLASE
def main():
    alex_location = Location("Colombia", "Bolivar", "Cartagena", "CRA", "Blas", 130001)
    print(alex_location)

if __name__ == '__main__':
    main()
