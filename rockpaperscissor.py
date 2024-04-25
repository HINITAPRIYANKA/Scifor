import random

class RPSGame:
    def __init__(self):
        self.choices = ["rock", "paper", "scissors"]
        self.player1_choice = None
        self.player2_choice = None

    def get_player_choice(self):
        choice = input("Enter your choice (rock/paper/scissors): ").lower()
        if choice in self.choices:
            return choice
        else:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            return self.get_player_choice()

    def get_computer_choice(self):
        return random.choice(self.choices)

    def determine_winner(self, player1, player2):
        if player1 == player2:
            return "It's a tie!"
        elif (player1 == "rock" and player2 == "scissors") or \
             (player1 == "paper" and player2 == "rock") or \
             (player1 == "scissors" and player2 == "paper"):
            return "Player 1 wins!"
        else:
            return "Player 2 wins!"

    def play_game(self):
        self.player1_choice = self.get_player_choice()
        self.player2_choice = self.get_computer_choice()

        print(f"Player 1 chose {self.player1_choice}")
        print(f"Player 2 chose {self.player2_choice}")

        result = self.determine_winner(self.player1_choice, self.player2_choice)
        print(result)

if __name__ == "__main__":
    game = RPSGame()
    game.play_game()



