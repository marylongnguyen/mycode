#!/usr/bin/env python3

"""Alta3 Research Python Certification Project | Author: Mary Nguyen
   Description:
   A script that creates an Animal Riddle Game.
   See README.txt file for more details."""

#import libraries
import csv
import random
import crayons

def main():

  begin = input('Are you ready to play (Y/N)? ') #the player is asked if they are ready to play the game
  
  #check if player's input is an expected value (Y/N) to proceed with the game
  while begin.upper() not in ['Y', 'N']: #loop until it meets the criteria of either Y/N
    begin = input('Invalid entry, please choose Y/N. ') #the player is asked to try again and suggested to enter Y/N 
          
  #if player input is N then end the game
  if begin.upper() == 'N':
    print('Boo! Goodbye!')
  
  #else begin the game
  else:     
    riddles_from_csv = {} #initiate dictionary to store data from animal_riddle.csv file

    #read animal_riddle.csv file and loop to store data into riddles_from_csv dictonary
    with open('animal_riddle.csv', 'r') as csvfile:
      reader = csv.reader(csvfile) 
      riddles_from_csv = {rows[0]:rows[1] for rows in reader}

    num_riddles = str(len(riddles_from_csv)) #create string of length of riddles_from_csv dictionary    
    riddles_correct = 0 #riddles correct begins at 0
    allowed_guesses = 3 #player is allowed 3 guesses

    print("There are " + num_riddles + " riddles total. Do you think you can get them all correct? Let's get started!")

    #loop until length of riddles_from_csv (aka number of riddles) is zero. 
    #The purpose is to display only riddles that the player has not answered
    #At the end there is a pop function to remove riddles the player has answered correctly
    while len(riddles_from_csv) != 0:
      guess_count = 1 #guess count begins at 1
      riddles = list(riddles_from_csv.values()) #get riddles from riddles_from_csv which are values
      answers = list(riddles_from_csv.keys())# get answers from riddles_from_csv which are keys
      
      riddle = random.choice(riddles) #randomly display a riddle to the player
      guess = input(riddle) #the players first time to try and guess the correct answer

      riddle_answer_key = riddles.index(riddle) #list index of riddle to be used to return value from matching index in answer list

      #loop until the player has reached guess count >= 3 and the players guess is incorrect
      while guess_count < 3 and guess.capitalize() != answers[riddle_answer_key]:
        chances_remaining = str(allowed_guesses-guess_count) 
        guess = input('Nope! Try again, you have '+ chances_remaining +' chances remaining. Who am I? ') #display the number of changes the player has remaining
        guess_count += 1

      #if the player does not answer correctly after 3 tries the "Sorry..." message is displayed and the game is ended
      if guess.capitalize() != answers[riddle_answer_key]: 
        print(crayons.red('Sorry! Better luck next time!'))
        break

      #if the player answers correctly they "Nice..." message is displayed
      #special handling was added for when the animal type begins with a vowel
      else:
          riddles_correct += 1
          vowels = ['A','E','I','O','U'] #used to help generate message for when the answer is correct

          if answers[riddle_answer_key][0] in vowels:
              print("Nice! Yes, I'm an " + answers[riddle_answer_key] + " :)")
          else:
              print("Nice! Yes, I'm a " + answers[riddle_answer_key] + " :)")

      riddles_from_csv.pop(answers[riddle_answer_key]) #remove riddles already answered during the same game session

    #if the play answers all the riddles correctly (aka no riddles remain in riddles_from_csv) then display "WOW! YOU WIN!" message
    if len(riddles_from_csv) == 0:
      print(crayons.green('WOW! YOU WIN!'))

if __name__ == "__main__":
    main()
