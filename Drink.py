from Product import Product


class Drink(Product):

    def __init__(self, name: str, price: int, volume: int) -> None:
        super().__init__(name, price)
        self.__volume = volume
