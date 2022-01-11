#The first section of the code will introduce the program with a print statment
print("Welcome to Console Hangman!")

print("")
print("")
#Then we can import some libraries that we will be using
import random
import sys
#Open our lexicon for use
txt = open('hangManList.txt', "r")


random_word = ""
#The first preliminary while loop is just used to find a word in the lexicon
#that is greater than 3 characters, it does this by selecting a random line-
#from the lexicon and then reading the word inside the line to check for its
#length.
while len(random_word) <= 3:
    random_word = (random.choice(open('hangManList.txt').read().split()))
    

#Assinging values to some variables that will be used in the upcoming while loop

play = True

guesses = 8

guessed_letters = []

bad_guessed_letters = []

i = 0
#Assinging a variable with dashes in the same length of our randomly chosen word
last_progress = "-" * len(random_word)
#The loop is set to True , so that it will only break if you win, or run out -
#of guesses
while play is True:
    progress = ""       
    guess = ""
    
#A loss statment and break
    if guesses == 0:

        print("You are out of guesses, you have lost.")
        print("")
        print("The secret word was ",random_word)

        break
#A winning statment and break    
    elif last_progress == random_word:

        print("Congratulations!")
        print("You guessed the secret word: ",random_word)
    
        break
#Introductory information, so that the player can always see the word in -
#progress
    print("")
    print("The sercet word looks like: ",last_progress)
    print("")
#An if statment for the bad guesses, that will only display once a bad guess-
#has been made
    if bad_guessed_letters:
        print("Your bad guesses so far: ",*bad_guessed_letters)
#print statment for the amount of guesses you have, followed by an input-
#statment asking for your next guess
    print("")
    print("You have",guesses,"guesses remaining.")
    print("")
    
    guess = str(input("What's your next guess? "))
    print("")    
            
#This if statment will check to see if the guess you just made was one that -
#you have already made, either bad or good. And then let you know as such
    if guess in guessed_letters or bad_guessed_letters:   
        print("You have already guessed this letter")
        print("")
        
        
#This if statment will check for the guess inside the characters of the -
#randomly chosen word.
#And if it isnt, it will let you know, and then run another if statment which -
#will then check if that guess was one you have already made and then decrease-
#the guess count accordingly
    if guess not in random_word:
        print("Sorry, there is no '",guess,"'.")
        print("")
        
        if guess not in bad_guessed_letters:
            bad_guessed_letters.append(guess)
            guesses -= 1
#The else statment is here to catch the only other outcome, which is a correct-
#guess. In which case it will let you know as such and then add that guess
#to a list of ones you have already guessed so that you dont end up guessing -
#it again
        
    else:
        print("Nice guess!")
        print("")
        guessed_letters.append(guess)
#The last section is going to be a for loop that follows after a correct guess.
#This for loop will run for the lenght of the random word. And while it runs
#it will compare the indicies of the randomly chosen word to the guess given.
#And when the guess overlaps it will replace our hidden words dash characters-
#with the guess given.
#Then eventually reassinging the "last_progress" so that it can be displayed -
#again and again as the player guesses

        for i in range(len(random_word)):
            
     
            if random_word[i] == guess:
                progress = progress + guess
            else:
                progress = progress + last_progress[i]
        last_progress = progress
        
#ensuring to close all files used                    
txt.close()

    
    
        
        
    
        
    
    



    





            
    
