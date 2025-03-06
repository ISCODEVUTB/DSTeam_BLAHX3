from enum import Enum

class OrderStatus(Enum):
    PENDING: str = 'pending'
    PAYMENT_DUE_DATE: str = 'payment due date'
