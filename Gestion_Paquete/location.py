class Location:
    def __init__(self, country: str, department: str, city: str,
                 address1: str, address2: str, zip_code: int):
        self._country = country
        self._department = department
        self._city = city
        self._address1 = address1
        self._address2 = address2
        self.zip_code = zip_code  # Usa el setter para aplicar la validación

    @property
    def country(self) -> str:
        return self._country

    @country.setter
    def country(self, value: str):
        self._country = value

    @property
    def department(self) -> str:
        return self._department

    @department.setter
    def department(self, value: str):
        self._department = value

    @property
    def city(self) -> str:
        return self._city

    @city.setter
    def city(self, value: str):
        self._city = value

    @property
    def address1(self) -> str:
        return self._address1

    @address1.setter
    def address1(self, value: str):
        self._address1 = value

    @property
    def address2(self) -> str:
        return self._address2

    @address2.setter
    def address2(self, value: str):
        self._address2 = value

    @property
    def zip_code(self) -> int:
        return self._zip_code

    @zip_code.setter
    def zip_code(self, value: int):
        if not isinstance(value, int):
            raise TypeError("El código postal debe ser un número entero")
        if value <= 0:
            raise ValueError("El código postal debe ser un número entero positivo")
        self._zip_code = value

    def __str__(self):
        return (
            f"Country: {self.country}, Department: {self.department}, City: {self.city},\n"
            f"Address 1: {self.address1}, Address 2: {self.address2}, Zip Code: {self.zip_code}"
        )

    def __repr__(self):
        return (
            f"Location(country={repr(self.country)}, department={repr(self.department)}, "
            f"city={repr(self.city)}, address1={repr(self.address1)}, "
            f"address2={repr(self.address2)}, zip_code={self.zip_code})"
        )


def main():
    alex_location = Location("Colombia", "Bolívar", "Cartagena", "CRA", "Blas", 130001)
    print(alex_location)
    print(repr(alex_location))


if __name__ == "__main__":
    main()
