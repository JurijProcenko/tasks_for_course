n = int(input())
l = []
pattern = 'anton'
for _ in range(n):
    l.append(input())
for i in range(n):
    j, k = 0, 0
    ai = False
    while j < len(l[i]) and k < len(pattern):
        if l[i][j]==pattern[k]:
            j += 1
            k += 1
        else:
            j += 1
        if k == len(pattern):
            ai = True
            break
    if ai:
        print(i+1, end=' ')
