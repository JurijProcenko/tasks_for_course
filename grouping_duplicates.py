# Grouping the same symbols to sub-list
s = input().split()
res = []
elem =[s[0]]
for i in range(1, len(s)):
    if s[i] not in elem:
        res.append(elem)
        del elem
        elem = [s[i]]
    else:
        elem.append(s[i])
res.append(elem)
print(res)
