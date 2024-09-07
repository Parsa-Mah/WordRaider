import random


game_title = "WordRaider"

word_bank = []

#rstrip removes end-of-the-line Char
with open("words.txt") as word_file:
    for line in word_file:
        word_bank.append(line.rstrip().lower())

random_word = random.choice(word_bank)
print("**Debug** word =", random_word)

misplaced_letters = []
wrong_letters = []
max_turns = 5
current_turn = 0


print("Hello, welcome to Word Raider, a word guessing game")
print(f"The words are all 5 letters and you will have {max_turns}")
print(f"Start guessing and I will tell you how many turns you have left")

while current_turn < 5:
    correct_letters = 0
    print()
    print()
    print(f"You now have {max_turns-current_turn}/{max_turns}")
    user_guess = input("Whats your guess? ").lower()
    print("*" * 30)
    if user_guess.isalpha() and len(user_guess) == 5:
        for i in range(5):
            if user_guess[i] == random_word[i]:
                print(user_guess[i], end=" ")
                correct_letters += 1
                if user_guess[i] in misplaced_letters:
                    misplaced_letters.remove(user_guess[i])
            else:
                for j in range(5):
                    if user_guess[i] == random_word[j]:
                        if user_guess[i] not in misplaced_letters:
                            misplaced_letters.append(user_guess[i])
                        print("_", end=" ")
                        break
                else:
                    print("_", end=" ")
                    if user_guess[i] not in wrong_letters:
                        wrong_letters.append(user_guess[i])
    else:
        print("**Enter only a 5 letter word**")
        continue

    if correct_letters == 5:
        print()
        print(f"Congrats You won and correctly guessed *{random_word}*")
        break

    print()
    print(f"Misplaced letters are: {misplaced_letters}")
    print(f"Wrong letters are: {wrong_letters}")

    current_turn += 1
else:
    print()
    print(f"The word was {random_word}")
    print("Sorry you lost")
