import time
import random
going = True
scores = []
def reactest():
    while going == True:
        #begin test
        begin = input("Type in go to start.")
        if begin == "go":
            print("As soon as you see the letter X appear in the terminal, press Enter.")
            time.sleep(random.randint(1,5))
            letter = input("x")
            start = time.time()
            end = time.time()
            if letter == "":
                print("Nice! Your reaction time is ", start - end)
            else:
                print("Do not type anything but enter! Try again.")
        elif begin != "go":
            print("wrong input to start")
            

reactest()
