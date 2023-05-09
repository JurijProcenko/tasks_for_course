def make_dict(word:str):
    d = {}
    for s in word:
        d[s]=d.get(s,0)+1
    return d

print('YES' if make_dict(input().lower())==make_dict(input().lower()) else 'NO')
x=10
