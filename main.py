import random
import string
import os
import sys
from string import punctuation

Polish_Diacritics = "ąęółćźżńś"
Available_CHARACTERS = string.ascii_letters + Polish_Diacritics + Polish_Diacritics.upper()
numbers = "1234567890"
not_available_characters = numbers + punctuation
used_letter = []
Stages = {
    5:
        """
    
    
    
    
    
    
    
    
    
    
        """,
    4:
        """
         ------
         |    |
         |    O
         |
         |
         |
         |
         |
         |
        ----------
        """,

    3:
        """
         ------
         |    |
         |    O
         |  /-+-\\
         | /     \\
         |   
         |   
         |   
         |   
        ----------
        """,
    2:
        """
         ------
         |    |
         |    O
         |  /-+-\\
         | /  |  \\
         |   
         |   
         |   
         |   
        ----------
        """,
    1:
        """
         ------
         |    |
         |    O
         |  /-+-\\
         | /  |  \\
         |    |
         |   | 
         |   | 
         |   
        ----------
        """,
    0:
        """
         ------
         |    |
         |    O
         |  /-+-\\
         | /  |  \\
         |    |
         |   | |
         |   | |
         |  
        ----------
        """,
}


class Game:
    def __init__(self, sentence: str):
        self.word = sentence
        self.guessed_letters = []
        self.tries = 5

        self.hint = self._get_hint()

    def show_state(self):
        message = f'Podpowiedź:{self.hint}\n Pozostało prób: {self.tries}'
        print(message)
        print("Wpisz quit by opuścić program")

    def guess(self, letter: str) -> bool:
        letter = letter.lower()
        if letter == "quit":
            sys.exit(0)
        if len(letter) > 1:
            os.system("cls")
            print("Podaj jeden znak zamiast kliku oszuście!")
            print(f"podane litery {used_letter}")
            return False

        if letter in used_letter:
            os.system("cls")
            print("Ta litera została już podana")
            print(f"podane litery {used_letter}")
            return False

        if letter in self.word:
            os.system("cls")
            used_letter.append(letter)
            print("Trafiona!")
            print(f"podane litery {used_letter}")
            if letter not in self.word:
                self.tries -= 1
                if letter in used_letter:
                    os.system("cls")
                else:
                    return False

        if letter not in self.word:
            os.system("cls")
            if letter not in not_available_characters:
                used_letter.append(letter)
                print("Pudło!")
                print(f"podane litery {used_letter}")
                self.tries -= 1
                return False

            else:
                os.system("cls")
                print("W haśle nie ma cyfr i znaków specjalych.")
                print(f"podane litery {used_letter}")
                return False

        self.guessed_letters.append(letter)
        self.hint = self._get_hint()
        return False

    def start(self):
        print("=" * 50)
        print(f"podane litery{used_letter}")
        print(Stages[self.tries])
        while self.tries > 0 and self.hint != self.word:
            self.show_state()
            letter = input("Zgadnij literę: ")

            was_guessed = self.guess(letter)

            print("=" * 50)
            if was_guessed is False:
                print(Stages[self.tries])

        if self.tries == 0:
            print("=" * 50)
            print("Koniec gry!")
        else:
            print("Brawo!")
        print(f"podane litery {used_letter}")
        print(f"Hasło to: {self.word}")

    def _get_hint(self):
        hint = ""
        for character in self.word:
            if character in Available_CHARACTERS and character.lower() not in self.guessed_letters:
                hint += "_"
            else:
                hint += character
        return hint


def get_random_sentence_from_file() -> str:
    with open("hasla.txt", encoding="UTF-8") as c:
        sentences = c.readlines()
        sentences = map(lambda x: x.strip(), sentences)
        sentences = list(filter(None, sentences))
        return random.choice(sentences).strip()


def welcome():
    print("Witam w grze - Szubienica.")
    print("Spróbuj zgadnąć przysłowie.")


if __name__ == "__main__":
    os.system("cls")
    welcome()
    decision = True
    while decision:
        game = Game(sentence=get_random_sentence_from_file())
        game.start()
        if input("Czy chcesz zagrać ponownie? (t/n)\n") not in ("t", "tak", "T"):
            decision = False
            os.system("cls")
            print("Koniec programu.")
            sys.exit(0)
        os.system("cls")
        print("Zaczynamy od nowa :)")
        print("Wylosowano nowe przysłowie. Spróbuj jeszcze raz.")
        used_letter = []
    print("Koniec gry.")