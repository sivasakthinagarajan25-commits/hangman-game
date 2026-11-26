import random

# ASCII Gallows Art - 0 to 6 mistakes
HANGMAN_STAGES = [
    """
     +---+
     |   |
         |
         |
         |
         |

    """,
    """
     +---+
     |   |
     O   |
         |
         |
         |

    """,
    """
     +---+
     |   |
     O   |
     |   |
         |
         |

    """,
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |

    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |

    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |

    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |

    """
]

# Word List - DATHEON ku theva padura maadhiri
WORDS = [
    "PYTHON", "COMPUTER", "HANGMAN", "PROGRAM",
    "KEYBOARD", "INTERNET", "LAPTOP", "DATHEON",
    "CODING", "STUDENT", "COLLEGE", "CHENNAI",
    "FRIEND", "GARDEN", "FLOWER", "MARKET"
]

def play_hangman():
    secret_word = random.choice(WORDS)
    guessed_letters = set()
    wrong_guesses = 0
    max_attempts = 6

    print("=== Welcome to HANGMAN Game ===")
    print("Guess the hidden word letter by letter!")
    print(f"You have {max_attempts} attempts.")

    while wrong_guesses < max_attempts:
        # Masked word display - ex: _ A _ H E O N
        display_word = ""
        for letter in secret_word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "

        print("\n" + HANGMAN_STAGES[wrong_guesses])
        print("Word:", display_word)
        print("Guessed Letters:", ", ".join(sorted(guessed_letters)) if guessed_letters else "None")
        print(f"Remaining Attempts: {max_attempts - wrong_guesses}")

        # Win check
        if all(letter in guessed_letters for letter in secret_word):
            print("\n🎉 Congratulations! You WON!")
            print(f"The word was: {secret_word}")
            return

        guess = input("\nEnter a letter: ").upper().strip()

        # Validation
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter only ONE letter!")
            continue

        # Duplicate check - penalty illa
        if guess in guessed_letters:
            print(f"You already guessed '{guess}'! No penalty. Try another letter.")
            continue

        guessed_letters.add(guess)

        if guess in secret_word:
            print(f"Good! '{guess}' is in the word.")
        else:
            wrong_guesses += 1
            print(f"Wrong! '{guess}' is NOT in the word.")

    # Lose
    print("\n" + HANGMAN_STAGES[wrong_guesses])
    print("\n💀 GAME OVER! You LOST!")
    print(f"The correct word was: {secret_word}")

# Game Start
if __name__ == "__main__":
    play_hangman()
