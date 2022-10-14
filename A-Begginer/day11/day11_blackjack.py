import random

card = '''
┌─────────┐
│{}       │
│         │
│         │
│    {}    │
│         │
│         │
│       {}│
└─────────┘
'''

flipped_card = '''
┌─────────┐
│░░░░░░░░░│
│░░░░░░░░░│
│░░░░░░░░░│
│░░░░░░░░░│
│░░░░░░░░░│
│░░░░░░░░░│
│░░░░░░░░░│
└─────────┘
'''

suits = {
    'Spades': '♠',
    'Diamonds': '♦',
    'Hearts': '♥',
    'Clubs': '♣',
}

card_values = {
    "Ace": {
        "symbol": 'A',
        "value": 11, # value of the ace is high until it needs to be low
    },
    "Two": {
        "symbol": '2',
        "value": 2,
    },
    "Three": {
        "symbol": '3',
        "value": 3,
    },
    "Four": {
        "symbol": '4',
        "value": 4,
    },
    "Five": {
        "symbol": '5',
        "value": 5,
    },
    "Six": {
        "symbol": '6',
        "value": 6,
    },
    "Seven": {
        "symbol": '7',
        "value": 7,
    },
    "Eight": {
        "symbol": '8',
        "value": 8,
    },
    "Nine": {
        "symbol": '9',
        "value": 9,
    },
    "Ten": {
        "symbol": '10',
        "value": 10,
    },
    "Jack": {
        "symbol": 'J',
        "value": 10,
    },
    "Queen": {
        "symbol": 'Q',
        "value": 10,
    },
    "King": {
        "symbol": 'K',
        "value": 10,
    },
}

def render_card(value, suit):
    if value < 10:
        left_value = f"{value} "
        right_value = f" {value}"
    else:
        left_value = value
        right_value = value
    rendered_card = card.format( left_value, suit, right_value)
    return rendered_card

def deal_card():
    random_card = random.choice(list(card_values.keys()))
    random_card_value = card_values[random_card]["value"]
    random_card_symbol = card_values[random_card]["symbol"]
    card_display = render_card(random_card_value, random_card_symbol)
    return {"value": random_card_value, "display": card_display}

# x = random.choice(list(card_values.keys()))
# print(x)
# card_1 = render_card(card_values[x]["value"], card_values[x]["symbol"])
# print(card_1)

player_data = {"cards": []}
dealer_data = {"cards": []}

for _ in range(2):
    player_data["cards"].append(deal_card())
    dealer_data["cards"].append(deal_card())

for player_card in player_data["cards"]:
    print(player_card["display"], end="")

# card_1 = deal_card()

# print(card_1["value"])
# print(card_1["display"])