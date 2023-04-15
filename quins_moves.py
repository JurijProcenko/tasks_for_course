# Possible quin's move on chessboard
def print_matrix(m):
    for i in range(8):
        for j in range(8):
            print(m[i][j], end=' ')
        print()


s = input()
col = 'abcdefgh'.index(s[0])
row = 8 - int(s[1])
cb = [['.' for _ in range(8)] for _ in range(8)]
cb[row][col] = 'Q'
for i in range(1, 8):
    # up and diag
    if 0 <= row - i <= 7:
        cb[row - i][col] = '*'
        if 0 <= col - i <= 7:
            cb[row - i][col - i] = '*'
        if 0 <= col + i <= 7:
            cb[row - i][col + i] = '*'

    # down and diag
    if 0 <= row + i <= 7:
        cb[row + i][col] = '*'
        if 0 <= col - i <= 7:
            cb[row + i][col - i] = '*'
        if 0 <= col + i <= 7:
            cb[row + i][col + i] = '*'

    # left
    if 0 <= col - i <= 7:
        cb[row][col - i] = '*'

    # right
    if 0 <= col + i <= 7:
        cb[row][col + i] = '*'

print_matrix(cb)