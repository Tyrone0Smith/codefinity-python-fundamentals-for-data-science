vegetables = ["tomatoes", "potatoes", "onions"]
vegetables.remove("onions")

print(f"Updated Vegetable Inventory: {vegetables}")

vegetables.append("carrots")
if "carrots" in vegetables:
    print("Carrots are already on the list.")

vegetables.append("cucumbers")
if "cucumbers" in vegetables:
    print("Cucumbers are already on the list.")

vegetables.sort()
    