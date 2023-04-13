# Заполнение произвольной матрицы NxM по спирали по часовой стрелке
n, m = [int(x) for x in input().split()]
a = [[0] * m for _ in range(n)]
c = 1
i,j = 0, 0
x = len(a)
y = len(a[0])

while c <= n * m:
    for jj in range(j, y):
        a[i][jj] = c
        c += 1
    i += 1
    if c> n*m:
        break
    for ii in range(i, x):
        a[ii][y - 1] = c
        c += 1
    y -= 1
    if c> n*m:
        break
    for jj in range(y - 1, j - 1, -1):
        a[x - 1][jj] = c
        c += 1
    x -= 1
    if c> n*m:
        break
    for ii in range(x - 1, i - 1, -1):
        a[ii][j] = c
        c += 1
    j += 1
for i in range(n):
    for j in range(m):
        print(str(a[i][j]).ljust(3), end='')
    print()