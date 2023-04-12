# Possible knight's move on chessboard
def print_matrix(m):
    for i in range(8):
        for j in range(8):
            print(m[i][j], end=' ')
        print()


s = input()
col = 'abcdefgh'.index(s[0])
row = 8 - int(s[1])
cb = [['.' for _ in range(8)] for _ in range(8)]
cb[row][col] = 'N'

# up
if 0<=row-2<=7:
    if 0<=col-1<=7:
        cb[row-2][col-1] = '*'
    if 0<=col+1<=7:
        cb[row-2][col+1] = '*'

# down
if 0<=row+2<=7:
    if 0<=col-1<=7:
        cb[row+2][col-1] = '*'
    if 0<=col+1<=7:
        cb[row+2][col+1] = '*'

# left
if 0<=col-2<=7:
    if 0<=row-1<=7:
        cb[row-1][col-2] = '*'
    if 0<=row+1<=7:
        cb[row+1][col-2] = '*'

# right
if 0<=col+2<=7:
    if 0<=row-1<=7:
        cb[row-1][col+2] = '*'
    if 0<=row+1<=7:
        cb[row+1][col+2] = '*'

print_matrix(cb)
