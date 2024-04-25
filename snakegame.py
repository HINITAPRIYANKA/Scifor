import tkinter as tk
import random

# Constants
GRID_SIZE = 20
CELL_SIZE = 20
DELAY = 100  # milliseconds


class SnakeGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Snake Game")
        self.master.geometry(f"{GRID_SIZE * CELL_SIZE}x{GRID_SIZE * CELL_SIZE}")

        self.canvas = tk.Canvas(self.master, bg="black", width=GRID_SIZE * CELL_SIZE, height=GRID_SIZE * CELL_SIZE)
        self.canvas.pack()

        self.snake = [(0, 0)]
        self.direction = "Right"
        self.food_position = self.generate_food()

        self.master.bind("<Key>", self.on_key_press)

        self.update()

    def on_key_press(self, event):
        key = event.keysym
        if (key == "Up" and self.direction != "Down") or \
                (key == "Down" and self.direction != "Up") or \
                (key == "Left" and self.direction != "Right") or \
                (key == "Right" and self.direction != "Left"):
            self.direction = key

    def generate_food(self):
        while True:
            food_position = (random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1))
            if food_position not in self.snake:
                self.canvas.create_rectangle(food_position[0] * CELL_SIZE, food_position[1] * CELL_SIZE,
                                             (food_position[0] + 1) * CELL_SIZE, (food_position[1] + 1) * CELL_SIZE,
                                             fill="red", outline="black")
                return food_position

    def update(self):
        # Move the snake
        head = self.snake[0]
        if self.direction == "Up":
            new_head = (head[0], (head[1] - 1) % GRID_SIZE)
        elif self.direction == "Down":
            new_head = (head[0], (head[1] + 1) % GRID_SIZE)
        elif self.direction == "Left":
            new_head = ((head[0] - 1) % GRID_SIZE, head[1])
        elif self.direction == "Right":
            new_head = ((head[0] + 1) % GRID_SIZE, head[1])

        self.snake = [new_head] + self.snake[:-1]

        # Check for collision with food
        if new_head == self.food_position:
            self.snake.append(self.food_position)
            self.food_position = self.generate_food()

        # Check for collision with itself
        if len(self.snake) > 1 and new_head in self.snake[1:]:
            self.game_over()

        # Update the canvas
        self.canvas.delete("all")
        for segment in self.snake:
            self.canvas.create_rectangle(segment[0] * CELL_SIZE, segment[1] * CELL_SIZE,
                                         (segment[0] + 1) * CELL_SIZE, (segment[1] + 1) * CELL_SIZE,
                                         fill="green", outline="black")
        self.canvas.create_rectangle(self.food_position[0] * CELL_SIZE, self.food_position[1] * CELL_SIZE,
                                     (self.food_position[0] + 1) * CELL_SIZE, (self.food_position[1] + 1) * CELL_SIZE,
                                     fill="red", outline="black")

        # Schedule the next update
        self.master.after(DELAY, self.update)

    def game_over(self):
        self.canvas.create_text(GRID_SIZE * CELL_SIZE // 2, GRID_SIZE * CELL_SIZE // 2,
                                text="Game Over!", fill="white", font=("Helvetica", 16, "bold"))
        self.master.after_cancel(self.update)


if __name__ == "__main__":
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()

