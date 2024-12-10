import random
import time
from genres import video_games, music

class genres:
    def __init__(self, video_games, music):
        self.video_games = video_games
        self.music = music
    

def main():
    def rules():
        print(f"Hangman is a wordguesser game, you have 7 tries to guess the word...")

    def welcome():
        print(f"Welcome to hangman!")
        time.sleep(2)
        print(f"""If you want to read the rules for the game type out "rules" """)
        time.sleep(2)
        print(f"""If you are ready to play type "play" """)
        while True:
            userinput = input("Response: ")
            if userinput == "play":
                break
            if userinput == "rules":
                rules()

    welcome()


main()
