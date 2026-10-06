# Create lists
meat     = ["Ham",    3.99, 50,  "Sliced"]
cheese   = ["Cheddar",5.49,100, "Sharp"]
condiment= ["Mustard", 1.99,75,  "Spicy"]

# Create main list
deli_dept = [meat, cheese, condiment]
print(f"Initial Deli List: {deli_dept}")

# Restock item
if meat[0] == "Ham" and meat[2] < 100:
    meat[2] = 100

# Add seasonal meat
seasonal_meat = ["Turkey", 4.50, 100, "Sliced"]
deli_dept.append(seasonal_meat)

# Remove condiment
deli_dept.remove(condiment)

# Sort the list by the first element of each sublist
deli_dept.sort()

# Print the updated state
print(f"Updated Deli List: {deli_dept}")