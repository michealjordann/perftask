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
            wait = time.sleep(random.randint(2,6))
            start = time.time()
            letter = input("x")
            end = time.time()
            if 
                print("Nice! Your reaction time is", end-start)
            else:
                print("Do not type anything but enter! Try again.")
                break
        elif begin != "go":
            print("wrong input to start")
            

reactest()
