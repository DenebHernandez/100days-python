'''Functions module for the coffee machine replica'''

from data import INITIAL_RESOURCES, COINS, MENU

def insert_coins():
    '''Prompts the user for an amount of coins to pay for the order,

    Returns: Total sum of inserted coins in dollars
    '''
    #Prompt
    print("Please insert coins.")

    #Ask for an amount of every of the 4 coin options
    payment = {}
    for coin in COINS.items():
        coin_amount = user_input(prompt="coins", coin=coin[0])
        # Sums the total amount of dollars inserted as coins
        payment[coin[0]] = coin_amount
        total = 0
    for payment_coins in payment.items():

        # Converts every set of coins inserted into its dollar
        # equivalent by multiplying it with the coin value stored
        # in the data dictionary
        conversion = payment_coins[1] * COINS[payment_coins[0]]
        total += conversion

    return total


def user_input(prompt, coin=None, available_resources=None):
    '''Asks user for an input and checks if its valid,
    else it asks to try again
    '''

    # For every coin type asks for amount of coins,
    # checks if user inputs a digit to convert into an int
    if prompt == "coins":
        while True:
            inserted_coins = input(f"How many {coin}?: ")
            if inserted_coins.isdigit():
                inserted_coins = int(inserted_coins)
                break
            print("\nInvalid input, type a number\n")
        return inserted_coins

    # Checks if user order is inside the menu
    if prompt == "order":
        while True:
            order = input("What would you like? (espresso/latte/cappuccino): ")
            order = order.lower()

            #Returns a urn off message if user enters "off"
            if order == "off" or order in MENU:
                break

            # Print report of current resources if user enters "report"
            if order == "report":
                report(available_resources)

            else:
                print(f"{order} is not part of the menu")
        return order


def report(available_resources:dict):
    '''Returns a report of available resources'''

    for resource in available_resources.items():
        if resource[0] == "coffee":
            print(f"{resource[0]}: {resource[1]}g")
        elif resource[0] == "money":
            print(f"{resource[0]}: ${resource[1]}")
        else:
            print(f"{resource[0]}: {resource[1]}ml")


def prepare_order(user_order, available_resources, payment):
    '''Checks if all inputs required to prepare an order
    are correct

    Returns: Error if one or more resources are missing,
    or completed order if all inputs pass the test
    '''

    # Chacks if available resources are enough to complete
    # the order, returns a dictionary with updated resources
    needed_resources = MENU[user_order]["ingredients"]
    new_resources = available_resources
    for ingredient in needed_resources:
        available = available_resources[ingredient]
        required = needed_resources[ingredient]
        print(f"{ingredient} a:{available} r:{required}")
        if available < required:
            print(
                f'''There's not enough {ingredient} to complete your order'''
            )
            return False
        new_resources[ingredient] = available - required

    # Checks the cost of user order in the menu and
    # validates if payment is enough
    order_cost = MENU[user_order]["cost"]
    if payment < order_cost:
        print(
            '''You didn't insert enough money to pay for the order'''
        )
        return False
    change = payment - order_cost

    result = {
            "resources": new_resources,
            "money": order_cost,
            "change": change,
        }
    return result

def run_machine():
    '''Starts the coffee machine and runs it untill
    user turns it off
    '''

    # Assings initial resources and collected money
    # to the machine as a variable
    order = ""
    money_stored = 0
    resources_left = INITIAL_RESOURCES
    while order != "off":

        order = user_input("order")
        if order == "off":
            continue
        order_payment = insert_coins()

        order_result = prepare_order(
            user_order=order,
            available_resources=resources_left,
            payment=order_payment
        )

        if order_result:
            resources_left = order_result["resources"]
            money_stored += order_result["money"]
    print(f"Bye bye. There's ${money_stored} in the bank")
