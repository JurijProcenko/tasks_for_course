# Testing matrix on diag simmetric
def get_matrix(r, t):
    x = [[0] * t for _ in range(r)]
    for i in range(r):
        x[i] = [int(nn) for nn in input().split()]
    return x

n = int(input())
a = get_matrix(n, n)
flag = True
for i in range(n):
    for j in range(n-i-1):
        if a[i][j]!=a[n-j-1][n-i-1]:
            print('NO')
            flag = False
            break
    if not flag:
        break
else:
    print("YES")