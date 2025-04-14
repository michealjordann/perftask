import time
import random
#leaderboard setup and functionality(ldb means leaderboard)
def ldbsetup(name, best_score):
    with open("leaderboard.txt", "a") as file:
        file.write(f"{name}: {best_score} seconds\n")

def ldb():
    try:
        with open("leaderboard.txt", "r") as file:
            print("Leaderboard:")
            print(file.read())
    except FileNotFoundError:
        #create leaderboard if not found
        print("No leaderboard file found, creating one now. If you did not save a score yet, do so or no leaderboard will show up.")
        with open("leaderboard.txt", "w") as file:
            file.write("") 
#Main reaction time game and saving score to text file
def reactest():
    scores = []  

    while True:
        choice = input("Type 'go' to test your reaction, 'done' to save your best score, or '1' to view leaderboard: ")

        if choice == "1":
            ldb()

        elif choice == "go":
            input("Press Enter to begin.")
            print("Wait until you see X in the terminal")
            time.sleep(random.randint(2, 6))
            start = time.time()
            user_input = input("X")
            end = time.time()
            rtime = round(end - start, 3)

            if rtime <= 0.101:
                print("Too early. Try again.")
                continue

            if user_input == "":
                scores.append(rtime)
                print(f"Reaction time: {rtime} seconds.")
            else:
                print("Only Press Enter. Try Again. ")

        elif choice == "done":
            if scores:
                best = min(scores)
                print(f"Your best reaction time this session: {best} seconds.")
                name = input("Enter your name to save your score: ")
                ldbsetup(name, best)
                scores.clear()  
            else:
                print("No recorded scores yet.")
        else:
            print("Invalid input.")

reactest()
