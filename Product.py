from abc import ABC, ABCMeta, abstractmethod
from functools import total_ordering


@total_ordering
class Product(ABC):
    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self, name: str, price: int) -> None:
        self.__name = name
        self.__price = price

    def get_name(self) -> str:
        return self.__name

    def __str__(self) -> str:
        return f"Продукт: {self.__name}. Цена: {self.__price}"

    def __lt__(self, other):
        return self.__price < other.__price

    def __eq__(self, other):
        return self.__price == other.__price
