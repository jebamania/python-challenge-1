# Menu dictionary
menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.9,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

# 1. Set up order list. Order list will store a list of dictionaries for
# menu item name, item price, and quantity ordered
customer_order = []

# Launch the store and present a greeting to the customer
print("Welcome to the variety food truck.")

# Customers may want to order multiple items, so let's create a continuous
# loop
place_order = True
while place_order:
    # Ask the customer from which menu category they want to order
    print("From which menu would you like to order? ")

    # Create a variable for the menu item number
    i = 1
    # Create a dictionary to store the menu for later retrieval
    menu_items = {}

    # Print the options to choose from menu headings (all the first level
    # dictionary items in menu).
    for key in menu.keys():
        print(f"{i}: {key}")
        # Store the menu category associated with its menu item number
        menu_items[i] = key
        # Add 1 to the menu item number
        i += 1

    # Get the customer's input
    menu_category = input("Type menu number: ")

    # Check if the customer's input is a number
    if menu_category.isdigit():
        # Check if the customer's input is a valid option
        if int(menu_category) in menu_items.keys():
            # Save the menu category name to a variable
            menu_category_name = menu_items[int(menu_category)]
            # Print out the menu category name they selected
            print(f"You selected {menu_category_name}")

            # Print out the menu options from the menu_category_name
            print(f"What {menu_category_name} item would you like to order?")

            i = 1
            menu_items = {}
            print("Item # | Item name                | Price")
            print("-------|--------------------------|-------")
            for key, value in menu[menu_category_name].items():
                # Check if the menu item is a dictionary to handle differently
                if type(value) is dict:
                    for key2, value2 in value.items():
                        num_item_spaces = 24 - len(key + key2) - 3
                        item_spaces = " " * num_item_spaces
                        print(f"{i}      | {key} - {key2}{item_spaces} | ${value2:.2f}")
                        menu_items[i] = {
                            "Item key": i,
                            "Item name": f'{key} - {key2}',
                            "Item category": key,
                            "Price": value2
                        }
                        i = i + 1
                else:
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{i}      | {key}{item_spaces} | ${value:.2f}")
                    menu_items[i] = {
                        "Item key": i,
                        "Item name": key,
                        "Item category": menu_category_name,
                        "Price": value
                    }
                    i += 1
            # 2. Ask customer to input menu item number
            menu_selection = input('Please enter the item number from the menu. ')

            # 3. Check if the customer typed a number
            if (type(menu_selection) is str and menu_selection.isdigit()) or menu_selection is int:
                # Convert the menu selection to an integer
                menu_selection = int(menu_selection)

                # 4. Check if the menu selection is in the menu items
                if menu_selection in menu_items.keys():

                    # Store the item name as a variable
                    menu_item = menu_items.get(menu_selection)

                    # Ask the customer for the quantity of the menu item
                    quantity = input(f'For your selection, {menu_item["Item name"]}, how many do you want?\n\nNote: If your quantity is invalid, it will default to 1. ')

                    # Check if the quantity is a number, default to 1 if not
                    if (type(quantity) is str and quantity.isdigit()) or quantity is int:
                        quantity = int(quantity)
                    else: quantity = 1

                    # Add the item name, price, and quantity to the order list
                    customer_order.append({
                        "Item key": menu_selection,
                        "Item name": menu_item["Item name"],
                        "Price": menu_item["Price"],
                        "Quantity": quantity
                    })

                # Tell the customer that their input isn't valid

                else: print(f'"{menu_selection}" is not a valid menu option as it can\'t be found in the menu.')

            # Tell the customer they didn't select a menu option
            else: print(f"Your menu selection, {menu_selection} is not a valid item number on our menu.")

        else:
            # Tell the customer they didn't select a menu option
            print(f"{menu_category} was not a menu option.")
    else:
        # Tell the customer they didn't select a number
        print("You didn't select a number.")

    while True:
        # Ask the customer if they would like to order anything else
        keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ")

        # 5. Check the customer's input
        match keep_ordering.lower():
            case "y" | "yes":
                # Keep ordering
                place_order = True
                # Exit the keep ordering question loop
                break

            case "n" | "no":
                # Complete the order
                # Since the customer decided to stop ordering, thank them for
                # their order
                place_order = False
                print('Thank you for ordering through our CLI! We appreciate your patience while we update our UI systems!')
                # Exit the keep ordering question loop
                break

            case _:
                # Tell the customer to try again
                print(f'Good try, but please try again. Input "{keep_ordering}" does not compute. ')


# Print out the customer's order
print("This is what we are preparing for you.\n")

# Uncomment the following line to check the structure of the order
#print(customer_order)

print("Item name                 | Price  | Quantity | Total")
print("--------------------------|--------|----------|------")
item_name_dashes = '--------------------------'
price_dashes = '--------'
quantity_dashes = '----------'

cost_per_item = [item['Price'] * item['Quantity'] for item in customer_order]

# 6. Loop through the items in the customer's order
order_index = 0
for order_item in customer_order:
    # 7. Store the dictionary items as variables
    # 8. Calculate the number of spaces for formatted printing
    # 9. Create space strings

    item_name_full = order_item['Item name']
    item_name = ''

    if len(item_name_full) > len(str(item_name_dashes)):
        item_name = f"{ item_name_full[0:len(str(item_name_dashes))] }"
    else:
        item_name = item_name_full

    item_price = '{:,.2f}'.format(order_item['Price'])

    item_by_quantity_print = '{:,.2f}'.format(cost_per_item[order_index])
    
    if len(str(order_item['Price'])) > len(str(price_dashes)):
        order_item['Price'] = f"{ order_item['Price'][0:len(str(price_dashes))] }"

    if len(str(order_item['Quantity'])) > len(str(quantity_dashes)):
        order_item['Quantity'] = f"{ order_item['Quantity'][0:len(str(quantity_dashes))] }"

    item_name_print = f"{item_name + ('-'* (len(str(item_name_dashes))-len(item_name)) )}"
    #subtracting the 1 extra here for the $
    item_price_print = f"${item_price + ('-'* (len(str(price_dashes))-len(item_price) -1) )}"
    item_quantity_print = f"{str(order_item['Quantity']) + ('-'* (len(str(quantity_dashes))-len(str(order_item['Quantity']))) )}"

    # 10. Print the item name, price, and quantity
    print( item_name_print + '|' + item_price_print + '|' + item_quantity_print + '|$' + item_by_quantity_print )
    order_index = order_index + 1


# 11. Calculate the cost of the order using list comprehension
# Multiply the price by quantity for each item in the order list, then sum()
# and print the prices.
total_cost = 0
[total_cost := total_cost + (item['Price'] * item['Quantity']) for item in customer_order]
total_cost = '{:,.2f}'.format(total_cost)

print( item_name_dashes + price_dashes + quantity_dashes + ('-'*10) )
print(f'Total: ${total_cost}')