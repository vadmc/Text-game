from abc import ABC, abstractmethod

# Шаг 1: Абстрактный класс оружия
class Weapon(ABC):
    @abstractmethod
    def attack(self) -> str:
        pass

# Шаг 2: Конкретные реализации оружия
class Sword(Weapon):
    def attack(self) -> str:
        return "наносит удар мечом!"

class Bow(Weapon):
    def attack(self) -> str:
        return "стреляет из лука!"

# Можно легко добавить новое оружие без изменения Fighter или Monster
class MagicWand(Weapon):
    def attack(self) -> str:
        return "колдует магическим жезлом!"

# Шаг 3: Класс бойца
class Fighter:
    def __init__(self, weapon: Weapon):
        self._weapon = weapon

    def change_weapon(self, weapon: Weapon):
        self._weapon = weapon

    def attack(self) -> str:
        return self._weapon.attack()

# Класс монстра (для полноты картины)
class Monster:
    def __init__(self, name: str = "Монстр"):
        self.name = name

    def is_defeated(self) -> str:
        return f"{self.name} побеждён!"

# Шаг 4: Механизм боя
def battle(fighter: Fighter, monster: Monster):
    print("Боец готовится к бою...")
    print(f"Боец {fighter.attack()}")
    print(monster.is_defeated())

# Демонстрация работы программы
if __name__ == "__main__":
    monster = Monster("Гоблин")

    # Боец с мечом
    fighter = Fighter(Sword())
    battle(fighter, monster)

    print("-" * 30)

    # Меняем оружие на лук
    fighter.change_weapon(Bow())
    battle(fighter, monster)

    print("-" * 30)

    # Добавляем новое оружие — магический жезл (без изменения Fighter или battle!)
    fighter.change_weapon(MagicWand())
    battle(fighter, monster)