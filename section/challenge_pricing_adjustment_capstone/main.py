# Create the Dictionary
grocery_inventory = {
    "Milk":   ("Dairy", 3.50, 8),
    "Eggs":   ("Dairy", 5.50, 30),
    "Bread":  ("Bakery", 2.99, 15),
    "Apples": ("Produce", 1.50, 50)
}

# Check and Update price
eggs_details = grocery_inventory["Eggs"]
eggs_price = eggs_details[1]
if eggs_price > 5.00:
    print("Eggs are too expensive, reducing the price by $1.00")
    grocery_inventory["Eggs"] = (eggs_details[0], eggs_price - 1.00, eggs_details[2])
else:    
    print("The price of Eggs is reasonable")

# Add a new item
grocery_inventory.update({"Tomatoes":  ("Produce", 1.20, 30)})
print("Inventory after adding Tomatoes:", grocery_inventory)

# Check the stock of milk
milk_details = grocery_inventory["Milk"]
milk_inventory = milk_details[2]
if milk_inventory < 10:
    print("Milk needs to be restocked. Increasing stock by 20 units.")
    grocery_inventory["Milk"] = (milk_details[0], milk_details[1], milk_inventory + 20)
else:
    print("Milk has sufficient stock.")

# Remove Item based on price
apples_details = grocery_inventory["Apples"]
apples_price = apples_details[1]
if apples_price > 2.00:
    grocery_inventory.pop("Apples")

print("Updated inventory:", grocery_inventory)