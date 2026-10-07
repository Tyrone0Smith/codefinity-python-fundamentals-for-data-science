# Initial items on shelf #1 (provided as a tuple)
shelf1 = ("celery", "spinach", "cucumbers")

# Items being added to the shelf #1 (provided as a list)
shelf1_update = ["tomatoes", "celery", "cilantro"]

# Convert the list shelf1_update into a tuple
shelf1_update_tuple = tuple(shelf1_update)

# Concatenate shelf1_update_tuple with existing tuple shelf1
shelf1_concat = shelf1 + shelf1_update_tuple

# Count how many times the string "celery" appears
celery_count = shelf1_concat.count("celery")

# Find the index of the first occurence of "celery"
celery_index = shelf1_concat.index("celery")
print(f"Updated Shelf #1: {shelf1_concat}")
print(f"Number of Celery: {celery_count}")
print(f"Celery Index: {celery_index}")
