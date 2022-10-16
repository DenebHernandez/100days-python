import os
import random

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

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

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
    # random_card_symbol = card_values[random_card]["symbol"]
    # card_display = render_card(random_card_value, random_card_symbol)
    # return {"value": random_card_value, "display": card_display}
    return random_card_value

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    
    return sum(cards)

def compare(player_score, dealer_score):
    if player_score == dealer_score:
        return "Draw"
    elif dealer_score == 0:
        return "You lost, dealer has a blackjack"
    elif player_score == 0:
        return "You have won, you got a blackjack"
    elif player_score > 21:
        return "You have lost, your score is over 21"
    elif dealer_score > 21:
        return "You have won, dealer score is over 21"
    elif player_score > dealer_score:
        return "You have won"
    else:
        return "You lose"

def blackjack():
    end_of_game = False
    player_data = {"cards": []}
    dealer_data = {"cards": []}
    for _ in range(2):
        player_data["cards"].append(deal_card())
        dealer_data["cards"].append(deal_card())

    while not end_of_game:
        cls()
        player_score = calculate_score(player_data["cards"])
        dealer_score = calculate_score(dealer_data["cards"])

        print(f'Your cards: {player_data["cards"]}, current score: {player_score}')
        print(f'The dealer\'s first card: {dealer_data["cards"][0]}')

        if player_score == 0 or player_score > 21:
            end_of_game = True
        else:
            deal_new_card = input("Type 'h' to hit, or 's' to stand: ")
            if deal_new_card == "h":
                player_data["cards"].append(deal_card())
            else:
                end_of_game = True

    while dealer_score != 0 and dealer_score < 17:
        dealer_data["cards"].append(deal_card())
        dealer_score = calculate_score(dealer_data["cards"])

    cls()
    print(f'Your cards: {player_data["cards"]}, Your score: {player_score}')
    print(f'The dealer\'s cards: {dealer_data["cards"]}, Dealer score: {dealer_score}')

    print(f"{compare(player_score, dealer_score)} \n")