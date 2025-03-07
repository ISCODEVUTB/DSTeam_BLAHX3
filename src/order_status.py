from enum import Enu


class OrderStatus(Enum):
    """
    Represents the possible statuses of an order.
    """
    PENDING = "Pending"
    SHIPPED = "Shipped"
    DELIVERED = "Delivered"
    CANCELED = "Canceled"
