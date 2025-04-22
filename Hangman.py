import random

def hangman():
    words = ["apple", "banana", "cherry", "orange"]
    word = random.choice(words)
    guessed_word = ["_"] * len(word)
    attempts = 6
    guessed_letters = set()

    print("Welcome to Hangman!")
    print(" ".join(guessed_word))

    while attempts > 0 and "_" in guessed_word:
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please guess a single valid letter.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        
        guessed_letters.add(guess)
        
        if guess in word:
            print(f"Good job! {guess} is in the word.")
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed_word[i] = guess
        else:
            attempts -= 1
            print(f"Wrong guess! You have {attempts} attempts left.")
        
        print(" ".join(guessed_word))
    
    if "_" not in guessed_word:
        print("Congratulations! You guessed the word:", word)
    else:
        print(f"Game over! The word was: {word}")

# Start the game
hangman()



