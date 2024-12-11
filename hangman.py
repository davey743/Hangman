import random
import time
from genres import video_games, music

class hangman:
    def __init__(self, video_games, music):
        self.video_games = video_games
        self.music = music 
        self.word_to_guess = None
        self.max_guesses = 7
        self.letterbank = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        
    def select_word(self,category):
        if category == "video_games":
            self.word_to_guess = random.choice("video_games")
        elif category == "music":
            self.word_to_guess = random.choice("music")
        else:
            print("Invalid category")
    
    def update_letterbank(self, guessed_letter):
        if guessed_letter in self.letterbank:
            self.wordbank = self.wordbank.replace(guessed_letter,"")

    def display_letterbank(self):
        spaced_letterbank = " ".join(self.letterbank)
        print(f"Letters available: {spaced_letterbank}")

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
            elif userinput == "rules":
                rules()
            else:
                print("Invalid input. Please type 'play' to play or 'rules' to read the rules")
    welcome()


main()
