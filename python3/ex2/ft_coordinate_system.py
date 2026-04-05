import math


def get_player_pos() -> tuple:
    while True:
        start = input("Enter new coordinates as floats in format 'x,y,z': ")
        parts = start.split(",")

        if len(parts) != 3:
            print("Invalid syntax")
            continue

        list = []
        error = False

        for part in parts:
            try:
                list.append(float(part.strip()))
            except ValueError as e:
                print("Error on parameter '" + part.strip() + "': " + str(e))
                error = True
                break
        if not error:
            return (list[0], list[1], list[2])


print("=== Game Coordinate System ===")

print("Get a first set of coordinates")
x = get_player_pos()
print("Got a first tuple:", x)
print("It includes: X=" + str(x[0]) + ", Y="
      + str(x[1]) + ", Z=" + str(x[2]))
dist_origine = math.sqrt(x[0]**2 + x[1]**2 + x[2]**2)
print("Distance to center:", round(dist_origine, 4))

print("Get a second set of coordinates")
y = get_player_pos()
dist_xy = math.sqrt((x[0]-y[0])**2 + (y[1]-x[1])**2 + (y[2]-x[2])**2)
print("Distance between the 2 sets of coordinates:", round(dist_xy, 4))
