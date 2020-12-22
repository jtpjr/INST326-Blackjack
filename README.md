# INST326-Blackjack

Files:
    blackjack.py: The blackjack.py file contains our code for the assignment.
    We created an interactive game of Blackjack, the gambling card game.
    This file contains functions and methods that allow you to perform any move 
    that you can do in a real life game of Blackjack. You as the user are competing 
    against the dealer, or computer, and you play a game of Blackjack. The command line
    allows you to enter bets and then as the game goes on it asks you a series of questions
    regarding what move you would like to make in each unique situation.

    blackjack_test.py: The blackjack_test.py file contains our Pytest script. 
    These file is used for testing certain functions to make sure when it is ran
    that it produces the correct outputs. We used assert statements to test certain unique
    situations and tried to cover all our bases for the specific functions that we 
    chose to test. 

    README.md: The README.md file explains the purpose of each file in our repository, 
    instructions on how to run your program from the command line,
    instructions on how to use your program and/or interpret the output of the program, 
    and an annotated bibliography of all sources we used to develop the project. 

Instructions on Running Program:
    Our game of blackjack is controlled and played in the command line. First, you enter
    "python3 blackjack.py X" in the command line if you have Mac or Linux, or you enter
    "python blackjack.py X" in command line, if you are on windows. Be sure to substitute "X" for a numeric value for your buy-in.
    Then, it will ask you to place a bet for the specific round and it will start from there. And then, as the game goes on it will keep
    asking you what move you would like to make based on the certain situation you are in, and to do so
    you enter the number into the command line that corresponds with the options shown to you. Finally, you just keep playing until you lose all your money or if you are winning and just want to stop.

Instructions on Interpreting the Output:
    The output is pretty simple and straightforward. If you win the round then you win your money back
    and the same amount that you bet. So, once a round is over it will tell you if you won or not and
    if you do win that money goes into your purse and if you lose then that money gets taken out of your purse. As your purse gets lower and lower you will see that and eventually once it is at 0 the game is over. 

Bibliography:
    https://www.businessinsider.com/blackjack-basics-2014-6
        Help learn rules of the game

    https://bicyclecards.com/how-to-play/blackjack/
        Help learn rules of the game

    https://stackoverflow.com
        Help us figure out some methods and functions that we didn't know how to do

    "Deck" class by Aric Bills
    	Inspiration and template for the "Deck" class in our code
