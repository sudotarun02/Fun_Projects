Board = [[0, 0, 3, 7, 0, 0, 0, 0, 4],
         [0, 5, 0, 0, 3, 0, 0, 7, 0],
         [7, 0, 0, 0, 0, 4, 8, 0, 0],
         [2, 0, 0, 0, 0, 3, 4, 0, 0],
         [0, 7, 0, 0, 9, 0, 0, 5, 0],
         [0, 0, 1, 5, 0, 0, 0, 0, 3],
         [0, 0, 2, 0, 0, 0, 0, 0, 1],
         [0, 8, 0, 0, 5, 0, 0, 6, 0],
         [1, 0, 0, 0, 0, 2, 5, 0, 0]]

print("-------------S U D O K U-------------")


def valid(m, a, b, n):
    r, c, g, h = 0, 0, 0, 0
    if a <= 2 and b <= 2:
        r, c, g, h = 0, 3, 0, 3
    if a <= 2 < b <= 5:
        r, c, g, h = 0, 3, 3, 6
    if a <= 2 and 8 >= b > 5:
        r, c, g, h = 0, 3, 6, 9
    if 5 >= a > 2 >= b:
        r, c, g, h = 3, 6, 0, 3
    if 5 >= a > 2 and 5 >= b > 2:
        r, c, g, h = 3, 6, 3, 6
    if 5 >= a < a >= b > 5:
        r, c, g, h = 3, 6, 6, 9
    if 8 >= a > 5 and b <= 2:
        r, c, g, h = 6, 9, 0, 3
    if 8 >= a > 5 >= b > 2:
        r, c, g, h = 6, 9, 3, 6
    if 8 >= a > 5 and 5 < b <= 8:
        r, c, g, h = 6, 9, 6, 9
    for i in range(r, c):
        for j in range(g, h):
            if i == a and j == b:
                continue
            if m[i][j] == n:
                return False
    for i in range(9):
        if i == b:
            continue
        if m[a][i] == n:
            return False
    for j in range(9):
        if j == a:
            continue
        if m[j][b] == n:
            return False
    return True


def solve(m, i=0, j=0):
    i, j = pos(m)
    if i == -1:
        print("-------------S O L V E D-------------")
        return True
    for x in range(1, 10):
        if valid(m, i, j, x):
            m[i][j] = x
            if solve(m, i, j):
                return True

            m[i][j] = 0
    return False


def pos(mat):
    for i in range(0, 9):
        for j in range(0, 9):
            if mat[i][j] == 0:
                return i, j
    return -1, -1


def print_board(mat):
    for i in range(9):
        for j in range(9):
            if j == 3 or j == 6:
                print("|", mat[i][j], end=" ")
            else:
                print(" ", mat[i][j], end=" ")
        print("")
        if i == 2 or i == 5:
            # print("+===+===+===+===+===+===+===+===+===+")
            print("+-----------+-----------+-----------+")
    print("_____________________________________")


print_board(Board)
solve(Board)
print_board(Board)
