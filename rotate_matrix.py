# Rotate the square matrix of numbers by 90∘ clockwise
def print_matrix(m):
    for i in range(n):
        print(*m[i])

n = int(input())
ma = list([int(x) for x in input().split()] for j in range(n))
ma2 = []
for i in range(n):
    ma2.append([ma[j][i] for j in range(n-1, -1, -1)])



print_matrix(ma2)