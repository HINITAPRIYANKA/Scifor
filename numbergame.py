import tkinter as tk
from tkinter import messagebox
import random

class NumberGuessingGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Number Guessing Game")

        self.secret_number = random.randint(1, 10)
        self.guesses_left = 3

        self.message_label = tk.Label(self.master, text="Guess the number between 1 and 10:")
        self.message_label.pack(pady=10)

        self.guess_entry = tk.Entry(self.master)
        self.guess_entry.pack(pady=10)

        self.submit_button = tk.Button(self.master, text="Submit Guess", command=self.check_guess)
        self.submit_button.pack(pady=10)

    def check_guess(self):
        user_guess = self.get_user_guess()

        if user_guess == self.secret_number:
            messagebox.showinfo("Congratulations", "Correct! You guessed the number.")
        else:
            self.guesses_left -= 1
            if self.guesses_left == 0:
                messagebox.showinfo("Game Over", f"Sorry, you've run out of guesses. The correct number was {self.secret_number}.")
                self.master.destroy()
            else:
                messagebox.showinfo("Incorrect", f"Wrong guess. You have {self.guesses_left} guesses left.")

    def get_user_guess(self):
        try:
            return int(self.guess_entry.get())
        except ValueError:
            messagebox.showinfo("Invalid Input", "Please enter a valid number.")
            return None


if __name__ == "__main__":
    root = tk.Tk()
    guessing_game = NumberGuessingGame(root)
    root.mainloop()


