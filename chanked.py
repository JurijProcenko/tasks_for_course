# divide string by chanks
source = input().split()
n = int(input())
if len(source)<= n:
    res=[]
    res.append(source)
else:
    res = [[source[j] for j in range(i, i+n)] if i != len(source)-1 else [source[i]] for i in range(0, len(source), n)]
print(res)

