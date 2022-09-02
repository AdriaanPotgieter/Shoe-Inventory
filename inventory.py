class Shoes():
    '''
    Create a class called Shoes. Use constructor to declare attributes. Use methods to return the cost, quantity
    and to change the attributes from objects to strings. Create method to add to stock.
    ''' 
    def __init__(self,country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity


    def get_cost(self):
        return self.cost


    def get_quanty(self):
        return int(self.quantity)
        

    def set_quanty(self, new_quanitty):
        self.quantity = str(new_quanitty + int(self.quantity))


    def __str__(self):
        return f"Country: {self.country}\n"\
            f"Code: {self.code}\n"\
            f"Product: {self.product}\n"\
            f"Cost: {self.cost}\n"\
            f"Quantity: {self.quantity}\n\n"


# Declare an empty list
shoe_list = []


def read_shoes_data():
    '''
    Defining a function. Use try and except to handle possible errors. This function will store all the
    inventory from the text file in the empty list.
    '''
    try:
        with open("inventory.txt", "r") as inventory:
            check_inventory = inventory.readlines()[1:]
            for invent in check_inventory:
                inv = invent.strip("\n").split(",")
                shoes_inventory = Shoes(inv[0], inv[1], inv[2], inv[3], inv[4])
                shoe_list.append(shoes_inventory)
    except FileNotFoundError:
        print("Sorry the file does not exist. Please try again.")


# Recalling function.
read_shoes_data()


def capture_shoes():
    '''
    Defining a function. Ask user to input data to use in the function. Storing the data in a new object
    by giving the parameters values in the Shoe class and then adding the info into the list.
    '''
    country_choice = input("From which country is the shoe?\n").capitalize()
    code_choice = input("Enter the code of the shoe here:\n").upper()
    product_choice = input("What is the make of the Nike shoe?\n").capitalize()
    cost_choice = int(input("How much does the shoe cost?\n"))
    quantity_choice = input("How many shoes do you want?\n")

    shoe_choices = Shoes(country_choice, code_choice, product_choice, cost_choice, quantity_choice)
    shoe_list.append(shoe_choices)


def view_all():
    '''
    Defining a function to view all the info of all the shoes. Use for loop to access all the shoes and their
    info in the list and print out the result.
    '''
    for shoe_details in shoe_list:
        print(shoe_details)


def re_stock():
    '''
    Defining a function. Declare an empty list, use for loop to access all the shoes in the list. Get the quantity
    by calling the quanty() method and then add to the empty list. Checking the least ammount then ask user how much they want to add
    add everything up and print the result. Firstly print the old stock before adding the new stock.
    '''
    lowest_shoe = shoe_list[0]

    for shoe in shoe_list:
        if shoe.get_quanty() <= lowest_shoe.get_quanty():
            lowest_shoe = shoe

    print(lowest_shoe)
    new_quantity = int(input("Quantity of new Stock: "))
    lowest_shoe.set_quanty(new_quantity)
    print(lowest_shoe)


def seach_shoe(code):
    '''
    defining a function with the attribute code. Use for loop to access all the shoes in the list. Check if 
    the codes are matching and then print the results.
    '''
    for shoe in shoe_list:
        if shoe.code == code:
            print(shoe)
            break


def value_per_item():
    '''
    defining a function. Create an empty list, use for loop to access all the shoes in the list. Get the cost
    of each and every shoe by using the .cost attribute and get the quantitiy by using the .quantity attribute
    calculate the value and add the results in the empty list. Use for loop to get all the values and print
    the results.
    '''
    values_items = []
    for value in shoe_list:
        cost_of_item = value.cost
        item_quantity = value.quantity
        val = int(cost_of_item) * int(item_quantity)
        values_items.append(f"The value of {value.product} is R {val}")

    for valu in values_items:
        print(valu)


def highest_qty():
    '''
    Defining a function. Declare an empty dictionary, use for loop to access all the shoes info. Get the shoe
    make and the quantity of it by using the attributes .product and .quantity. Switch the position of the
    quantity with the product to access it better in the dictionary. Use the max() function to get the higest
    quantity and print out the result.
    '''
    most_shoes ={}
    for most in shoe_list:
        shoe_make = most.product
        qty_shoes = most.quantity
        most_shoes[int(qty_shoes)] = shoe_make
        most_valued = max(most_shoes.keys())
    print(f"The shoes that is on sale is: {most_shoes[most_valued]}")


# Use while loop to print the menu continuously and ask user to input info.
while True:
    shoe_menu = input('''Welcome to our shoe store! Please select one of the following options:
    Capture Shoes - cs
    View Shoes - vs
    Restock - r
    Search Shoe - ss
    Item Values - iv
    Sale - s
    Exit - e
    :\n''').lower()

    # Use if statements to help with the decision making of the user. Each menu option will call different functions.
    # To exit the program the user must enter e.
    if shoe_menu == "cs":
        capture_shoes()
    elif shoe_menu == "vs":
        view_all()
    elif shoe_menu =="r":
        re_stock()
    elif shoe_menu == "ss":
        # Ask user to enter the code and print the result.
        shoe_code = input("Enter the code of the shoe that you are looking for here:\n")
        seach_shoe(shoe_code)
    elif shoe_menu == "iv":
        value_per_item()
    elif shoe_menu == "s":
        highest_qty()
    elif shoe_menu == "e":
        print("Thank you for visiting our shoe store! Enjoy your day.")
        exit()