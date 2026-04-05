class SecurePlant:
    def __init__(self, name, height=15.0, age=10):
        self.name = name
        self._height = height
        self._age = age

    def set_height(self, height):
        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = height
            print(f"Height updated: {height}cm")

    def set_age(self, age):
        if age < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = age
            print(f"Age updated: {age} days")

    def get_height(self):
        return self._height

    def get_age(self):
        return self._age


print("=== Garden Security System ===")

plant = SecurePlant("Rose")
print(
    f"Plant created: {plant.name}: "
    f"{plant.get_height()}cm, {plant.get_age()} days old"
)

plant.set_height(25)
plant.set_age(30)

plant.set_height(-5)
plant.set_age(-10)

print(
    f"Current state: {plant.name}: "
    f"{plant.get_height()}cm, {plant.get_age()} days old"
)