class Plant:
    def __init__(self, name, starting_height, starting_age):
        self.name = name
        self.height = starting_height
        self.age = starting_age

    def get_info(self):
        print(f"Created: {self.name} ({self.height}cm, {self.age} days)")


if __name__ == "__main__":
    print("=== Plant Factory Output ===")

    data = [
        ("Rose", 25, 30),
        ("Oak", 200, 365),
        ("Cactus", 5, 90),
        ("Sunflower", 80, 45),
        ("Fern", 15, 120)
    ]

    plants = []
    count = 0

    for i in range(5):
        name, height, age = data[i]
        plant = Plant(name, height, age)
        plants.append(plant)
        count += 1

    for i in range(5):
        plants[i].get_info()

    print(f"\nTotal plants created: {count}")
