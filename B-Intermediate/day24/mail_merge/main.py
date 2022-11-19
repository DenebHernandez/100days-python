import os

cwd = os.getcwd()
names = []
with open(f"{cwd}\B-Intermediate\day24\mail_merge\\names.txt") as file:
    # all_names = file.read()
    # names = all_names.split()
    names = file.readlines()
    print(names)
    # print(names)

with open(f"{cwd}\B-Intermediate\day24\mail_merge\starting_letter.txt") as file:
    letter = file.read()

for name in names:
    name = name.strip()
    print(name)
    with open(f"{cwd}\B-Intermediate\day24\mail_merge\\ready_to_send\letter_for_{name}.txt", mode="w") as file:
        current_letter = letter.replace("[name]", name)
        file.write(current_letter)
