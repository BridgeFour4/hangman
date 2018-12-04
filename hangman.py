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
def menu():
    print("welcome to Hangman. ")
    while True:
                play=input("would you like to play y/n")
                if play.lower()=="y":
                    game()
                    break
                elif play.lower()=="n":
                    print("goodbye")
                    break
                else:
                    print("i didn't get that")
    
def game():
    global wrong
    global  soFar
    global used
    global word
    
    while wrong<MAX_WRONG and soFar !=word:
        display()
        guess=guess_check("what letter would you like to guess")
        guess = guess.upper()

        while guess in used:
            print("you've already guessed the letter",guess)
            guess=guess_check("Enter your guess")
            guess = guess.upper()

        used.append(guess)
        print(word)
        if guess in word:
            print("\nYes!",guess,"is in the word!")
            
            #create a new so far
            new=""
            for i in range(len(word)):
                if guess==word[i]:
                    new+=guess
                else:
                    new+=soFar[i]
            soFar=new
        else:
            print("\nSorry,",guess,"isn't in the word")
            wrong+=1
        guess_word=input("would you like to guess the word y/n")
        if guess_word.lower()=="y":
            value=guessWord(word)
        else:
                print("continue then")
    if wrong ==MAX_WRONG:
        lose()
    else:
        win()
    input("\n\nPress the enter key to exit")
        

def display():
    print(HANGMAN[wrong])
    print("\nYou've used the following letters so far",used)
    print("\nSo far the word is:\n",soFar)
def guess_check(message):
    guess=input(message)
    while True:
        if guess.isalpha():
            return guess
        else:
            guess=input(message)
            
def guessWord(word,MAX_WRONG):
    while True:
        word_guess=input("enter the word")
        if word_guess.upper()==word:
            return win
        else:
            return MAX_WRONG
        
def win():
    print("\n you guessed it")
    print("\nthe word was ",word)
    while True:
                play=input("would you like to play again y/n")
                if play.lower()=="y":
                    game()
                    break
                else:
                    print("goodbye")
                    break
                
def lose():
    print(HANG_MAN[wrong])
    print("you've been hanged")
    print("\nthe word was ",word)
    while True:
                play=input("would you like to play again y/n")
                if play.lower()=="y":
                    game()
                    break
                else:
                    print("goodbye")
                    break

menu()


