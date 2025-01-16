import random

words = ['pikachu','beast','shadow','biker','timepass','granny','boom']

chosen_word = random.choice(words)
word_display = [ '_' for _ in chosen_word]
attempts = 8

print("Welcome to hangman")

while attempts>0 and '_' in word_display:
    print("\n" + ' '.join(word_display))
    guess = input("Guess the letter: ").lower()
    if guess in chosen_word:
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                word_display[index] = guess
    else:
        print("That letter doesn't appear in the word!")
        attempts -= 1

if '_' not in word_display:
    print("You guessed the word!")
    print(' '.join(word_display))
    print("You survived")
else:
     print("You ran out of attempts. The chosen word was: "+ chosen_word)
     print("You died")
