import random
import webbrowser


def open_congratulatory_gif():
    url = 'https://i.gifer.com/7561.gif'
    webbrowser.open(url)

def choose_word():
    words = ["python", "hangman", "computer", "programming", "banana", "apple", "cat", "dog", "elephant", "guitar"
                                                                                                          "happy",
             "sad", "engine", "flower", "racecar", "universe", "free", "Prison", "lost", "find", "anger", "place",
             "print", "decisive", "room", "bent", "representative", "precious", "unlucky", "lucky", "road",
             "sweet", "savory", "bland", "new", "old", "piano", "match", "lighter", "lamp", "bed", "sun", "son",
             "villain",
             "hero", "bed", "sweat", "nerves", "research", "development", "economics", "mathematics", "geography",
             "spanish", "German", "english", "favorite", "hatred", "love"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    word = choose_word()
    guessed_letters = []
    difficulty = input("Choose difficulty level (easy/hard): ").lower()
    if difficulty == "easy":
        attempts = 7
    elif difficulty == "hard":
        attempts = 4
    else:
        print("Invalid difficulty level. Setting to easy.")
        attempts = 7
    hangman_images = [
        """
         +---+
         |   |
             |
             |
             |
             |
       =========
        """,
        """
         +---+
         |   |
         O   |
             |
             |
             |
       =========
        """,
        """
         +---+
         |   |
         O   |
         |   |
             |
             |
       =========
        """,
        """
         +---+
         |   |
         O   |
        /|   |
             |
             |
       =========
        """,
        """
         +---+
         |   |
         O   |
        /|\\  |
             |
             |
       =========
        """,
        """
         +---+
         |   |
         O   |
        /|\\  |
        /    |
             |
       =========
        """,
        """
         +---+
         |   |
         O   |
        /|\\  |
        / \\  |
             |
       =========
        """
    ]

    print("Welcome to Hangman!")
    print("You have", attempts, "attempts to guess the word.")

    while attempts > 0:
        print("\nWord:", display_word(word, guessed_letters))
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Correct guess!")
            if display_word(word, guessed_letters) == word:
                print("https://i.gifer.com/7561.gif","Congratulations! You've guessed the word:", word)
                break
        else:
            print("Incorrect guess!")
            print(hangman_images[len(hangman_images) - attempts])  # Print the corresponding hangman image depending on the level choosen
            attempts -= 1
            print("Attempts remaining:", attempts)

    if attempts == 0:
        print("Sorry, you've run out of attempts. The word was:", word)

if __name__ == "__main__":
    hangman()



