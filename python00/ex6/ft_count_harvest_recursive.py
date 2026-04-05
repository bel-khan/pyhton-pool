def ft_count_harvest_recursive():
    x = int(input("Days until harvest: "))
    ft_count_recursive(1, x)
    print("Harvest time!")


def ft_count_recursive(day, days):
    if day > days:
        return
    print(f"Day {day}")
    ft_count_recursive(day + 1, days)
