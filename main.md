from zoo import Zoo
from animals_species import Lion, Elephant, Bird, Snake

def main_menu():
    zoo = Zoo()

    zoo.add_animal(Lion("Алекс", 10, "lion", 80))
    zoo.add_animal(Elephant("Бобо", 6, "elephant", 90))
    zoo.add_animal(Bird("Кеша", 2, "parrot", 70))

    while True:
        print("\n=== 🦁 МЕНЮ ЗООПАРКА ===")
        print("1. Добавить животное")
        print("2. Показать всех животных")
        print("3. Покормить всех")
        print("4. Удалить животное")
        print("5. Выйти")
        choice = input("Выберите действие: ")

        if choice == "1":
            kind = input("Введите вид (lion, elephant, bird, snake): ").lower()
            name = input("Имя животного: ")
            age = int(input("Возраст: "))
            if kind == "lion":
                zoo.add_animal(Lion(name, age, kind, 100))
            elif kind == "elephant":
                zoo.add_animal(Elephant(name, age, kind, 100))
            elif kind == "bird":
                zoo.add_animal(Bird(name, age, kind, 100))
            elif kind == "snake":
                zoo.add_animal(Snake(name, age, kind, 100))
            else:
                print("❌ Неизвестный вид!")
        elif choice == "2":
            zoo.show_animals()
        elif choice == "3":
            zoo.feed_all()
        elif choice == "4":
            name = input("Введите имя животного для удаления: ")
            zoo.remove_animal(name)
        elif choice == "5":
            print("👋 До встречи в зоопарке!")
            break
        else:
            print("⚠️ Неверный ввод!")


if __name__ == "__main__":
    main_menu()


