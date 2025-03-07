from enum import Enum
from datetime import date


class PaymentMethod(Enum):
    """Enumeration that represents the different available payment methods."""
    CREDIT = 'Credit'
    DEBIT = 'Debit'
    TRANSFER = 'Transfer'
    CASH = 'Cash'


class Payment:
    def __init__(self, payment_id: int, amount: float, method: PaymentMethod, date: date):
        # Check that the method initialized is part of payment method
        if not isinstance(method, PaymentMethod):
            raise ValueError("Invalid payment method")

        self.__payment_id = payment_id
        self.__amount = amount
        self.__method = method
        self.__date = date

    @property
    def payment_id(self) -> int:
        return self.__payment_id

    @payment_id.setter
    def payment_id(self, value: int):
        self.__payment_id = value

    @property
    def amount(self) -> float:
        return self.__amount

    @amount.setter
    def amount(self, value: float):
        self.__amount = value

    @property
    def method(self) -> PaymentMethod:
        return self.__method

    @method.setter
    def method(self, value: PaymentMethod):
        self.__method = value

    @property
    def date(self) -> date:
        return self.__date

    @date.setter
    def date(self, value: date):
        self.__date = value

    def __str__(self):
        return (f"Payment(ID: {self.payment_id}, Amount: ${self.amount:.2f}, "
                f"Method: {self.method.value}, Date: {self.date.strftime('%Y-%m-%d')})")
