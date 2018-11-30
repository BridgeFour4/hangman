#nathan Broadbent
#11/18
#hangman game

#imports
import random
import time
#constants
HANGMAN=(
    """
   ______
    |           |
    |
    |
    |
    |
    |
    |
 _|______
 """
    ,
"""
   ______
    |           |
    |          O
    |
    |
    |
    |
    |
 _|______
 """
        ,
"""
 ______
  |           |
  |          O
  |          +
  |          +
  |
  |
  |
 _______
 """
            ,
"""
 ______
  |           |
  |          O
  |    /- +-
  | /       +   
  |
  |
  |
 _______
 """
                ,
"""
   ______
    |           |
    |          O
    |    /- +-\\
    | /       +      \\
    |
    |
    |
 _|______
 """
                ,
"""
   ______
    |           |
    |          O
    |    /- +-\\
    | /       +      \\
    |         |
    |         |
    |
 _|______
 """
                    ,
"""
   ______
    |           |
    |          O
    |    /- +-\\
    | /       +      \\
    |        |   |
    |        |   |
    |
 _|______
 """
                        ,
"""
   ______
    |           |
    |          O
    |    /- +-\\
    | /       +      \\
    |        |   |
    |        |   |
    |       -   
 _|______
 """
                        ,
"""
   ______
    |           |
    |          O
    |    /- +-\\
    | /       +      \\
    |        |   |
    |        |   |
    |       -   -
 _|______
 """
    )

MAX_WRONG=len(HANGMAN)-1
WORDS=("INDEX","INPUT","VARIABLE","STRING","INTEGER")
word=random.choice(WORDS)#the word to be guessed
soFar="_"*len(word)
wrong=0
used=[]#letters already guessed
print("welcome to Hangman. Good luck")

while wrong<MAX_WRONG and soFar !=word:
    
    print(HANGMAN[wrong])
    print("\nYou've used the folling letters so far",used)
    print("\nSo far the word is:\n",so_far)

    guess=input("what letter would you like to guess")
    guess = guess.upper()

    while guess in used:
        print("you've already guessed the letter",guess)
        guess=input("Enter your guess")
        guess = guess.upper()

    used.append(guess)
    if guess in word:
        print("\nYes!",guess,"is in the word!")
        #create a new so far
        new=""
        for i in range(len(word)):
            if guess==word[i]:
                new+=guess
            else:
                new+=soFar[i]
        so_far=new
    else:
        print("\nSorry,",guess,"isn't in the word")
        wrong+=1

if wrong ==MAX_WRONG:
    print(HANG_MAN[wrong])
    print("you've been hanged")

else:
    print("\n you guessed it")
print("\nthe word was ",word)

input("\n\nPress the enter key to exit")

        
    

