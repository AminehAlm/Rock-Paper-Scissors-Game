# **🪨✋✂️ Rock Paper Scissors — Python Game**

An interactive **Rock–Paper–Scissors** console game built with Python.  
You can play either **against the computer** or in **two-player mode** with a friend — featuring automatic score tracking, round setup, and result saving.

---

## 🌟 Features

✅ **Two Game Modes**  
- 1️⃣ Single Player — play against a smart random computer opponent  
- 2️⃣ Two Player — challenge your friend in turn-based mode  

✅ **Score System**  
- Each round awards **10 points** to the winner  
- Final results are calculated after all rounds  

✅ **Game Logging**  
- Every match is automatically saved in `game_results.txt` with:  
  - Date and time  
  - Player names  
  - Scores  
  - Final winner  

✅ **Replay Option**  
- After each match, you can choose to play again or quit safely  

✅ **Error Handling**  
- Prevents invalid inputs (letters, negative numbers, etc.)  
- Clear messages and user prompts  

---

## 🧠 How It Works

- Players choose between:  
  - 1️⃣ Paper  
  - 2️⃣ Scissors  
  - 3️⃣ Rock  
  - 4️⃣ Quit  

- Winning logic is handled via:

```python
self.winnerchoices = [(1, 3), (2, 1), (3, 2)]

•	Each tuple represents a winning (winner, loser) pair
•	Scores are added automatically and shown at the end of the match

⚙️ Installation & Setup

1. Clone the Repository
git clone https://github.com/AminehAlm/rock-paper-scissors.git
cd rock-paper-scissors

2. (Optional) Create a Virtual Environment
python -m venv venv
# macOS/Linux
source venv/bin/activate
# Windows
venv\Scripts\activate

3. Run the Game
python main.py

💡 The game will start in your terminal. Follow the on-screen prompts.

🎮 Example Gameplay
Welcome to Rock, Paper, Scissors Game :)
Please select the mode:
1: Play with computer
2: Play with another player
Your choice: 1

Please type your name here: Amineh
🔢 How many rounds do you want to play? 3

Round 1:
Amineh, make your move:
1️⃣ Paper
2️⃣ Scissors
3️⃣ Rock
4️⃣ Quit
👉 Your choice: 2
💻 Computer chose rock
You win this round!

...
🏆 Final Result:
Computer score is 10 and your score is 20.
Congratulations! You won the game!

🗂️ File Structure
rock-paper-scissors/
│
├── main.py              # Main game logic
├── game_results.txt     # Game history (auto-generated)
├── README.md            # Documentation
├── .gitignore           # Ignored system & cache files
└── LICENSE              # License file (MIT recommended)

📁 Example of game_results.txt
2025-10-31 12:45:33: Mode 1, Player1: Amineh Score: 30, Computer Score: 10, Winner: Amineh
________________________________________

🔁 Future Improvements

🚀 Ideas for next versions:
	•	Add graphical interface (Tkinter or PyGame)
	•	Implement leaderboard and statistics
	•	Add sound effects and animations
	•	Create multiplayer mode via network sockets

⸻

👩‍💻 Author

Amineh Alimohammadi
💬 A passionate learner exploring Python and data projects
🔗 GitHub Profile￼

📜 License

This project is licensed under the MIT License — free to use, modify, and distribute
MIT License
Copyright (c) 2025 Amineh

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction...

