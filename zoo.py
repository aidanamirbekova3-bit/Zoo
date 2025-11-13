from animals_species import Lion, Elephant, Bird, Snake

class Zoo:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"✅ {animal.name} добавлен(а) в зоопарк!")

    def show_animals(self):
        if not self.animals:
            print("Пока нет животных в зоопарке.")
        else:
            for i, a in enumerate(self.animals, start=1):
                print(f"{i}. {a.info()} — здоровье: {a.get_health_value()}%")

    def feed_all(self):
        if not self.animals:
            print("Нет животных для кормления.")
        else:
            for a in self.animals:
                print(a.feed(10))

    def remove_animal(self, name):
        for a in self.animals:
            if a.name.lower() == name.lower():
                self.animals.remove(a)
                print(f"❌ {a.name} удалён(а) из зоопарка.")
                return
        print(f"Животное {name} не найдено.")
