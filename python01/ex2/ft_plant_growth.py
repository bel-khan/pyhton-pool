class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.age = age
        self.height = height

    def get_info(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")

    def grow(self):
        self.height += 1

    def age_up(self):
        self.age += 1


if __name__ == "__main__":
    n = 7
    plant = Plant("Rose", 25, 30)
    initial_height = plant.height
    print("=== Day 1 ===")
    plant.get_info()
    for i in range(1, n):
        plant.grow()
        plant.age_up()

    print(f"=== Day {n} ===")
    plant.get_info()
    growthn = plant.height - initial_height
    if growthn > 0:
        print(f"Growth this week: +{growthn}cm")
    elif growthn == 0:
        print("Your plant has not changed")
    else:
        print(f"Growth this week: {growthn}cm (your plant decreased)")
