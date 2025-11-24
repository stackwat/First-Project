# First-Project
Guess The Number — Python Terminal Game
Overview
“Guess The Number” is a simple, interactive Python terminal game designed to give users a quick dopamine hit while sharpening their intuition. The game offers three difficulty levels, each with its own range and number of attempts. It’s beginner-friendly, lightweight, and runs straight from the terminal — no dependencies, no drama.

This project is perfect for anyone learning Python and exploring core concepts like loops, conditionals, user input, and random number generation.
 Features

 Three Difficulty Levels

Level 1: Guess a number between 1–5 (2 attempts)

Level 2: Guess a number between 1–10 (3 attempts)

Level 3: Guess a number between 1–20 (5 attempts)

 Randomized Number Generation
Each attempt generates a fresh challenge using Python’s built-in random module.

 Interactive CLI Experience
Real-time prompts, instant feedback, and a clean flow for repeated gameplay.

 Replayable Game Loop
Choose levels repeatedly, exit anytime, grind your way to victory.

 Technologies / Tools Used

Python 3.x

random module (built-in)

Terminal/Command Prompt

Basic Control Structures (loops, conditionals, input/output)

 Installation & Running the Project
1. Clone the Repository
git clone https://github.com/your-username/your-repo-name.git

2. Navigate into the Project Folder
cd your-repo-name

3. Run the Python File
python guess_the_number.py


(Use python3 if you're on macOS/Linux.)

 Instructions for Testing the Game

To ensure everything works as intended:

1. Start the Program

Run the script and verify that the main menu displays correctly:

Level 1

Level 2

Level 3

Exit

2. Test Each Level

Confirm the number of attempts matches the level specification.

Enter correct and incorrect guesses to test both win and fail paths.

Validate that the chosen number is revealed only after attempts are exhausted (or on win).

3. Try Invalid Inputs

Enter alphabets or symbols (program currently expects only integers; this tests robustness).

Enter a menu choice outside 1–4 and check if it offers the “Go to main menu” option.

4. Restart & Exit

Loop back to try different levels.

Exit cleanly using option 4
