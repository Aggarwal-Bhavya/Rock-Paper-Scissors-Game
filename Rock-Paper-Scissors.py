import random

print ("WELCOME!")
#Printing rules of game
print ("The rules for winning a game of Rock-Paper-Scissors are as follows: \n"
        + "Rock vs Paper => Paper wins \n" 
        + "Rock vs Scissors => Rock wins \n" 
        + "Paper vs Scissors => Scissors wins \n")

print ("1 Player Mode OR 2 Player Mode")
mode = int(input("Enter player mode: "))

while mode > 2 or mode < 1:
    mode = int(input("Enter valid player mode: "))
    
player1 = input("Enter player 1 name: ")

if mode == 1:
    print ("\n" + player1 + " vs CPU" )
elif mode == 2:
    player2 = input("Enter player 2 name: ")
    print ("\n" + player1 + " vs " + player2)

print ("\nDISCLAIMER: \n" 
        + "5 games will be played and the winner of maximum games will be the tournament winner \n"
        + "Let's Begin!\n")

gameCount = 1
player1_win_count = 0
comp_win_count = 0
while gameCount <= 5:
    print ("\nGAME", gameCount)
    print ("\nEnter choice \n 1. Rock \n 2. Paper \n 3. Scissors \n")

    #taking user input 
    choice = int(input("Player1 turn: "))

    #looping until user enters valid input
    while choice > 3 or choice < 1:
        choice = int(input("Enter valid choice: "))
    
    #initializing choice_name
    if choice == 1:
        choice_name = "Rock"
    elif choice == 2:
        choice_name = "Paper"
    else:
        choice_name = "Scissors"
    
    #print user choice:
    print ("\n" + player1 + " played " + choice_name)

    if mode == 1:
        print ("\nCPU turn...")
        comp_choice = random.randint(1, 3)

        #looping until comp_choice value is equal to choice value
        while comp_choice == choice:
            comp_choice = random.randint(1,3)
        
        #initialiazing comp_choice_name
        if comp_choice == 1:
            comp_choice_name = "Rock"
        elif comp_choice == 2:
            comp_choice_name = "Paper"
        else: 
            comp_choice_name = "Scissors"

        #print CPU choice
        print ("\nCPU played " + comp_choice_name)

    elif mode == 2:
        #taking user input 
        comp_choice = int(input("\nPlayer2 turn: "))

        #looping until user enters valid input
        while comp_choice>3 or comp_choice<1:
            comp_choice = int(input("Enter valid choice: "))
            
        #initializing choice_name
        if comp_choice == 1:
            comp_choice_name = "Rock"
        elif comp_choice == 2:
            comp_choice_name = "Paper"
        else:
            comp_choice_name = "Scissors"
            
        #print user choice:
        print ("\n" + player2 + " played " + comp_choice_name)
    
    print ("\n" + choice_name + " vs " + comp_choice_name)

   #Winning conditions then incrementing gameCount and winCount for each player
    if ((choice==1 and comp_choice==2) or (choice==2 and comp_choice==1)):
        print ("\nPaper wins =>", end = "") #end is used to prevent python print statement to go to nextline
        result = "Paper"
    elif ((choice==1 and comp_choice==3) or (choice==3 and comp_choice==1)):
        print ("\nRock wins =>", end = "")
        result = "Rock" 
    elif ((choice==1 and comp_choice==1) or (choice==2 and comp_choice==2) or (choice==3 and comp_choice==3)):
        result = "tied"
    else:
        print ("\nScissors wins =>", end = "")
        result = "Scissors"
    
    #Printing either user or computer wins
    if result == "tied":
        print ("\n Match tied.")
        player1_win_count += 1
        comp_win_count += 1
    elif result == choice_name:
        print (" <====== " + player1 + " wins ======> ")
        player1_win_count += 1
    else:
        comp_win_count += 1
        if mode == 1:
            print (" <====== CPU wins ======> ")
        elif mode == 2:
            print (" <====== " + player2 + " wins ======> ")

    #increasing gameCount
    gameCount += 1
    if player1_win_count == comp_win_count:
        print ("\n\nGAME TIED")
    elif player1_win_count >= 3:
        print ("\n\nWINNER " + player1)
    elif comp_win_count >= 3:
        if mode == 1:
            print ("\n\nWINNER CPU")
        elif mode == 2:
            print ("\n\nWINNER " + player2)
    
    if gameCount == 6:
        print ("\n  GAME OVER   ")