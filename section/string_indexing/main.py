grocery_item = "Grilled Chicken Salad"

# Find the length of a string
length_of_item = len(grocery_item)

# Use positive indexing to get 1st char of each word
first_char = grocery_item[0]
second_char = grocery_item[8]
third_char = grocery_item[16]

# Use negative indexing to get last char of each word
last_char1 = grocery_item[-1]
last_char2 = grocery_item[-7]
last_char3 = grocery_item[-15]

# Testing
print("Length of item name:", length_of_item)
print("First character of each word:", first_char, second_char, third_char)
print("Last character of each word:", last_char1, last_char2, last_char3)