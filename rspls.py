timur = input()
ruslan = input()
l = ['ящерица', 'камень', 'бумага', 'ножницы', 'Спок']
n = ['ножницы', 'камень', 'Спок', 'бумага', 'ящерица']
if l.index(timur) == l.index(ruslan):
    print('ничья')
elif l.index(timur) == l.index(ruslan) + 1 or l.index(timur) == l.index(ruslan) - 4:
    print('Тимур')
elif n.index(timur) == n.index(ruslan) + 1 or n.index(timur) == n.index(ruslan) - 4:
    print('Тимур')
else:
    print('Руслан')
