word = input() + ' запретил букву'
letters = 'абвгдежзиклмнопрстуфхцчшщьыъэюя'
i = 0
while i < len(letters) and len(word) != 0:
    if letters[i] in word:
        if '  ' in word:
            word = word.replace('  ', ' ')
        print(word, letters[i])
        word = word.replace(letters[i], '').strip()
    i += 1
