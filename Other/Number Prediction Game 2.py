import random
import os
# Ideas: New increased difficulty function, open youtube, name+highscores file

def MainMenu():                 #Main menu, starts the game
    Diffselected = False
    while True:
        Userinput = str(input("""Main Menu
    1.Play
    2.Select Difficulty
    3.Exit
    : """))
        os.system('cls')
        if Userinput == "1":
            if Diffselected == True:
                print ("Starting game...")
                Main(Range,Lives,Difficulty)
            else:
                print ("Hey! You gotta select a difficulty first!")
        elif Userinput == "2":
            [Range,Lives,Difficulty] = DifficultyMenu()
            Diffselected = True
        elif Userinput == "3":
            ExitMenu()
        else:
            print("Invalid option selected")

def DifficultyMenu():                 #Difficulty selection menu, lets user select difficulty
    annoyance = 0
    valid = False
    while not valid:
        Userinput2 = str(input("""Difficulty Selection
        Option. Difficulty <Range> <Lives>
        1.Easy               100     10
        2.Normal             100     15
        3.Hard               100     20
        4.Heroic             200     25
        5.Legendary          50      25
        6.InstantDeath       100     25
        7.Details <-- (FOR NOOBS LIKE YOU)
        : """))
        os.system('cls')

        try:
            Userinput2 = int(Userinput2)
            valid = True
        except ValueError:
            annoyance += 1
            Annoyed(annoyance)
    
    if Userinput2 == 1: 
        rng = 100
        Lives = 40
        Difficulty = 0
        print ("Easy difficulty, mommy let you use her computer for the first time?")
    if Userinput2 == 2:
        rng = 100
        Lives = 60
        Difficulty = 0
        print ("Normal difficulty, what a normie.")
    if Userinput2 == 3:
        rng = 100
        Lives = 80
        Difficulty = 1
        print ("You have selected hard, you must be up for a challenge!")
    if Userinput2 == 4:
        rng = 200
        Lives = 100
        Difficulty = 1
        print ("You have selected heroic, but are you really though?")
    if Userinput2 == 5:
        rng = 50
        Lives = 100
        Difficulty = 2
        print ("Legendary difficulty, god speed to you...")
    if Userinput2 == 6:
        rng = 100
        Lives = 100
        Difficulty = 2
        print ("Insane in the membrane, insane in the brain!")
    if Userinput2 == 7:
        print("""Explanations of game modes:
Easy -   You will recieve hints before each game,
         you will be told if your guess is greater
         or less than the number.
       
Medium - You will only be told whether your guess
         is greater or less than the number.

Hard -   You will only be told whether your current
         guess is closer than your last.\n-------------------------------------\n""")
        MainMenu()
        
    return [rng,int(Lives/4),Difficulty]

def ExitMenu():                 #Exit menu, allows user to exit program
    annoyance = 0
    while True:
        choice = str(input("""
    1.Return to main menu
    2.Exit
    : """))
        os.system('cls')
        if choice == ("1"):
            print("Returning to main menu. . .")
            MainMenu()
        elif choice == ("2"):
            Confirm = str(input("""Are you sure you want to leave?
    1.Yes
    2.No
    : """))
            os.system('cls')
            if Confirm == "1":
                exit()
            elif Confirm == "2":
                annoyance += 1
                if annoyance <= 8:
                    print ("Make up your mind!")
                elif annoyance > 8:
                    print ("*Silence...*")
            else:
                annoyance += 1
                Annoyed(annoyance)
        else:
            annoyance += 1
            Annoyed(annoyance)

def Annoyed(annoyance):                 #Replies to invalid inputs
    if annoyance == 1:
        print ("Uh...could you repeat that?")
    if annoyance == 2:
        print ("I'm sorry, what?")
    if annoyance == 3:
        print ("Look, the menu is simple, you just input the number next to the option, it isn't that hard.")
    if annoyance == 4:
        print ("Oh now you're just trying to waste my time.")
    if annoyance == 5:
        print ("What do you think you're going to gain from this??")
    if annoyance == 6:
        print ("I bite my thumb at thee!")
    if annoyance == 7:
        print ("Can you STOP wasting both of our time and just pick an actual option.")
    if annoyance == 8:
        print ("Alright, I'm gonna go catch up on some netflix series, have fun being a numpty.")
    if annoyance > 8:
        print ("*No one responds...*")

def Main(rng,Lives,Difficulty):                 #Main game controller
    ScoreMult = 1
    streak = 0
    HighestStreak = 0
    score = 0
    BonusCount = 1
    print ("""\n-------------------------------------\nWelcome to the game...
Numbers generated within this difficulty are between 0 and""", rng)
    while Lives > 0:
        Num = random.randrange(0,rng)
        [Lives,KeepStreak,Win] = Game(Num,Lives,Difficulty,score,HighestStreak)
        if Lives > 0:
            score += ScoreMult*Win
            if KeepStreak:
                streak += 1
                BonusCount += 1
            else:
                streak = Win
                BonusCount = Win
            if streak > HighestStreak:
                HighestStreak = streak
            if BonusCount >= 5:
                BonusCount -= 5
                ScoreMult += 1
                Lives += 1
                print ("Score multiplier increased to ",ScoreMult,", you have gained a life! You now have ",Lives," lives!")
            if Win == 1:
                print ("Correct! Current score: ", score, ", current streak: ", streak)
        
    EndGameMenu(score,HighestStreak)

def Game(Num,Lives,Difficulty,score,streak):                 #A single round of the game
    block = "\n-------------------------------------\n"
    KeepStreak = True
    First = True
    PrevGuess = 1000

    if Difficulty == 0:
        EasyMode(Num)
    
    while Lives > 0:
        print()
        Guess = str(input("Enter your guess here(or 'e' to exit): "))
        print("\n-------------------------------------\n")
        if Guess == "e":
            EndGameMenu(score,streak)
        
        try:
            Guess = int(Guess)
        except ValueError:
            print("That isn't even a number...")
            continue
        
        if Guess == Num:
            return [Lives,KeepStreak,1]
        
        elif Guess > Num:
            Lives -= 1
            KeepStreak = False
        elif Guess < Num:
            Lives -= 1
            KeepStreak = False
        
        if Difficulty in [0,1]:
            MedMode(Num,Guess,Lives)
        elif Difficulty == 2 and not First:
            HardMode(Num,Guess,PrevGuess,Lives)
        elif Difficulty == 2 and First:
            print(Lives, " lives left.")
        PrevGuess = Guess
        First = False
        
    return [Lives,KeepStreak,0]

def EndGameMenu(score,streak):
    print ("Game over man!")
    print ("You have scored", score, "points!")
    print ("Your highest streak was", streak)
    print()
    while True:
        choice = input("""
    1. Save score
    2. Exit or return to main menu
    : """)
        try:
            choice = int(choice)
        except ValueError:
            print("Invalid input")
            continue
        if 1 > choice > 2:
            print("Choice not within range")
            continue
        elif choice == 1:
            name = str(input("Enter your name: "))
            AddToFile(name,score,streak)
        elif choice == 2:
            ExitMenu()

def AddToFile(name,score,streak):
    print("Feature currently not available")
    ExitMenu()

def EasyMode(number):
    if number > 50:
        print ("The number is greater than 50")
        if number < 75:
            print ("But it is less than 75")
        if number > 75:
            print("And it is greater than 75")
    elif number < 50:
        print ("The number is less than 50")
        if number < 25:
            print ("And it is less than 25")
        if number > 25:
            print ("But it is greater than 25")

def MedMode(Num,Guess,Lives):
    if Guess > Num:
        print ("My number is less than that, you have", Lives, "lives remaining.")
    elif Guess < Num:
        print ("My number is greater than that, you have", Lives, "lives remaining.")

def HardMode(Num,Guess,PrevGuess,Lives):
    Difference = (Num-Guess)**2
    PrevDifference = (Num-PrevGuess)**2
    if Difference == PrevDifference:
        print("You didn't get closer or further from the number.")
    elif Difference > PrevDifference:
        print("Your last guess was closer.")
    elif Difference < PrevDifference:
        print("You are getting closer.")
    print(Lives, " lives left.")

MainMenu()
