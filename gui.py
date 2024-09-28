import random
import tkinter as tk
from tkinter import messagebox

class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Challenge")

        self.words = ["python", "hangman", "challenge", "programming", "developer"]
        self.word = random.choice(self.words).lower()
        self.word_letters = set(self.word)
        self.guessed_letters = set()
        self.attempts = 6

        # Create GUI components
        self.word_label = tk.Label(self.root, text="_ " * len(self.word), font=("Arial", 20))
        self.word_label.pack(pady=20)

        self.entry = tk.Entry(self.root, font=("Arial", 14))
        self.entry.pack(pady=10)

        self.guess_button = tk.Button(self.root, text="Guess", command=self.check_guess)
        self.guess_button.pack(pady=10)

        self.info_label = tk.Label(self.root, text="Attempts remaining: 6", font=("Arial", 14))
        self.info_label.pack(pady=10)

        self.guessed_label = tk.Label(self.root, text="Guessed letters: ", font=("Arial", 14))
        self.guessed_label.pack(pady=10)

    def update_word_display(self):
        current_word = [letter if letter in self.guessed_letters else "_" for letter in self.word]
        self.word_label.config(text=" ".join(current_word))

    def check_guess(self):
        guess = self.entry.get().lower()
        self.entry.delete(0, tk.END)

        if not guess or len(guess) != 1:
            messagebox.showerror("Invalid Input", "Please enter a single letter.")
            return

        if guess in self.guessed_letters:
            messagebox.showinfo("Already Guessed", "You already guessed that letter.")
        elif guess in self.word_letters:
            self.guessed_letters.add(guess)
            self.word_letters.remove(guess)
            self.update_word_display()
            if not self.word_letters:
                messagebox.showinfo("You Win!", f"Congratulations! You guessed the word '{self.word}' correctly.")
                self.reset_game()
        else:
            self.guessed_letters.add(guess)
            self.attempts -= 1
            self.info_label.config(text=f"Attempts remaining: {self.attempts}")
            self.guessed_label.config(text="Guessed letters: " + " ".join(sorted(self.guessed_letters)))

            if self.attempts == 0:
                messagebox.showinfo("Game Over", f"Sorry, you lost! The correct word was '{self.word}'.")
                self.reset_game()

    def reset_game(self):
        self.word = random.choice(self.words).lower()
        self.word_letters = set(self.word)
        self.guessed_letters.clear()
        self.attempts = 6
        self.update_word_display()
        self.info_label.config(text="Attempts remaining: 6")
        self.guessed_label.config(text="Guessed letters: ")

# Run the Tkinter GUI
if __name__ == "__main__":
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()
