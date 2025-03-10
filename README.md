Blackjack Game
A command-line-based Blackjack game implemented in Python. This interactive program allows you to play a simplified version of Blackjack against the computer (dealer).

Features
Interactive Gameplay: Choose to "hit" (draw a card) or "stand" (end your turn) during your turn.

Dealer Logic: The dealer automatically draws cards until their score is at least 17.

Score Calculation: Handles Aces dynamically (value 11 or 1) to avoid busting.

Win/Lose Conditions: Determines the winner based on standard Blackjack rules.

Code Structure
blackjack.py: The main script containing the game logic.

README.md: This file, providing an overview of the project.

Example Gameplay
Welcome to Blackjack!
Your cards: [('7', 'Hearts'), ('King', 'Diamonds')], Current score: 17
Dealer's first card: ('5', 'Clubs')
Do you want to 'hit' or 'stand'? hit
Your cards: [('7', 'Hearts'), ('King', 'Diamonds'), ('4', 'Spades')], Current score: 21
Do you want to 'hit' or 'stand'? stand
Dealer's cards: [('5', 'Clubs'), ('9', 'Diamonds'), ('8', 'Hearts')], Dealer's score: 22
Dealer busts! You win!
Do you want to play again? (yes/no): no
Thanks for playing! Goodbye!

Requirements
Python 3.x

Contributing
Contributions are welcome! If you have any suggestions or improvements, feel free to open an issue or submit a pull request.
