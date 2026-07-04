import random

# List of words
words = ["python", "computer", "keyboard", "programming",
         "monitor", "internet", "developer", "software"]

# Select a random word
word = random.choice(words)

# Scramble the word
letters = list(word)
random.shuffle(letters)
scrambled_word = "".join(letters)

print("===== Word Scramble Game =====")
print("Unscramble the word:")
print(scrambled_word)

# User guess
guess = input("\nEnter your guess: ")

# Check answer
if guess.lower() == word:
    print("🎉 Congratulations! You guessed correctly.")
else:
    print("❌ Wrong guess!")
    print("The correct word is:", word)