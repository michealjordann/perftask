import time
import random
import tkinter as tk
#leaderboard setup
def ldbsetup():
    user = input("type in your name to save your time to the leaderboard.")
    names.append(user)

def ldb():
    print("add a way to show the best time here with rtime idk how yet")
#main game
going = True
scores = []
names = []
def reactest():
    while going == True:
        #begin test
        begin = input("Type in go to start, or type in 1 for leaderboard.")
        if begin == "go":
            ldbsetup()
            print("As soon as you see the letter X appear in the terminal, press Enter.")
            time.sleep(random.randint(2,6))
            start = time.time()
            letter = input("x")
            end = time.time()
            rtime = round(end - start,3)
            if rtime <= 0.101:
                print("you pressed enter too early! try again")
                continue
            if letter == "":
                print("Nice! Your reaction time is", rtime)
                scores.append(rtime)
            else:
                print("Do not type anything but enter! Try again.")
                continue
        #leaderboard
        elif begin == "1":
            print("pravin rasiah")
        else:
            print("wrong input to start")
            continue
            
reactest()


