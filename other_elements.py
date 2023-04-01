l = [int(i) for i in input().split()]
count = 1
for i in range(len(l) - 1):
    if l[i] < l[i + 1]:
        count += 1
print(count)
