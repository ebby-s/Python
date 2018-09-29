import random
import math
predict2 = 0

def predictiongame():
    global msg
    global Lives
    global number
    global predict
    global predict2
    global predictdiff
    global predictdiff2
    predict = int(input(msg + """\nI have a number between 1 and 100
Try to guess it!: """))
    Lives -=1
    if diff != 4:
        if predict > number:
            msg += str(predict) + " is higher than my number.\n"
        elif predict < number:
            msg += str(predict) + " is lower than my number.\n"
    elif diff == 4 and predict2 != 0:
        predictdiffs = (predict - number)**2
        predictdiff2s = (predict2 - number)**2
        predictdiff = math.sqrt(predictdiffs)
        predictdiff2 = math.sqrt(predictdiff2s)
        if predictdiff2 > predictdiff:
            msg += "You are getting closer. \n"
        elif predictdiff2 < predictdiff:
            msg += "Your last guess was closer. \n"
    print (Lives, """Lives left
----------------------------------------------------------""")
        
    if Lives == 0:
        msg = ""
        print ("Game over!")
        retry = input("""Do you want to try again?
Y/N""")
        if retry == ("y"):
             print ("Restarting...")
             predictiongame()
        elif retry == ("n"):
            print ("Goodbye!")
            quit()
    if predict == number:
         print("\n\nGreat, you got it with {0} Lives remaining!\n\n".format(Lives))
         msg = ""
         begin()
    predict2 = predict

def ezstart():
    global number
    while True:
        if number > 50:
            print ("The number is greater than 50")
            if number < 75:
                print ("But it is less than 75")
            if number > 75: ("And it is greater than 75")
            predictiongame()
        elif number < 50:
            print ("The number is less than 50")
            if number < 25:
                print ("And it is less than 25")
            if number > 25:
                print ("But it is greater than 25")
            predictiongame()

def begin():
    global diff
    global Lives
    global number
    global msg
    numgen = random.Random()
    number = numgen.randrange(1, 100)
    msg = ""
    print ("""Choose difficulty:
 1. Easy
 2. Medium
 3. Hard
 4. You are getting a bit cocky now""")
    diff = int(input("\n  : "))
    if diff == 1:
        Lives = 6
        ezstart()
    elif diff == 2:
        Lives = 8
        while True:
            predictiongame()
    elif diff == 3:
        Lives = 7
        while True:
            predictiongame()
    elif diff == 4:
        Lives = 8
        while True:
            predictiongame()

begin()
