import sys

print("=== Inventory System Analysis ===")

inventory = {}

for arg in sys.argv[1:]:
    parts = arg.split(":")
    
    if len(parts) != 2:
        print("Error - invalid parameter '" + arg + "'")
        continue

    name = parts[0]
    quantity = parts[1]
    
    if name in inventory:
        print("Redundant item '" + name + "' - discarding")
        continue

    try:
        inventory[name] = int(quantity)
    except ValueError as e:
        print("Quantity error for '" + name + "': " + str(e))

print("Got inventory:", inventory)

item_list = list(dict.keys(inventory))
print("Item list:", item_list)

total = sum(dict.values(inventory))
print("Total quantity of the " + str(len(inventory)) + " items: " + str(total))

for name in item_list:
    percentage = round(inventory[name] / total * 100, 1)
    print("Item " + name + " represents " + str(percentage) + "%")

most = item_list[0]
least = item_list[0]

for name in item_list:
    if inventory[name] > inventory[most]:
        most = name
    if inventory[name] < inventory[least]:
        least = name

print("Item most abundant: " + most + " with quantity " + str(inventory[most]))
print("Item least abundant: " + least + " with quantity " + str(inventory[least]))

dict.update(inventory, {"magic_item": 1})
print("Updated inventory:", inventory)