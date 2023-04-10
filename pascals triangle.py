# Make Pascal's triangle from n-lines
def pascal(n):
    if n == 0:
        return [1]
    if n == 1:
        return [1, 1]
    l = [[1], [1, 1]]
    for i in range(1, n):
        inner_list = [1]
        for j in range(0, i):
            inner_list.append(l[i][j]+l[i][j+1])
        inner_list.append(1)
        l.append(inner_list)
    return l

n = int(input())
l = pascal(n-1)
for line in l:
    print(' '.join(str(x) for x in line).center(n*10))