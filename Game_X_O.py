def pick_fun():  # checking correct input
    if pick == "1" or pick == "2" or pick == "3" or pick == "4" or pick == "5" or pick == "6" or pick == "7" \
            or pick == "8" or pick == "9":
        return 1
    return 0


def dub():  # checking if number has already been entered.
    if pick == r1:
        return 0
    elif pick == r2:
        return 0
    elif pick == r3:
        return 0
    elif pick == r4:
        return 0
    elif pick == r5:
        return 0
    elif pick == r6:
        return 0
    elif pick == r7:
        return 0
    elif pick == r8:
        return 0
    elif pick == r9:
        return 0


def table():  # Game table
    global i1, i2, i3, i4, i5, i6, i7, i8, i9
    global r1, r2, r3, r4, r5, r6, r7, r8, r9
    if pick == str(i1):
        i1 = x0
        r1 = pick
    elif pick == str(i2):
        i2 = x0
        r2 = pick
    elif pick == str(i3):
        i3 = x0
        r3 = pick
    elif pick == str(i4):
        i4 = x0
        r4 = pick
    elif pick == str(i5):
        i5 = x0
        r5 = pick
    elif pick == str(i6):
        i6 = x0
        r6 = pick
    elif pick == str(i7):
        i7 = x0
        r7 = pick
    elif pick == str(i8):
        i8 = x0
        r8 = pick
    elif pick == str(i9):
        i9 = x0
        r9 = pick

    print("-------------------")
    print("|  " + str(i7) + "  |  " + str(i8) + "  |  " + str(i9) + "  |")
    print("-------------------")
    print("|  " + str(i4) + "  |  " + str(i5) + "  |  " + str(i6) + "  |")
    print("-------------------")
    print("|  " + str(i1) + "  |  " + str(i2) + "  |  " + str(i3) + "  |")
    print("-------------------")


def chw():  # Checking win condition
    if i1 == "X" and i2 == "X" and i3 == "X" or i1 == "O" and i2 == "O" and i3 == "O":
        return 1
    elif i4 == "X" and i5 == "X" and i6 == "X" or i4 == "O" and i5 == "O" and i6 == "O":
        return 1
    elif i7 == "X" and i8 == "X" and i9 == "X" or i7 == "O" and i8 == "O" and i9 == "O":
        return 1
    elif i1 == "X" and i4 == "X" and i7 == "X" or i1 == "O" and i4 == "O" and i7 == "O":
        return 1
    elif i2 == "X" and i5 == "X" and i8 == "X" or i2 == "O" and i5 == "O" and i8 == "O":
        return 1
    elif i3 == "X" and i6 == "X" and i9 == "X" or i3 == "O" and i6 == "O" and i9 == "O":
        return 1
    elif i1 == "X" and i5 == "X" and i9 == "X" or i1 == "O" and i5 == "O" and i9 == "O":
        return 1
    elif i7 == "X" and i5 == "X" and i3 == "X" or i7 == "O" and i5 == "O" and i3 == "O":
        return 1
    return 0


def che():  # Checking full table
    if i1 == "X" or i1 == "O":
        if i2 == "X" or i2 == "O":
            if i3 == "X" or i3 == "O":
                if i4 == "X" or i4 == "O":
                    if i5 == "X" or i5 == "O":
                        if i6 == "X" or i6 == "O":
                            if i7 == "X" or i7 == "O":
                                if i8 == "X" or i8 == "O":
                                    if i9 == "X" or i9 == "O":
                                        return 1
    return 0


run = 0
while run == 0:  # Menu selecting
    print("1. Start new game")
    print("2. Terminate program")
    select = input()
    if select == "1":  # Game start
        draw = 0
        x0 = "X"

        i1 = 1
        i2 = 2
        i3 = 3
        i4 = 4
        i5 = 5
        i6 = 6
        i7 = 7
        i8 = 8
        i9 = 9

        r1 = 0
        r2 = 0
        r3 = 0
        r4 = 0
        r5 = 0
        r6 = 0
        r7 = 0
        r8 = 0
        r9 = 0

        print("-------------------")
        print("|  " + str(i7) + "  |  " + str(i8) + "  |  " + str(i9) + "  |")
        print("-------------------")
        print("|  " + str(i4) + "  |  " + str(i5) + "  |  " + str(i6) + "  |")
        print("-------------------")
        print("|  " + str(i1) + "  |  " + str(i2) + "  |  " + str(i3) + "  |")
        print("-------------------")
        print("Player 1 (X) turn:")

        while chw() == 0 and che() == 0:  # Game till end
            pick = input()
            if pick_fun() == 0:  # checking correct input
                print("Chose a digit from 1 to 9")
            else:
                if dub() == 0:  # checking if number has already been entered.
                    print("That number has already been entered.")
                else:
                    table()  # Game table
                    if chw() == 0:  # Checking win condition
                        if x0 == "X":
                            x0 = "O"
                            print("Player O turn:")
                        else:
                            x0 = "X"
                            print("Player X turn:")
                    else:
                        print("Congratulations, Player " + str(x0) + " you WIN!!!!!!!!!!")
                    if che() == 1:  # Checking full table
                        print("It's a DRAW!!!!")
    elif select == "2":
        run = 1
    else:
        print("Please enter option 1 or 2")
