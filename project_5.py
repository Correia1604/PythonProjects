import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll

while True:
    players = input("How many players? (2 - 4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 and 4 players")
    else:
        print("Error. Try again.")

max_score = 20
player_scores = [0 for _ in range(players)]

while max(player_scores) < max_score:

    for player_idx in range(players):
        print("\nPlayer number ", player_idx + 1, " it's your turn.\n")
        print("Your total score is:", player_scores[player_idx], "\n")
        current_score = 0

        while True:
            should_roll = input("Would you like to roll? (y/n): ")
            if should_roll.lower() != "y":
                break

            value=roll()
            if value == 1:
                print("you rolled a 1! Turn done.")
                current_score = 0
                break
            else:
                current_score += value
                print(f"you rolled a:", value)

            print("Your current score is:", current_score)

        player_scores[player_idx] += current_score
        print("Your total score is:", player_scores[player_idx])

max_score = max(player_scores)
player_winning_idx = player_scores.index(max_score)
print("Player number ", player_winning_idx + 1, " wins with a score of ", max_score, "!")