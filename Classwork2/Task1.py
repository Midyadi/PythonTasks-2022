import itertools as it
with open("input.txt",'rt', encoding = 'utf-8') as i, open('output.txt', 'w',encoding = 'utf-8') as o:
    matrix = [[int(num) for num in line.strip().split()] for line in i.readlines()]
    summa = map(lambda x: sum(x), it.zip_longest(*matrix, fillvalue = 0))
    print(*summa, file = o)

