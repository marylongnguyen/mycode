#!/usr/bin/env python3

"""Alta3 Research Python Certification Project | Author: Mary Nguyen

   Description:
   A script that creates an Animal Riddle Game.
   See README.txt file for more details."""

import csv
import random
import crayons


def main():
  
  begin = input('Are you ready (Y/N)? ')
    
  while begin.upper() not in ['Y', 'N']:
    begin = input('Invalid entry, please choose Y/N. ')
          
  if begin.upper() == 'N':
    print('Boo! Goodbye!')
      
  else: 
    riddles_from_csv = {}

    with open('animal_riddle.csv', 'r') as csvfile:
      reader = csv.reader(csvfile)
      riddles_from_csv = {rows[0]:rows[1] for rows in reader}

#     riddles_from_csv = {'Goldfish': 'I live in a bowl. I can swim. I have a tail. I also have fins and big eyes. What am I? ', 
#                         'Kangaroo': 'I jump when I walk and sit when I stand. What am I? ', 
#                         'Owl': 'I like to stay awake at night and sleep during the day. What am I? ', 
#                         'Cow': 'I am a domestic animal living in the field. I like to eat grass and produce milk. What am I? ', 
#                         'Bat': 'I fly all night and sleep at dawn. When I do that I hang upside down. What am I? '}


    num_riddles = len(riddles_from_csv)
    guess_count = 1
    riddles_correct = 0
    allowed_guesses = 3

    while num_riddles != 0:
      riddles = list(riddles_from_csv.values())
      answers = list(riddles_from_csv.keys())
      
      riddle = random.choice(riddles)
      guess = input(riddle)

      riddle_answer_key = riddles.index(riddle) #list index of riddle to be used to return value from matching index in answer list

      while guess_count < 3 and guess.capitalize() != answers[riddle_answer_key]:
        chances_remaining = str(allowed_guesses-guess_count)
        guess = input('Nope! Try again, you have '+ chances_remaining +' chances remaining. Who am I? ')    
        guess_count += 1

      if guess.capitalize() != answers[riddle_answer_key]: 
        print('Sorry, better luck next time!')
        break

      else:
          riddles_correct += 1
          vowels = ['A','E','I','O','U'] #used to help generate message for when the answer is correct

          if answers[riddle_answer_key][0] in vowels:
              print("Nice! Yes, I'm an " + answers[riddle_answer_key] + " :)")
          else:
              print("Nice! Yes, I'm a " + answers[riddle_answer_key] + " :)")

      riddles_from_csv.pop(answers[riddle_answer_key]) #remove riddles already answered during the same game session
      num_riddles = len(riddles_from_csv) #update length of num_riddles
      
  # print crayons.red('red string')

if __name__ == "__main__":
    main()
