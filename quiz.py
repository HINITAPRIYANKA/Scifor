import tkinter as tk
from tkinter import messagebox

class QuizGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Quiz Game")

        self.points = 0
        self.level = tk.StringVar(value="Easy")

        self.question_label = tk.Label(self.master, text="What is the capital of France?")
        self.question_label.pack(pady=10)

        self.answer_entry = tk.Entry(self.master)
        self.answer_entry.pack(pady=10)

        self.level_menu = tk.OptionMenu(self.master, self.level, "Easy", "Medium", "Hard")
        self.level_menu.pack(pady=10)

        self.submit_button = tk.Button(self.master, text="Submit", command=self.check_answer)
        self.submit_button.pack(pady=10)

    def check_answer(self):
        user_answer = self.answer_entry.get().strip().lower()
        correct_answer = self.get_correct_answer()

        if user_answer == correct_answer:
            self.points += 1
            messagebox.showinfo("Correct", "Correct answer! You earned 1 point.")
        else:
            messagebox.showinfo("Incorrect", f"Wrong answer. The correct answer is {correct_answer}.")

        if self.points >= 3:
            messagebox.showinfo("Congratulations", "You have reached 3 points! You win a reward.")

    def get_correct_answer(self):
        if self.level.get() == "Easy":
            return "paris"
        elif self.level.get() == "Medium":
            return "paris"
        elif self.level.get() == "Hard":
            return "paris"


if __name__ == "__main__":
    root = tk.Tk()
    quiz_app = QuizGame(root)
    root.mainloop()


