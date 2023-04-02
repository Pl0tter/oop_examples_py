from abc import ABC, abstractmethod
from typing import List
from Product import Product


class VendingMachine(ABC):
    __list_product: list[Product]

    @abstractmethod
    def init_product(self, list_product: List[Product]):
        pass

    @abstractmethod
    def get_product(self, name: str) -> Product:
        pass
