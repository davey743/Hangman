import random
import time
from genres import video_games, music_artists, movies, countries
from stickman import get_hangman_figure


class Hangman:
    def __init__(self, video_games, music_artists, movies, countries):
        self.video_games = video_games
        self.music_artists = music_artists 
        self.movies = movies
        self.countries = countries
        self.chosen_category = None
        self.chosen_word = None
        self.guessed_word = None
        self.letter_bank = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    def choose_category(self):
        while True:
            category = input("Pick a category: video games, music artists, movies and countries").lower()
            if category == "video games":
                self.chosen_category = self.video_games
                break
            elif category == "music artists":
                self.chosen_category = self.music_artists
                break
            elif category == "movies":
                self.chosen_category = self.movies
                break
            elif category == "countries":
                self.chosen_category = self.countries
                break
            else:
                print("Invalid category. Please choose a valid category.")

    def choose_word(self):
        self.chosen_word = random.choice(self.chosen_category)
        self.guessed_word = ["_"] * len(self.chosen_word)
        for i in range(len(self.chosen_word)):
            if self.chosen_word[i] == " ":
                self.guessed_word[i] = " "

    def display_word(self):
        print("Word: " + " ".join(self.guessed_word))

    def display_letter_bank(self):
        print("Letters you have left: " + ", ".join(self.letter_bank))

    def play(self):
        self.choose_category()
        self.choose_word()
        attempts = 7
        while attempts > 0 and "_" in self.guessed_word:
            print(get_hangman_figure(attempts))
            self.display_word()
            self.display_letter_bank()
            user_input = input("Guess a letter or the entire word: ")
            if len(user_input) > 1:
                if user_input.lower() == self.chosen_word.lower():
                    self.guessed_word = list(self.chosen_word)
                    print("Congratulations! You guessed the word correctly.")
                    return
                else:
                    attempts -= 1
                    
            elif len(user_input) == 1 and user_input.upper() in self.letter_bank:
                self.letter_bank.remove(user_input.upper())
                if user_input.upper() in self.chosen_word.upper():
                    for i in range(len(self.chosen_word)):
                        if self.chosen_word[i].upper() == user_input.upper():
                            self.guessed_word[i] = self.chosen_word[i]
                else:
                    attempts -= 1
            else:
                print("Invalid input. Please guess a letter or the entire word.")
        if "_" not in self.guessed_word:
            print("Congratulations! You guessed the word!")
        else:
            print(get_hangman_figure(0))
            print(f"Game over! The word was {self.chosen_word}.")
           

    def rules(self):
        print("\nHangman is a word guessing game.\nYou have 7 attempts to guess the word")
        print("You can choose from 4 different categories\nThose categories are video games, music artists, movies, or countries")

    def welcome(self):
        print("Welcome to hangman!")
        time.sleep(2)
        print("If you want to read about the rules of the game(type 'rules')")
        time.sleep(2)
        print("If you are ready to play the game (type 'play')")
        
        while True:
            user_input = input("Input: ").lower()
            if user_input == "rules":
                self.rules()
            elif user_input == "play":
                self.play()
                break
            else:
                print("Invalid input. Please type 'rules' or 'play'")

def main():
    game = Hangman(video_games, music_artists, movies, countries)
    game.welcome()

if __name__ == "__main__":
    main()
