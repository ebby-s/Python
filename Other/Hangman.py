import random
import math
import webbrowser
WordList = []
while True:
    with open('WordList.txt') as f:
        for line in f:
            line = line.strip()
            WordList.append(line)
    break
 
kword = []
glist=[]
score = 0
ksword = ""

print("""
   ___________________________________________________
  /                                                  /|
  HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH |
  H  _                                              H |
  H | | Welcome to                                  H |
  H | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __   H |
  H | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \  H |
  H | | | | (_| | | | | (_| | | | | | | (_| | | | | H |
  H |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_| H |
  H                     __/ |                       H |
  H  A text based game |___/   By Ebby              H /
  HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH/

  Copyright © SpaceYee Inc. 1987 (Not really)
  
""")

def turn():
    global word
    global cletter
    global wlen
    global glen
    global lives
    global lcount
    global wcount
    global kword
    global glist
    global score
    global ksword
    glen = len(kword)
    lcount = 0
    wcount = 0
    ksword = ""
    Ded = False
    print("------------------------------------------------------------------")
    print("Guessed letters: ", glist)
    print(lives, " lives remaining")
    for i in range(0,glen,1):
        ksword += kword[i]
    print("Word: ", ksword)
    cletter = input("Guess a letter: ")
    if len(cletter) != 1:
        Ded = True
    try:
        cletter = float(cletter)
        Ded = True
    except ValueError:
        "Do Nothin"

    if Ded == False:
        try:
            check=glist.index(cletter)
        except ValueError:
            glist.append(cletter)
        else:
            Ded = True
    for i in range (0,wlen,1):
        if word[i] == cletter:
            kword[i] = cletter
        else:
            lcount += 1

    if lcount == wlen and Ded == False:
        lives = lives - 1

    if lives < 1:
        print (" _________     ")
    else:
        print("")
    if lives < 2:
        print ("|         |    ")
    else:
        print("")
    if lives < 3:
        print ("|         0    ")
    else:
        print("")
    if lives < 4:
        print ("|        /|\   ")
    else:
        print("")
    if lives < 5:
        print ("|        / \   ")
    else:
        print("")
    if lives < 6:
        print ("|              ")
    else:
        print("")
    if lives < 7:
        print ("|HHHHHHHHHHHHHH|\n")
    else:
        print("")
    if lives == 0:
        print ("Game over")
        #for i in range(0,10,1):
        webbrowser.open('https://www.youtube.com/watch?v=M5QGkOGZubQ', new=2)
        print("Your final score is: ", score)
        print("The word was ", word)
        restart = input("Would you like to restart y/n?")
        if restart == "y":
            kword = []
            glist = []
            score = 0
            begin()
        else:
            exit()
    for i in range(0,glen,1):
        if kword[i] == "-":
            wcount += 1

    if wcount == 0:
        print("You win!")
        print("The word was ", word)
        kword = []
        glist = []
        score += wlen
        score += lives
        print("Your score is now: ", score)
        begin()

def begin():
    global word
    global lives
    global number
    global wlen
    numgen = random.Random()
    number = numgen.randrange(0, len(WordList))
    word = WordList[number]
    wlen = len(word)
    for i in range(0,wlen,1):
        kword.append("-")
    lives = 7
    while True:
        turn()
    lcount = 0

begin()
