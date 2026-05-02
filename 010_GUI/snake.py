import tkinter as tk
import random

# Game settings
WIDTH = 600
HEIGHT = 400
CELL_SIZE = 20
SPEED = 100

# Colors
BG_COLOR = "black"
SNAKE_COLOR = "green"
FOOD_COLOR = "red"

class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake Game")

        self.canvas = tk.Canvas(root, bg=BG_COLOR, width=WIDTH, height=HEIGHT)
        self.canvas.pack()

        self.direction = "Right"
        self.snake = [(100, 100), (80, 100), (60, 100)]
        self.food = None

        self.create_food()
        self.draw_snake()

        self.root.bind("<Key>", self.change_direction)

        self.running = True
        self.move()

    def draw_snake(self):
        self.canvas.delete("snake")
        for x, y in self.snake:
            self.canvas.create_rectangle(
                x, y, x + CELL_SIZE, y + CELL_SIZE,
                fill=SNAKE_COLOR, tag="snake"
            )

    def create_food(self):
        x = random.randint(0, (WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
        y = random.randint(0, (HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE

        self.food = (x, y)
        self.canvas.delete("food")
        self.canvas.create_oval(
            x, y, x + CELL_SIZE, y + CELL_SIZE,
            fill=FOOD_COLOR, tag="food"
        )

    def move(self):
        if not self.running:
            return

        head_x, head_y = self.snake[0]

        if self.direction == "Up":
            head_y -= CELL_SIZE
        elif self.direction == "Down":
            head_y += CELL_SIZE
        elif self.direction == "Left":
            head_x -= CELL_SIZE
        elif self.direction == "Right":
            head_x += CELL_SIZE

        new_head = (head_x, head_y)

        # Collision with wall
        if (head_x < 0 or head_x >= WIDTH or
            head_y < 0 or head_y >= HEIGHT or
            new_head in self.snake):
            self.game_over()
            return

        self.snake.insert(0, new_head)

        # Eating food
        if new_head == self.food:
            self.create_food()
        else:
            self.snake.pop()

        self.draw_snake()
        self.root.after(SPEED, self.move)

    def change_direction(self, event):
        key = event.keysym

        if key == "Up" and self.direction != "Down":
            self.direction = "Up"
        elif key == "Down" and self.direction != "Up":
            self.direction = "Down"
        elif key == "Left" and self.direction != "Right":
            self.direction = "Left"
        elif key == "Right" and self.direction != "Left":
            self.direction = "Right"

    def game_over(self):
        self.running = False
        self.canvas.create_text(
            WIDTH // 2, HEIGHT // 2,
            text="GAME OVER",
            fill="white",
            font=("Arial", 24)
        )

# Run game
root = tk.Tk()
game = SnakeGame(root)
root.mainloop()