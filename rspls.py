timur = input()
ruslan = input()
l = ['lizard', 'rock', 'paper', 'scissors', 'Spock']
n = ['scissors', 'rock', 'Spock', 'paper', 'lizard']
if l.index(timur) == l.index(ruslan):
    print('draw in the game')
elif l.index(timur) == l.index(ruslan) + 1 or l.index(timur) == l.index(ruslan) - 4:
    print('1st player wins!')
elif n.index(timur) == n.index(ruslan) + 1 or n.index(timur) == n.index(ruslan) - 4:
    print('1st player wins!')
else:
    print('2nd player wins!')
