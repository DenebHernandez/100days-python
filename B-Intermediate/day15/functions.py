'''Functions module for the coffee machine replica'''

from data import COINS, MENU, resources


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


def user_input(prompt, coin=None):
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
            if order == "off" or order in MENU:
                break
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


report(resources)
