
"""
main.py
Main script for the Higher or Lower Game.
"""

import random
from data import data
from art import logo

def get_random_entry(exclude=None):
    """Return a random (name, value) tuple from data, excluding a specific name if provided."""
    choices = list(data.items())
    if exclude:
        choices = [item for item in choices if item[0] != exclude]
    return random.choice(choices)

def format_entry(name, value):
    """Format the entry for display."""
    return f"{name} (searched {value} times)"

def play_game():
    """Main game loop for Higher or Lower."""
    print(logo)
    score = 0
    game_should_continue = True
    entry_a_name, entry_a_value = get_random_entry()
    while game_should_continue:
        entry_b_name, entry_b_value = get_random_entry(exclude=entry_a_name)
        print(f"\nCompare A: {entry_a_name}")
        print("vs")
        print(f"Compare B: {entry_b_name}")
        guess = input(
            "Who has been searched more? Type 'A' or 'B': "
        ).strip().lower()
        if (
            (entry_a_value > entry_b_value and guess == 'a') or
            (entry_b_value > entry_a_value and guess == 'b')
        ):
            score += 1
            print(f"\nCorrect! Current score: {score}.")
            if guess == 'a':
                # Keep A, get new B
                pass
            else:
                # B becomes new A
                entry_a_name, entry_a_value = entry_b_name, entry_b_value
        else:
            print(f"\nSorry, that's wrong. Final score: {score}.")
            game_should_continue = False

if __name__ == "__main__":
    play_game()
