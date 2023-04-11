# Reading matrix's element and writing each sub-list on line
r = int(input())
c = int(input())
matrix = []
for _ in range(r):
    t = []
    for j in range(c):
        t.append(input())
    matrix.append(t)
    del t
for i in range(r):
    for j in range(c):
        print(matrix[i][j], end=' ')
    print()