import random

def hangman():
    words = ["python", "hangman", "challenge", "programming", "developer"]
    word = random.choice(words).lower()
    word_letters = set(word)  # letters in the word
    guessed_letters = set()  # guessed letters by the player
    attempts = 6  # max number of wrong attempts

    print("Welcome to Hangman Challenge!")
    print("_ " * len(word))  # initial hidden word

    # Game loop
    while attempts > 0 and word_letters:
        print("\nYou have", attempts, "incorrect guesses left.")
        print("Guessed letters:", " ".join(sorted(guessed_letters)))

        # Display current state of the word
        current_word = [letter if letter in guessed_letters else "_" for letter in word]
        print("Word: ", " ".join(current_word))

        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word_letters:
            guessed_letters.add(guess)
            word_letters.remove(guess)
            print("Good guess!")
        else:
            guessed_letters.add(guess)
            attempts -= 1
            print("Incorrect guess.")

    # Win or lose message
    if not word_letters:
        print(f"\nCongratulations! You guessed the word '{word}' correctly.")
    else:
        print(f"\nSorry, you lost! The correct word was '{word}'.")

# Run the game
if __name__ == "__main__":
    hangman()
