class Plant:
    class _Stats:
        def __init__(self) -> None:
            self.grow_calls: int = 0
            self.age_calls: int = 0
            self.show_calls: int = 0

        def display(self) -> None:
            print(f"Stats: {self.grow_calls} grow, "
                  f"{self.age_calls} age, {self.show_calls} show")

    def __init__(self, name: str, height: float = 15.0, age: int = 10) -> None:
        self.name: str = name
        self._height: float = height
        self._age: int = age
        self.__stats: Plant._Stats = Plant._Stats()

    def grow(self, amount: float) -> None:
        self._height += amount
        self.__stats.grow_calls += 1

    def age(self, days: int) -> None:
        self._age += days
        self.__stats.age_calls += 1

    def show_stats(self) -> None:
        print(f"[statistics for {self.name}]")
        self.__stats.display()

    def show(self) -> None:
        print(f"{self.name}: {self._height}cm, {self._age} days old")
        self.__stats.show_calls += 1

    @classmethod
    def anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)

    @staticmethod
    def is_older_than_year(days: int) -> bool:
        return days > 365


class Flower(Plant):
    def __init__(
        self,
        name: str,
        color: str,
        height: float = 15.0,
        age: int = 10
    ) -> None:
        super().__init__(name, height, age)
        self.color: str = color
        self.bloomed: bool = False

    def bloom(self) -> None:
        self.bloomed = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if self.bloomed:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")


class Tree(Plant):
    def __init__(
        self,
        name: str,
        trunk_diameter: float,
        height: float = 200.0,
        age: int = 365
    ) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter: float = trunk_diameter
        self._shade_calls: int = 0

    def produce_shade(self) -> None:
        self._shade_calls += 1
        print(f"Tree {self.name} now produces a shade of "
              f"{self._height}cm long and {self.trunk_diameter}cm wide.")

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}cm")

    def show_stats(self) -> None:
        super().show_stats()
        print(f"{self._shade_calls} shade")


class Seed(Flower):
    def __init__(
        self,
        name: str,
        color: str,
        height: float = 80.0,
        age: int = 45
    ) -> None:
        super().__init__(name, color, height, age)
        self.seeds: int = 0

    def bloom(self) -> None:
        super().bloom()
        self.seeds = 42

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self.seeds}")


def show_plant_stats(plant: Plant) -> None:
    plant.show_stats()


print("=== Garden statistics ===")

print("=== Check year-old")
print("Is 30 days more than a year? ->", Plant.is_older_than_year(30))
print("Is 400 days more than a year? ->", Plant.is_older_than_year(400))

print("")
print("=== Flower")
Rose = Flower("Rose", "red")

Rose.show()
show_plant_stats(Rose)

print(f"[asking the {Rose.name.lower()} to grow and bloom]")

Rose.grow(8)
Rose.bloom()

Rose.show()
show_plant_stats(Rose)

print()
print("=== Tree")
oak = Tree("Oak", 5.0)

oak.show()
show_plant_stats(oak)

print("[asking the oak to produce shade]")
oak.produce_shade()
show_plant_stats(oak)
print()

print("=== Seed")
sunflower = Seed("Sunflower", "yellow")

sunflower.show()

print("[make sunflower grow, age and bloom]")
sunflower.grow(30)
sunflower.age(20)
sunflower.bloom()

sunflower.show()
show_plant_stats(sunflower)

print()
print("=== Anonymous")
unknown = Plant.anonymous()

unknown.show()
show_plant_stats(unknown)
