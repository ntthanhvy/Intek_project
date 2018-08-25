import sys


# Khoi tao board a giong trang thai ban co ban dau cua game
def print_board(a):
    # in dong dau tien cua ban co
    print('  a b c d e f g h')
    for j in range(len(a)):
        print(str(j + 1) + ' ', end='')
        print(' '.join(i for i in a[j]))


def init_board(a):
    # duyet theo dong
    for i in range(8):
        # them phan tu dong
        a.append([])
        for j in range(8):
            # gan gia tri cua phan tu cot cua dong thu i voi gia tri '.'
            a[i].append('.')
    # Cap nhat tthemai cac vi tri (3,3) (4,4) (3,4) (4,3)
    # sao cho giong nhu ban co ban dau
    a[3][3] = a[4][4] = 'W'
    a[3][4] = a[4][3] = 'B'


# Ham kiem tra da ket thuc game(Khong con nuoc di) hay chua
def is_end_game(a, turn):
    return len(find_valid_choice(a, turn)) == 0


# Ham kiem tra toa do (x,y) co nam ben trong ban co
# Tra ve True neu nam trong toa do cua ban co va nguoc lai tra ve False
def is_in_board(a, x, y):
    return y < len(a) and x < len(a[0]) and y >= 0 and x >= 0


def find_valid_choice_with_orient(a, i, j, v, player, opponent):
    y = i + v[1]
    x = j + v[0]
    check = False
    while is_in_board(a, x, y) and a[y][x] == opponent:

        y += v[1]
        x += v[0]
        check = True
    if is_in_board(a, x, y) and a[y][x] == player and check:
        return (x, y)
    else:
        return ()


# Tim toa do cua nhung o hop le de danh
def find_valid_choice(a, player='B'):
    if player == 'B':
        opponent = 'W'
    elif player == 'W':
        opponent = 'B'
    valid_choice = {}
    vs = [[0, 1], [1, 0], [-1, 0], [0, -1], [1, 1], [-1, -1], [1, -1], [-1, 1]]
    for j in range(len(a[0])):
        for i in range(len(a)):
            if a[i][j] == '.':
                choice = []
                for k in range(len(vs)):
                    valid_choice_ij = find_valid_choice_with_orient(a, i, j,
                                                                    vs[k],
                                                                    player,
                                                                    opponent)
                    if len(valid_choice_ij) > 0:
                        choice.append([vs[k], valid_choice_ij])
                if len(choice) > 0:
                    valid_choice[(j, i)] = choice
    return valid_choice


def print_valid_player(valid_choice):
    s = ""
    i = 0
    validList = []
    for key in valid_choice.keys():
        x = chr(key[0] + ord('a'))
        y = str(key[1] + 1)
        s = x+""+y
        validList.append(s)
        # if i != len(valid_choice) - 1:
            # s += " "
        i += 1
    validList.sort()
    print("Valid choices:", ' '.join(i for i in validList))


def input_player(a, valid_choice, player, opponent):

    while True:
        print_valid_player(valid_choice)
        command = input("Player " + player + ": ")
        if len(command) != 2:
            print(command + ": Invalid choice")
            # continue
            sys.exit()
        c1 = command[0]
        c2 = command[1]
        if c1 < 'a' or c1 > 'h' or c2 < '1' or c2 > '8':
            print(command + ": Invalid choice")
            sys.exit()
            # continue
        x = ord(c1) - ord('a')
        y = int(c2) - 1
        if (x, y) in valid_choice:
            a[y][x] = player
            choice = valid_choice[(x, y)]
            for c in choice:
                vy = c[0][1]
                vx = c[0][0]
                xx = x + vx
                yy = y + vy
                while a[yy][xx] != player:
                    # Ghi de quan nguoi choi len quan doi phuong
                    a[yy][xx] = player
                    xx = xx + vx
                    yy = yy + vy
            break
        else:
            print(command + ": Invalid choice")


# update board
# Ham tinh diem
def get_score(a, player):
    score = 0
    for row in a:
        for c in row:
            if c == player:
                score += 1
    return score


# Main game
def main_game():
    a = []
    # Khoi tao ban co
    init_board(a)
    # In ban co ra may
    # print_board(a)
    player = 'W'
    opponent = 'B'
    turn = 'B'
    number_cannot_play = 0
    # Vao vong lap de choi game
    # Lap cho den khi kiem tra game da ket thuc(Khong con nuoc de di)
    while True:
        print_board(a)
        if player == 'W':
            player = 'B'
            opponent = 'W'
        else:
            player = 'W'
            opponent = 'B'
        # Nguoi choi 'B'
        valid_choice = find_valid_choice(a, player)
        if len(valid_choice) > 0:
            number_cannot_play = 0
            input_player(a, valid_choice, player, opponent)
            # print_board(a)
        else:
            print("Player " + player + " cannot play.")
            number_cannot_play += 1
            if number_cannot_play == 2:
                break

    score_w = get_score(a, 'W')
    score_b = get_score(a, 'B')
    print("End of the game. W: " + score_w + ", B: " + score_b)
    if score_w > score_b:
        print("B wins.")
    else:
        print("W wins.")


# Chay ham main game
def main_game():
    a = []
    init_board(a)
    print_board(a)
    turn = 'B'
    number_cannot_play = 0
    # Vao vong lap de choi game
    # Lap cho den khi kiem tra game da ket thuc(Khong con nuoc de di)
    while True:

        # Nguoi choi 'B'
        valid_choice = find_valid_choice(a, player='B')
        if len(valid_choice) > 0:
            # tthemai cac vi tri (3, 3) (4, 4) (3, 4) (4, 3)
            # sao cho giong nhu ban co ban dau
            number_cannot_play = 0
            input_player(a, valid_choice, 'B', 'W')
            print_board(a)
        else:
            print("Player B cannot play.")
            number_cannot_play += 1
            if number_cannot_play == 2:
                break

        # Nguoi choi 'W'
        valid_choice = find_valid_choice(a, player='W')
        if len(valid_choice) > 0:
            number_cannot_play = 0
            input_player(a, valid_choice, 'W', 'B')
            print_board(a)
        else:
            print("Player W cannot play.")
            number_cannot_play += 1
            if number_cannot_play == 2:
                break

    score_w = get_score(a, 'W')
    score_b = get_score(a, 'B')
    print("End of the game. W: " + str(score_w) + ", B: " + str(score_b))
    if score_w > score_b:
        print("W wins.")
    else:
        print("B wins.")


# Chay ham main gameRedIntek
main_game()
