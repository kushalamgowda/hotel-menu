menu = {
    'Pizza': 40,
    'Pasta': 50,
    'Burger': 60,
    'Salad': 70,
    'Coffee': 80,
}

print("Welcome to Python Restaurant!")
print("Menu:")
for item, price in menu.items():
    print(f"{item}: RS{price}")

order_total = 0

# First item order
item_1 = input("Enter the name of the item you want to order: ").title()
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item '{item_1}' has been added to your order.")
else:
    print(f"Ordered item '{item_1}' is not available yet!")

# Asking for another order
another_order = input("Do you want to add another item? (yes/no): ").lower()
if another_order == "yes":
    item_2 = input("Enter the name of the second item: ").title()
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item '{item_2}' has been added to your order.")
    else:
        print(f"Ordered item '{item_2}' is not available!")

# Print total only if something was ordered
if order_total > 0:
    print(f"The total amount to pay is RS{order_total}.")
else:
    print("No items were ordered.")

