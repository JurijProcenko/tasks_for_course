# Find all sublists in list
source = input().split()
res = [[]]
for i in range(1, len(source)+1):
    for j in range(0, len(source)):
        if j + i <= len(source):
            res.append([source[j + k] for k in range(i)])
print(res)
