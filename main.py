import time
import random
import tkinter as tk
#GUI
r = tk.Tk()
r.title("Reaction Time Test By Tanush Pusulrui")
r.geometry("400x300")
#main game
going = True
scores = []
def reactest():
    while going == True:
        #begin test
        begin = input("Type in go to start.")
        if begin == "go":
            print("As soon as you see the letter X appear in the terminal, press Enter.")
            time.sleep(random.randint(2,6))
            start = time.time()
            letter = input("x")
            end = time.time()
            rtime = round(end - start,3)
            if rtime <= 0.101:
                print("you pressed enter too early! try again")
                break
            if letter == "":
                print("Nice! Your reaction time is", rtime)
            else:
                print("Do not type anything but enter! Try again.")
                break
        elif begin != "go":
            print("wrong input to start")
            

reactest()
