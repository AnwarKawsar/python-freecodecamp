import random

def get_choices():
  player_choose = input("Enter a choice('rock','paper','scissors'): \n")
  options = ["rock", "paper", "scissors"]
  computer_choose = random.choice(options)
  choices = {"player": player_choose, "computer": computer_choose}

  return choices


def check_wins(player, computer):
  print(f"You choose {player} computer choose {computer}")
  if player == computer:
    return "It's a tie!!!!"
  elif player == "rock":
    if computer == "paper":
      return "Paper raps rock,you loss."
    else:
      return "Rock breaks scissors,you win!!!"
  elif player == "paper":
    if computer == "rock":
      return "Paper raps rock,you win!!!"
    else:
      return "✂ cuts 📄,you loss."
  elif player == "scissors":
    if computer == "paper":
      return "✂ cuts 📄,you win."
    else:
      return "Rock breaks scissors,you loss."


choices = get_choices()
result = check_wins(choices["player"], choices["computer"])
print(result)