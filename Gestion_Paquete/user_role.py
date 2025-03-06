from enum import Enum

class UserRole(Enum):
    CLIENT: str = 'client'
    ADMIN: str = 'admin'
    WORKER: str = 'worker'
    DISTRIBUTOR: str = 'distributor'
