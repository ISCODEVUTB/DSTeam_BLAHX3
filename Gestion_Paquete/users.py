from bcrypt import hashpw, gensalt
from Gestion_Paquete.location import Location

class User(object):
    def __init__(self, surname: str, last_name: str, national_id: str, 
                 email: str, address: Location, password: str):
        self._name = surname
        self._last_name = last_name
        self._national_id = national_id
        self._email = email
        self._address = address
        self._password = self.hashpwd(password.encode('utf-8'))
    
    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, value: str):
        self._name = value

    @property
    def last_name(self) -> str:
        return self._last_name
    
    @last_name.setter
    def last_name(self, value: str):
        self._last_name = value
    
    @property
    def national_id(self) -> str:
        return self._national_id
    
    @national_id.setter
    def national_id(self, value: str):
        self._national_id = value
    
    @property
    def email(self) -> str:
        return self._email
    
    @email.setter
    def email(self, value: str):
        self._email = value
    
    @property
    def address(self) -> Location:
        return self._address
    
    @address.setter
    def address(self, value: Location):
        self._address = value

    def hashpwd(self, pwd: bytes) -> bytes:
        return hashpw(pwd, gensalt())

    def __str__(self):
        return f"Name: {self._name}, Last name: {self._last_name}, National id: {self._national_id}, Email: {self._email}, Address: ({self._address}), Password: {self._password}"

def main():
    alex_location = Location("Colombia", "Bolivar", "Cartagena", "CRA", "Danis", 130001)
    alex = User("Alex", "Prens", "1944682", "a@gmail.com", alex_location, "Rococco")
    print(alex)
    

if __name__ == '__main__':
    main()
