import random

def choose_word():
   # List of words for the game
   words = ["python", "hangman", "computer", "programming", "banana", "apple", "cat", "dog", "elephant", "guitar"]
   return random.choice(words)

def display_word(word, guessed_letters):
   # Display the word with blanks for letters not yet guessed
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
   attempts = 6

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
               print("Congratulations! You've guessed the word:", word)
               break
       else:
           print("Incorrect guess!")
           attempts -= 1
           print("Attempts remaining:", attempts)

   if attempts == 0:
       print("Sorry, you've run out of attempts. The word was:", word)

if __name__ == "__main__":
   hangman()
