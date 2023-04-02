from Drink import Drink
from VendingMachineDrink import VendingMachineDrink

list_product = [Drink('cola', 60, 2), Drink('tea', 50, 1), Drink('water', 40, 1)]
machine_drink = VendingMachineDrink()
machine_drink.init_product(list_product)

print("Выдача продукта по имени:")
print(machine_drink.get_product("water"))

print("Итерирование экземпляров класса")
for item in machine_drink:
    print(item)

print("Сравнение экземпляров класса")
print(Drink('cola', 60, 2) > Drink('tea', 50, 1))

