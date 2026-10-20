from wordle_functions import choose_word, get_guess, evaluate_guess, display_guess, has_won


def play_game():
    """Run one game of Mystery Wordle."""
    secret_word = choose_word()
    previous_guesses = []
    max_attempts = 6

    print("\nWelcome to Mystery Wordle!")
    print("Guess the five-letter word.")
    print("\nG = correct letter and position")
    print("Y = correct letter, wrong position")
    print("- = letter is not in the word\n")

    # Give the player up to six valid guesses.
    for attempt in range(1, max_attempts + 1):
        print("Attempt " + str(attempt) + " of " + str(max_attempts))
        guess = get_guess(previous_guesses)
        previous_guesses.append(guess)

        feedback = evaluate_guess(guess, secret_word)
        display_guess(guess, feedback)

        if has_won(guess, secret_word):
            print("\nCongratulations! You solved the puzzle.")
            return

        print()

    # Reveal the answer if the player uses all attempts without winning.
    print("Out of guesses! The secret word was " + secret_word + ".")


def main():
    """Play again until the player chooses to stop."""
    play_again = "yes"

    while play_again == "yes" or play_again == "y":
        play_game()
        play_again = input("\nWould you like to play again? (yes/no): ").strip().lower()
        while play_again not in ["yes", "y", "no", "n"]:
            play_again = input("Please enter yes or no: ").strip().lower()

    print("\nThanks for playing!")


if __name__ == "__main__":
    main()
