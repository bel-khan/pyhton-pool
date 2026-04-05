class Plant:
    def __init__(self, name, height=15.0, age=10):
        self.name = name
        self._height = height
        self._age = age

    def grow(self, amount):
        self._height += amount

    def age(self, days):
        self._age += days

    def show(self):
        print(f"{self.name}: {self._height}cm, {self._age} days old")


# 🌸 Flower
class Flower(Plant):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color
        self.bloomed = False

    def bloom(self):
        self.bloomed = True

    def show(self):
        super().show()
        print(f"Color: {self.color}")
        if self.bloomed:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")


# 🌳 Tree
class Tree(Plant):
    def __init__(self, name, trunk_diameter):
        super().__init__(name, 200.0, 365)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        print(
            f"Tree {self.name} now produces a shade of "
            f"{self._height}cm long and {self.trunk_diameter}cm wide."
        )

    def show(self):
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}cm")


# 🥕 Vegetable
class Vegetable(Plant):
    def __init__(self, name, harvest_season):
        super().__init__(name, 5.0, 10)
        self.harvest_season = harvest_season 
        self.nutritional_value = 0

    def grow(self, amount):
        super().grow(amount)
        self.nutritional_value += amount

    def age(self, days):
        super().age(days)
        self.nutritional_value += days

    def show(self):
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")


print("=== Garden Plant Types ===")

# 🌸 Flower
print("=== Flower")
rose = Flower("Rose", "red")
rose.show()
print("[asking the rose to bloom]")
rose.bloom()
rose.show()

# 🌳 Tree
print("=== Tree")
oak = Tree("Oak", 5.0)
oak.show()
print("[asking the oak to produce shade]")
oak.produce_shade()

# 🥕 Vegetable
print("=== Vegetable")
tomato = Vegetable("Tomato", "April")
tomato.show()
print("[make tomato grow and age for 20 days]")
tomato.grow(42)   # 5 → 47
tomato.age(20)    # 10 → 30
tomato.show()