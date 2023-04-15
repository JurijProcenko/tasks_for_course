def get_matrix():
    x = [[0] * m for _ in range(n)]
    for i in range(n):
        x[i] = [int(nn) for nn in input().split()]
    return x


n, m = [int(x) for x in input().split()]
a = get_matrix()
input()
b = get_matrix()
for i in range(n):
    for j in range(m):
        print(a[i][j] + b[i][j], end=' ')
    print()
