from Gestion_Paquete.users import User
from Gestion_Paquete.package import Package

class Order:
    def __init__(self, order_id: int, user: User, packages: list, status: str):
        self.__order_id = order_id
        self.__user = user
        self.__packages = packages
        self.__status = status

    @property
    def order_id(self) -> int:
        return self.__order_id

    @order_id.setter
    def order_id(self, value: int):
        self.__order_id = value

    @property
    def user(self) -> User:
        return self.__user

    @user.setter
    def user(self, value: User):
        self.__user = value

    @property
    def packages(self) -> list:
        return self.__packages

    @packages.setter
    def packages(self, value: list):
        self.__packages = value

    @property
    def status(self) -> str:
        return self.__status

    @status.setter
    def status(self, value: str):
        self.__status = value

    def add_package(self, package: Package):
        self.__packages.append(package)

    def remove_package(self, package_id: int):
        self.__packages = [pkg for pkg in self.__packages if pkg.package_id != package_id]

    def __str__(self):
        package_info = ', '.join(str(pkg) for pkg in self.__packages)
        return f"Order(ID: {self.order_id}, User: {self.user.name}, Packages: [{package_info}], Status: {self.status})"
