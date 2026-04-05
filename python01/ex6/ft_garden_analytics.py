class Plant:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def grow(self):
        self.height += 1
        print(f"{self.name} grew 1cm")


class FloweringPlant(Plant):
    def __init__(self, name, height, color):
        super().__init__(name, height)
        self.color = color
        self.blooming = True


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, color, prize_points):
        super().__init__(name, height, color)
        self.prize_points = prize_points


class GardenManager:
    total_gardens = 0

    class GardenStats:
        def __init__(self):
            self.plants_added = 0
            self.total_growth = 0

        def add_plant(self):
            self.plants_added += 1

        def add_growth(self):
            self.total_growth += 1

    def __init__(self, owner):
        self.owner = owner
        self.plants = []
        self.stats = self.GardenStats()
        GardenManager.total_gardens += 1

    def add_plant(self, plant):
        self.plants.append(plant)
        self.stats.add_plant()
        print(f"Added {plant.name} to {self.owner}'s garden")

    def grow_all(self):
        print(f"{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()
            self.stats.add_growth()

    def report(self):
        print(f"=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")

        regular = 0
        flowering = 0
        prize = 0

        for plant in self.plants:
            if isinstance(plant, PrizeFlower):
                print(f"- {plant.name}: {plant.height}cm, "
                      f"{plant.color} flowers (blooming), "
                      f"Prize points: {plant.prize_points}")
                prize += 1
            elif isinstance(plant, FloweringPlant):
                print(f"- {plant.name}: {plant.height}cm, "
                      f"{plant.color} flowers (blooming)")
                flowering += 1
            else:
                print(f"- {plant.name}: {plant.height}cm")
                regular += 1

        print(f"Plants added: {self.stats.plants_added}, "
              f"Total growth: {self.stats.total_growth}cm")

        print(f"Plant types: {regular} regular, "
              f"{flowering} flowering, {prize} prize flowers")

    @classmethod
    def create_garden_network(cls):
        print(f"Total gardens managed: {cls.total_gardens}")

    @staticmethod
    def validate_height(height):
        return height >= 0


print("=== Garden Management System Demo ===")

garden1 = GardenManager("Alice")
garden2 = GardenManager("Bob")
p1 = Plant("Oak Tree", 140)
p2 = FloweringPlant("Rose", 50, "red")
p3 = PrizeFlower("Sunflower", 25, "yellow", 10)
garden1.add_plant(p1)
garden1.add_plant(p2)
garden1.add_plant(p3)
p4 = Plant("Pine Tree", 91)
garden2.add_plant(p4)
print()
garden1.grow_all()
garden2.grow_all()
print()
garden1.report()
print()
print("Height validation test:",
      GardenManager.validate_height(10))
score1 = sum(p.height for p in garden1.plants)
score2 = sum(p.height for p in garden2.plants)
print(f"Garden scores - Alice: {score1}, Bob: {score2}")
GardenManager.create_garden_network()
