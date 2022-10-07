from day8_art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphabet_lenght = len(alphabet)

print(logo)

def caesar(message, shift_amount, shift_direction):
    return_text = ""
    if shift_amount >= alphabet_lenght:
        shift_amount = shift_amount % alphabet_lenght 
    if shift_direction == "encode":
        for character in message:
            if character in alphabet:
                original_index = alphabet.index(character)
                shifted_index = original_index + shift_amount
                if shifted_index > alphabet_lenght - 1:
                    shifted_index = shifted_index - alphabet_lenght
                shifted_character = alphabet[shifted_index]
                return_text += shifted_character
            else:
                return_text += character
        print(f"You encrypted message is {return_text}")
    elif shift_direction == "decode":
        for character in message:
            if character in alphabet:
                original_index = alphabet.index(character)
                shifted_index = original_index - shift_amount
                shifted_character = alphabet[shifted_index]
                return_text += shifted_character
            else:
                return_text += character
        print(f"You decrypted message is {return_text}")
    else:
        print("Invalid shift direction")

continue_game = True
while continue_game:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(message=text, shift_amount=shift, shift_direction=direction)
    run_again = input("Type 'yes' if you want to go again. Otherwise type 'no':\n")
    if run_again == "no":
        continue_game = False
        print("Goodbye")