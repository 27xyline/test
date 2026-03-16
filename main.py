# class GameCharacter:
#     def __init__(self, name, damage, health):
#         self.name = name
#         self.damage = damage
#         self.health = health
    
#     def attack(self):
#         print(f"{self.name} наносит {self.damage} урона")
    
#     def take_damage(self, amount):
#         self.health -= amount
#         if self.health < 0:
#             self.health = 0
#             print(f"Убит")
#             return
#         print(f"{self.name} получил {amount} урона. Осталось здоровья {self.health}")


# user1 = GameCharacter(name="Gleb", damage=17, health=80)
# user1.attack()
# user1.take_damage(23)
# user1.take_damage(12)


class Cart:
    def __init__(self, owner,):
        self.owner = owner
        self.items = []
    
    def add_item(self, name, price):
        self.items.append(dict(name=name, price=price))
    
    def get_total(self):
        total = sum(el['price'] for el in self.items)
        return total

    def show_items(self):
        if not self.items:
            print("Корзина пуста")
            return
        for el in self.items:
            print(f"{el['name']} - {el['price']}")


user1 = Cart(owner="Gleb")

user1.add_item(name="iPhone 17", price=80000)
user1.add_item(name="iPhone 15", price=50000)
user1.add_item(name="Дерьмо", price=100)
print()
user1.get_total()
print()
user1.show_items()
print()
print(user1.items)
