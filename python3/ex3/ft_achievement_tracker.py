import random

ACHIEVEMENTS = [
    "First Steps", "Boss Slayer", "Master Explorer", "Speed Runner",
    "Collector Supreme", "Untouchable", "World Savior", "Crafting Genius",
    "Treasure Hunter", "Survivor", "Unstoppable", "Sharp Mind",
    "Strategist", "Hidden Path Finder", "Sharp Mind"
]


def gen_player_achievements() -> set:
    count = random.randint(1, len(ACHIEVEMENTS))
    return set(random.sample(ACHIEVEMENTS, count))


print("=== Achievement Tracker System ===")

alice = gen_player_achievements()
bob = gen_player_achievements()
charlie = gen_player_achievements()
dylan = gen_player_achievements()

print("Player Alice:", alice)
print("Player Bob:", bob)
print("Player Charlie:", charlie)
print("Player Dylan:", dylan)

all_achievements_commun = set.union(alice, bob, charlie, dylan)
print("All distinct achievements:", all_achievements_commun)

common = set.intersection(alice, bob, charlie, dylan)
print("Common achievements:", common)

except_alice = set.union(bob, charlie, dylan)
except_bob = set.union(alice, charlie, dylan)
except_charlie = set.union(alice, bob, dylan)
except_dylan = set.union(alice, bob, charlie)

print("Only Alice has:", set.difference(alice, except_alice))
print("Only Bob has:", set.difference(bob, except_bob))
print("Only Charlie has:", set.difference(charlie, except_charlie))
print("Only Dylan has:", set.difference(dylan, except_dylan))

print("Alice is missing:", set.difference(all_achievements_commun, alice))
print("Bob is missing:", set.difference(all_achievements_commun, bob))
print("Charlie is missing:", set.difference(all_achievements_commun, charlie))
print("Dylan is missing:", set.difference(all_achievements_commun, dylan))
