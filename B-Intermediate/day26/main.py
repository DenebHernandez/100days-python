import os
import pandas as pd

main_folder = os.getcwd()
cwd = f"{main_folder}\B-Intermediate\day26"

df = pd.read_csv(f"{cwd}\\nato_phonetic_alphabet.csv")

# Create a dictionary from the dataframe
nato_dict = {row.letter:row.code for (index, row) in df.iterrows()}
# print(nato_dict)

word = input("Enter a word").upper()

#Create a list of the phonetic code words from a word that the user inputs.
result = [nato_dict[letter] for letter in word]
print(result)
