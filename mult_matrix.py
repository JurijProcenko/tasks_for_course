# multiplication of two matrices
def get_matrix(r, t):
    x = [[0] * t for _ in range(r)]
    for i in range(r):
        x[i] = [int(nn) for nn in input().split()]
    return x


n, m = [int(x) for x in input().split()]
a = get_matrix(n, m)
input()
l, k = [int(x) for x in input().split()]
c = [[0]*k for _ in range(n)]
if m==l:
    b = get_matrix(l, k)
    for i in range(n):
        for j in range(k):
            c[i][j]=sum([a[i][s]*b[s][j] for s in range(m)])
            print(c[i][j], end=' ')
        print()

else:
    print("Sorry, I can't multiply these matrices ")
