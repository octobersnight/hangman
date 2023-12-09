# Hangman Game!!!
# Pham 2023-12-08

import random
import hangmanstages

word_list = ["ardvark", "baboon", "camel", "fornite", "final", "susanoo", "megaman", "monster"]



print(hangmanstages.title)
print("Welcome to Guess the Word A.K.A \"Hangman!!!!\"")

# atler. 1
# generate random number to select the index and pass it to the variable
# len_word_list = random.choice(word_list)
# chosen_word = len_word_list
# word_length = len(chosen_word)

# display = []
# for _ in range(len(chosen_word)):
#     display += "_"

# print(display)

# ask user to pick a letter and convert t to lower case
# guess = input("Guess a Letter: ").lower()

# check each index if the letter matches
# for position in range(word_length):
#     letter = chosen_word[position]
#     if letter == guess:
#         display[position] = letter

# print(display)

# this negate if there are no more underscore in the display
# if "_" not in display:
#     end_of_game = True


################################################################################

# alter. 2
# generate random number to select the index and pass it to the variable
len_word_list = random.randint(0, len(word_list) - 1)
chosen_word = word_list[len_word_list]

# testing code
#print(f"The solution is {chosen_word} \n")

fill_in_blank = []
display = []
number_of_space = "_"
blank_word = ""
guess_word = ""
total_try = 0

for _ in range(0, len(chosen_word)):
    fill_in_blank.append(number_of_space)
    blank_word += number_of_space + " "

# print(blank_word)

while "_" in fill_in_blank:
    print(hangmanstages.stage[total_try])
    print(' '.join(fill_in_blank) + "\n")
    # ask user to pick a letter and convert to lower case
    guess_variable = input("Guess a Letter: ")
    guess = guess_variable.lower()

    # check each index if the letter matches
    for x in range(0, len(chosen_word)):
        #print(chosen_word[x])
        if guess == chosen_word[x]:
            #print("right")
            fill_in_blank[x] = guess

    # check if any index matches the letter, if not, increase the tried 
    if guess not in fill_in_blank:
        total_try += 1
    
    # when number of guesses reach 7, gameover.
    if hangmanstages.stage[total_try] == hangmanstages.stage[7]:
        print(hangmanstages.stage[7])
        print("Hangman!!! you Lose!!!")
        print("Thank you for playing with us!!!")
        exit()

    # using join() display the list from ['_', '_',...] to " _ _ _ _ _ "
    print(' '.join(fill_in_blank))
    guess_word = ''.join(fill_in_blank)
    print("\n")

print("Thank you for playing with us!!!")

# checking/testing each output
# 
#print(hangmanstages.stage[3])

