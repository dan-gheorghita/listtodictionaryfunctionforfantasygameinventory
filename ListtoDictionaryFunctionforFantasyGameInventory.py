```python
def displayInventory(inventory):  # Function to display the current inventory
    print("Inventory:")  # Print the title of the inventory
    item_total = 0  # Initialize a variable to keep track of the total number of items
    for k, v in inventory.items():  # Iterate over each item in the inventory
        print(str(v) + ' ' + k)  # Print the quantity and name of the item
        item_total += v  # Increment the total number of items
    print("Total number of items: " + str(item_total))  # Print the total number of items

def addToInventory(inventory, addedItems):  # Function to add items to the inventory
    for item in addedItems:  # Iterate over each item in the list of added items
        if(item not in inventory):  # Check if the item is not already in the inventory
            inventory[item] = 1  # If not, add it to the inventory with a quantity of 1
        else:
            inventory[item] += 1  # If the item is already in the inventory, increment its quantity
    return inventory  # Return the updated inventory

inv = {'gold coin': 42, 'rope': 1}  # Initialize the inventory with some items

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']  # List of items to add to the inventory

inv = addToInventory(inv, dragonLoot)  # Add the items to the inventory

displayInventory(inv)  # Display the updated inventory
```