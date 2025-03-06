from enum import Enum

class OrderStatus(Enum):
    """
    Represents the possible statuses of an order.
    """
    PENDING = 'pending'
    PAYMENT_DUE_DATE = 'payment due date'
