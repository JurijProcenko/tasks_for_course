timur = input()
ruslan = input()
l = ['камень', 'бумага', 'ножницы']
if l.index(timur) == l.index(ruslan) + 1 or l.index(timur) == l.index(ruslan) - 2:
    print('Тимур')
elif l.index(timur) == l.index(ruslan):
    print('ничья')
else:
    print('Руслан')
