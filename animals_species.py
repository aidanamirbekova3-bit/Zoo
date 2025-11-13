from animal import Animal

class Lion(Animal):
    def make_sound(self):
        return "🦁 Лев рычит громко и грозно!"
    def move(self):
        return "Лев идёт величественно на четырёх лапах."
    def info(self):
        return f"Лев {self.name}, {self.age} лет. Хищник, живёт в прайде."

class Elephant(Animal):
    def make_sound(self):
        return "🐘 Слон трубит хоботом!"
    def move(self):
        return "Слон идёт неторопливо, тяжело ступая."
    def info(self):
        return f"Слон {self.name}, {self.age} лет. Самое крупное наземное животное."

class Bird(Animal):
    def make_sound(self):
        return "🐦 Птица поёт и щебечет."
    def move(self):
        return "Птица летит высоко в небе."
    def info(self):
        return f"Птица {self.name}, {self.age} лет. Любит зерно и свежий воздух."

class Snake(Animal):
    def make_sound(self):
        return "🐍 Змея шипит угрожающе."
    def move(self):
        return "Змея скользит по земле волнообразно."
    def info(self):
        return f"Змея {self.name}, {self.age} лет. Хладнокровное пресмыкающееся."
