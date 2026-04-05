import random

print("=== Game Data Alchemist ===")

PLAYERS = [
    "alice",
    "bob",
    "charlie",
    "dylan",
    "emma",
    "gregory",
    "john",
    "kevin",
    "liam"
]
print("Initial list of players:", PLAYERS)

all_capitalized = [name.capitalize() for name in PLAYERS]
print("New list with all names capitalized:", all_capitalized)

only_capitalized = [name for name in PLAYERS if name[0].isupper()]
print("New list of capitalized names only:", only_capitalized)

score_dict = {name: random.randint(1, 1000) for name in all_capitalized}
print("Score dict:", score_dict)

average = round(sum(score_dict.values()) / len(score_dict), 2)
print("Score average is", average)

high_scores = {name: score for name, score in score_dict.items() if score > average}
print("High scores:", high_scores)