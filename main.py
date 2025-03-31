"""projekt_1.py: první projekt do Engeto Online Python Akademie

author: Tomáš Ječmínek
email: jecminek.tomas@gmail.com"""

TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

registered_users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

print("Username:", end=" ")
username = input().strip()
print("Password:", end=" ")
password = input().strip()

if username not in registered_users or registered_users[username] != password:
    print("Unregistered user, terminating the program..")
    exit()

print("-" * 40)
print(f"Welcome to the app, {username}")
print("We have 3 texts to be analyzed.")
print("-" * 40)

try:
    text_choice = int(input("Enter a number btw. 1 and 3 to select: "))
    if text_choice < 1 or text_choice > 3:
        raise ValueError
except ValueError:
    print("Invalid selection, terminating the program...")
    exit()

selected_text = TEXTS[text_choice - 1]
words = selected_text.split()

word_count = len(words)
titlecase_count = sum(1 for word in words if word.istitle())
uppercase_count = sum(1 for word in words if word.isupper() and word.isalpha())
lowercase_count = sum(1 for word in words if word.islower())
numeric_count = sum(1 for word in words if word.isdigit())
sum_of_numbers = sum(int(word) for word in words if word.isdigit())

print("-" * 40)
print(f"There are {word_count} words in the selected text.")
print(f"There are {titlecase_count} titlecase words.")
print(f"There are {uppercase_count} uppercase words.")
print(f"There are {lowercase_count} lowercase words.")
print(f"There are {numeric_count} numeric strings.")
print(f"The sum of all the numbers {sum_of_numbers}")
print("-" * 40)

word_lengths = {}
for word in words:
    length = len(word.strip(".,!?"))
    word_lengths[length] = word_lengths.get(length, 0) + 1

print("LEN|  OCCURRENCES  |NR.")
print("-" * 40)
for length, count in sorted(word_lengths.items()):
    print(f"{length:2}| {'*' * count:<15} |{count}")
