class Plant:
    def __init__(self, name, height, age) -> None:
        self.name = name
        self.age = age
        self.height = height

    def greet(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")

    plant1 = Plant("Rose", 25, 30)
    plant2 = Plant("Sunflower", 80, 45)
    plant3 = Plant("Cactus", 15, 120)

    plant1.greet()
    plant2.greet()
    plant3.greet()
