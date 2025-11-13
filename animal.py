from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name, age, species, health):
        self.name = name
        self.age = age
        self.species = species
        self.__health = health  # приватное поле

    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def info(self):
        pass

    # --- Инкапсуляция ---
    def get_health(self):
        if 100 >= self.__health > 70:
            return f'{self.name} здоров(а) ✅'
        elif 70 >= self.__health > 30:
            return f'{self.name} чувствует себя неважно ⚠️'
        elif 30 >= self.__health > 0:
            return f'{self.name} болен(а) ❌'
        else:
            return f'{self.name} погиб... 💀'

    def feed(self, amount):
        if self.__health <= 0:
            return f'{self.name} уже не может есть.'
        self.__health = min(100, self.__health + amount)
        return f'{self.name} накормлен(а)! Здоровье: {self.__health}%'

    def damage(self, amount):
        self.__health = max(0, self.__health - amount)
        return f'{self.name} получил(а) урон! Текущее здоровье: {self.__health}%'

    def get_health_value(self):
        return self.__health
