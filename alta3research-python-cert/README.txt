# alta3research-python-cert
Project for Python Certification from Alta3 Research

The program is an Animal Riddle Game. 

The player is first asked if they are ready to play. There is a loop setup to check if the player's input is an expected value of either "Y" or "N". 
* If the input does not meet the criteria of either "Y" or "N", then they will be continually prompted to enter a valid value. 
* If the player's input meets the criteria of "N" then the message "BOO! Goodbye!" is displayed and the game ends
* If the player's input meets the criteria of "Y" then they will proceed with the game. 

When the game proceeds, the animal_riddle.csv file is read and stores the data as a dictionary. 
The answers are the keys in the dictionary and the riddles are the values. 
The riddles are displayed to the player randomly (no particular order from how it was read from the animal_riddle.csv file). 
The player has 3 chances per riddle to guess the correct answer. 
If the player answers all of the riddles correctly, they are displayed the "WOW! YOU WIN!" message. 
If the player does not answer all/any of the riddles correctly, they are displayed the "Sorry! Better luck next time!" message.



## Prerequisites
* This program requires [python3](https://wiki.python.org/moin/BeginnersGuide/Download). Proceed to the URL for instructions on how to install.
* This program also utilizes the crayons library. Install the crayons library by using: *$ pip install crayons*
* Lastly, the program uses the built in csv library.



## Built With
* [Python](https://www.python.org/)



## Authors
* Mary Nguyen 
