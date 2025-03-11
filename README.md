# hotel-menu

A dictionary menu stores food items as keys and their prices as values.
The program prints a welcome message and the available menu items with prices.
The user is asked to enter an item name.
The input is converted to title case using .title() to ensure correct matching.
If the item exists in menu, it is added to order_total, and a confirmation message is printed.
If the item is not found, an error message is displayed.
The user is asked if they want to add another item.
The response is converted to lowercase (.lower()) for better handling.
If the user enters "yes", they can order a second item.
The second item is also checked in the menu, and the price is added to the total.
If at least one item was ordered, the program prints the total amount.
If no valid items were ordered, it prints "No items were ordered."
