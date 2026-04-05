def ft_water_reminder():
    x = int(input("Days since last watering: "))
    if x <= 2:
        print("Plants are fine")
    else:
        print("Water the plants!")
