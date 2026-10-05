# The item's discount and stock status have been defined
discounted = False
lowStock = True

# Define a bool var
movingProduct = discounted or lowStock

# Create a bool var
promotion = not discounted and not lowStock

print(f"Is the item eligible for promotion? {promotion}")