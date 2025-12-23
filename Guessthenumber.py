def guess_my_number():
    import random
    import getpass
    player_wins=0
    comp_wins=0
    other_player_wins=0
    
    def home_screen():
        print("Welcome To guess the number")
        print("1.Play Game")
        print("2.Game History")
        print("3.Quit Game")
        player_choice= int(input())
        


        if (player_choice==1):
            
            Play_new_game()
        if (player_choice==2):
            print("Number of Games Played: " , player_wins+comp_wins+other_player_wins)
            print("Number of Player Wins: ", player_wins)
            print("Number of Computer Wins: ", comp_wins)
            player_choice=input("Press B to go Back:")
            if(player_choice=="B" or player_choice=="b"):
                return home_screen()
        if (player_choice==3):
            quiting_game()
        else:
            print("Enter a Valid Number:")
            return home_screen()
        

    def Play_new_game():
        
        print("Choose Who you want to Play against:-")
        print("Computer or Second Person:")
        
        global player_choice
        player_choice = str(input())
        if (player_choice == "computer" or player_choice == "Computer" or player_choice == "COMPUTER"):
            game_with_computer()
            
           
        elif (player_choice == "second person" or player_choice == "Second Person" or player_choice == "SECOND PERSON"):
             game_with_human()
             

        else: 
            print ("Enter Computer or Second Person")
            return Play_new_game()
        
    def game_with_computer():
        print("Playing with Computer")
        comp_choice = random.randint(1,100)
        print("Computer: Guess My Number?")
        global player_choice
        player_choice=int(input("Enter the Number:"))
        if (player_choice<0 or player_choice>100):
            print("Enter a Valid Number ")
            return game_with_computer()
        if (comp_choice== player_choice):
            print("YOU WON🎊🎊")
            nonlocal player_wins
            player_wins+=1
            return home_screen()
        elif(comp_choice!=player_choice):
            print("You Lost....😭😭")
            nonlocal comp_wins
            comp_wins+=1
            return home_screen()
                
    def game_with_human():
        print("playing with 2nd person:-")
        player_choice_1=int(getpass.getpass("Enter Your Number:"))
        print("Please turn to the Other Player")
        player_choice_2=int(input("Guess the Number?:"))
        if (player_choice_1==player_choice_2):
            print("You Guessed the Number!!!")
            nonlocal player_wins
            player_wins+=1
            return home_screen()
        else: 
            print("Not the Same Number...")
            nonlocal other_player_wins
            other_player_wins+=1
            return home_screen()
        
        

    
    def quiting_game():
        print("Are you Sure About Quiting?")
        global player_choice
        player_choice = str(input())
        

        if (player_choice== "YES" or player_choice=="Yes" or player_choice=="yes"):
                if (player_wins+comp_wins+other_player_wins!=0):
                    print("Thank you for Playing")
                    return
                else:
                    print("Thank you for Visiting")
                    return 
        elif  (player_choice== "NO" or player_choice=="No" or player_choice=="no"):
            return home_screen()
        else:
            print("Enter YES or NO")
            return quiting_game()
    home_screen()
guess_my_number()