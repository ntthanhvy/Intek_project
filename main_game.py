import sys


def print_board(a): # a is an list
    print("  a b c d e f g h")
    for j in range(len(a)): #j is row of this list(a)
        print(str(j + 1), end=" ")
        print(' '.join(k for k in a[j]))


def init_board(a):
    for j in range(8):
        a.append([])
        for i in range(8):
            a[j].append(".")

    a[3][3] = a[4][4] = "W"
    a[4][3] = a[3][4] = "B"
    return a


def endGame(a, turn):
    return len(find_valid_choice(a, turn) == 0 #turn can be 'B or 'W


def isInBoard(a, x, y):
    return y < len(a) and x < len(a[0]) and y >= 0 and x >= 0


def find_valid_move(a, i, j, v, player, opponent):
#v is the position of value in the list 'vs'
    x = i + v[1] # x is the col aka a[][]
    y = j + v[0] # y is the row aka a[]
    check = False
    while isInBoard(a, x, y) and a[y][x] == opponent:
        x += v[1]
        y += v[0]
        check = True
    if isInBoard(a, x, y) and a[y][x] == player and check:
        return (x, y)
    else:
        return ()
#This function check whether a the position of x, y is there a valid move


#Find position of valid choice
def find_valid_choice(a, player='B'):
    if player == 'B':
        opponent = 'W'
    elif player == 'W':
        opponent = 'B'
    validChoices = {}
    vs = [[0, 1], [1, 0], [-1, 0], [0, -1], [1, 1], [-1, -1], [1, -1], [-1, 1]]
    for j in range(len(a[0])): # j is col
        for i in range(len(a)): # i is row
            #Here will check for each element of list(a)
            if a[i][j] = ".":
                choice = []
                for k in range(len(vs)):
                # k is an value of vs in which is the surrounding position
                # of player tile
                    validChoice_ij = find_valid_move(a, i, j, vs[k], player, opponent)
                    #This check whether at position (i, j) there is a valid move
                    if len(validChoices) > 0:
                        choice.append([vs[k], validChoice_ij])
                if len(choice) > 0:
                    validChoices [(j, i)] = choice
    return validChoices


def print_valid_choice(validChoices): #validChoices is a dictionary
    s = ""
    i = 0
    validList = []
    for key in validChoices.keys():
        x = chr(key[0] + ord('a'))
# x is col, so x is a character, ord('a') return a unicode of 'a' and add key[0],
# after all change this into a character using chr()
        y = int(key[1] + 1)
# y is row, so y is an integer,
        s = x+''+y
        validList.append(s) #adding s to validList
        validList.sort() # sorting validList in order
    print("Valid Choices:",' '.join(i for i in validList))


def inputPlayer(a, validChoices, player, opponent):
#Check whether player input move right of is it in the valid choices
    while True:
        print_valid_choice(validChoices)
        com = input("Player " + player + ": ")
        if len(com) > 2:
            print(com + ": Invalid choice")
            sys.exit()
        com1 = com[0]
        com2 = com[1]
        if com1 < 'a' or com1 > 'h' or com2 < '1' or com2 > '8':
            print(com + ": Invalid choice")
        x = ord(com1) - ord('a')
        # getting the position of x by minus out the two value com1 and a
        # because ord() return an unicode which is an integer have distance = 1
        # for each letter in the alphabet
        y = int(com2) - 1
        # getting the position of y by minus 1 of the value com2
        # because the list run from 0 so to count the value we need to minus 1
        # in order to get the correct index
        if (x, y) in validChoices:
            a[y][x] = player # change the value at a[y][x] into the present Player
            choice = validChoices[(x, y)]
            #choice is the value of validChoices with the key is (x, y)
            #choice have strucure like s, an char follow by an int
            for c in choice: 






def main_game():
    a = []
    init_board(a)
    print_board(a)



main_game()
