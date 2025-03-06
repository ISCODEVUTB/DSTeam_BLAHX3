"""
Module containing user-related functionality.

This module defines the User class, which represents a user with 
specific attributes such as name, last name, national id, email,
address, password, and role. 

Imports:
    randbytes (random): Generates random bytes for unique identifiers.
    hashpw, gensalt (bcrypt): Used for password hashing and salting.
    Location (location): Represents a user's location.
    UserRole (user_role): Defines different user roles in the system.

Classes:
    - User: Eepresents a user with an ID, name, last name, national id, 
    email, address, password, and role.
"""
from random import randbytes
from bcrypt import hashpw, gensalt
from location import Location
from user_role import UserRole

class User:
    def __init__(self, name: str, last_name: str, national_id: str, 
                 email: str, address: Location, password: str = "blahx3", role: UserRole = UserRole.CLIENT):
        """
        Initializes a new instance of the class.

        Args:
            name (str): The user's first name.
            last_name (str): The user's last name.
            national_id (str): The user's national identification number.
            email (str): The user's email address.
            address (Location): The user's location or address.
            password (str, optional): The user's password (encrypted before storage). 
                                    Defaults to "blahx3".
            role (UserRole, optional): The user's role in the system. Defaults to UserRole.CLIENT.

        Attributes:
            __id (str): A unique identifier generated randomly.
            _name (str): The user's first name.
            _last_name (str): The user's last name.
            _national_id (str): The user's national identification number.
            _email (str): The user's email address.
            _address (Location): The user's address.
            _password (str): The hashed password of the user.
            _role (UserRole): The user's role in the system.
        """
        self.__id = randbytes(5).hex() # Generate a unique user ID
        self._name = name
        self._last_name = last_name
        self._national_id = national_id
        self._email = email
        self._address = address
        self._password = self.hashpwd(password.encode())
        self._role = role
    
    @property
    def user_id(self) -> str:
        """
        Gets the user's unique identifier.

        Returns:
            str: The user's ID as a string.
        """
        return str(self.__id)

    @property
    def name(self) -> str:
        """
        Gets the user's name.

        Returns:
            str: The user's name as a string.
        """
        return self._name
    
    @name.setter
    def name(self, value: str):
        """
        Sets the user's name.

        Args:
            value (str): The new name of the user.
        """
        self._name = value

    @property
    def last_name(self) -> str:
        """
        Gets the user's last name.

        Returns:
            str: The user's last name as a string.
        """
        return self._last_name
    
    @last_name.setter
    def last_name(self, value: str):
        """
        Sets the user's last name.

        Args:
            value (str): The new last name of the user.
        """
        self._last_name = value
    
    @property
    def national_id(self) -> str:
        """
        Gets the user's national identification.

        Returns:
            str: The user's national identification as a string.
        """
        return self._national_id
    
    @property
    def email(self) -> str:
        """
        Gets the user's email.

        Returns:
            str: The user's email as a string.
        """
        return self._email
    
    @email.setter
    def email(self, value: str):
        """
        Sets the user's email.

        Args:
            value (str): The new email of the user.
        """
        self._email = value
    
    @property
    def address(self) -> Location:
        """
        Gets the user's address.

        Returns:
            Location: The user's location.
        """
        return self._address
    
    @address.setter
    def address(self, value: Location):
        """
        Sets the user's address.

        Args:
            value (Location): The new location to assign to the user.
        """
        self._address = value.location_id

    @property
    def password(self) -> bytes:
        """
        Gets the hashed password of the user.

        Returns:
            bytes: The hashed password.
        """
        return self._password
    
    @password.setter
    def password(self, value: str):
        """
        Sets and hashes the user's password.

        Args:
            value (str): The new password to be hashed and stored.
        """
        self._password = self.hashpwd(value.encode())

    @property
    def role(self) -> str:
        """
        Gets the user's role.

        Returns:
            str: The user's role as a string.
        """
        return self._role.name
    
    @role.setter
    def role(self, value: UserRole):
        """
        Sets the user's role.

        Args:
            value (UserRole): The new role of the user.
        """
        self._role = value

    def hashpwd(self, pwd: bytes) -> bytes:
        """
        Hashes a password using bcrypt.

        Args:
            pwd (bytes): The password in bytes to be hashed.

        Returns:
            bytes: The hashed password.
        """
        return hashpw(pwd, gensalt())

    def __str__(self):
        return f"ID: {self.user_id}\nRole: {self.role}\nName: {self.name}\nLast-name: {self.last_name}\nNational-id:{self.national_id}\nEmail: {self.email}\nAddress: ({self.address})"

def main():
    """
    Main entry point of the program.

    This function tests the User class.
    """
    alex_location = Location("Colombia", "Bolivar", "Cartagena", "CRA", "Blas", 130001)
    alex = User("Alex", "Pres", "230495", "a@gmail.com", alex_location, "Rococco")
    print(alex)
    

if __name__ == '__main__':
    main()
