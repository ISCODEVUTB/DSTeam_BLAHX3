"""
Module containing user's order-related functionality.

This module defines the Order class, which represents an order with 
specific attributes such as sender, receiver, packages, and status,

Imports:
    randbytes (random): Generates random bytes for unique identifiers.
    List (typing): Import List for type hinting lists
    User (user): Represents a user.
    Package (package): Represents a package

Classes:
    - Location: Represents an address with an ID, country, department, 
    city, address1, address2, and zip code.
"""
import uuid
from typing import List
from src.users import User
from src.package import Package
from src.order_status import OrderStatus


class Order:
    def __init__(self, sender: User, receiver: User, 
                 packages: List[Package], status: OrderStatus = OrderStatus.PENDING):
        """Initializes an Order with sender, receiver, packages, and status.

        Args:
            order_id (int): The unique identifier for the order.
            sender (User): The user sending the order.
            receiver (User): The user receiving the order.
            packages (List[Package]): A list of packages in the order.
            status (str): The current status of the order.

            __order_id (str): A unique identifier for the order.
            __sender (User): The user sending the order.
            __receiver (User): The user receiving the order.
            __packages (List[Package]): A list of packages included in the order.
            __status (OrderStatus): The current status of the order.
                                    Defaults to OrderStatus.PENDING
        """
        self.__order_id = str(uuid.uuid4())  # Generate a unique order ID
        self.__sender = sender
        self.__receiver = receiver
        self.__packages = packages
        self.__status = status

    @property
    def order_id(self) -> int:
        """Gets the unique order ID.

        Returns:
            int: The order ID.
        """
        return self.__order_id

    @property
    def sender(self) -> User:
        """Gets the sender of the order.

        Returns:
            User: The sender.
        """
        return self.__sender
    
    @sender.setter
    def sender(self, value: User):
        """Sets the sender of the order.

        Args:
            value (User): The new sender.
        """
        self.__sender = value

    @property
    def receiver(self) -> User:
        """Gets the receiver of the order.

        Returns:
            User: The receiver.
        """
        return self.__receiver

    @receiver.setter
    def receiver(self, value: User):
        """Sets the receiver of the order.

        Args:
            value (User): The new receiver.
        """
        self.__receiver = value

    @property
    def packages(self) -> List[Package]:
        """Gets the list of packages in the order.

        Returns:
            List[Package]: The list of packages.
        """
        return self.__packages

    @packages.setter
    def packages(self, value: List[Package]):
        """Sets the list of packages in the order.

        Args:
            value (List[Package]): The new package list.
        """
        self.__packages = value

    @property
    def status(self) -> str:
        """Gets the current status of the order.

        Returns:
            str: The order status.
        """
        return self.__status.name

    @status.setter
    def status(self, value: OrderStatus):
        """Sets the status of the order.

        Args:
            value (OrderStatus): The new status.
        """
        self.__status = value

    def add_package(self, package: Package):
        """Adds a package to the order.

        Args:
            package (Package): The package to add.
        """
        self.__packages.append(package)

    def remove_package(self, package_id: str):
        """Removes a package from the order by package ID.

        Args:
            package_id (int): The ID of the package to remove.
        """
        self.__packages = [pkg for pkg in self.__packages if pkg.package_id != package_id]

    def __str__(self):
        package_info = ', '.join(str(pkg) for pkg in self.__packages)
        return f"Order(ID: {self.order_id}, Sender: {self.sender.name}, Receiver: {self.receiver.name}, Packages: [{package_info}], Status: {self.status})"
