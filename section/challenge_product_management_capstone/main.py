# Input variables
days_until_expiration = 5  # Example value
stock_level = 60           # Example value
product_type = "Perishable"  # Can be "Perishable" or "Non-Perishable"

if product_type == "Perishable":
    # 30% if 3 days or less and stock > 50
    if days_until_expiration <= 3 and stock_level > 50:
        print("30% discount applied")
    # 20% if 4–6 days and stock > 50
    elif 4 <= days_until_expiration <= 6 and stock_level > 50:
        print("20% discount applied")
    # 10% if >6 days or stock ≤ 50
    elif days_until_expiration > 6 or stock_level <= 50:
        print("10% discount applied")
else:
    print("no discount available for non-perishable items.")