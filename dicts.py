
def create_inventory(items):
    elementos = dict()
    for element in items:
        elementos[element] = items.count(element)
    return elementos


def add_items(inventory, items):
    keys = inventory.keys()
    for element in items:
        if element in keys:
            inventory[element] += 1
        else:
            inventory[element] = +1
    return inventory


def decrement_items(inventory, items):
    keys = inventory.keys()
    for element in items:
        if element in keys and inventory[element] > 0:
            inventory[element] -= 1
    return inventory


def remove_item(inventory, item):
    keys = inventory.keys()
    if item in keys:
        del inventory[item]
    return inventory


def list_inventory(inventory):
    list = []
    for key, value in inventory.items():
        if value > 0:
            list.append((key, value))

    return list

