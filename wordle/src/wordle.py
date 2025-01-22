'''
Code up a game of wordle.
- 5 letter words
- 6 turns
- in each turn, inspect the input word given by the user and return an output showing 3 categories:
  1) Letters present in the exact location
  2) Letters present in the target word, but at a different location
  3) Letters are not present at all in the target word

Data:
List of 5 letter words was taken from Donald Knuth's (Stanford) webpage:
    https://www-cs-faculty.stanford.edu/~knuth/programs.html
    wordlists.tgz/words5-from-OSPD4.txt - 'English words of lengths 2 thru 12 [OSPD4], ordered by frequency'

Class and it's methods

Issues left to be resolved:
    feedback when a letter is present but not in the same location or appears 2 times.

'''
import random

class TargetWord:

    # the purpose of this class is to store a target word as an object and then to give feedback comparing an input word with the target word.

    def __init__(self, filepath):

        # at every instance of the class, assign a 5 letter target word from a txt file.
        with open(filepath, 'r') as file:
            words_str = file.read().strip()

        words_lst = words_str.split()
        random_index = random.randint(0,len(words_lst))

        self.target_word = words_lst[random_index]

    def play_round(self, player_word):
        # takes a user's word and provides feedback comparing the 2 strings

        if player_word == self.target_word:
            return 'Success'


        feedback = ''
        for index in range(len(player_word)):
            if player_word[index] == self.target_word[index]:
                feedback += player_word[index]

            elif player_word[index] in self.target_word:
                feedback += player_word[index].upper()

            else:
                feedback += '_'

        return feedback

# Workflow
filepath = '/Users/mukti/Documents/learning_courses/short-scripts/wordle/data/words5-from-OSPD4'

wordle_1 = TargetWord(filepath)

# access/see the target word
wod = wordle_1.target_word
print(wod)
user_word = ''
round_num = 0
rounds = 6

while user_word != wod:

    if round_num == rounds:
        print(f'Failed! Word of the day was {wod}')
        break

    user_word = input(f'Enter a {len(wod)} letter word.')

    # process the user's input and standardize it; assuming no special characters
    user_word = user_word.lower().strip()

    if len(user_word) != len(wod):
        print(f'Error. Word should be of {len(wod)} letters.')

    else:
        feedback = wordle_1.play_round(user_word)
        round_num += 1
        print(feedback)
