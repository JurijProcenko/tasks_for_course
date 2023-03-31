l = [int(i) for i in input().split()]
s = [l[-1]]
s.extend(l[:-1])
print(*s)