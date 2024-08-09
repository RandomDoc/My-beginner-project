import random
import time
import webbrowser

def victory():
    print("You won")
    while True:
        game_victory = input("Do you want to play another game? (yes/no)\n")
        if game_victory.lower() == "yes":
            game_changer = input("Which game would you like to play? (dnd/tictactoe/numberguessing/rpc)\n").lower()
            print("Note:choosing the same game will repeat it\n")
            if game_changer == "dnd":
                for seconds in range(3, 0, -1):
                    print("Your game will start in", seconds)
                    time.sleep(1)
                DnD()
            elif game_changer == "rpc":
                for seconds in range(3, 0, -1):
                    print("Your game will start in", seconds)
                    time.sleep(1)
                playRPS()
            elif game_changer == "tictactoe":
                for seconds in range(3, 0, -1):
                    print("Your game will start in", seconds)
                    time.sleep(1)
                tictactoe()
            elif game_changer == "numberguessing":
                for seconds in range(3, 0, -1):
                    print("Your game will start in", seconds)
                    time.sleep(1)
                numberguessing()
            else:
                print("Invalid game selection. Please choose a valid game.")
        else:
            break

def defeat():
    print("You lost")
    while True:
        game_defeat = input("Do you want to play another game? (yes/no)\n").lower()
        if game_defeat== "yes":
            game_changer = input("Which game would you like to play? (dnd/tictactoe/numberguessing/rpc)\n").lower()
            print("Note:choosing the same game will repeat it\n")
            if game_changer == "dnd":
                for seconds in range(3, 0, -1):
                    print("Your game will start in", seconds)
                    time.sleep(1)
                DnD()
            elif game_changer == "rpc":
                for seconds in range(3, 0, -1):
                    print("Your game will start in", seconds)
                    time.sleep(1)
                playRPS()
            elif game_changer == "tictactoe":
                for seconds in range(3, 0, -1):
                    print("Your game will start in", seconds)
                    time.sleep(1)
                tictactoe()
            elif game_changer == "numberguessing":
                for seconds in range(3, 0, -1):
                    print("Your game will start in", seconds)
                    time.sleep(1)
                numberguessing()
            else:
                print("This game isn't in the options!")
        else:
            break

def play():
    game_changer = input("Which game would you like to play? (dnd/tictactoe/numberguessing/rpc)\n").lower()
        
    if game_changer == "dnd":
                for seconds in range(3, 0, -1):
                    print("Your game will start in", seconds)
                    time.sleep(1)
                DnD()
    elif game_changer == "rpc":
                for seconds in range(3, 0, -1):
                    print("Your game will start in", seconds)
                    time.sleep(1)
                playRPS()
    elif game_changer == "tictactoe":
                for seconds in range(3, 0, -1):
                    print("Your game will start in", seconds)
                    time.sleep(1)
                tictactoe() 
    elif game_changer == "numberguessing":
                for seconds in range(3, 0, -1):
                    print("Your game will start in", seconds)
                    time.sleep(1)
                numberguessing()
    else:
                print("This game isn't in the options!")
                

def tictactoe():
    print("Tic Tac Toe game is starting...\n")
    l = ["      ", "      ", "      ", "      ", "      ", "      ", "      ", "      ", "      "]
    player_points = 0
    computer_points = 0 
    
    def is_odd(x):
        return x % 2

    count = 0

    while True:
        count += 1

        if is_odd(count):
            z = int(input("Pick a block from 1 to 9\n"))
            while l[z-1] != "      ":
                z = int(input("Block already occupied\n"))
            l[z-1] = "  X   "
        else:
            r = random.choice([i for i in range(9) if l[i] == "      "])
            
            l[r] = "  O   "

        print(f"""\n  
                                            _____________________
                                            |      |      |      |
                                            |{l[0]}|{l[1]}|{l[2]}|
                                            |______|______|______|
                                            |      |      |      |   
                                            |{l[3]}|{l[4]}|{l[5]}|
                                            |______|______|______|
                                            |      |      |      |
                                            |{l[6]}|{l[7]}|{l[8]}|
                                            |______|______|______|
            """)

        if (l[0]==l[1]==l[2]=="  X   ") or (l[0]==l[4]==l[8]=="  X   ") or (l[2]==l[4]==l[6]=="  X   ") or \
           (l[3]==l[4]==l[5]=="  X   ") or (l[6]==l[7]==l[8]=="  X   ") or (l[0]==l[3]==l[6]=="  X   ") or \
           (l[1]==l[4]==l[7]=="  X   ") or (l[2]==l[5]==l[8]=="  X   "):
            print("Victory!")
            player_points += 1
            for i in range(9):
                l[i] = "      "
            count = 0

        elif (l[0]==l[1]==l[2]=="  O   ") or (l[0]==l[4]==l[8]=="  O   ") or (l[2]==l[4]==l[6]=="  O   ") or \
             (l[3]==l[4]==l[5]=="  O   ") or (l[6]==l[7]==l[8]=="  O   ") or (l[0]==l[3]==l[6]=="  O   ") or \
             (l[1]==l[4]==l[7]=="  O   ") or (l[2]==l[5]==l[8]=="  O   "):
            print("Defeat!")
            computer_points += 1
            for i in range(9):
                l[i] = "      "
            count = 0

        elif all(cell != "      " for cell in l):
            print("No winners")
            for i in range(9):
                l[i] = "      "
            count = 0
        print(f"player:{player_points}, computer:{computer_points}")

def numberguessing():
    print("Number Guessing game is starting...\n")
    global computer_points, player_points
    computer_points = 0
    player_points = 0
    
    for i in range(1):
        player_choice1 = int(input("Pick a number from one to five \n"))
        Mylist1 = list(range(1, 6))
        computer_choice1 = random.choice(Mylist1)
        if player_choice1 == computer_choice1:
            print("Level 1 completed")
            player_points += 1
            player_choice2 = int(input("Pick a number from one to ten \n"))
            Mylist2 = list(range(1, 11))
            computer_choice2 = random.choice(Mylist2)
            if player_choice2 == computer_choice2:
                print("Level 2 completed")
                player_points += 1
                player_choice3 = int(input("Pick a number from one to twenty \n"))
                Mylist3 = list(range(1, 21))
                computer_choice3 = random.choice(Mylist3)
                if player_choice3 == computer_choice3:
                    print("Level 3 completed")
                    player_points += 1
                    player_choice4 = int(input("Pick a number from one to fifty \n"))
                    Mylist4 = list(range(1, 51))
                    computer_choice4 = random.choice(Mylist4)
                    if player_choice4 == computer_choice4:
                        print("Level 4 completed")
                        player_points += 1
                        player_choice5 = int(input("Pick a number from one to one-hundred \n"))
                        Mylist5 = list(range(1, 101))
                        computer_choice5 = random.choice(Mylist5)
                        if player_choice5 == computer_choice5:
                            print("You won the game!")
                        else:
                            computer_points+=1
                    else:
                        computer_points+=1
                else:
                    computer_points+=1
            else: 
                computer_points+=1
        else:
            computer_points+=1
    while True:
            for i in range(1):
                numberguessing()
                print(f"player:{player_points} computer:{computer_points}")
                
            if player_points>computer_points:
                computer_points=0
                player_points=0
                print("You won")
            else:
                defeat()

def DnD():
    print("DnD game is starting...\n")
    global Player_Health, Monster_Health, Monster_Damage, Player_damage
    Player_Health = 100
    Monster_Health = 200
    Player_damage = 100
    Monster_Damage = 50
    name = input("What is your Hero name?\n")
    while name == "":
        name = input("What is your Hero name?\n")
    print("Hello", name)

    while Player_Health > 0 and Monster_Health > 0:
        x = input("What will you do? (attack/defence)\n")
        if x == "attack":
            Monster_Health -= Player_damage
            print("You dealt", Player_damage, "damage!")
        elif x == "defence":
            Player_Health -= Monster_Damage
            print("You lost", Monster_Damage, "HP!")

    if Player_Health <= 0:
        defeat()
    if Monster_Health <= 0:
        print("Victory!")
        claim_prize = input("Do you wish to claim your prize? (yes/no)\n")
        if claim_prize.lower() == "yes":
            for seconds in range(10, 0, -1):
                print(seconds)
                time.sleep(1)
            url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
            webbrowser.open(url)
        else :
            victory()

def playRPS():
    print("Rock Paper Scissors ")
    global computer_points, player_points
    MyList = ["rock", "paper", "scissors"]
    computer_choice = random.choice(MyList)
    player_choice = input("\nrock, paper, scissors\n").lower()
    if player_choice == computer_choice:
        print("It's a tie!")
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        print("Victory!")
        player_points += 1
    else:
        print("Defeat!")
        computer_points += 1

    while True:
        for i in range(5):
            playRPS()
            print(f"player:{player_points} computer:{computer_points}")
            
        if player_points>computer_points:
             computer_points=0
             player_points=0
             victory()
        else:
            defeat()


play()

