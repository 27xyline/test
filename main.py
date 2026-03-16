class GameCharacter:
    def __init__(self, name, damage, health):
        self.name = name
        self.damage = damage
        self.health = health
    
    def attack(self):
        print(f"{self.name} наносит {self.damage} урона")
    
    def take_damage(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0
            print(f"Убит")
            return
        print(f"{self.name} получил {amount} урона. Осталось здоровья {self.health}")


user1 = GameCharacter(name="Gleb", damage=17, health=80)
user1.attack()
user1.take_damage(23)
user1.take_damage(12)
