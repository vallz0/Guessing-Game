import random
from typing import Optional

class GuessingGame:
    def __init__(self, min_number: int = 0, max_number: int = 20):
        self.min_number = min_number
        self.max_number = max_number
        self.random_number: Optional[int] = None

    def start_game(self) -> None:
        print("Welcome to the Guessing Game!")
        self.random_number = random.randint(self.min_number, self.max_number)
        self._play()

    def _play(self) -> None:
        while True:
            try:
                user_guess = self._get_user_input()
                if self._check_guess(user_guess):
                    print("Congratulations! You guessed the correct number.")
                    break
            except ValueError as e:
                print(f"Invalid input: {e}")

    def _get_user_input(self) -> int:
        user_input = input(f"Guess a number between {self.min_number} and {self.max_number}: ")
        if not user_input.isdigit():
            raise ValueError("Please enter a valid integer.")
        return int(user_input)

    def _check_guess(self, guess: int) -> bool:
        if self.random_number is None:
            raise RuntimeError("The game has not started yet.")

        if guess == self.random_number:
            return True
        elif guess > self.random_number:
            print("Your number is higher than expected.")
        else:
            print("Your number is lower than expected.")
        return False

if __name__ == "__main__":
    game = GuessingGame()
    game.start_game()
