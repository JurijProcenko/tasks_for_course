# exponentiation of a matrix
def get_matrix(r, t):
    x = [[0] * t for _ in range(r)]
    for i in range(r):
        x[i] = [int(nn) for nn in input().split()]
    return x


def mult_matrices(a, b):
    c = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            c[i][j] = sum([a[i][s] * b[s][j] for s in range(n)])
    return c


n = int(input())
a = get_matrix(n, n)
l = int(input())
c = a
for _ in range(l - 1):
    c = mult_matrices(c, a)
for i in range(n):
    print(*c[i])
s = input().strip().replace(' ','')