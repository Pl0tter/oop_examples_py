from typing import List
from Product import Product
from VendingMachine import VendingMachine


# from Product import Product
# from typing import List


class VendingMachineDrink(VendingMachine):
    def __init__(self):
        self.__list_product = []

    def init_product(self, list_product: List[Product]):
        self.__list_product = list_product

    def get_product(self, name: str) -> Product:
        for product in self.__list_product:
            if product.get_name().lower() == name.lower():
                return product

    def __iter__(self):
        self.__count = -1
        return self

    def __next__(self):
        self.__count += 1
        if self.__count < len(self.__list_product):
            return self.__list_product[self.__count]
        else:
            raise StopIteration
