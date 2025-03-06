from enum import Enum


class PaymentMethod(Enum):
    """Enumeration that represents the different available payment methods."""
    CREDIT = 'Credit'
    DEBIT = 'Debit'
    TRANSFER = 'Transfer'
    CASH = 'Cash'


class Payment:
    """Class representing a payment with its ID, amount, method, and date."""

    def __init__(self, payment_id: int, amount: float, method: PaymentMethod, date: str):
        """
        Initializes a Payment object.

        Args:
            payment_id (int): Unique identifier of the payment.
            amount (float): Amount of the payment.
            method (PaymentMethod): Payment method used.
            date (str): Payment date as a string.
        """
        self.__payment_id = payment_id
        self.__amount = amount
        self.__method = method
        self.__date = date

    @property
    def payment_id(self) -> int:
        """Returns the payment identifier."""
        return self.__payment_id

    @property
    def amount(self) -> float:
        """Returns the payment amount."""
        return self.__amount

    @property
    def method(self) -> PaymentMethod:
        """Returns the payment method used."""
        return self.__method

    @property
    def date(self) -> str:
        """Returns the payment date."""
        return self.__date

    def __str__(self) -> str:
        """Returns a string representation of the Payment object."""
        return (f"Payment(ID: {self.payment_id}, Amount: ${self.amount:.2f}, "
                f"Method: {self.method.value}, Date: {self.date})")
