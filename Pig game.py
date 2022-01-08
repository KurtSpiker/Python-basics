import random
#Import random library, and assign some variables a value so that they can used
Player = 1
P1_total = 0
P2_total = 0
Turn = 1
#Much like the CPU vs CPU we have an outer while loop with and if and else statment to seperate the two players turns
while (True):
#First if statment allows the game to know whos turn it is, and then we can print the current scores
    if Turn == Player:
        print("Player One's score: ", P1_total)
        print("Player Two's score: ", P2_total)
        print("It's Player One's turn")
#Reset our turn score so that it doesnt carry over from the other players phase
        Turn_score = 0
#Create our nested while loop for the CPU
        while (True):
#Using our same basic rolling system it will display current results and break if a 1 is rolled, when the turn score reaches 20, and when the score of the player reaches 100
            Roll = random.randint(1, 6)
            if Roll == 1:
                print("- rolled a  1")
                print("Pigged out!")
                Turn_score = 0
                break
            else:
                Turn_score += Roll
                print("- rolled a ", Roll)
            if Turn_score >= 20:
                break
            if P1_total >= 100:
                break
#Swapping the value of the turn variable(player) allows the game to loop back into player two's turn instead of player one's
        P1_total += Turn_score
        print("Total turn score = ", Turn_score)                    
        Player = 2
        if P1_total >= 100:
            print("Player One Wins!")
            break
#Create our else statment for the outer loop, and then create another nested loop containing the second players turn the human player
    else:
        print("Player One's score: ", P1_total)
        print("Player Two's score: ", P2_total)
        print("It's Player Two's turn")
        Turn_score = 0
        while (True):
#The first step in the human's turn is to ask for an imput so that the game can roll again or hold and record the round score
            Choice = input("Would you like to [r]oll or [h]old? ")
#You only really need an if statment for stopping the loop and holding, because the loop is made to repeat stopping it would be the only necessity
            if Choice == 'h':
                break
#The loop functions much the CPU phase the only differense if the added choice to stop whenever you want
            Roll = random.randint(1, 6)
            if Roll == 1:
                print("- rolled a  1")
                print("Pigged out!")
                Turn_score = 0
                break
            else:
                Turn_score += Roll
                print("- rolled a ", Roll)
            
            if P2_total >= 100:
                break
        P2_total += Turn_score
        print("Total turn score = ", Turn_score)
#A statment at the end of the outer loop allows the turn to swap back to player one
        Player = 1       
        
        if P2_total >= 100:
            print("Player Two Wins!")
            break
#A final print statment for the results once someone has reached 100 points
print("Final score: ", P1_total, "vs ", P2_total)
