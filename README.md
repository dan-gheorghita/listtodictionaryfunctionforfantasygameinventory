# ListtoDictionaryFunctionforFantasyGameInventory.py

**Inventory Management System**

The provided Python code implements a simple inventory management system. It consists of two functions: `displayInventory` and `addToInventory`.

### `displayInventory(inventory)`

This function takes an inventory dictionary as input and displays its contents. The inventory is iterated over, and for each item, its quantity and name are printed. The total number of items in the inventory is also calculated and displayed.

**Example Output:**

```
Inventory:
42 gold coin
1 rope
Total number of items: 43
```

### `addToInventory(inventory, addedItems)`

This function takes an inventory dictionary and a list of items to be added as input. It iterates over the list of added items and performs the following actions:

1. Checks if the item is not already in the inventory.
2. If the item is not in the inventory, adds it with a quantity of 1.
3. If the item is already in the inventory, increments its