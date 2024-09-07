import random


game_title = "WordRaider"

word_bank = []

#rstrip removes end-of-the-line Char
with open("words.txt") as word_file:
    for line in word_file:
        word_bank.append(line.rstrip().lower())

random_word = random.choice(word_bank)

misplaced_letters = []
wrong_letters = []
max_turns = 5
current_turn = 0

print("Hello, welcome to Word Raider, a word guessing game")
print(f"The words are all 5 letters and you will have {max_turns}")
print(f"Start guessing and I will tell you how many turns you have left")

while current_turn <= 5:
    print(f"You now have {max_turns-current_turn}/{max_turns}")
    user_guess = input("Whats your guess? ")
    if user_guess.isalpha() and len(user_guess) == 5:
        pass
    else:
        print("**Enter only a 5 letter word**")
        continue
    current_turn += 1
