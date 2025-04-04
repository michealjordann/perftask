import time
import random
import tkinter as tk
#leaderboard setup
rtime = 0
going = True
scores = []
names = []
def ldbsetup():
    global rtime
    user = input("type in your name to save your time to the leaderboard.")
    names.append(user)
    #accesses leaderboard text file
    with open("leaderboard.txt", "a") as file:
        file.write(f"{names}: {rtime} seconds\n")

def ldb():
    with open("leaderboard.txt", "r") as file:
            print("Leaderboard:")
            print(file.read())
#main game
def reactest():
    while going == True:
        #begin test
        global rtime
        ldbsetup()
        begin = input("Type in go to start, or type in 1 for leaderboard.")
        if begin == "go":
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
            ldb()
        else:
            print("wrong input to execute action")
            continue
            
reactest()


