n = int(input())
l = []
for _ in range(n):
    l.append(int(input()))
x = int(input())
yn = 'НЕТ'
for i in range(len(l)):
    if l[i] == 0:
        continue
    p = l[:]
    p.pop(i)
    if x / l[i] in p:
        print('ДА')
        break
else:
    print(yn)
