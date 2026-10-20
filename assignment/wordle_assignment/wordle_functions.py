import random


def choose_word():
    """Choose and return a five-letter secret word."""
    # These words have five letters and no repeated letters for the basic version.
    words = [
        "APPLE", "BRAIN", "CHAIR", "CLOUD", "DREAM",
        "FLAME", "GRAPE", "HOUSE", "LIGHT", "MONEY",
        "NIGHT", "PLANT", "QUICK", "SMILE", "TRAIN"
    ]
    return random.choice(words)


def get_guess(previous_guesses):
    """Ask for a guess until it is valid and has not been used before."""
    while True:
        guess = input("Enter a five-letter word: ").strip().upper()

        if len(guess) != 5:
            print("Your guess must contain exactly five letters. Try again.")
        elif not guess.isalpha():
            print("Please enter letters only. Try again.")
        elif guess in previous_guesses:
            print("You already guessed that word. Try a different word.")
        else:
            return guess


def evaluate_guess(guess, secret_word):
    """Return a list containing G, Y, or - for each letter in the guess."""
    feedback = ["-"] * 5
    remaining_letters = list(secret_word)

    # First mark letters that are correct and in the correct position.
    for index in range(5):
        if guess[index] == secret_word[index]:
            feedback[index] = "G"
            remaining_letters[index] = ""

    # Then mark correct letters that are in the wrong position.
    # This two-step method handles repeated letters correctly.
    for index in range(5):
        if feedback[index] != "G" and guess[index] in remaining_letters:
            feedback[index] = "Y"
            letter_index = remaining_letters.index(guess[index])
            remaining_letters[letter_index] = ""

    return feedback


def display_guess(guess, feedback):
    """Display the guess and the feedback for each letter."""
    print("Guess:    " + " ".join(guess))
    print("Feedback: " + " ".join(feedback))


def has_won(guess, secret_word):
    """Return True if the guess matches the secret word."""
    return guess == secret_word
