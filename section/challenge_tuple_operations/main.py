# Current inventory on shelf
shelf = ("apples", "oranges", "bananas", "apples", "grapes", "bananas", "apples")

# Count and print how many times "apples" appear in the shelf tuple
apple_count = shelf.count("apples")
print(f"Number of Apples: {apple_count}")

# Find and print the index of the first occurrence of "bananas" in the shelf tuple
banana_index = shelf.index("bananas")
print(f"First Banana Index: {banana_index}")

# Check if the number of apples is less than 5
if apple_count < 5:
    print("Apples need to be restocked.")
else:
    print("Apples are sufficiently stocked.")

# Count and print how many times "grapes" appear in the shelf tuple
grape_count = shelf.count("grapes")
if grape_count == 1:
    print("Grapes need to be restocked.")
else:
    print("Grapes are sufficiently stocked.")

# Check if "oranges" exist in the shelf tuple
orange_count = shelf.index("oranges")
if "oranges" in shelf:
    print(f"Oranges are at index: {orange_count}")
else:
    print("Oranges are out of stock.")