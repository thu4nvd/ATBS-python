from pprint import pprint

inventory = {
    'arrow': 12,
    'gold coin': 42,
    'rope': 1,
    'torch': 6,
    'dagger': 1
    }

dragonLoot = [
    'gold coin',
    'dagger',
    'gold coin',
    'gold coin',
    'ruby'
    ]

def displayInventory(inventory):
    print('Inventory:')
    for item, qty in inventory.items():
        print('%d %s' % (qty, item))
    total = sum(inventory.values())
    print('\nTotal number of items: %d' % total)

def addToInventory(inventory, items):
    for item in items:
        inventory[item] = inventory.get(item, 0) + 1
    return inventory

addToInventory(inventory, dragonLoot)
displayInventory(inventory)
