import random
import time
from genres import video_games, music
from stick_figure import get_stickman_stages

def main():
    def rules():
        print("\nHangman is a wordguesser game\nYou have 7 attempts to guess the word")
        print("You can choose 2 different categories\nThose categories are: Video games and Music.")

    def welcome():
        print(f"Welcome to hangman!")
        # time.sleep(2)
        print(f"""If you want to read the rules for the game (type "rules") """)
        # time.sleep(2)
        print(f"""If you are ready to play (type "play") """)
       
        while True:
            userinput = input("Response: ").lower()
            if userinput == "play":
                print("\nTo find out the different categories (type 'categories')")
                while True:
                    category = input("Pick a category: ").lower()
                    if category == "video games":
                        print(video_games)
                    elif category == "music": 
                       print(music)
                    else:
                        pass
            elif userinput == "rules":
                rules()
            else:
                print("Invalid input. Please type 'play' to play or 'rules' to read the rules")
    welcome()


if __name__ == "__main__":
    main()