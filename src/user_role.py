1from enum import Enum


class UserRole(Enum):
    """
    Represents the possible roles of an user.
    """
    CLIENT = 'client'
    ADMIN = 'admin'
    WORKER = 'worker'
    DISTRIBUTOR = 'distributor'
