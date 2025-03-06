"""Importing bcrypt for hashing passwords securely"""
from bcrypt import hashpw, gensalt

"""Importing the Location class from the 'Gestion_Paquete' """
from Gestion_Paquete.location import Location


class User:
    """Represents a user"""

    def __init__(self, surname: str, last_name: str, national_id: str, 
                 email: str, address: Location, password: str):
        """Initializes a User instance with personal details and hashed password"""
        self._name = surname
        self._last_name = last_name
        self._national_id = national_id
        self._email = email
        self._address = address
        self._password = self.hashpwd(password.encode('utf-8'))

    @property
    def name(self) -> str:
        """Returns the name"""
        return self._name

    @name.setter
    def name(self, value: str):
        """Sets the name"""
        self._name = value

    @property
    def last_name(self) -> str:
        """Return the last name"""
        return self._last_name

    @last_name.setter
    def last_name(self, value: str):
        """Sets the last name"""
        self._last_name = value

    @property
    def national_id(self) -> str:
        """Returns the user's national ID."""
        return self._national_id

    @national_id.setter
    def national_id(self, value: str):
        """Sets the user's national ID."""
        self._national_id = value

    @property
    def email(self) -> str:
        """Returns the user's email address."""
        return self._email

    @email.setter
    def email(self, value: str):
        """Sets the user's email address."""
        self._email = value

    @property
    def address(self) -> Location:
        """Returns the user's associated address."""
        return self._address

    @address.setter
    def address(self, value: Location):
        """Sets the user's address."""
        self._address = value

    def hashpwd(self, pwd: bytes) -> bytes:
        """Hashes the password using bcrypt"""
        return hashpw(pwd, gensalt())

    def __str__(self):
        """Returns a string representation of the User instance"""
        return f"Name: {self.name}, Last name: {self.last_name}, National id: {self.national_id}, Email: {self.email}, Address: ({self.address}), Password: {self._password}"


def main():
    alex_location = Location("Colombia", "Bolivar", "Cartagena", "CRA", "Danis", 130001)
    alex = User("Alex", "Prens", "1944682", "a@gmail.com", alex_location, "Rococco")
    print(alex)


if __name__ == '__main__':
    main()
