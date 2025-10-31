import random
from datetime import datetime


class RockPaperScissors:
    def __init__(self, playername):
        # Initialize player name and core data
        self.playername = playername
        # Winning combinations: (winner, loser)
        self.winnerchoices = [(1, 3), (2, 1), (3, 2)]
        # Mapping numeric choices to words
        self.dic = {1: "paper", 2: "scissors", 3: "rock"}
        self.reset_scores()

    def reset_scores(self):
        """Reset all scores and game settings before starting a new match."""
        self.computerscore = 0
        self.player1score = 0
        self.player2score = 0
        self.modeinput = None
        self.rounds = None
        self.stop_game = False

    def rock_paper_scissors(self):
        """Main loop: Handles game restart and overall control flow."""
        while True:
            self.reset_scores()
            self.modeinput = self.mode()
            self.rounds = self.round_input()

            # --- Single Player Mode ---
            if self.modeinput == 1:
                self.player1name = input("Please type your name here: ")

                for r in range(1, self.rounds + 1):
                    if self.stop_game:
                        print("Exiting the game. Goodbye!")
                        break

                    # Player’s move
                    player_choice = self.player_input(self.player1name)
                    if player_choice is None: 
                        self.stop_game = True
                        print("Game stopped by user.")
                        break

                    # Computer’s move
                    com_choice = self.com_input()

                    # Determine round result
                    if player_choice == com_choice:
                        print("It's a tie!")
                    elif (com_choice, player_choice) in self.winnerchoices:
                        print("Computer wins this round!")
                        self.computerscore += 10
                    else:
                        print("You win this round!")
                        self.player1score += 10

                self.final_winner()

            # --- Two Player Mode ---
            elif self.modeinput == 2:
                self.player1name = input("Please type first player's name here: ")
                self.player2name = input("Please type second player's name here: ")

                for r in range(1, self.rounds + 1):
                    if self.stop_game:
                        print("Exiting the game. Goodbye!")
                        break

                    # Player 1’s move
                    player1choice = self.player_input(self.player1name)
                    if player1choice is None: 
                        self.stop_game = True
                        print("Game stopped by user.")
                        break

                    # Player 2’s move
                    player2choice = self.player_input(self.player2name)
                    if player2choice is None: 
                        self.stop_game = True
                        print("Game stopped by user.")
                        break

                    # Determine round result
                    if player1choice == player2choice:
                        print("It's a tie!")
                    elif (player2choice, player1choice) in self.winnerchoices:
                        print(f"{self.player2name} wins this round!")
                        self.player2score += 10
                    else:
                        print(f"{self.player1name} wins this round!")
                        self.player1score += 10

                self.final_winner()

            # Ask if the user wants to play another game
            if not self.play_again():
                print("Thanks for playing! Goodbye!")
                break

    def mode(self):
        """Ask the user which game mode they want to play."""
        while True:
            try:
                modeinput = int(input(
                    "Welcome to Rock, Paper, Scissors Game :)\n"
                    "Please select the mode:\n"
                    "1: Play with computer\n"
                    "2: Play with another player\n"
                    "Your choice: "
                ))
                if modeinput in (1, 2):
                    return modeinput
                else:
                    print("❌ Please enter only 1 or 2.")
            except ValueError:
                print("❌ Invalid input. Please enter a number (1 or 2).")

    def round_input(self):
        """Ask for the number of rounds to play."""
        while True:
            try:
                rounds = int(input("🔢 How many rounds do you want to play? "))
                if rounds > 0:
                    return rounds
                else:
                    print("❌ Please enter a positive number.\n")
            except ValueError:
                print("⚠️ Invalid input. Please enter a number.\n")

    def player_input(self, player_name):
        """Get the player's move; returns None if they choose to quit."""
        while True:
            try:
                playerinput = int(input(
                    f"\n{player_name}, make your move:\n"
                    "1️⃣ Paper\n2️⃣ Scissors\n3️⃣ Rock\n4️⃣ Quit\n👉 Your choice: "
                ))
                if playerinput in (1, 2, 3):
                    print(f"{player_name} chose {self.dic[playerinput]}")
                    return playerinput
                elif playerinput == 4:
                    print(f"{player_name} chose to quit.")
                    return None
                else:
                    print("❌ Invalid choice. Please enter 1, 2, 3 or 4.")
            except ValueError:
                print("⚠️ Invalid input. Please type a number.")

    def com_input(self):
        """Generate and display a random computer move."""
        cominput = random.randint(1, 3)
        print(f"💻 Computer chose {self.dic[cominput]}")
        return cominput

    def final_winner(self):
        """Determine the final winner and save results to file."""
        if self.modeinput == 1:
            if self.computerscore == self.player1score:
                print(f"The scores are equal: {self.computerscore}")
                winner = "Tie"
            elif self.computerscore > self.player1score:
                print(f"Computer score is {self.computerscore} and your score is {self.player1score}. Computer won the game!")
                winner = "Computer"
            else:
                print(f"Computer score is {self.computerscore} and your score is {self.player1score}. Congratulations! You won the game!")
                winner = self.player1name

        elif self.modeinput == 2:
            if self.player1score == self.player2score:
                print(f"The scores are equal: {self.player1score}")
                winner = "Tie"
            elif self.player2score > self.player1score:
                print(f"Congratulations to {self.player2name}! You are the winner")
                winner = self.player2name
            else:
                print(f"Congratulations to {self.player1name}! You won the game")
                winner = self.player1name

        # Save results to file
        with open("game_results.txt", "a") as f:
            f.write(f"{datetime.now()}: Mode {self.modeinput}, Player1: {self.player1name} Score: {self.player1score}, ")
            if self.modeinput == 1:
                f.write(f"Computer Score: {self.computerscore}, Winner: {winner}\n")
            else:
                f.write(f"Player2: {self.player2name} Score: {self.player2score}, Winner: {winner}\n")
                f.write("_" * 40 + "\n")

    def play_again(self):
        """Ask the user whether they want to replay or exit."""
        while True:
            try:
                choice = int(input(
                    "\n🔁 Do you want to play another game?\n"
                    "1️⃣ Yes, play again\n"
                    "2️⃣ No, exit game\n👉 Your choice: "
                ))
                if choice == 1:
                    return True
                elif choice == 2:
                    return False
                else:
                    print("❌ Please enter 1 or 2.")
            except ValueError:
                print("⚠️ Invalid input. Please enter 1 or 2.")


# --- Run the game ---
if __name__ == "__main__":
    game = RockPaperScissors("Player")
    game.rock_paper_scissors()