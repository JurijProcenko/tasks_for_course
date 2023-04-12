# Magic sqare or not magic sqare - that is the question

def test(mas):
    m = []
    for i in range(len(mas)):
        for j in range(len(mas)):
            m.append(mas[i][j])
    for i in range(len(m)):
        if m.count(m[i])>1 or m[i]<1 or m[i]>n**2:
            return True
    return False
def generate(sq):
    m = []
    d1 = 0
    d2 = 0
    for i in range(n):
        col = 0
        m.append(sum(sq[i]))
        d1 += sq[i][i]
        d2 += sq[i][n - i - 1]
        for j in range(n):
            col += sq[j][i]
        m.append(col)
    m.append(d1)
    m.append(d2)
    return m

n = int(input())
sq = list([int(x) for x in input().split()] for j in range(n))
if test(sq):
    print(('NO'))
else:
    m = generate(sq)
    for i in range(len(m)-1):
        if m[i] != m[i+1]:
            print('NO')
            break
        else:
            print('YES')