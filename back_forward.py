l = [int(i) for i in input().split()]
for i in range(1, len(l), 2):
    l[i], l[i-1] = l[i-1], l[i]
print(*l)