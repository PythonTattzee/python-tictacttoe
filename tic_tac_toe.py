import random

table = [["", "", ""],
         ["", "", ""],
         ["", "", ""]]


CHOICES = []
ENEMY_CHOICES = []

def introduction():
    print("------------------------------------------------------------------------------")
    print("1. The game is played on a grid that's 3 squares by 3 squares.")
    print("2. your symbol is 'O' and a symbol of your opponent is 'X'")
    print("3. The first player to get 3 of her marks in a row (up, down, across, or diagonally) is the winner.")
    print("4. When all 9 squares are full, the game is over.")
    print("5. type-in two numbers in a range 1 to 3 where the first number is a row and the second number is column")
    print("   for example: 12 (1 - is a row, 2 - is a column)")
    print("      1    2    3 ")
    print("   1    |     |   ")
    print("     ---+-----+---")
    print("   1    |     |   ")
    print("     ---+-----+---")
    print("   1    |     |   ")
    print("------------------------------------------------------------------------------")


def board():
    print(" 1    2    3")
    print("1", table[0][0], " |", table[0][1], " |", table[0][2])
    print("----+---+---")
    print("2", table[1][0], " |", table[1][1], " |", table[1][2])
    print("----+---+---")
    print("3", table[2][0], " |", table[2][1], " |", table[2][2])


play = True
introduction()
print("////////////////////")
print("---SO, LET'S play---")
print("////////////////////")
board()


while play:
    occupied = True
    choice = input("Choose two numbers from 1 to 3 separated by comma where first number is a row and a second number is a column:").replace(",", "")
    table[int(choice[0]) - 1][int(choice[1]) - 1] = "O"

    xy = f"{random.randint(0, 2)}{random.randint(0, 2)}"
    table[int(xy[0])][int(xy[1])] = "X"
    board()

    for row in table:
        if row.count("X") == 3:
            print("Oops...Sorry. You've lost.")
            play = False
        elif row.count("O") == 3:
            print("You Won!!!")
            play = False
        elif row.count("X") == 3 and row.count("O") == 3:
            print("You are even. Shake hands)")
            play = False

    if table[0][0] == "X" and table[1][1] == "X" and table[2][2] == "X":
        print("Oooh, Sorry. You've Lost!!!")
        play = False
    elif table[0][2] == "X" and table[1][1] == "X" and table[2][0] == "X":
        print("Oooh, Sorry. You've Lost!!!")
        play = False
    elif table[0][0] == "O" and table[1][1] == "O" and table[2][2] == "O":
        print("You Won!!!")
        play = False
    elif table[0][2] == "O" and table[1][1] == "O" and table[2][0] == "O":
        print("You Won!!!")
        play = False

    elif table[0][0] == "X" and table[1][0] == "X" and table[2][0] == "X":
        print("Oooh, Sorry. You've Lost!!!")
        play = False
    elif table[1][0] == "X" and table[1][1] == "X" and table[1][2] == "X":
        print("Oooh, Sorry. You've Lost!!!")
        play = False
    elif table[2][0] == "X" and table[2][1] == "X" and table[2][2] == "X":
        print("Oooh, Sorry. You've Lost!!!")
        play = False

    elif table[0][0] == "O" and table[1][0] == "O" and table[2][0] == "O":
        print("You Won!!!")
        play = False
    elif table[1][0] == "O" and table[1][1] == "O" and table[1][2] == "O":
        print("You Won!!!")
        play = False
    elif table[2][0] == "O" and table[2][1] == "O" and table[2][2] == "O":
        print("You Won!!!")
        play = False




