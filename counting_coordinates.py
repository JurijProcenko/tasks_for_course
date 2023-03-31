# Counting the number of points by quarters of the coordinate system
n = int(input())
quarts = [0, 0, 0, 0]
for i in range(n):
    x, y = input().split()
    x = int(x)
    y = int(y)
    if x > 0:
        if y > 0:
            quarts[0] += 1
        elif y < 0:
            quarts[3] += 1
    elif x < 0:
        if y > 0:
            quarts[1] += 1
        elif y < 0:
            quarts[2] += 1
print(f'Первая четверть: {quarts[0]}')
print(f'Вторая четверть: {quarts[1]}')
print(f'Третья четверть: {quarts[2]}')
print(f'Четвертая четверть: {quarts[3]}')
