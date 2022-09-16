import itertools as it
with open("input.txt", 'rt',encoding='utf-8') as i, open('output.txt', 'w', encoding = 'utf-8') as o:
    a = [[int(i) for i in line.strip().split()] for line in i.readlines()]
    b = map(lambda x: sum(x), it.zip_longest(*a))
    print(*b, file = o)

