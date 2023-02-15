import random
import os


def run():
    IMAGES = ['''
              +---+
              |   |
                  |
                  |
                  |
                  |
            =========''', '''
              +---+
              |   |
              O   |
                  |
                  |
                  |
            =========''', '''
              +---+
              |   |
              O   |
              |   |
                  |
                  |
            =========''', '''
              +---+
              |   |
              O   |
            /|   |
                  |
                  |
            =========''', '''
              +---+
              |   |
              O   |
            /|\  |
                  |
                  |
            =========''', '''
              +---+
              |   |
              O   |
            /|\  |
            /    |
                  |
            =========''', '''
              +---+
              |   |
              O   |
            /|\  |
            / \  |
                  |
            =========
            ''']

    DB = [
        "C",
        "PYTHON",
        "JAVA",
        "JAVASCRIPT",
        "PHP"
    ]

    word = random.choice(DB).upper()
    spaces = ["_"] * len(word)
    lives = 6

    while True:
        os.system("cls")  # Windows clear screen
        for character in spaces:
            print(character, end=" ")
            print(IMAGES[lives])
            letter = input("Elige una letra: ").upper()

        found = False
        for idx, character in enumerate(word):
            if character == letter:
                spaces[idx] = letter
                found = True

            if not found:
                lives -= 1

            if "_" not in spaces:
                print("Ganaste!")
                break
                input("Presiona enter para continuar...")

            if lives == 0:
                os.system("cls")
                print("Perdiste!")
                break


if __name__ == "__main__":
    run()
