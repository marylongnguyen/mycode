#!/usr/bin/env python3
  
import csv
import random
import crayons


def main():
  
  begin = input('Are you ready (Y/N)? ')
    
  if begin.capitalize() not in ['Y', 'N']:
    while begin.capitalize() not in ['Y', 'N']:
      print('Invalid entry, please choose Y/N. ')
      begin = input('Are you ready(Y/N)? ')
      if begin.capitalize() == 'N':
        print('Boo! Goodbye!')

  elif begin.capitalize() == 'N':
    print('Boo! Goodbye!')
      
  else: 
    riddles_from_csv = {}

    with open('animal_riddle.csv', 'r') as csvfile:
      reader = csv.reader(csvfile)
      riddles_from_csv = {rows[0]:rows[1] for rows in reader}

    riddles_from_csv = {'Goldfish': 'I live in a bowl. I can swim. I have a tail. I also have fins and big eyes. What am I?', 
                        'Kangaroo': 'I jump when I walk and sit when I stand. What am I?', 
                        'Owl': 'I like to stay awake at night and sleep during the day. Who am I?', 
                        'Cow': 'I am a domestic animal living in the field. I like to eat grass and produce milk. Who am I?', 
                        'Bat': 'I fly all night and sleep at dawn. When I do that I hang upside down. Who am I?'}

    riddle = list(riddles_from_csv.values())
    answer = list(riddles_from_csv.keys())

    question = random.choice(riddle)
    print(question)

    riddle_answer_key = riddle.index(question) #list index of riddle to be used to return value from matching index in answer list
    print(answer[riddle_answer_key])

  # print crayons.red('red string')

main()
