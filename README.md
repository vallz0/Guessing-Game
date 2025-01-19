# Guessing Game

## Overview
The **Guessing Game** is a Python-based number guessing game designed with clean code principles and object-oriented programming. This project is ideal for beginners learning Python or exploring OOP concepts. The game challenges players to guess a randomly generated number with helpful hints provided after each guess.

## Features
- Random number generation within a customizable range.
- Input validation to ensure a smooth gameplay experience.
- Modular design for easy code extension and maintenance.
- Provides feedback on whether the guessed number is too high or too low.

## How to Play
1. Run the Python script.
2. Enter your guess when prompted.
3. Receive feedback until you guess the correct number.

## Requirements
- Python 3.8 or higher.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/vallz0/Guessing-Game.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Guessing-Game
   ```
3. Run the script:
   ```bash
   python main.py
   ```

## Code Structure
- **`GuessingGame` class**: Handles the game logic, user input, and feedback.
- **Main script**: Instantiates the `GuessingGame` class and starts the game.

## Customization
You can modify the range of numbers by adjusting the `min_number` and `max_number` parameters in the `GuessingGame` class:
```python
# Example:
game = GuessingGame(min_number=1, max_number=50)
```

